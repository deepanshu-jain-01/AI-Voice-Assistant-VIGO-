# IMPORTING REQUIRED LIBRARIRES:

# IMPORTING PYTHON TEXT TO SPEECH CONVERSION BASED LIBRARY CALLED PYTTSX3 USING PIP INSTALL PYTTSX3:
import pyttsx3

# IMPORTING SPEECH_RECOGNITION LIBRARY THAT WILL ALLOW TO CONVERT SPEECH INTO TEXT. INSTALL:
# 1. pip install SpeechRecognition
# 2. pip install pyaudio (IF ERROR COME THEN DO : pip install pywin and then pyaudio)
import speech_recognition as sr

# IMPORTING DATETIME AND CALENDaR LIBRARY FOR EXTRACTING DATE, TIME, CALENDER RELATED QUERIES:
import calendar
import datetime

# IMPORTING LIBRARIES REQUIRED TO SEND EMAILS AND EMAIL ALERTS TO MAILS AND PHONE NUMBERS:
import smtplib
from email.message import EmailMessage

# IMPORTING LIBRARIES TO INTERACT WITH OPERATING SYSTEM:
import os
import subprocess as sp

# IMPORTING REQUEST LIBRARY TO WORK WITH APIs (APPLICATION PROGRAMMING INTERFACE).
# In order to work with APIs in Python, we need tools that will make those requests. In Python, the most common library for making requests and working with APIs is the requests library.
import requests

# IMPORTING LIBRARY TO GET DATA FROM WIKIPEDIA:
import wikipedia

# IMPORTING PYWHATKIT:
import pywhatkit as kit

# IMPORTING LIBRARYTO OPEN WEBPAGES:
import webbrowser

# IMPORT PYTHON JOKES:
import pyjokes

# IMPORT WOLFRAM INTELLIGENCE:
import wolframalpha

# IMPORTING CTYPE LIBRARY FOR CONNECTING THROUGH FUNCTIONS INTERACTING WITH THE SYSTEM:
import ctypes
import winshell

# IMPORTING LIBRARY FOR EXTRACTING PHONE NUMBERS:
import phonenumbers

# IMPORTING TIME LIBRARY FOR SLEEP FUNCTIONALITY
import time

#from fer import FER
#import matplotlib.pyplot as plt 
#import cv2
#import numpy as np
#def emotion_detection():
    #Using cv2.CAP_DSHOW removes the warning, but slows down my frame rate from 30fps to 7fps, on Windows.
    #cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    #while True:
    #    ret, frame = cap.read()
    #    emo_detector = FER(mtcnn=True)
    #    cv2.imshow("Emotion Recognition",frame)
    #    k=cv2.waitKey(1)
    #    if k==27:
    #        dominant_emotion, emotion_score = emo_detector.top_emotion(frame)
    #        break
    #cap.release()
    #cv2.destroyAllWindows()
    #return dominant_emotion
# import _pywrap_tensorflow

# DEFINING A DICTIONARY OF PATHS FOR ACCESSING THE LOCATION COORDINATES OF VARIOUS APPLICATIONS:
paths = {
    'calculator' : "C:\\Windows\\System32\\calc.exe",
}


# DEFINING THE REQUIRED FUNCTIONS:
def speak(text):
    """ FUNCTION THAT WILL ALLOW THE A.I. ASSISTANT TO SPEAK THE GIVEN TEXT. """

    # INIT WILL INITIATE THE ENGINE(VARIABLE) FOR IT TO PERFORM THE FUNCTIONALITY:
    engine = pyttsx3.init()

    # GETTING AND SETTING UP THE VOICE GENDER:
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    # GETTING AND SETTING UP THE RATE OF THE VOICE:
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 175)

    # ALLOWS THE ENGINE TO SPEAK THE TEXT GIVEN TO IT:
    engine.say(text)

    # THIS COMMAND WILL NOT LET THE ENGINE STOP UNTIL THE TEXT PASSED INTO THE SPEAK FUNCTION HAS BEEN COMPLETED:
    engine.runAndWait()


