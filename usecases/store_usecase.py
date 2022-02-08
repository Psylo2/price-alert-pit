from abc import abstractmethod, ABC
from typing import List, Dict


class StoreUseCase(ABC):
    @abstractmethod
    def all_stores(self) -> List:
        ...

    @abstractmethod
    def create_store(self, name: str, url_prefix: str, tag_name: str, query: Dict) -> None:
        ...

    @abstractmethod
    def update_store(self, store_id: str, name: str, url_prefix: str, tag_name: str, query: Dict) -> None:
        ...

    @abstractmethod
    def delete_store(self, store_id: str) -> None:
        ...

    @abstractmethod
    def get_store(self, store_id: str) -> Dict:
        ...
