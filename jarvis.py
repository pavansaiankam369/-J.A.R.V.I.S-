import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk 
import os

engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('vioce',voices[0].id)
engine.setProperty('rate',150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("radhaee radhae,Good Morning !")
    elif hour>=12 and hour<18:
        speak("radhaee radhae ,Good Afternoon !")
    else:
        speak(" radhaee radhae , Good Evening !")
    speak("Ready to comply .what can i do for you ?")
    
def takerCommand():
    
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.. ")
        r.pause_threshold= 1
        audio = r.listen(source)
        
    try :
        print("Recognizing..")
        query =r.recognize_google(audio,language= 'en-in')
        print(f"user said:{query}\n")
        
    except Exception as e:
        print("Say that again please ...")
        return "None"
    return query


if __name__ =="__main__":
    wishme()
    while True:
        query =takerCommand().lower()
        if 'jarvis' in query :
            print("yes sir")
            speak("yes sir")
        elif 'who are you'in query:
            print("My name is jarvis")
            speak("My name is jarvis")
            print('I can do Everything that my creator programmed me to do so ')
            speak('I can do Everything that my creator programmed me to do so ')
            
        elif "who created you"in query:
            print('I donot know his name , I created with Pyhton language, in vs code ')
            speak('I donot know his name , I created with Pyhton language, in vs code ')
        
        elif 'what is' in query: 
            speak('Searching wikipedia..')
            query = query.replace("what is","")
            results =wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'who is' in query: 
            speak('Searching wikipedia..')
            query = query.replace("who is","")
            results =wikipedia.summary(query,sentences = 2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open google' in query :
            webbrowser.open('google.com')
         
        elif 'open google' in query :
            speak("what should I search?")
            qry =takerCommand().lower()
            webbrowser.open(f"{qry}")
            results =wikipedia.summary(qry,sentences =1)
            speak(results)
            
        elif 'just open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open youtube' in query :
            speak("what you will like to watch?")
            qrry = takerCommand().lower()
            wk.playonyt(f"{qrry}")
            
        elif 'search on youtube' in query:
            query =query.replace("search on youtube", "")
            webbrowser.open(f"www.youtube.com /resluts?search_query={query}")
        
        elif 'close browser' in query:
            os.system("taskkill/f /im msedge.exe")
         
        elif 'close browser' in query:
            os.system("taskkill/f /im chrome.exe")
        
            