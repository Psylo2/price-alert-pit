import os

from application.core.services import AppConfigurationService


class AppConfiguration(AppConfigurationService):
    def __init__(self, app):
        self._app = app
        self._activate_configuration()

    def _activate_configuration(self) -> None:
        self._app.secret_key = os.environ.get('APP_SECRET_KEY')
        self._app.config.update(ADMIN=os.environ.get('ADMIN'))
