from abc import abstractmethod, ABC
from typing import Union, Dict


class StoreHandlerService(ABC):

    @abstractmethod
    def find_store_by_url(self, url: str) -> Dict:
        ...

    @abstractmethod
    def _get_store_by_url_prefix(self, url_prefix: str) -> Dict:
        ...

    @abstractmethod
    def _validate_url(self, url: str) -> str:
        ...