def listen():
    """ FUNCTION THAT WILL ALLOW THE A.I. ASSISTANT TO LISTEN TO THE USER. """

    # THE MOST IMPORTANT CLASS IN SPEECH_RECOGNITION LIBRARY IS THE CLASS : RECOGNIZER(). THUS WE WILL CALL THIS CLASS AND STORE IT INTO A VARIABLE:
    r = sr.Recognizer()

    # SETTING ITS ENERGY THRESHOLD TO 300 (ENERGY_THRESHOLD MEANS LOUDNESS OF THE AUDIO):
    r.energy_threshold = 300

    with sr.Microphone() as source:
        print("LISTENING . . . ")
        audio = r.listen(source)

    try:
        print("RECOGNIZING . . . ")
        query = r.recognize_google(audio, language = 'en-in')
        print(query)

    except:
        print("Sorry, Could Not Understand What You Said. It was nice talking to you.")
        speak("Sorry, Could Not Understand What You Said. It was nice talking to you.")
        exit()
        

    return query

def greet(name):
    """ FUNCTION THAT WILL HELP THE A.I. ASSISTANT TO GREET THE USER WHEN IT IS ACTIVATED. """

    # THIS WILL USE THE DATETIME LIBRARY IN ORDER TO GET THE CURRENT HOUR OF THE DAY WHEN THE DEVICE IS ACTIVATED:
    hour = datetime.datetime.now().hour

    # GREETING ARE MADE BASED ON THE HOUR:
    if hour >= 0 and hour < 12:
        print(f"Good Morning {name}, I Am TRIXIE, IEEE's Personal Artificial Intelligence Assistant! How May I Assist You ?")
        speak(f"Good Morning {name}, I Am TRIXIE, IEEE's Personal Artificial Intelligence Assistant! How May I Assist You ?")
    elif hour >= 12 and hour < 18:
        print(f"Good Afternoon {name}, I Am TRIXIE, IEEE's Personal Artificial Intelligence Assistant! How May I Assist You ?")
        speak(f"Good Afternoon {name}, I Am TRIXIE, IEEE's Personal Artificial Intelligence Assistant! How May I Assist You ?")
    else:
        print(f"Good Evening {name}, I Am TRIXIE, IEEE's Personal Artificial Intelligence Assistant! How May I Assist You ?")
        speak(f"Good Evening {name}, I Am TRIXIE, IEEE's Personal Artificial Intelligence Assistant! How May I Assist You ?")


def sendEmail(to, content):
    """" FUNCTION THAT WILL SEND EMAIL CONTAINING SUBJECT, CONTENT FOR THE BODY, OR ANY ATTACHMENTS TO THE REQUIRED PERSON. """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    speak("Please Enter your e-mail password: ")
    password=getpass.getpass("Enter your password: ")
    try:
        server.login('djjain844@gmail.com',password)
        server.sendmail('djjain844@gmail.com', to, content)
    except:
        print("Sorry! Invalid Credentials.")
    server.close()

# def send_email(to, subject, content):
#     """" FUNCTION THAT WILL SEND EMAIL CONTAINING SUBJECT, CONTENT FOR THE BODY, OR ANY ATTACHMENTS TO THE REQUIRED PERSON. """
#     try:
#         email = EmailMessage()
#         email['To'] = receiver_address
#         email["Subject"] = subject
#         email['From'] = USER_MAIL
#         email.set_content(content)
#
#         # PARAMETERS REQUIRED TO INITIATE THE SERVER OF SMTPLIB:
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.ehlo()
#         server.starttls()
#
#         # PASSING THE CREDENTIALS OF "FROM", WHERE PASS IS GENERATED FROM APP PASSWORD OF THE GMAIL ACCOUNT BY TURNING ON THE LESS SECURE APP AND 2 FACTOR AUTHORIZATION:
#         USER_MAIL = "yashii.2401@gmail.com"
#         PASSWORD = "tutgzizjakeoczhg"
#
#         # LOGGING IN THE GMAIL ACCOUNT FROM WHERE THE EMAIL WILL BE SENT.
#         server.login(USER_MAIL, PASSWORD)
#
#         # SENDING THE MAIL(FROM, TO, CONTENT OF THE MAIL):
#         server.sendmail(USER_MAIL, to, content)
#
#         # SERVER IS THEN CLOSED AFTER SENDING THE MAIL:
#         server.close()
#
#         return True
#
#     except Exception as e:
#         print(e)
#         return False


