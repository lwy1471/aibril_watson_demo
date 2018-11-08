from flask import Flask, render_template, request, Response, Blueprint
import json
#from decorators import *

print('in controller')

api_app = Blueprint('api', __name__)

@api_app.route("/member")
#@login_required
def member_page():
    return "member_page"

@api_app.route('/apis/')
def hello():
	return render_template('apis.html')

@api_app.route('/apis/assistant_old')
def assistant_old():
    return render_template('assistant_test.html')

@api_app.route('/apis/assistant')
def assistant():
    return render_template('assistant.html')
    
@api_app.route('/apis/assistant/getService',methods=['GET','POST'])
def assistantGetService():
    if (request.method=='POST'):
        
        username = request.form['username']
        password = request.form['password']
        workspaceId = request.form['workspaceId']
        
      
        return json.dumps(request.form)
    else:
        return "bye"
