
#https://azurestorageacc2000.blob.core.windows.net/uploads/Sample-pdf.pdf
#pip install  azure-ai-documentintelligence==1.0.0b4

from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential 
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.ai.documentintelligence.models import AnalyzeResult

from azure.ai.textanalytics import TextAnalyticsClient 

endpoint="https://azuredocumentintell.cognitiveservices.azure.com/"
key="9Bxw16fcI0cTGvCJQnNaDQheyHyTufQNXXha4UArvpeiaYfSswQgJQQJ99BLACYeBjFXJ3w3AAALACOGNmWK"
documenturl="https://azurestorageacc2000.blob.core.windows.net/uploads/sample-local-pdf.pdf"

language_endpoint="https://ailangservice200.cognitiveservices.azure.com/"
language_key="5JXc0vdxUB1XwA9jk9sp11oV7a90Bwg0inYrskyLvF7T6fjUewQxJQQJ99BLACYeBjFXJ3w3AAAaACOGzaTz"
textAnalyticsClient = TextAnalyticsClient(endpoint=language_endpoint, credential=AzureKeyCredential(language_key))

client= DocumentIntelligenceClient(endpoint=endpoint, credential=AzureKeyCredential(key=key))

response=client.begin_analyze_document("prebuilt-read",AnalyzeDocumentRequest(url_source=documenturl))

result: AnalyzeResult=response.result()

documents=[]
for each_page in result.pages:
    for index, line in enumerate(each_page.lines):
        documents.append(line.content)


language_response=textAnalyticsClient.analyze_sentiment(documents=documents)

for result in language_response:
    print(f"{result.sentences}")
