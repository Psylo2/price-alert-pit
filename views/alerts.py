from flask import Blueprint, render_template, request, url_for, redirect, session

from models.alert import Alert
from models.item import Item
from models.store import Store
from models.user import requires_login


alert_blueprint = Blueprint('alerts', __name__)


@alert_blueprint.get('/')
@requires_login
def index():
    _alerts = Alert.find_many_by('user_email', session['email'])
    return render_template('alerts/index.html', alerts=_alerts)


@alert_blueprint.post('/new')
@requires_login
def new_alert_post():
    alert_name = request.form['name']
    item_url = request.form['item_url']
    price_limit = request.form['price_limit']
    store = Store.find_by_url(item_url)
    item = Item(item_url, store.tag_name, store.query)
    item.fetch_price()
    item.save_to_mongo()

    Alert(alert_name, item._id,
          float(price_limit),
          session['email']).save_to_mongo()
    return new_alert_get()


@alert_blueprint.get('/new')
@requires_login
def new_alert_get():
    return render_template('alerts/new_alert.html')

@alert_blueprint.get('/edit/<string:alert_id>')
@requires_login
def edit_alert_get(alert_id):
    _alert = Alert.get_by_id(alert_id)
    return render_template('alerts/edit_alert.html', alert=_alert)

@alert_blueprint.post('/edit/<string:alert_id>')
@requires_login
def edit_alert_post(alert_id):
    alert = Alert.get_by_id(alert_id)
    price_limit = float(request.form['price_limit'])
    alert.price_limit = price_limit
    alert.save_to_mongo()
    return redirect(url_for('.index'))

@alert_blueprint.get('/delete/<string:alert_id>')
@requires_login
def delete_alert(alert_id):
    alert = Alert.get_by_id(alert_id)
    if alert.user_email == session['email']:
        alert.remove_from_mongo()
    return redirect(url_for('.index'))
