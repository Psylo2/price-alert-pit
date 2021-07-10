import json
import os

from flask import Blueprint, render_template, request, redirect, url_for, session

from models.store import Store
from models.user import requires_admin, requires_login

store_blueprint = Blueprint('stores', __name__)

@store_blueprint.get('/')
@requires_login
def index():
    _stores = Store.get_all()
    return render_template('stores/index.html', stores=_stores)


@store_blueprint.post('/new')
@requires_admin
def new_store_post():
    name = request.form['name']
    url_prefix = request.form['url_prefix']
    tag_name = request.form['tag_name']
    query = json.loads(request.form['query'])
    Store(name, url_prefix, tag_name, query).save_to_mongo()
    return new_store_get()

@store_blueprint.get('/new')
@requires_admin
def new_store_get():
    return render_template('stores/new_store.html')

@store_blueprint.get('/edit/<string:store_id>')
@requires_admin
def edit_store_get(store_id):
    _store = Store.get_by_id(store_id)
    return render_template('stores/edit_store.html', store=_store)

@store_blueprint.post('/edit/<string:store_id>')
@requires_admin
def edit_store_post(store_id):
    store = Store.get_by_id(store_id)
    store.name = request.form['name']
    store.url_prefix = request.form['url_prefix']
    store.tag_name = request.form['tag_name']
    store.query = eval(request.form['query'])

    return redirect(url_for('.index'))

@store_blueprint.get('/delete/<string:store_id>')
@requires_admin
def delete_store(store_id):
    Store.get_by_id(store_id).remove_from_mongo()
    return redirect(url_for('.index'))
