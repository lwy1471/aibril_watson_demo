#-*-coding: utf-8 -*-

from flask import Flask, render_template, request, Response, Blueprint, flash, jsonify, session
from application.services.assistant import Assistant
import json
from application.services.common import *


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
        initRes=assistantModel.initial_message()
        
        if(assistantModel.status!=False):
            welcomeMsg = initRes['output']['text']

            #Set Session
            session['username'] = request.form['username']
            session['password'] = request.form['password']
            session['workspaceId'] = request.form['workspaceId']
            session['context'] = None

            resData = {'text':'인증에 성공하였습니다.', 'welcomeMsg': welcomeMsg}
            
            return response_200(resData)
        else:
            print('Service authorizing Error')
            errMsg = {'err':"서비스 인증에 실패하였습니다."}
            return response_500(errMsg)


    @api_app.route('/assistant/sendMessage',methods=['POST'])
    def sendMessage():
        assistantModel = Assistant(version=None, username=session['username'],\
        password=session['password'],\
        workspace_id=session['workspaceId'])
        
        if(assistantModel.status!=False):
            #Set Context Session
            session['context'] = request.form['context']
            
            userInput = request.form['text']
            
            if len(request.form['context'])==0:
                session['context'] = {}

            resData = assistantModel.sendMessage(userInput, session['context'])
            return response_200(resData)
        else:
            errMsg = "서비스 인증에 실패하였습니다."
            return response_500(errMsg)       
        

