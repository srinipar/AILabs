import os
from openai import AzureOpenAI
import base64

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://srini-mih5qttt-eastus2.cognitiveservices.azure.com/",
    api_key="951MeJX1BMHjXcyY6QfrHXiRX5afcAO3xl3k9kdx7OnPuLkSD91wJQQJ99BKACHYHv6XJ3w3AAAAACOGjUHk",
)
with open("E1.jpg","rb") as image_file:
    image_details=base64.b64encode(image_file.read()).decode("utf-8")
#print(image_details)
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a assistant like Rajnikanth to describe the image.",
        },
        {
            "role": "user",
            "content": [
                {
                "type":"text",
                "text":"Explain me about the image"
                },
                {
                "type":"image_url",
                "image_url":{
                    "url":f"data:image/png;base64,{image_details}"
                }
                }
                ],
        }
    ],
    max_tokens=16384,
    temperature=1.0,
    top_p=1.0,
    model="gpt-5-chat"
)
print(response.choices[0].message.content)