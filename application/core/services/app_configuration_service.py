from abc import ABC, abstractmethod

class AppConfigurationService(ABC):

    @abstractmethod
    def _activate_configuration(self) -> None:
        ...
