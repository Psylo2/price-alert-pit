import json

from flask import Blueprint, render_template, request, redirect, url_for

from domain.models.user import requires_admin, requires_login

store_blueprint = Blueprint('stores', __name__)
store_blueprint.handler = None


@store_blueprint.get('/')
@requires_login
def index():
    try:
        all_stores = store_blueprint.handler.all_stores()
        return render_template('stores/index.html', stores=all_stores)
    except Exception as e:
        return e


@store_blueprint.post('/new')
@requires_admin
def new_store_post():
    try:
        query = json.loads(request.form['query'])
        store_blueprint.handler.create_store(name=request.form['name'], url_prefix=request.form['url_prefix'],
                                             tag_name=request.form['tag_name'], query=query)
        return new_store_get()
    except Exception as e:
        return e


@store_blueprint.get('/new')
@requires_admin
def new_store_get():
    return render_template('stores/new_store.html')


@store_blueprint.get('/edit/<string:store_id>')
@requires_admin
def edit_store_get(store_id):
    try:
        store = store_blueprint.handler.get_store(store_id=store_id)
        return render_template('stores/edit_store.html', store=store)
    except Exception as e:
        return e


@store_blueprint.post('/edit/<string:store_id>')
@requires_admin
def edit_store_post(store_id):
    try:
        query = json.loads(request.form['query'])
        store_blueprint.handler.update_store(store_id=store_id,name=request.form['name'],
                                             url_prefix=request.form['url_prefix'],
                                             tag_name=request.form['tag_name'], query=query)
        return redirect(url_for('.index'))
    except Exception as e:
        return e


@store_blueprint.get('/delete/<string:store_id>')
@requires_admin
def delete_store(store_id):
    try:
        store_blueprint.handler.delete_store(store_id=store_id)
        return redirect(url_for('.index'))
    except Exception as e:
        return e

