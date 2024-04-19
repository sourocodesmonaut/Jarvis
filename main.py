from cgitb import text
import datetime
from msilib.schema import Class
import speech_recognition as sr
import wikipedia
import random
import os
from bs4 import BeautifulSoup
from googletrans import Translator
import webbrowser
from playsound import playsound
#from PyDictionary import PyDictionary as Diction
import pyautogui
from pip import main
import pyttsx3
from flask import Flask
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 190)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
        speak("Good Morning!")
     elif hour>=12 and hour<18:
        speak("Good Afternoon!")
     else:
        speak("Good Evening!")
     speak("I am Jarvis Sir. I am Here to assist You. Please, tell me how may I help You")
     #speak("I am Friday Sir. I am Here to assist You. Please, tell me how may I help You")

def takeCommand():
    #It is taking input from user and printing it

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio,language='en-in')
            print(f"User said: {query}")
        except Exception as Error:
            print("Say that again please...") 
            return None
    return query

def Dict():
    speak("Activating dictionary")
    speak("Tell Me the Problem")
    probl = takeCommand()

    if 'meaning' in probl:
        probl = probl.replace("What is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("of")
        probl = probl.replace("meaning of","")
        result = Diction.meaning(probl)
        speak(f"The Meaning For {probl} is {result}")

    elif 'synonym' in probl:
        probl = probl.replace("What is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("of")
        probl = probl.replace("synonym of","")
        result = Diction.synonym(probl)
        speak(f"The Synonym For {probl} is {result}")

    elif 'antonym' in probl:
        probl = probl.replace("What is the","")
        probl = probl.replace("jarvis","")
        probl = probl.replace("of")
        probl = probl.replace("antonym of","")
        result = Diction.antonym(probl)
        speak(f"The Antonym For {probl} is {result}")
    speak("Exiting Dictionary")
def Screenshot():
    speak("ok boss,What should i name the file?")
    path=takeCommand()
    path1name = path +".png"
    path1 = "E:\\SS\\" + path1name
    kk = pyautogui.screenshot()
    kk.save(path1)
    os.startfile("E:\SS")
    speak("Here is your screen shot")
def Whatsapp():
    speak("Tell me the name of the Person!")
    wname = takeCommand().lower()

    if 'mum' in wname:
        speak("Tell me the Message!")
        msg = takeCommand()
        speak("Tell me the time sir")
        speak("Time in hour")
        hour=int(takeCommand())
        speak("Time in Minutes")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+918972945560",msg,hour,min,20)
        speak("Ok! Sir, Sending sending message")
    elif 'baba' in wname:
        speak("Tell me the Message!")
        msg = takeCommand()
        speak("Tell me the time sir")
        speak("Time in hour")
        hour=int(takeCommand())
        speak("Time in Minutes")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+919800180721",msg,hour,min,20)
        speak("Ok! Sir, Sending sending message")
    else:
        speak("Ok Tell me the phone number")
        num = int(takeCommand())
        ph = '+91' + num
        speak("Tell me the Message!")
        msg = takeCommand()
        speak("Tell me the time sir")
        speak("Time in hour")
        hour=int(takeCommand())
        speak("Time in Minutes")
        min = int(takeCommand())
        pywhatkit.sendwhatmsg(ph,msg,hour,min,20)
        speak("Ok! Sir, Sending sending message")
def TakeHindi():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognising...")
            query = r.recognize_google(audio,language='hi')
            print(f"User said: {query}")
        except Exception as Error:
            print("Say that again please...") 
            return None
    return query
def Tran():
    speak("Tell me the line!")
    line = TakeHindi()
    traslate = Translator()
    ans = traslate.translate(line)
    Text = ans.text
    print("       ")
    print(Text)
    speak(Text)


#Tasks
def TaskEXE():
    if _name_ == "_main_":
        wishMe()
        while True:
            query = takeCommand().lower()
            #Logic executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query=query.replace("wikipedia","")
                results=wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'hello jarvis' in query:
                speak("Hello Sir, What can i do for You")
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            elif 'open google' in query:
                webbrowser.open("www.google.com")
            elif 'open facebook' in query:
                webbrowser.open("www.facebook.com")
            elif 'open gmail' in query:
                webbrowser.open("mail.google.com")
            elif 'open school' in query:
                webbrowser.open("sksps.edunext1.com")
            elif 'play music' in query:
                speak("Sir play music from, offline,  or look, online")
                choice= takeCommand().lower()
                if "offline" in choice:
                    music_dir = 'D:\\Songs\\Music'
                    songs = os.listdir(music_dir)
                    #print(songs)
                    a=random.randint(1,700)
                    os.startfile(os.path.join(music_dir, songs[a]))
                else:
                    speak("Tell the name of the music")
                    musicname=takeCommand()
                    pywhatkit.playonyt(musicname)
                speak("Your Song has been started, Enjoy Sir")
            elif 'the time' in query:
                strtime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, The time is {strtime}")
            elif 'open ms word' in query:
                word='"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"'
                os.startfile(word)
            elif 'open zoom' in query:
                zoompath='C:\\Users\\soubh\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe'
                os.startfile(zoompath)
            elif 'show my youtube channel' in query:
                webbrowser.open("www.youtube.com/channel/UCVu_kIJI9LqbQqBJKe-8YwQ")
            elif 'tell about yourself' in query:
                speak("Hello Sir, Allow me to introduce myself, I am Jarvis Your Personal Artificial Intelligence AI assisstant")
                speak("I am here to make your life easier, I can perform several tasks for you 24 hours a day and 7days a week")
                speak("importing all preferences from home interface.....Thank You")
            elif 'search in youtube' in query:
                speak("Ok Sir, This is what i found in your search")
                query=query.replace("jarvis","")
                query=query.replace("search in youtube","")
                web='https://www.youtube.com/results?search_query=' + query
                link=web
                print(link)
                webbrowser.open(link)
                speak("Done sir")
            elif 'search in google' in query:
                speak("Ok Sir, This is what i found in your search")
                query=query.replace("jarvis","")
                query=query.replace("search in google","")
                pywhatkit.search(query)
                speak("Done Sir")
            elif 'exit' in query:
                speak("Bye Sir, Nice Meeting You")
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<12:
                    speak("Have a nice Day!")
                elif hour>=12 and hour<18:
                    speak("Have a nice Day!")
                else:
                    speak("Hope Your Day Went well!")
                break
            elif 'who built you' in query:
                speak("I was built by Master Soubhik Sadhu")
            elif 'who created you' in query:
                speak("I was built by Master Soubhik Sadhu")
            elif 'open sql' in query:
                zoomsql='E:\\Xampp\\xampp-control.exe'
                os.startfile(zoomsql)
            elif 'thank you' in query:
                speak("It's my Pleasure, Sir")
            elif 'run speed test' in query:
                webbrowser.open("www.speedtest.net")
                speak("Checking the Speed Sir, Just a second")
                speak("Done Sir")
            elif "dictionary" in query:
                Dict()
            elif 'take screenshot' in query:
                Screenshot()
            elif 'send message' in query:
                Whatsapp()
            elif 'whatsapp' in query:
                Whatsapp()
            elif 'translator' in query:
                Tran()
            elif 'google search' in query:
                import wikipedia as googleScrap
                query=query.replace("jarvis","")
                query=query.replace("google search","")
                query=query.replace("google","")
                speak("This is what i found on the web!")

                try:
                    pywhatkit.search(query)
                    result=googleScrap.summary(query,3)
                    speak(result)
                except:
                    speak("No Callable Data Available!")
            elif 'take a break' in query:
                speak("Ok Sir! You can call me again Whenever you need me!")
                speak("Just say wake up jarvis!")
                break
            elif 'you need a break' in query:
                speak("Ok Sir! You can call me again Whenever you need me!")
                speak("Just say wake up jarvis!")
                break
            elif 'meditation' in query:
                word="D:\Backup 1\Meditation"
                msword = os.listdir(word)
                os.startfile(word)
                speak("Opened Sir!")


TaskEXE()