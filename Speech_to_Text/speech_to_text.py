"""
    A program that can convert Speech into Text using python
    # Run:
    *The text Will be saved in output.txt file*
"""

import pyttsx3
import speech_recognition as sr
import os

engine =  pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speake(audio):
    engine.say(audio)
    engine.runAndWait()


def get():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('say something!')
        audio = r.listen(source)
        print('done')
        try:
            text = r.recognize_google(audio)
            print(f'google thinks you said: \n {text}')
        except Exception as e:
            print(e)
        
        with open('output.txt', 'w') as remember:
            remember.write(text)

if __name__ == '__main__':
    get()