# DEFINING FUNCTIONS TO OPEN APPLICATIONS USING URI COMMANDS (UNIFORM RESOURCE IDENTIFIER)
def open_camera():
    """ FUNCTION THAT WILL OPEN THE CAMERA """
    sp.run('start microsoft.windows.camera:', shell = True)


def open_calculator():
    """ FUNCTION THAT WILL OPEN THE CALCULATOR """
    # sp.Popen(paths['calculator'])
    sp.run('start calculator:', shell = True)


def open_clock():
    """ FUNCTION THAT WILL OPEN THE CLOCKS """
    sp.run('start ms-clock:', shell = True)


def open_calendar():
    """ FUNCTION THAT WILL OPEN THE CALENDAR """
    sp.run('start outlookcal:', shell = True)


def open_cortana():
    """ FUNCTION THAT WILL OPEN THE CORTANA """
    sp.run('start ms-cortana::', shell = True)


def open_music():
    """ FUNCTION THAT WILL OPEN THE GROOVE MUSIC APP """
    sp.run('start mswindowsmusic:', shell = True)


def open_outlook():
    """ FUNCTION THAT WILL OPEN THE OULOOK MAIL"""
    sp.run('start outlookmail:', shell = True)


def open_edge():
    """ FUNCTION THAT WILL OPEN THE MICROSOFT EDGE """
    sp.run('start microsoft-edge:', shell = True)


def open_photos():
    """ FUNCTION THAT WILL OPEN THE GALLERY """
    sp.run('start ms-photos:', shell = True)


def open_snip():
    """ FUNCTION THAT WILL OPEN THE SNIP AND SKETCH """
    sp.run('start ms-screenclip:', shell = True)


def open_settings():
    """ FUNCTION THAT WILL OPEN THE SETTINGS """
    sp.run('start ms-settings:', shell = True)


def open_cmd():
    """ FUNCTION THAT WILL OPEN THE COMMAND PROMPT """
    sp.run('start cmd', shell = True)


# DEFINING FUNCTIONS FOR WORKING WITH ONLINE AVAILABILITIES NOW:
def find_my_ip():
    """" FUNCTION FOR FINDING IP ADDRESS """
    ip_address = requests.get('https://api64.ipify.org/?format=json').json()
    return ip_address["ip"]


def search_wiki(query):
    """" FUNCTION FOR DOING A WIKI SEARCH"""
    results = wikipedia.summary(query, sentences = 5)
    return(speak(results))

# FUNCTIONS USING PYWHATKIT:
def play_on_youtube(video):
    """FUNCTION TO PLAY A VIDEO RELATED TO THE TOPIC ON YOUTUBE"""
    kit.playonyt(video)


def search_on_google(query):
    """FUNCTION FOR GOOGLE SEARCH"""
    kit.search(query)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


# NEWS_API_KEY = config("7c4b4460e02b4c9ba7400a386dd1a989")
#
# def get_latest_news():
#     """FUNCTION FOR GOOGLE NEWS UPDATES"""
#     news_headlines = []
#     res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
#     articles = res["articles"]
#     for article in articles:
#         news_headlines.append(article["title"])
#     return news_headlines[:5]

# def emotion_detection():
#     # cap = cv2.VideoCapture(0)
#     # while True:
#     #     ret, frame = cap.read()
#     #     emo_detector = FER(mtcnn=True)
#     #     cv2.imshpython --versionow("Emotion Recognition",frame)
#     #     k=cv2.waitKey(1)
#     #     if k==27:
#     #         out = cv2.imwrite('capture.jpg', frame)
#     #         dominant_emotion, emotion_score = emo_detector.top_emotion(frame)
#     #         speak(dominant_emotion, emotion_score)
#     #         break
#     #
#     # cap.release()
#     # cv2.destroyAllWindows()


