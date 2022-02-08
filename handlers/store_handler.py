import re
import uuid
from typing import List, Dict

from usecases import StoreUseCase
from handlers.services import StoreHandlerService
from models.store import StoreModel


class StoreHandler(StoreUseCase, StoreHandlerService):

    def __init__(self, repository):
        self._repository = repository.get_collection('item')

    def all_stores(self) -> List:
        return self._repository.fetch_all()

    def create_store(self, name: str, url_prefix: str, tag_name: str, query: Dict) -> None:
        store_id = uuid.uuid4()
        store_model = StoreModel(store_id=store_id, name=name, url_prefix=url_prefix,
                           tag_name=tag_name, query=query)
        self._repository.insert(data=store_model.dict())

    def update_store(self, store_id: str, name: str, url_prefix: str, tag_name: str, query: Dict) -> None:
        store = StoreModel(store_id=store_id, name=name, url_prefix=url_prefix,
                            tag_name=tag_name, query=query)
        self._repository.update(_id=store_id, data=store.dict())

    def delete_store(self, store_id: str) -> None:
        store = self.get_store(store_id=store_id)
        if store:
            self._repository.remove(store_id=store_id)

    def get_store(self, store_id: str) -> Dict:
        return self._repository.find_one(_id=store_id)

    def find_store_by_url(self, url: str) -> Dict:
        url_prefix = self._validate_url(url=url)
        store = self._get_store_by_url_prefix(url_prefix=url_prefix)
        return StoreModel(**store).dict()

    def _get_store_by_url_prefix(self, url_prefix: str) -> Dict:
        url_regex = {"$regex": f"^{url_prefix}"}
        query = {"url_prefix": url_regex}
        return self._repository.find(query=query)

    def _validate_url(self, url: str) -> str:
        pattern = re.compile(r"(http*s?://.*?/)")
        match = pattern.match(url)
        return match.group(1)
