from typing import Dict, List

from app import repository
from manager.services import RepositoryServices


class AlertRepository(RepositoryServices):

    def __init__(self):
        self._repository_instance = None
        self._repository_name = "alert"

    @property
    def repository(self):
        if not self._repository_instance:
            self._repository_instance = repository.create_collection(self._repository_name)
        return self._repository_instance

    def insert(self, data: dict) -> None:
        self.repository.insert_one(document=data)

    def find(self, query: dict) -> Dict:
        return self.repository.find(query)

    def find_one(self, _id: str) -> Dict:
        filter_ = {"_id": _id}
        return self.repository.find_one(filter=filter_)

    def update(self, _id: str, data: dict) -> None:
        filter_ = {"_id": _id}
        self.repository.update_one(filter=filter_, update=data, upsert=True)

    def remove(self, _id: str) -> Dict:
        filter_ = {"_id": _id}
        return self.repository.delete_one(filter=filter_)

    def fetch_all(self) -> List:
        return self.repository.find({})
