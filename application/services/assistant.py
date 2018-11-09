from watson_developer_cloud import AssistantV1
from watson_developer_cloud import WatsonApiException
#from application.config import watson_config as config
import json

class Assistant:

    init_status=False
    def __init__(self, version, username, password, workspace_id, endpoint=None):
        self.username=username
        self.password=password
        self.endpoint=endpoint
        self.version=version
        self.workspace_id=workspace_id
        
        if(endpoint==None):
            self.endpoint="https://gateway.aibril-watson.kr/assistant/api"
        if(version==None):
            self.version="2018-02-16"
        
        self.initial_call()

    
    def initial_call(self):
        try:
            assistant = AssistantV1(version=self.version, username=self.username, password=self.password, url=self.endpoint)
            response = assistant.message(workspace_id=self.workspace_id, input={'text': ''})

            self.init_status=True
        except WatsonApiException as ex:
            print("Method failed with status code {} : {}".format(str(ex.code),ex.message))
            self.init_status=False
        

"""
{
"url" : "https://gateway.aibril-watson.kr/assistant/api",
"username" : "2f27a362-a5da-4f9a-9877-7fdfb77b7942",
"password" : "22jeKRq4lkV1" 
 Workspace ID: "66a052f0-cc1b-492b-9b05-4a84b0b10fc8"
}
"""