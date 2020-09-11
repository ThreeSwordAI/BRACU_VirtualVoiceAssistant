import os
import time
import playsound
import speech_recognition as sr 
from gtts import gTTS
import model_teacher
import view_teacher
import model_calendar
import view_calendar
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




class Controll(object):
	def __init__(self, text):
		print("Rafs")
		if "teacher" in text:
			speak("Which faculty information do you want?")
			faculty = get_audio()
			
			teacher = model_teacher.Model_teacher(faculty)
			view_teacher.View_Teacher(teacher)

		elif "event" in text:
			speak("Let me check")
			calendar = model_calendar.Model_calendar()
			view_calendar.View_Calendar(calendar)