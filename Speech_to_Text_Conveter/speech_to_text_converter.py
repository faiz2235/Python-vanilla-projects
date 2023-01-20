"""
`    This Python script converts the Speech input into Text using NLP (Natural
    Langauge Processing).
    ### Requirements
    **Installation Required** :
    * Python Speech Recognition module:
    `pip install speechrecognition`
    * PyAudio:
    * Use the following command for linux users
    `sudo apt-get install python3-pyaudio`
    * Windows users can install pyaudio by executing the following command
    in a terminal
    `pip install pyaudio`
    ### How to run the script
    - Enter the audio input by speaking into the microphone.
    - Run converter_terminal.py script
    - Output Text will be displayed
"""

import speech_recognition

def record_voice():
    microphone = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as live_phone:
        microphone.adjust_for_ambient_noise(live_phone)
        print("I'm trying to hear you...")
        audio = microphone.listen(live_phone)
        try:
            phrase =  microphone.recognize_google(audio, language="en")
            return phrase

        except speech_recognition.UnknownValueError:
            return "I didn't understand what you said"

if __name__ == "__main__":
    phrase = record_voice()

    with open("you_said_this.txt", "w") as file:
        file.write(phrase)

        print("the last sentece you said was saved in you_said_this.txt")