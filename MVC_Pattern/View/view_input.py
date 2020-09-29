import os
import time
import playsound
import speech_recognition as sr 
from gtts import gTTS
import controll
import view_output

def speak(text):
	tts = gTTS(text=text, lang="en")
	filename = "voice.mp3"
	tts.save(filename)
	playsound.playsound(filename)

def get_audio():
	r  = sr.Recognizer()	
	with sr.Microphone() as source:		
		audio = r.listen(source)
		said=""
		try:
			said = r.recognize_google(audio)
			print(said)
		except Exception as e:
			print("Exception"+ str(e))
	return said

speak("Hello Rafs, How may I help you?")
text = get_audio()
m = controll.Controll(text)


x=True
while(x==True):
	speak("Do you need anyting else?")
	text = get_audio()
	if "no" in text:
			speak("Your welcome.")
			break
	else:
		b = controll.Controll(text)
