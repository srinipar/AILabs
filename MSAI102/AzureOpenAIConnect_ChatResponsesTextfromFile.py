import os
from openai import AzureOpenAI
import base64

client = AzureOpenAI(
    api_version="2025-03-01-preview",
    azure_endpoint="https://srini-mih5qttt-eastus2.cognitiveservices.azure.com/",
    api_key="951MeJX1BMHjXcyY6QfrHXiRX5afcAO3xl3k9kdx7OnPuLkSD91wJQQJ99BKACHYHv6XJ3w3AAAAACOGjUHk",
)
file=client.files.create(
    file=open("Sample-pdf.pdf","rb"),
    purpose="assistants"
)
 
response = client.responses.create(
    input=[
         
        {
            "role": "user",
            "content":[
                {
                    "type":"input_text",
                    "text":"Explain about this file"                            
                },
                {
                    "type":"input_file",
                    "file_id":file.id                            
                }

            ]
                 
        }
    ],
    max_output_tokens=16384,
    temperature=1.0,
    top_p=1.0,
    model="gpt-5-chat",
    stream=True
)
for event in response:
    if event.type=="response.output_text.delta":
        print(event.delta,end="", flush=True)
    elif event.type=="response.output_text.done":
        print("")

#print(response.output_text)

#print(response)