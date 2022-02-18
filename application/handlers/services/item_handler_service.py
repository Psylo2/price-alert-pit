from abc import abstractmethod, ABC


class ItemHandlerService(ABC):

    @abstractmethod
    def _fetch_price(self, item: "ItemModel") -> float:
        ...

    @abstractmethod
    def _price(self, item: "ItemModel", price: str) -> float:
        ...

    @abstractmethod
    def _clean_string_price(self, price: str) -> float:
        ...
