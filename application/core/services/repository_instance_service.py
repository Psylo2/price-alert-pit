from abc import abstractmethod, ABC


class RepositoryInstanceService(ABC):

    @abstractmethod
    def get_repository(self, repository_name: str) -> "Collection":
        ...

    @abstractmethod
    def create_collection(self, collection_name: str):
        ...
