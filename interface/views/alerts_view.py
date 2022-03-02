from flask import Blueprint, render_template, request, url_for, redirect

from application.usecases.services import AlertUseCaseService
from domain.models.user import requires_login


alert_blueprint = Blueprint(name='alerts',
                            import_name=__name__)
alert_blueprint.__setattr__("use_case", AlertUseCaseService)


@alert_blueprint.get('/')
@requires_login
def index():
    try:
        all_user_alerts = alert_blueprint.use_case.all_user_alerts()
        return render_template('alerts/index.html', alerts=all_user_alerts)
    except Exception as e:
        return e


@alert_blueprint.post('/new')
@requires_login
def new_alert_post():
    try:
        alert_blueprint.use_case.create_alert(alert_name=request.form['name'],
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
        alert = alert_blueprint.use_case.get_alert(alert_id=alert_id)
        return render_template('alerts/edit_alert.html', alert=alert)
    except Exception as e:
        return e


@alert_blueprint.post('/edit/<string:alert_id>')
@requires_login
def edit_alert_post(alert_id):
    try:
        price_limit = request.form['price_limit']
        alert_blueprint.use_case.update_alert(alert_id=alert_id, price_limit=price_limit)
        return redirect(url_for('.index'))
    except Exception as e:
        return e


@alert_blueprint.get('/delete/<string:alert_id>')
@requires_login
def delete_alert(alert_id):
    try:
        alert_blueprint.use_case.delete_alert(alert_id=alert_id)
        return redirect(url_for('.index'))
    except Exception as e:
        return e

