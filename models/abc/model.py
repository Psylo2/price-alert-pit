from abc import ABCMeta, abstractmethod
from typing import Type, TypeVar, Dict, List, Union
from db.db import Database

T = TypeVar('T', bound="Model")


class Model(metaclass=ABCMeta):
    _collection: str
    _id: str

    def save_to_mongo(self) -> None:
        Database.update(self._collection, {"_id": self._id}, self.json())

    def remove_from_mongo(self) -> None:
        Database.remove(self._collection, {"_id": self._id})

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError

    @classmethod
    def get_all(cls: Type[T]) -> List[T]:
        _elements = Database.find(cls._collection, {})
        return [cls(**_ele) for _ele in _elements]

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: Union[str, Dict]) -> T:
        return cls(**Database.find_one(cls._collection, {attribute: value}))

    @classmethod
    def find_many_by(cls: Type[T], attribute: str, value: [str, Dict]) -> List[T]:
        return [cls(**_ele) for _ele in Database.find(cls._collection, {attribute: value})]
