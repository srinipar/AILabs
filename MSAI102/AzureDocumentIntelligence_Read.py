
#https://azurestorageacc2000.blob.core.windows.net/uploads/Sample-pdf.pdf
#pip install  azure-ai-documentintelligence==1.0.0b4

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential 
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult

endpoint="https://azuredocumentintell.cognitiveservices.azure.com/"
key="9Bxw16fcI0cTGvCJQnNaDQheyHyTufQNXXha4UArvpeiaYfSswQgJQQJ99BLACYeBjFXJ3w3AAALACOGNmWK"
documenturl="https://azurestorageacc2000.blob.core.windows.net/uploads/Sample-pdf.pdf"


client= DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key=key))

response=client.begin_analyze_document("prebuilt-read",AnalyzeDocumentRequest(url_source=documenturl))

result: AnalyzeResult=response.result()

for index, para in enumerate(result.paragraphs):
    print(f"Para {index+1}::{para}")