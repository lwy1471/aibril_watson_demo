#-*-coding: utf-8 -*-

from flask import Flask, render_template, request, Response, Blueprint, flash, jsonify
from application.services.assistant import Assistant
import json


print('in controller')

api_app = Blueprint('apis', __name__, template_folder="templates", static_folder="static")

@api_app.route("/member")
#@login_required
def member_page():
    return "member_page"

@api_app.route('/')
def hello():
	return render_template('apis.html')

    
# Test 용
@api_app.route('/assistant_test')
def assistant_test():
    init = Assistant(version=None, username="2f27a362-a5da-4f9a-9877-7fdfb77b7942", password="22jeKRq4lkV1")
    return ("True" if init.init_status else "False")

@api_app.route('/assistant')
def assistant():
    return render_template('assistant.html')
    
@api_app.route('/assistant/InitService',methods=['POST'])
def assistantInitService():
    init = Assistant(version=None, username=request.form['username'],\
    password=request.form['password'],\
    workspace_id=request.form['workspaceId'])
    
    print(init.init_status)
    status = True if init.init_status else False
    
    
    # Assistant Authorizing errror
    if status==False:
        data = {'Message':'Assistant Access is Denied : Invalid credentials'}
        err_response = Response(json.dumps(data), status=403, mimetype='application/json')
        return err_response
        

    return json.dumps(request.form, ensure_ascii=False)
