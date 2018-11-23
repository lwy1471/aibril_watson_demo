#-*-coding: utf-8 -*-

from flask import Flask, render_template, request, Response, Blueprint, flash, jsonify, g
from application.services.assistant import Assistant
import json


print('in controller')

class ApiContoller:
    api_app = Blueprint('apis', __name__, template_folder="templates", static_folder="static")
    g.assistantModel = None

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
        g.assistantModel = Assistant(version=None, username="2f27a362-a5da-4f9a-9877-7fdfb77b7942", password="22jeKRq4lkV1")
        return ("True" if g.assistantModel.init_status else "False")

    @api_app.route('/assistant')
    def assistant():
        return render_template('assistant.html')
        
    @api_app.route('/assistant/InitService',methods=['POST'])
    def assistantInitService():
        g.assistantModel = Assistant(version=None, username=request.form['username'],\
        password=request.form['password'],\
        workspace_id=request.form['workspaceId'])
        
        print(g.assistantModel.init_status)
        status = True if g.assistantModel.init_status else False

        # Assistant Authorizing errror
        if status==False:
            data = {'Message':'Assistant Access is Denied : Invalid credentials'}
            err_response = Response(json.dumps(data), status=403, mimetype='application/json')
            return err_response

        return json.dumps(request.form, ensure_ascii=False)

        
    @api_app.route('/assistant/sendMessage',methods=['POST'])
    def sendMessage():
        g.assistantModel.sendMessage(request.form['text'])
        print('hi')
        pass