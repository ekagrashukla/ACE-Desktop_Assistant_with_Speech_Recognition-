import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install speechrecogition
import wikipedia  # pip install wikipedia 
import smtplib
import webbrowser as wb
import psutil  # pip install psutil
import pyjokes  # pip install pyjokes
import os
import pyautogui  # pip install pyautogui
import random
import json
import requests
from urllib.request import urlopen 
import wolframalpha # pip install wolframalpha
import time

engine=pyttsx3.init()
wolframalpha_app_id = "U5WAE8-UHPYGPRTWL"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date_():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    date = datetime.datetime.now().day
    speak("The Current date is")
    speak(date)
    speak(month)
    speak(year)

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    # for this function to work, you must enable low security in your gmail which you are going to use to send email
    server.login('username@gmail.com','password')
    server.sendemail('username@gmail.com',to,content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU Is at'+usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

def screenshot():
    img = pyautogui.screenshot()
    img.save('C:/Users/JunkGear/Desktop/screenshot_'+str(random.randint(1,100000000000000000))+'.png')

def wishme():
    speak("Welcome back Sir")
    time_()
    date_()

    #Greetings

    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")
    elif hour>=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good Night Sir!")

    speak("Ace at your service. Please tell me how can I help you today")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-US')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = TakeCommand().lower()
        if 'time' in query:
            time_()
        elif 'date' in query:
            date_()
        elif 'wikipedia' or 'what is' in query:
            speak("Searching")
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=3)
            speak('According to Wikipedia')
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say")
                content=TakeCommand()
                # Provide receiver email address
                speak("Who is the receiver")
                receiver=input("Enter Receiver's Email:")
                to = receiver
                sendEmail(to,content)
                speak(content)
                speak('Email is sent.')
            except Exception as e:
                print(e)
                speak("Unable to send Email.")
        elif 'search in chrome' in query:
            speak('What should I search?')
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            # chromepath is location of chrome's installation on computer'

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')
        elif 'search youtube' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak("Here we go to youtube!")
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search google' in query:
            speak('What should I search?')
            search_Term = TakeCommand().lower()
            speak("Searching...")
            wb.open('https://www.google.com/search?q='+search_Term)
        
        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            speak('Going Offline Sir!')
            quit()

        elif 'word' in query:
            speak('Opening MS Word..')
            ms_word=r'C:/...Path...'
            os.startfile(ms_word)

        elif 'write a note' in query:
            speak('What should I write, Sir')
            notes = TakeCommand()
            file = open('notes.txt','w')
            speak('Sir should I include Date and Time?')
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('Done Taking Notes, SIR!')
            else:
                file.write(notes)
                speak('Done Taking Notes, SIR!')

        elif 'show note' in query:
            speak('showing notes')
            file = open('notes.txt','r')
            print(file.read())
            speak(file.read())

        elif 'screenshot' in query:
            screenshot()
            speak('Screenshot Taken, SIR!')

        elif 'play music' in query:
            songs_dir = 'D:/SONGS'
            music = os.listdir(songs_dir)
            speak('What should I play?')
            speak('SELECT A NUMBER..')
            ans = TakeCommand().lower()
            while('number' not in ans and ans != 'random'):
                speak('Please say something like number 2 or random')
                ans = TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number',''))
            elif 'random' or 'you choose' in ans:
                no = random.randint(1,10)
            os.startfile(os.path.join(songs_dir,music))
        
        elif 'remember that' in query:
            speak("What should I remember?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open('memory.txt','w')
            reember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('memory.txt','r')
            speak('You asked me to remember that')
            speak(remember.read())

        elif 'news' in query:
            try:
                jsonObj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=853a426a6c6349eba37b8eb0f9801d02")
                data = json.load(jsonObj)
                i = 1
                speak("Here are the top headlines from business industry")
                print("==============TOP HEADLINES==============")
                for item in data['articles']:
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description'])
                    speak(item['title'])
                    i += 1
            except Exception as e:
                print(str(e))

        elif 'where is' in query:
            query = query.replace("Where is",'')
            location = query
            speak("User asked to locate"+location)
            wb.open_new_tab("https://www.google.com/maps/place"+locatin)

        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx+1:]
            print("query",query)
            try:
                res = client.query(''.join(query))
                answer = next(res.results).text
                print("The Answer is:"+answer)
                speak("The Answer is:"+answer)
            except:
                speak("I'm Sorry I can't do that yet")
        
        elif "define" in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except:
                speak("No Result Found")

        elif "stop listening" in query:
            speak("For how many seconds you want me to stop listening to your commands?")
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans)

        elif 'log out' or 'logout' in query:
            os.system("shutdown -l")
        elif "restart" in query:
            os.system("shutdown /r /t 1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
