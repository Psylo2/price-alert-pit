from flask import Blueprint, session, request, url_for, render_template, redirect, flash

from models.user import User, UserErrors

user_blueprint = Blueprint('users', __name__)


@user_blueprint.get('/register')
def register_get():
    return render_template('users/register.html')


@user_blueprint.post('/register')
def register_post():
    email = request.form['email']
    password = request.form['password']
    try:
        User.register_user(email, password)
        session['email'] = email

        return redirect(url_for('alerts.index'))

    except UserErrors.UserError as e:
        print(e.message)
        return login_get()


@user_blueprint.get('/login')
def login_get():
    return render_template('users/login.html')


@user_blueprint.post('/login')
def login_post():
    email = request.form['email']
    password = request.form['password']
    try:
        if User.valid_login(email, password):
            session['email'] = email

            return redirect(url_for('alerts.index'))

    except UserErrors.UserError as e:
        return e.message

    return login_get()


@user_blueprint.get('/logout')
def logout():
    session['email'] = None
    return redirect(url_for('users.login_get'))
