from functools import wraps
from flask import session, url_for

def login_required(f):
    @wraps(f)
    print("hi")
    def login_decorated(*args, **kwargs):
        if session.get('user', None) is None:
            return "you have to log in"
        return f(*args, **kwargs)
    return login_decorated