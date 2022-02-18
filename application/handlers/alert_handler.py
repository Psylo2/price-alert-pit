from flask import session
from typing import List, Union, Dict

from application.handlers.usecases import AlertUseCase
from application.handlers.services import AlertHandlerService
from domain.models import AlertModel


class AlertHandler(AlertUseCase, AlertHandlerService):

    def __init__(self, repository, store_handler, item_handler):
        self._repository = repository.get_collection('alert')
        self._store_handler = store_handler
        self._item_handler = item_handler

    def all_user_alerts(self) -> List:
        query = {'user_email': session['email']}
        all_user_alerts = self._repository.find(query=query)
        if not all_user_alerts:
            return []
        return [AlertModel(**alert).dict() for alert in all_user_alerts]

    def create_alert(self, name: str, item_url: str, price_limit: str) -> None:
        store = self._store_handler.find_store_by_url(url=item_url)
        store_tag = store.get('tag_name')
        store_query = store.get('query')

        item = self._item_handler.save_item(url=item_url, tag_name=store_tag, query=store_query)

        self._save_alert(alert_name=name, price_limit=price_limit, item_id=item.id)

    def update_alert(self, alert_id: str, price_limit: str) -> None:
        alert = self.get_alert(alert_id=alert_id)
        alert['price_limit'] = float(price_limit)
        self._repository.update(_id=alert_id, data=alert)

    def delete_alert(self, alert_id: str) -> None:
        alert = self.get_alert(alert_id=alert_id)
        user_email = alert.get('user_email')

        if user_email == session['email']:
            self._repository.remove(_id=alert_id)

    def get_alert(self, alert_id: str) -> Union[Dict, None]:
        return self._repository.find_one(_id=alert_id)

    def notify_reach_price(self, item_id: str) -> bool:
        item = self._item_handler.get_item(item_id=item_id)
        alert = self._repository.find(query={"item_id": item_id})
        if item['price'] < alert['price_limit']:
            return True

    def _all_user_alerts(self, alerts: Union[List, None]) -> List:
        if not alerts:
            return []
        return [AlertModel(**alert).dict() for alert in alerts]

    def _save_alert(self, alert_name: str, price_limit: str, item_id: str) -> None:
        price_limit = float(price_limit)
        alert = AlertModel(alert_name=alert_name, item_id=item_id,
                           price_limit=price_limit, user_email=session['email'])
        self._repository.insert(data=alert.dict())
