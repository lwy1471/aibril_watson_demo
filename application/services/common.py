from flask import Response
import json
from functools import wraps

def json_response(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        res=f(*args, **kwargs)
        res=json.dumps(res, ensure_ascii=False).encode('utf8')
    return decorated_function