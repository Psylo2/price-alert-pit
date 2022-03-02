from abc import abstractmethod, ABC
from typing import Dict, List


class RepositoryServices(ABC):

    @abstractmethod
    def repository(self,):
        ...

    @abstractmethod
    def insert(self, data: dict) -> None:
        ...

    @abstractmethod
    def find(self, query: dict) -> Dict:
        ...

    @abstractmethod
    def find_one(self, _id: str) -> Dict:
        ...

    @abstractmethod
    def update(self, _id: str, data: dict) -> None:
        ...

    @abstractmethod
    def remove(self, _id: str) -> Dict:
        ...

    @abstractmethod
    def fetch_all(self) -> List:
        ...
