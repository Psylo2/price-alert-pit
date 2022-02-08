from abc import abstractmethod, ABC
from typing import Union, Dict


class UserHandlerService(ABC):

    @abstractmethod
    def _register_user(self, email: str, password: str) -> None:
        ...

    @abstractmethod
    def _valid_user_login(self, user: Dict, password: str) -> bool:
        ...

    @abstractmethod
    def _validate_user_login(self, user: Dict, password: str) -> bool:
        ...

    @abstractmethod
    def _find_user_by_email(self, email: str) -> Union[Dict, None]:
        ...
