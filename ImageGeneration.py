import os
from openai import AzureOpenAI
import requests

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://srini-mih6pbyc-swedencentral.cognitiveservices.azure.com/",
    api_key="1KOw5duE0wXGPQ7HpmNyLxtyLyACgJvy9Uz8C4Wg4qUGXcEshGAQJQQJ99BKACfhMk5XJ3w3AAAAACOGEgW7",
)
 
response = client.images.generate(
    model="dall-e-3",
    prompt="A Dog",
    n=1,
    size="1024x1024"
)
image1_url=response.data[0].url
image1_data=requests.get(image1_url).content
with open("imagegeneration1.png", "wb") as handler:
    handler.write(image1_data)
print("Done")