# SETTING UP THE MAIN BODY:

if __name__ == '__main__':
    # WAKE = "wake up"
    user_name = "NBA"
    greet("user_name")
    # query = listen()
    
    while True:
        # time.sleep(2)
        # if query.count(WAKE) > 0:
        #     print("Identify Yourself.")
        #     speak("Identify Yourself.")
            # user_name = listen().capitalize()
        1
        # greet(user_name)

        query = listen()
        if 'how are you' in query.lower():
            print(f"I am fine, Thank you {user_name}")
            speak(f"I am fine, Thank you {user_name}")

        elif 'projects' in query.lower():
            print(f"IEEE have been successful in making different projects like TRIXIE, Oh Thats me, RFID, Fire alarm system, face mask detection, Invisible cloak just like the one that harry potter had, snake game, robots, research papers and soo much more!")
            speak(f"IEEE have been successful in making different projects like TRIXIE, Oh Thats me, RFID, Fire alarm system, face mask detection, Invisible cloak just like the one that harry potter had, snake game, robots, research papers and soo much more!")

        elif 'achievements' in query.lower():
            print(f"Members of IEEE ADGITM received the JK Pal Memorial Award. JK Pal Memorial Award for one student per branch every year This award is given to one student per branch in the final year. Moreover IEEE ADGITM secured 3 positions among top 5 positions in IEEE R10 SAC Android App Designing competition. 1st position was secured by the team IEEE. 5th position was shared between team IEEE. IEEE ADGITM website secured 3rd position in IEEE R10 SAC Student Branch Website Contest. All of this was possible only because of the hard work and team efforts of the website team")
            speak(f"Members of IEEE ADGITM received the JK Pal Memorial Award. JK Pal Memorial Award for one student per branch every year This award is given to one student per branch in the final year. Moreover IEEE ADGITM secured 3 positions among top 5 positions in IEEE R10 SAC Android App Designing competition. 1st position was secured by the team IEEE. 5th position was shared between team IEEE. IEEE ADGITM website secured 3rd position in IEEE R10 SAC Student Branch Website Contest. All of this was possible only because of the hard work and team efforts of the website team")

        elif 'about' in query.lower():
            print(f"IEEE ADGITM is a student branch under IEEE Region 10 (Asia-Pacific) in IEEE Delhi Section. We are a community of technically active engineering students who aim to learn, share, and create. IEEE conducts various Events like Student Professional Talks, Lectures, Workshops, Webinars, SIGS, WIE Events, Industrial Visits, Small hands-on training, Hackathons, Engineering Fairs, Research Paper Writing and Project Development Program, etc. We help students expand their knowledge horizons and apply to various  Scholarships and awards.")
            speak(f"IEEE ADGITM is a student branch under IEEE Region 10 (Asia-Pacific) in IEEE Delhi Section. We are a community of technically active engineering students who aim to learn, share, and create. IEEE conducts various Events like Student Professional Talks, Lectures, Workshops, Webinars, SIGS, WIE Events, Industrial Visits, Small hands-on training, Hackathons, Engineering Fairs, Research Paper Writing and Project Development Program, etc. We help students expand their knowledge horizons and apply to various  Scholarships and awards.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        elif 'bad' in query.lower() or "hate" in query.lower():
            print("You should not talk to anyone like this!")
            speak("You should not talk to anyone like this!")

        elif 'fine' in query.lower() or "good" in query.lower():
            print("It is so good to hear that your fine!")
            speak("It is so good to hear that your fine!")

        elif 'exit' in query.lower() or 'thankyou' in query.lower():
            print("It was lovely talking to you!")
            speak("It was lovely talking to you!")
            exit()

        elif 'open youtube' in query.lower():
            webbrowser.open('youtube.com')

        elif 'open google' in query.lower():
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query.lower():
            webbrowser.open("stackoverflow.com")

        elif 'open command prompt' in query.lower() or 'open cmd' in query.lower():
            open_cmd()

        elif 'open camera' in query.lower():
            open_camera()

        elif 'open calculator' in query.lower():
            open_calculator()

        elif 'screenshot' in query.lower():
            open_snip()

        elif 'edge' in query.lower():
            open_edge()

        elif 'cortana' in query.lower():
            open_cortana()

        elif 'clock' in query.lower():
            open_clock()

        elif 'open calculator' in query.lower():
            open_calculator()

        elif 'open outlook' in query.lower():
            open_outlook()

        elif 'calender' in query.lower():
            print(calender())

        elif 'ip address' in query.lower():
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen..')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query.lower():
            speak(f'What do you want to search on Wikipedia, {user_name}?')
            search_query = listen().lower()
            results = search_wiki(search_query)
            speak(f"According to Wikipedia, {results}")
            speak(f"For your convenience, I am printing it on the screen user_name.")
            print(results)

        elif 'youtube' in query.lower():
            speak(f'What do you want to play on Youtube, {user_name}?')
            video = listen().lower()
            play_on_youtube(video)

        elif 'google' in query.lower():
            speak(f'What do you want to search on Google, {user_name}?')
            query = listen().lower()
            search_on_google(query)

        elif "whatsapp" in query.lower():
            speak(f'On what number should I send the message {user_name}? Please enter in the console: ')
            number = input("Enter the number: ")
            speak(f"What is the message {user_name}?")
            message = listen().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message" + user_name)

        elif "email" in query.lower():
            try:
                speak(f"What is the message {user_name}")
                content = listen()
                speak(f"On what email address do I send {user_name}.? Please enter in the console: ")
                to = input(f"Enter email address: \n")
                sendEmail(to, content)
                speak(f"Email has been sent {user_name}!")
                print("Email has been sent successfully.")

            except Exception as e:
                print(e)
                speak(f"Something went wrong while I was sending the mail. Please check the error logs {user_name}")
            # speak(f"On what email address do I send {user_name}.? Please enter in the console: ")
            # receiver_address = input("Enter email address: ")
            # speak(f"What should be the subject {user_name}")
            # subject = listen().capitalize()
            # speak(f"What is the message {user_name}")
            # message = listen().capitalize()
            #
            # if send_email(receiver_address, subject, message):
            #     speak(f"I've sent the email {user_name}")
            # else:
            #     speak(f"Something went wrong while I was sending the mail. Please check the error logs {user_name}")

        elif 'joke' in query.lower():
            speak(f"Hope you like this one {user_name}")
            joke = pyjokes.get_joke()
            speak(joke)
            speak(f"For your convenience, I am printing the joke on screen {user_name}")
            print(joke)

        elif "calculate" in query:

            app_id = 'JGL8AP-98UJVQ7QK2'
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("Hang On, I will help you Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps")

        elif "what is" in query.lower() or "who is" in query.lower() or "tell me" in query.lower():
            question = query

            app_id = 'JGL8AP-98UJVQ7QK2'

            # Instance of wolf ram alpha
            # client class
            client = wolframalpha.Client('JGL8AP-98UJVQ7QK2')

            # Stores the response from wolfram alpha
            response = client.query(question)

            # Includes only text from the response
            answer = next(response.results).text

            print(answer)
            speak(answer)

        elif "restart" in query.lower():
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query.lower() or "sleep" in query.lower():
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log out" in query.lower() or "sign out" in query.lower():
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'lock window' in query.lower():
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query.lower():
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query.lower():
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")
        #elif 'emotion' in query.lower():
        #    print("Detecting your emotion, Press Esc Key to Detect.")
        #    speak("Detecting your emotion, Press Escape Key to Detect.")
        #    emote=emotion_detection()
        #    print(f"You are {emote}.")
        #    speak(f"You are {emote}.")
