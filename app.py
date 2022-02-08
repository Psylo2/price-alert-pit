import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv(".env", verbose=True)

from manager import Repository, AppConfiguration
repository = Repository()

from handlers import UserHandler, AlertHandler, StoreHandler, ItemHandler
from views import home_blueprint, alert_blueprint, user_blueprint, store_blueprint, item_blueprint

app = Flask(__name__)

AppConfiguration(app=app)

@app.before_first_request
def init_db():
    repository.initialize()


# handlers
user_handler = UserHandler(repository=repository)
store_handler = StoreHandler(repository=repository)
item_handler = ItemHandler(repository=repository)
alert_handler = AlertHandler(repository=repository,
                             store_handler=store_handler,
                             item_handler=item_handler)

# inject handlers to blueprints
user_blueprint.handler = user_handler
store_blueprint.handler = store_handler
alert_blueprint.handler = alert_handler
item_blueprint.handler = item_handler

app.register_blueprint(home_blueprint)
app.register_blueprint(item_blueprint,
                       url_prefix="/items")
app.register_blueprint(alert_blueprint,
                       url_prefix="/alerts")
app.register_blueprint(store_blueprint,
                       url_prefix="/stores")
app.register_blueprint(user_blueprint,
                       url_prefix="/users")

if __name__ == "__main__":
    app.run(debug=True)
