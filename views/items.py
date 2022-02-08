from flask import Blueprint, render_template, request

item_blueprint = Blueprint('items', __name__)
item_blueprint.handler = None


@item_blueprint.get('/')
def index():
    try:
        all_items = item_blueprint.handler.all_items()
        return render_template('items/index.html', items=all_items)
    except Exception as e:
        return e


@item_blueprint.post('/new')
def new_item_post():
    try:
        query = {"id": request.form['_id']}
        item_blueprint.handler.save_item(url=request.form['url'],
                                         tag_name=request.form['tag_name'],
                                         query=query)
        return new_item_get()
    except Exception as e:
        return e


@item_blueprint.get('/new')
def new_item_get():
    return render_template('items/new_item.html')
