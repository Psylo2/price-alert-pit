from abc import abstractmethod, ABC
from typing import List, Dict


class ItemUseCaseService(ABC):

    @abstractmethod
    def save_item(self, url: str, tag_name: str, query: str) -> "ItemModel":
        ...

    @abstractmethod
    def all_items(self) -> List[Dict]:
        ...

    @abstractmethod
    def load_item_price(self, item_id: str) -> float:
        ...

    @abstractmethod
    def notify_reach_price(self, item_id: str) -> bool:
        ...

    @abstractmethod
    def get_item(self, item_id: str) -> Dict:
        ...
