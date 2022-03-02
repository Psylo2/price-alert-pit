import uuid
import re
import requests
from bs4 import BeautifulSoup
from typing import List, Dict

from infrastructure.repositories.services import RepositoryServices
from application.usecases.services import ItemUseCaseService
from domain.models import ItemModel


class ItemUseCase(ItemUseCaseService):
    def __init__(self, repository_service: RepositoryServices):
        self._repository = repository_service

    def save_item(self, url: str, tag_name: str, query: str) -> ItemModel:
        item_id = uuid.uuid4()
        item = ItemModel(item_id=item_id, url=url, tag_name=tag_name, query=query)
        self._fetch_price(item=item)
        self._repository.insert(data=item.dict())
        return item

    def all_items(self) -> List[Dict]:
        return self._repository.fetch_all()

    def load_item_price(self, item_id: str) -> float:
        item = self._repository.find_one(_id=item_id)
        item_model = ItemModel(**item)
        return self._fetch_price(item=item_model)

    def notify_reach_price(self, item_id: str) -> bool:
        item = self._repository.find_one(_id=item_id)
        item_model = ItemModel(**item)
        if item_model.price < item_model.price_limit:
            return True

    def get_item(self, item_id: str) -> Dict:
        return self._repository.find_one(_id=item_id)

    def _fetch_price(self, item: ItemModel) -> float:
        response = requests.get(item.url)
        content = response.content

        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(item.tag_name, item.query)
        str_price = element.text.strip()

    def _price(self, item: ItemModel, price: str) -> float:
        pattern = re.compile(r"(\d+,?\d*\.\d{2})")
        match = pattern.search(price)
        found_price = match.group(1)

        item.price = self._clean_string_price(price=found_price)
        return item.price

    def _clean_string_price(self, price: str) -> float:
        price = price.replace(",", "")
        return float(price)
