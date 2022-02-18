from flask import Blueprint, render_template, request, url_for, redirect

from domain.models.user import requires_login

alert_blueprint = Blueprint('alerts', __name__)
alert_blueprint.handler = None


@alert_blueprint.get('/')
@requires_login
def index():
    try:
        all_user_alerts = alert_blueprint.handler.all_user_alerts()
        return render_template('alerts/index.html', alerts=all_user_alerts)
    except Exception as e:
        return e


@alert_blueprint.post('/new')
@requires_login
def new_alert_post():
    try:
        alert_blueprint.handler.create_alert(alert_name=request.form['name'],
                                             item_url=request.form['item_url'],
                                             price_limit=request.form['price_limit'])
        return new_alert_get()
    except Exception as e:
        return e


@alert_blueprint.get('/new')
@requires_login
def new_alert_get():
    return render_template('alerts/new_alert.html')


@alert_blueprint.get('/edit/<string:alert_id>')
@requires_login
def edit_alert_get(alert_id):
    try:
        alert = alert_blueprint.handler.get_alert(alert_id=alert_id)
        return render_template('alerts/edit_alert.html', alert=alert)
    except Exception as e:
        return e


@alert_blueprint.post('/edit/<string:alert_id>')
@requires_login
def edit_alert_post(alert_id):
    try:
        price_limit = request.form['price_limit']
        alert_blueprint.handler.update_alert(alert_id=alert_id, price_limit=price_limit)
        return redirect(url_for('.index'))
    except Exception as e:
        return e


@alert_blueprint.get('/delete/<string:alert_id>')
@requires_login
def delete_alert(alert_id):
    try:
        alert_blueprint.handler.delete_alert(alert_id=alert_id)
        return redirect(url_for('.index'))
    except Exception as e:
        return e

