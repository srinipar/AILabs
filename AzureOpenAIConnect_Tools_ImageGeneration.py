import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_version="2025-03-01-preview",
    azure_endpoint="https://srini-mih5qttt-eastus2.cognitiveservices.azure.com/",
    api_key="951MeJX1BMHjXcyY6QfrHXiRX5afcAO3xl3k9kdx7OnPuLkSD91wJQQJ99BKACHYHv6XJ3w3AAAAACOGjUHk",
)
 
response = client.responses.create(
    input=[
        {
            "role": "system",
            "content": "You are a assistant like Rajnikanth to describe the image.",
        },
        {
            "role": "user",
            "content": "Explain me about the python"
                 
        }
    ],
    max_output_tokens=16384,
    temperature=1.0,
    top_p=1.0,
    model="gpt-5-chat"
)
print(response.output_text)

print(response)