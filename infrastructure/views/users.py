from flask import Blueprint, request, url_for, render_template, redirect

user_blueprint = Blueprint('users', __name__)
user_blueprint.handler = None

@user_blueprint.get('/register')
def register_get():
    return render_template('users/register.html')


@user_blueprint.post('/register')
def register_post():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user_blueprint.handler.user_register(email=email,
                                             password=password)
        return register_get()
    except Exception as e:
        return e

@user_blueprint.get('/login')
def login_get():
    return render_template('users/login.html')

@user_blueprint.post('/login')
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        if user_blueprint.handler.user_login(email=email,
                                             password=password):
            return redirect(url_for('alerts.index'))
        return login_get()

    except Exception as e:
        return e

@user_blueprint.get('/logout')
def logout():
    try:
        user_blueprint.handler.user_logout()
        return redirect(url_for('users.login_get'))
    except Exception as e:
        return e

