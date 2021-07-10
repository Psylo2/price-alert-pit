import re
import uuid
from typing import Dict
from dataclasses import dataclass, field
import requests
from bs4 import BeautifulSoup

from models.abc.model import Model


@dataclass(eq=False)
class Item(Model):
    _collection: str = field(init=False, default='items')
    url: str
    tag_name: str
    query: Dict
    price: float = field(default=None)
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def fetch_price(self) -> float:
        response = requests.get(self.url)
        content = response.content

        soup = BeautifulSoup(content, "html.parser")
        element = soup.find(self.tag_name, self.query)
        str_price = element.text.strip()

        pattern = re.compile(r"(\d+,?\d*\.\d{2})")
        match = pattern.search(str_price)
        found_price = match.group(1)
        clean_found = found_price.replace(",", "")
        self.price = float(clean_found)
        return self.price

    def json(self) -> Dict:
        return {
            "_id": self._id,
            "url": self.url,
            "tag_name": self.tag_name,
            "query": self.query,
            "price": self.price
        }

    @classmethod
    def get_by_id(cls, item_id: str):
        return cls.find_one_by("_id", item_id)
