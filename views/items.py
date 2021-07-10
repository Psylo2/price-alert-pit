from flask import Blueprint, render_template, request, flash

from models.item import Item

item_blueprint = Blueprint('items', __name__)

@item_blueprint.get('/')
def index():
    _items = Item.get_all()
    return render_template('items/index.html', items=_items)


@item_blueprint.post('/new')
def new_item_post():
    url = request.form['url']
    tag_name = request.form['tag_name']
    query = {"id": request.form['_id']}
    Item(url, tag_name, query).save_to_mongo()
    return new_item_get()

@item_blueprint.get('/new')
def new_item_get():
    return render_template('items/new_item.html')