#pip install azure.ai.language.conversations
from azure.ai.language.conversations import ConversationAnalysisClient
from azure.core.credentials import AzureKeyCredential

endpoint="https://ailangservice200.cognitiveservices.azure.com/"
key="5JXc0vdxUB1XwA9jk9sp11oV7a90Bwg0inYrskyLvF7T6fjUewQxJQQJ99BLACYeBjFXJ3w3AAAaACOGzaTz"

client= ConversationAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

utternace="I need room for me"
project_name="ConversationLanguageUnderstanding"
deployment_name="Dep"

response=client.analyze_conversation(
    task={
        "kind":"Conversation",
            "analysisInput":{
               "conversationItem":{
                    "participantId":"1",
                    "id":"1",
                    "modality":"text",
                    "language" :"en",
                    "text":utternace 

               },     
               "isLoggingEnabled":False 
            },
            "parameters":{
                    "projectName":project_name,
                    "deploymentName":deployment_name 
            } 
    } 
)

print(response)