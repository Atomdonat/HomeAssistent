import speech_recognition as sr
from playsound import playsound
import os
import time
from gtts import gTTS
import pyaudio


def input_listen(ausgabe):
    spr = sr.Recognizer()
    with sr.Microphone() as micro:
        print(ausgabe)
        audio = spr.listen(micro)
        print("ich verarbeite...")
        text = spr.recognize_google(audio, language="de-DE")
        text = text.lower().replace("ä","ae").replace("ö","oe").replace("ü","ue")
        print(text)
        return text


def speak(text):
    tts = gTTS(text=text, lang="de")
    file_name = "voice.mp3"
    tts.save(file_name)
    playsound(file_name)


def text_to_speak(text):
    tts = gTTS(text=text, lang="de")
    text = text.lower().replace(" ", "").replace("ä","ae").replace("ö","oe").replace("ü","ue")
    filename = str(text[0:20]+ ".mp3")
    # tts.save(filename)
    playsound(filename)

def read_file_and_speak(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if word == "**":
                    time.sleep(1)  # Pause for 1 second
                else:
                    text_to_speak(word)


def output_device():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
            if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))

if __name__ == "__main__":
    file_path = "text4text2speech.txt"
    read_file_and_speak(file_path)

    # output_speak("Guten Abend meine Damen und Herren ich begrueße Sie")

    speak("Hallo Welt")