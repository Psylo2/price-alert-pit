from abc import abstractmethod, ABC
from typing import Union, Dict, List


class AlertHandlerService(ABC):

    @abstractmethod
    def _all_user_alerts(self, alerts: Union[List, None]) -> List:
        ...

    @abstractmethod
    def _save_alert(self, alert_name: str, price_limit: float, item_id: str) -> None:
        ...
