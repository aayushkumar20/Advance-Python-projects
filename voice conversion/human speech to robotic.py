import speech_recognition as sr
from gtts import gTTS
import os

voice=""
while True:
    r=sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Speak Anything : ")
            audio=r.listen(source)
            Text=r.recognize_google(audio)
            print(Text)
            if Text=="stop":
                break
            Text=r.recognize_google(audio)
            voice=voice+str(Text)
        except:
            print("Say something...")
hr=gTTS(text=voice,lang="en",slow=False)
hr.save("voice.mp3")