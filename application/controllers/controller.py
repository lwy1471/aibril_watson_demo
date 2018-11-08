#-*-coding: utf-8

from flask import Flask, render_template, request, Response, Blueprint
from application.services.assistant import Assistant
import json


print('in controller')

api_app = Blueprint('api', __name__)

@api_app.route("/member")
#@login_required
def member_page():
    return "member_page"

@api_app.route('/apis/')
def hello():
	return render_template('apis.html')

    
# Test 용
@api_app.route('/apis/assistant_test')
def assistant_test():
    a = Assistant(username="2f27a362-a5da-4f9a-9877-7fdfb77b7942", password="22jeKRq4lkV1")
    return "hi"

@api_app.route('/apis/assistant')
def assistant():
    return render_template('assistant.html')
    
@api_app.route('/apis/assistant/getService',methods=['GET','POST'])
def assistantGetService():
    if (request.method=='POST'):
        username = request.form['username']
        password = request.form['password']
        workspaceId = request.form['workspaceId']
        
      
        return json.dumps(request.form, ensure_ascii=False)
    else:
        return "bye"
