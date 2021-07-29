
import os
import speech_recognition as sr
import sys
import pyttsx3
from testweather import get_weather

# weather = get_weather()
# print(round(weather))


def speech_to_text(command):
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()

# speech_to_text(str(round(weather)))


def get_command():
	r = sr.Recognizer()

	with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source, duration=0.25)
			audio = r.listen(source)
			try:
				recongnizing_text = r.recognize_google(audio)
				MyText = recongnizing_text.lower()
			except Exception as e:
				print('unable to recongnize your voice')








while True:
	try:
		
			if MyText == 'jarvis what is the weather':
				
				speech_to_text(str(round(get_weather())))
			else:
				speech_to_text('did you say {}'.format(MyText))
				pass
	except sr.RequestError:
		print('oooppps')
	except sr.UnknownValueError as e:
		print('there was a {} error '.format(e))