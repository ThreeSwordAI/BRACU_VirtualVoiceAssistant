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

class View_Calendar(object):
	def __init__(self, calendar):
		print(calendar.event['summary'])
		speak("Your next event is "+ calendar.event['summary'])
        