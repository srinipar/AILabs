 
from azure.ai.vision.face import FaceClient
from azure.ai.vision.face.models import *
from azure.core.credentials import AzureKeyCredential 

import json
#pip install azure-ai-vision-face
client = FaceClient(
    
    endpoint="https://aiface400.cognitiveservices.azure.com/",
    credential=AzureKeyCredential(
        "DoTpMpkV218xlfkw6xsWFHVVEEOPfkrsJNIegUzkUlvTkqrwodflJQQJ99BLACYeBjFXJ3w3AAAKACOGNr1H")
)

face_features=[
FaceAttributeTypeDetection01.HEAD_POSE,
FaceAttributeTypeDetection01.GLASSES

]

with open("face.avif","rb") as image_file:
    image_details=image_file.read()

response=client.detect(
    image_content=image_details, 
                       detection_model=FaceDetectionModel.DETECTION01,
                       recognition_model=FaceRecognitionModel.RECOGNITION01,
                       return_face_id=False
                       )
print(json.dumps(response.as_dict(), indent=4))