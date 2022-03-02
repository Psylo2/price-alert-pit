from abc import abstractmethod, ABC
from typing import Union, Dict, List


class AlertUseCaseService(ABC):

    @abstractmethod
    def all_user_alerts(self) -> List:
        ...

    @abstractmethod
    def create_alert(self, name: str, item_url: str, price_limit: float) -> None:
        ...

    @abstractmethod
    def update_alert(self, alert_id: str, price_limit: str) -> None:
        ...

    @abstractmethod
    def delete_alert(self, alert_id: str) -> None:
        ...

    @abstractmethod
    def get_alert(self, alert_id: str) -> Union[Dict, None]:
        ...

    @abstractmethod
    def notify_reach_price(self, item_id: str) -> bool:
        ...
