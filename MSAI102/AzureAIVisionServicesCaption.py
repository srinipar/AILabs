 
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.vision.imageanalysis.models import VisualFeatures
import json
#pip install azure-ai-vision-imageanalysis
client = ImageAnalysisClient(
    
    endpoint="https://visionsrini.cognitiveservices.azure.com/",
    credential=AzureKeyCredential(
        "3gVCvdUB4zxaOd8vPUP1QKz7gdzWNENqs9pJUFwdiE9I0QZtczosJQQJ99BLACYeBjFXJ3w3AAAFACOG4NnJ")
)
with open("E1.png","rb") as image_file:
    image_details=image_file.read()

response=client.analyze(image_data=image_details, visual_features=[VisualFeatures.CAPTION])
print(json.dumps(response.as_dict(), indent=4))