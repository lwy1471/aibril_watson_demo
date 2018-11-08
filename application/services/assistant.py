from watson_developer_cloud import AssistantV1
#from application.config import watson_config as config
import json

class Assistant():
    username=None
    password=None
    endpoint=None
    
    assistant=None
    
    def __init__(version, username, password, endpoint=None):
        username=username
        password=password
        endpoint=endpoint
        
        if(endpoint==None):
            endpoint="https://gateway.aibril-watson.kr/assistant/api"
        if(version==None):
            version="2018-02-16"
        
        assistant = AssistantV1(version="2018-02-16", username=username, password=password, url=endpoint)
        response = assistant.message(workspace_id="66a052f0-cc1b-492b-9b05-4a84b0b10fc8", input={'text': '예약'})
        print(json.dumps(response, indent=2))

        

"""
{
"url" : "https://gateway.aibril-watson.kr/assistant/api",
"username" : "2f27a362-a5da-4f9a-9877-7fdfb77b7942",
"password" : "22jeKRq4lkV1" 
 Workspace ID: 66a052f0-cc1b-492b-9b05-4a84b0b10fc8
}
"""