 
from azure.ai.translation.text import TextTranslationClient, TranslatorCredential
from azure.ai.translation.text.models import InputTextItem
#pip install azure-ai-translation-text==1.0.0b1  
client = TextTranslationClient(
    endpoint="https://api.cognitive.microsofttranslator.com/",
    credential=TranslatorCredential(
      key=  "GKOzIUWXq9E1foSFZYMauAbt9CfOUXtqZTQXaQhQXSEH7HOvjE5lJQQJ99BLACYeBjFXJ3w3AAAbACOGOoyX",
        region="eastus")
) 
#print(client.get_supported_languages())
documents=[
               InputTextItem(text= "Seeni")
    ]
source_language="en"
target_language=["ta"]
response=client.translate( 
    content=documents, 
    to=target_language,
    from_parameter=source_language
)
print(response)
 