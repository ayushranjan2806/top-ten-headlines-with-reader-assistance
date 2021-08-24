import requests 
import json
import pyttsx3


# import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':
    speak ("top headlines from india  ")
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=8472e47aa5e743018c88e0fc5ad43bd4"
    news =requests.get(url)
    x=news.json()
    speak("TODAY TOP 15 HEADLINES")
    print("TODAY  TOP  15 HEADLINES")
    for i in range(15):
        results=f"{i+1}.{x['articles'][i]['title']}"

        print(results)
        speak(results)
        speak("now  comes to next news... ")
  
