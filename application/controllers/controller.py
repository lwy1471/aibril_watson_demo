#-*-coding: utf-8 -*-

from flask import Flask, render_template, request, Response, Blueprint, flash, jsonify, session, make_response
from application.services.assistant import Assistant
import json
from application.services.common import json_response

print('in controller')

class ApiContoller:
    api_app = Blueprint('apis', __name__, template_folder="templates", static_folder="static")

    @api_app.route('/')
    def hello():
        return render_template('apis.html')

    @api_app.route('/assistant')
    def assistant():
        return render_template('assistant.html')
    
    @api_app.route('/assistant/initService',methods=['POST'])
    def assistantInitService():
        assistantModel = Assistant(version=None, username=request.form['username'],\
        password=request.form['password'],\
        workspace_id=request.form['workspaceId'])
        init = assistantModel.initial_message()
        
        welcomeMsg = init['output']['text']
        
        status = True if assistantModel.init_status else False      
        # Assistant Authorizing errror
        """
        if status==False:
            data = {'Message':'Assistant Access is Denied : Invalid credentials'}
            err_response = Response(json.dumps(data), status=403, mimetype='application/json')
            return err_response
        """

        #Set Session
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        session['workspaceId'] = request.form['workspaceId']

        resData = {'text':'인증에 성공하였습니다.', 'welcomeMsg': welcomeMsg}
        res = make_response(json.dumps(resData))
        res.headers['Content-type'] = 'application/json'
        return res


    @api_app.route('/assistant/sendMessage',methods=['POST'])
    @json_response
    def sendMessage():

        assistantModel = Assistant(version=None, username=session['username'],\
        password=session['password'],\
        workspace_id=session['workspaceId'])
        
        userInput = request.form['text']
        context = request.form['context']
        resData = assistantModel.sendMessage(userInput, context)
        
        res = make_response(json.dumps(resData, ensure_ascii=False))
        res.headers['Content-type'] = 'application/json'
        print(json.dumps(resData, indent=2, ensure_ascii=False))
        return res