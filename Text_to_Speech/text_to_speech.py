'''
    When executed the text from abc.txt will be turned into an mp3, saved and
    then played on your device.
    ### Prerequisites
    - abc.txt with your text
    - the gTTS==2.1.1 module (pip install gTTS to download)
    - the os module (pip install os)
    ### How to run the script
    Write your desired text into the abc.txt file
    then execute the text_to_speech.py file. This can be
    done by typing 'python text_to_speech.py' into your Terminal.
'''

import os
from gtts import gTTS

with open("./abc.txt", "r") as f:
    file = f.read()

# the file format should be str
def speech(file:str) -> any:
    speech = gTTS(text=file, lang="en", slow=False)
    speech.save("voice.mp3")
    os.system("voice.mp3")

speech(file)
# print(file)