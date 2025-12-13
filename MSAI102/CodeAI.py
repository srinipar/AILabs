import os
from openai import AzureOpenAI
import base64

client = AzureOpenAI(
    api_version="2024-12-01-preview",
    azure_endpoint="https://srini-mih5qttt-eastus2.cognitiveservices.azure.com/",
    api_key="951MeJX1BMHjXcyY6QfrHXiRX5afcAO3xl3k9kdx7OnPuLkSD91wJQQJ99BKACHYHv6XJ3w3AAAAACOGjUHk",
)
with open("01.py","r",encoding="utf-8") as  code_file:
    code=code_file.read()
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a assistant like Rajnikanth to describe the code.",
        },
        {
            "role": "user",
            "content": [
                {
                "type":"text",
                "text":f"Explain me about the code : {code}"
                },
                ],
        }
    ],
    max_tokens=16384,
    temperature=1.0,
    top_p=1.0,
    model="gpt-5-chat"
)
print(response.choices[0].message.content)