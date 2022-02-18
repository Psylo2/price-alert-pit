from abc import abstractmethod, ABC


class UserUseCase(ABC):

    @abstractmethod
    def user_register(self, email: str, password: str) -> bool:
        ...

    @abstractmethod
    def user_login(self, email: str, password: str) -> bool:
        ...

    @abstractmethod
    def user_logout(self) -> None:
        ...
