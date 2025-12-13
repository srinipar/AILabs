 
import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential
 
import json
#pip install azure-cognitiveservices-speech
config=speechsdk.SpeechConfig(
    subscription= "4tXVumCrndQOUyveK7n7kgVAOQKR4MxZHypWi7eaCHlEUDDxBrFoJQQJ99BLACYeBjFXJ3w3AAAEACOGfKxL",
                    endpoint=  "https://aiaiservicesazure200.cognitiveservices.azure.com/" )
config.speech_synthesis_voice_name="en-US-SteffanMultilingualNeural"

input="Hello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself Srini"

output_file="speechSrini.wav"

audio_output=speechsdk.audio.AudioConfig(filename=output_file)

speech_generator=speechsdk.SpeechSynthesizer(speech_config=config, audio_config=audio_output)

result=speech_generator.speak_text(input).get()

if result.reason==speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Done")
