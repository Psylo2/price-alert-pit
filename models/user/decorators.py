import functools
from typing import Callable
from flask import session, flash, redirect, url_for, current_app

def requires_login(fun: Callable) -> Callable:
    @functools.wraps(fun)
    def decorated_function(*args, **kwargs):
        if not session.get('email'):
            flash('You need to be singed in fot this page', 'danger')
            return redirect(url_for('users.login_get'))
        return fun(*args, **kwargs)
    return decorated_function

def requires_admin( fun: Callable) -> Callable:
    @functools.wraps(fun)
    def decorated_function(*args, **kwargs):
        if session.get('email') != current_app.config.get('ADMIN'):
            flash('You need to be administrator to access this page', 'danger')
            return redirect(url_for('users.login_get'))
        return fun(*args, **kwargs)
    return decorated_function