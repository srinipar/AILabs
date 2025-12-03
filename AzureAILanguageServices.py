 
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential 

import json
#pip install azure-ai-textanalytics
client = TextAnalyticsClient(
    endpoint="https://ailangservice200.cognitiveservices.azure.com/",
    credential=AzureKeyCredential(
        "5JXc0vdxUB1XwA9jk9sp11oV7a90Bwg0inYrskyLvF7T6fjUewQxJQQJ99BLACYeBjFXJ3w3AAAaACOGzaTz")
)

with open("face.jpg","rb") as image_file:
    image_details=image_file.read()

response=client.detect_language(
    documents=[
  {
               "id":"1",
               "text":"நான்" 
           },
           {
                "id":"2",
                "text":"aaja"
           } 

    ]
)
print(response)