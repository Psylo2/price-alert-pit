import uuid
from typing import Dict, Union
from dataclasses import dataclass, field

from models.abc.model import Model
from models.user import User
from models.item import Item


@dataclass(eq=False)
class Alert(Model):
    _collection: str = field(init=False, default="alerts")
    name: str
    item_id: str
    price_limit: float
    user_email: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __post_init__(self):
        self.item = Item.get_by_id(self.item_id)
        self.user = User.find_by_email(self.user_email)

    def json(self) -> Dict:
        return {

            "_id": self._id,
            "name": self.name,
            "price_limit": self.price_limit,
            "item_id": self.item_id,
            "user_email": self.user_email
        }

    def load_item_price(self) -> float:
        return self.item.fetch_price()

    def notify_reach_price(self) -> bool:
        if self.item.price < self.price_limit:
            return True

    @classmethod
    def get_by_id(cls, alert_id: str) -> "Alert":
        return cls.find_one_by("_id", alert_id)
