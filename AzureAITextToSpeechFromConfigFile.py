 
import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential
 
import json
#pip install azure-cognitiveservices-speech
config=speechsdk.SpeechConfig(
    subscription= "4tXVumCrndQOUyveK7n7kgVAOQKR4MxZHypWi7eaCHlEUDDxBrFoJQQJ99BLACYeBjFXJ3w3AAAEACOGfKxL",
                    endpoint=  "https://aiaiservicesazure200.cognitiveservices.azure.com/" ) 
output_file="speechSriniFromConfigFile.wav" 
audio_output=speechsdk.audio.AudioConfig(filename=output_file) 
speech_generator=speechsdk.SpeechSynthesizer(speech_config=config, audio_config=audio_output) 

with open("speechConfig.xml","r", encoding="utf-8") as configFile:
    ssmConfigs=configFile.read()

#print(ssmConfigs)    

result=speech_generator.speak_ssml(ssmConfigs) 

if result.reason==speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Done")
