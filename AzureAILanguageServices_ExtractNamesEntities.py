 
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential 
 
#pip install azure-ai-textanalytics
client = TextAnalyticsClient(
    endpoint="https://ailangservice200.cognitiveservices.azure.com/",
    credential=AzureKeyCredential(
        "5JXc0vdxUB1XwA9jk9sp11oV7a90Bwg0inYrskyLvF7T6fjUewQxJQQJ99BLACYeBjFXJ3w3AAAaACOGzaTz")
) 
response=client.recognize_entities(
    documents=[
                "I am srini, working as Consultant, it is not good" , 
                "My finance are great",
                "Microsoft is great"
    ]

    
)

for resp in response: 
    print(resp.entities )