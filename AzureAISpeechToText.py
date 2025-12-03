import json
import azure.cognitiveservices.speech as speechsdk
 
#pip install azure-cognitiveservices-speech
config=speechsdk.SpeechConfig(
    subscription= "4tXVumCrndQOUyveK7n7kgVAOQKR4MxZHypWi7eaCHlEUDDxBrFoJQQJ99BLACYeBjFXJ3w3AAAEACOGfKxL",
                    endpoint=  "https://aiaiservicesazure200.cognitiveservices.azure.com/" ) 
config.speech_synthesis_voice_name="en-US-SteffanMultilingualNeural"

input="Hello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself SriniHello, How are you, myself Srini"

output_file="speechTrasnscribed.txt"
audio_fileName="speechSrini.wav"
config.speech_recognition_language="en-US"

audio_input=speechsdk.audio.AudioConfig(filename=audio_fileName)

txt_generator=speechsdk.SpeechRecognizer(speech_config=config, audio_config=audio_input)

result=txt_generator.recognize_once_async().get()

if result.reason==speechsdk.ResultReason.RecognizedSpeech:
    print("Done")
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(result.text)

else:
    if result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Recognition canceled: {}".format(cancellation_details.reason))

    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Error details: {}".format(cancellation_details.error_details))
