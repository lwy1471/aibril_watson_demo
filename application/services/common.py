from flask import Response
import json
from functools import wraps


#using Function
def response_200(dictionary):
    response = json.dumps(dictionary)
    return Response(response, status=200, mimetype='application/json')

def response_500(errMsg):
    response = json.dumps(errMsg)
    return Response(response, status=500, mimetype='application/json')
        
#not usings
def json_response(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        res=f(*args, **kwargs)
        res=json.dumps(res, ensure_ascii=False).encode('utf8')
    return decorated_function