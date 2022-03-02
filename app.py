from flask import Flask
from dotenv import load_dotenv

load_dotenv(".env", verbose=True)

from interface.views import home_blueprint, alert_blueprint, user_blueprint, store_blueprint, item_blueprint
from infrastructure.repositories import UserRepository, StoreRepository, ItemRepository, AlertRepository

from application.core import RepositoryInstance, AppConfiguration
from application.usecases import UserUseCase, StoreUseCase, ItemUseCase, AlertUseCase


app = Flask(__name__,
            template_folder='interface/gui/templates')

AppConfiguration(app=app)

# Repositories Instance
repository_instance = RepositoryInstance()
user_repository = UserRepository(repository_service=repository_instance)
store_repository = StoreRepository(repository_service=repository_instance)
item_repository = ItemRepository(repository_service=repository_instance)
alert_repository = AlertRepository(repository_service=repository_instance)

# Repositories Services
user_repository_service = user_repository.get_repository()
store_repository_service = store_repository.get_repository()
item_repository_service = item_repository.get_repository()
alert_repository_service = alert_repository.get_repository()

# Use Cases
user_use_case = UserUseCase(repository_service=user_repository_service)
store_use_case = StoreUseCase(repository_service=store_repository_service)
item_use_case = ItemUseCase(repository_service=item_repository_service)
alert_use_case = AlertUseCase(repository_service=alert_repository_service,
                              store_services=store_use_case,
                              item_services=item_use_case)

# Inject Use Cases to Blueprints
user_blueprint.use_case = user_use_case
store_blueprint.use_case = store_use_case
item_blueprint.use_case = item_use_case
alert_blueprint.use_case = alert_use_case


# Register Blueprint
app.register_blueprint(home_blueprint)
app.register_blueprint(item_blueprint,
                       url_prefix="/items")
app.register_blueprint(alert_blueprint,
                       url_prefix="/alerts")
app.register_blueprint(store_blueprint,
                       url_prefix="/stores")
app.register_blueprint(user_blueprint,
                       url_prefix="/users")


@app.before_first_request
def init_db():
    repository_instance.initialize()


if __name__ == "__main__":
    app.run(debug=False)
