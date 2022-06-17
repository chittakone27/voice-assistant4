import subprocess
import wolframalpha
import pywhatkit
import pyttsx3
import json
import random

import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes

import smtplib
import ctypes
import time
import requests
from twilio.rest import Client

from ecapture import ecapture as ec

from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir !")

    else:
        speak("Good Evening Sir !")

    assname = "Oracle"
    speak("I am your Assistant")
    speak(assname)


#def username():
 #   speak("What should i call you sir")
  #  uname = takeCommand()
   # speak("Welcome Mister")
    #speak(uname)
    #columns = shutil.get_terminal_size().columns

    #print("Welcome Sir Mr.", uname.center(columns))
    speak("How can i Help you, Sir")


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-th')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query


def Speak(audio):
    # initial constructor of pyttsx3
    engine = pyttsx3.init()

    # getter and setter method
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()




def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('owen27th@gmail.com', 'cogpxcgzmcvaavrf')
    server.sendmail('owen27th@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear()
    wishMe()
    #username()

    while True:

        query = takeCommand().lower()

        # All the commands said by user will be
        # stored here in 'query' and will be
        # converted to lower case for easily
        # recognition of command
        if 'wikipedia' in query or "Wikipedia" in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'play' in query:
            if query =="none":
                print("....")
            else:
                song = query.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)
        elif 'open music' in query or "open song" in query:
            speak("Here you go with random music")

            n = random.randint(0,10)
            music_dir = "C:\\Users\\wen7myrz\\Desktop\\FL Studio 20\\beat"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[n]))
        elif 'open youtube' in query:
            speak("Here you go to Youtube\n")

            webbrowser.open("http://youtube.com")
        elif 'open email' in query or 'open gmail' in query or 'go to gmail' in query or 'go to email' in query \
                or 'open my email' in query or 'open my gmail' in query or 'go to my gmail' in query or 'go to my email' in query:
            speak("Here you go to gmail\n")

            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
        elif 'open google' in query:
            speak("Here you go to Google\n")

            webbrowser.open("https://google.com")
        elif 'open vk' in query:
            speak("Here you go to VK\n")

            webbrowser.open("https://vk.com/im")
        elif 'search' in query or 'shoot' in query or "should" in query:
            speak(" what you want to search for ")
            print("what you want to search for : ")
            sf = takeCommand()
            if sf == "None":
                print("i don't hear you sir ")
                speak("i don't hear you sir")
            else:
                url="https://www.google.com/search?q=" + sf
                webbrowser.open(url)

        elif 'open stackoverflow' in query or 'open stack overflow'in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("https://stackoverflow.com/")



        elif 'time' in query:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"Sir, the time is {strTime}")




        elif 'email to myself' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "owen27th@gmail.com"
                sendEmail(to, content)
                print("the message is :")
                speak("the message is :")
                print(content)
                speak(content)
                speak("make sure the message is corrected, sir ")

                confirm = takeCommand()
                if confirm == "sure" or confirm == "yes":
                    sendEmail(to, content)
                    speak("Email has been sent !")
                else:
                    speak("please select email by, send email command again, sir ")
                    print("please select email by email command to myself again sir ")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'send email' in query:
            try:

                speak("What should I say?")
                content = takeCommand()

                speak("please write email address whome should i send")
                to = input("whome should i send :")
                speak("make sure the email and content is, corrected sir  ")
                print("make sure the email and content is corrected sir  ")
                print("to username : ", to)
                speak("to, username : ")
                speak(to)

                print("the message is :")
                speak("the message is :")
                print(content)
                speak(content)
                print("are you sure sir ")
                speak("are you sure sir ")

                confirm = takeCommand()
                if confirm == "sure" or confirm == "yes":
                    sendEmail(to, content)
                    print("Email has been sent !")
                    speak("Email has been sent !")
                else:
                    speak("please select email by, send email command again, sir ")
                    print("please select email by send email command again sir ")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")


        elif "change my name to" in query:

            query = query.replace("change my name to", "")
            user = query
            print("hello Sir your username change to :", user)
            speak("hello Sir your username change to ")
            speak(user)
        elif "what is my username" in query or "what is my name" in query:
              print("your username is :", user)
              speak("your username is ")
              speak(user)
        elif "what's your name" in query or "what is your name" in query:
                assname="oracle"
                speak("My friends call me")

                speak(assname)

                print("My friends call me", assname)


        elif "change your name" in query:


            speak("What would you like to call me, Sir ")

            assname1 = takeCommand()
            speak("hello sir I am your Assistant")
            speak(assname1)
            speak("how should i help you sir")
        elif"your name i change" in query or "you name i change" in query:
            print("my name change to:", assname1)

            speak("my name change to")
            speak(assname1)
        elif 'exit system' in query or 'closed system' in query or 'stop system' in query:
            print("Thanks for giving me your time sir")
            speak("Thanks for giving me your time sir")
            exit()

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by chittakone he created me for diploma.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif "who i am" in query:
            speak("If you talk then definitely your human.")

        elif "why you came to world" in query:
            speak("Thanks to chittakone. further It's a secret")

        elif 'file diploma' in query:
            speak("opening file diploma in word")
            word = "F:\\4\\Глава_1.docx"
            os.startfile(word)

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")

        elif "who are you" in query:
            speak("I am your virtual assistant created by chittakone")

        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister chittakone ")

        elif 'background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            speak("Background changed successfully")

        elif 'open chrome' in query:
            appli = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(appli)

        elif 'news' in query:

            try:
                jsonObj = urlopen('https://newsapi.org/v2/everything?q=keyword&apiKey=e31acf83ae77419184170a2f4a4e26c6')
                data = json.load(jsonObj)
                i = 1

                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')

                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:

                print(str(e))


        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            print("Recycling Recycle Bin ........")
            speak("Recycling Recycle Bin ")
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time(in second) you want to stop ORACLE from listening commands")
            print("for how much time(in second) you want to stop ORACLE from listening commands")
            a =int(takeCommand())
            print("stop listening for ", a , "second")
            speak("stop listening for ")
            speak(a)
            speak("second")
            time.sleep(a)
            speak("hello sir the time's up sir i'm listening ")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")

        elif "camera" in query or "take a photo" in query:
            ec.capture(0,"test","img.jpg")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "closed computer" in query or "lock computer" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        elif "shutdown computer" in query or "shut down computer" in query:
            speak("Make sure all the application are closed before shutdown")

            subprocess.call(["shutdown", "/s"])
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('oracle.txt', 'w')
            speak("Sir, Should i include date and time")
            print("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm or 'okay' in snfm or 'ok' in snfm:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                date = datetime.date.today().strftime("%m/%d/%y")
                file.write(date)
                file.write(" :- ")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)

                print("included")
                speak("included")
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("oracle.txt", "r")
            print(file.read())

        elif "what day is today" in query or "what day" in query:
            week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            td = datetime.date.today().strftime("%m/%d/%y")
            week_num = datetime.date.today().weekday()
            print(week_days[week_num], td)
            speak(week_days[week_num])
            speak(td)

        elif "reading note" in query or "quitting note" in query or "greeting note" in query:
            file = open("oracle.txt", "r+")
            speak(file.read())


        elif "the weather" in query:

            # Google Open weather website
            # to get API of Open weather
            api_key = "5adaf62fc85827fb5f0cebe4fe77069c"

            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()

            complete_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=5adaf62fc85827fb5f0cebe4fe77069c&units=metric".format(city_name)

            response = requests.get(complete_url)


            x = response.json()

            if x["cod"] != "404":

                y = x["wind"]

                current_speed = y["speed"]

                current_deg = y["deg"]

                current_gust = y["gust"]
                y = x["main"]

                current_humidity = y["humidity"]
                current_temp = y["temp"]

                z = x["weather"]

                weather_description = z[0]["description"]
                print(" Temperature (Температура) = " +
                      str("%d"%(current_temp)) +"  °C"+
                      "\n description (описание) = " +
                      str(weather_description) +
                      "\n humidity (влажность) = " +
                      str(current_humidity) +" %"+
                      "\n wind (ветер) = " +
                      str(current_speed)+" m/s")
                speak(" Temperature "+
                  str("%d"%(current_temp)) +" degree celsius"
                  "\n description = = " +
                  str(weather_description) +
                  "\n humidity (in percentage) " +
                  str(current_humidity) +"precent"+
                  "\n wind " +
                  str(current_speed)+"meters per second ")
            else:
                speak(" City Not Found ")

        elif "send message " in query:
            # You need to create an account on Twilio to use this service
            account_sid = 'Account Sid key'
            auth_token = 'Auth token'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                body=takeCommand(),
                from_='Sender No',
                to='Receiver No'
            )

            print(message.sid)

        elif "open wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "morning" in query:
            speak("A warm" + query)
            speak("How are you SIR")


        # most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")

        elif "how are you" in query:
            speak("I'm fine, glad you me that")

        elif "i love you" in query:
            speak("It's hard to understand")

        elif "i want to know" in query or "tell me" in query:

            # Use the same API key
            # that we have generated earlier
            speak(" what you want to know sir ")
            print(" what you want to know sir  : ")
            know = takeCommand()
            client = wolframalpha.Client("879U93-2PU4VV84YX")
            res = client.query(know)

            try:
                print(next(res.results).text)
                speak(next(res.results).text)

            except StopIteration:
                print("No results")
                speak("No results")
        elif "calculate" in query:

            app_id = "879U93-2PU4VV84YX"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)



