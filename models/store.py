import re
import uuid
from typing import Dict
from dataclasses import dataclass, field

from models.abc.model import Model

@dataclass(eq=False)
class Store(Model):
    _collection: str = field(init=False, default="stores")
    name: str
    url_prefix: str
    tag_name: str
    query: Dict
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self) -> Dict:
        return {

            "_id": self._id,
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query
        }

    @classmethod
    def get_by_url_prefix(cls, _url_prefix: str) -> "Store":
        url_regex = {"$regex": f"^{_url_prefix}"}
        return cls.find_one_by("url_prefix", url_regex)

    @classmethod
    def find_by_url(cls, _url: str) -> "Store":
        pattern = re.compile(r"(http*s?://.*?/)")
        match = pattern.match(_url)
        url_prefix = match.group(1)
        return cls.get_by_url_prefix(url_prefix)

    @classmethod
    def get_by_id(cls, store_id: str):
        return cls.find_one_by("_id", store_id)




