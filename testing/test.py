#import os
#import time
#import playsound
import pandas as pd
#import speech_recognition as sr 
#from gtts import gTTS

'''def speak(text):
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
	return said'''

class Teacher(object):
	def _init_(self, n):
		df = pd.read_csv("data.csv")
		df1=df[df['Small_Name'].str.contains(n, regex=False)]
		self.name=df1.values[0][3]
		self.initial=df1.values[0][1]
		self.room=df1.values[0][5]
		self.email=df1.values[0][6]
		


Mercedes = Teacher('Saiful')

print (Mercedes.name)






