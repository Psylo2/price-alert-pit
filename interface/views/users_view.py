from flask import Blueprint, request, url_for, render_template, redirect

from application.usecases.services import UserUseCaseService

user_blueprint = Blueprint(name='users',
                           import_name=__name__)
user_blueprint.__setattr__("use_case", UserUseCaseService)


@user_blueprint.get('/register')
def register_get():
    return render_template('users/register.html')


@user_blueprint.post('/register')
def register_post():
    try:
        email = request.form.get('email', default="", type=str)
        password = request.form.get('password', default="", type=str)
        user_blueprint.use_case.user_register(email=email,
                                              password=password)
        return register_get()
    except Exception as e:
        return e


@user_blueprint.get('/login')
def login_get():
    return render_template('users/login.html')


@user_blueprint.post('/login')
def login_post():
    try:
        email = request.form.get(key='email', default="", type=str)
        password = request.form.get('password', default="", type=str)
        if user_blueprint.use_case.user_login(email=email,
                                              password=password):
            return redirect(url_for('alerts.index'))
        return login_get()

    except Exception as e:
        return e


@user_blueprint.get('/logout')
def logout():
    try:
        user_blueprint.use_case.user_logout()
        return redirect(url_for('users.login_get'))
    except Exception as e:
        return e
