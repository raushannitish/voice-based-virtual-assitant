import requests 
from online_ops import find_my_ip,get_random_advice, get_random_joke, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message,check_internet_speed
import pyttsx3
import speech_recognition as sr
from datetime import datetime
from os_ops import open_calculator, open_camera, open_cmd, open_notepad,tellDay,tellTime,take_screenshot,play_music,stop_music,shutdown
from random import choice
from utils import opening_text
from pprint import pprint
import webbrowser 


#I developed by Microsoft for implementing speech recognition and
#  synthesis capabilities in Windows-based applications.
engine = pyttsx3.init('sapi5') 

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Text to Speech Conversion
def speak(text):
    """Used to speak whatever text is passed to it"""

    engine.say(text)
    print(text)
    engine.runAndWait()


# Greet the user
def greet_user():
    """Greets the user according to the time"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon")
    elif (hour >= 16) and (hour < 24):
        speak(f"Good Evening")
    speak(f"I am your Assistant. How may I assist you?")


# Takes Input from User
def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(query)
        if any(phrase in query for phrase in ["bye","okk tata bye bye",'bye bye','phir milte hai','exit']):
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            speak("Thank you")
            exit()
        else:
            speak(choice(opening_text))
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if any(phrase in query for phrase in ['open notepad', 'notepad kholo', 'please open notepad', 'notepad khul ja','notepad']):
            open_notepad()
            

        elif any(phrase in query for phrase in ['open command prompt', 'open cmd', 'command prompt kholo', 'please open command prompt','cmd']):
            open_cmd()

        elif any(phrase in query for phrase in ['time','time btao','time now','time kya ho raha hai abhi','kitna baj raha hai','samay','abhi ka time']):
            hour,min=tellTime()
            speak("The time is "+hour+"and"+min)
        elif any(phrase in query for phrase in ['date','date btao','date now','Aaj kon sa date hai','date kya hai','tarik','aj kaun sa tarik hai']):
            day=tellDay()
            speak("The day is "+day)

        elif any(phrase in query for phrase in ['open camera','camera kholo','please open camera','camera','chalchitra']):

            open_camera()
            speak("Picture taken successfully!")

        elif any(phrase in query for phrase in ['open calculator','calculator','calculator kholo']):
            open_calculator()

        elif any(phrase in query for phrase in ['ip address','mera ip address btao','tell my ip address','my ip','ip address']):
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif any(phrase in query for phrase in ['wikipedia','wikipedia pr khojo','search on wikepedia','wikipedia se dekho','wikipedia open kro','open wikipedia']):
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif any(phrase in query for phrase in ['youtube','open youtube','youtube kholo','youtube dekhna hai']):
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)
            exit()

        elif any(phrase in query for phrase in ['search on google','google se dekho','open google','google','google kholo']):
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif any(phrase in query for phrase in ["send whatsapp message","ek whatsapp messase bhejo",'ek whatsapp message bhejna hai','whatsapp','whatsapp krna hai']):
            speak(
                'On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif any(phrase in query for phrase in ["send an email","send email",'ek mail send kro','email','ek email kro','ek mail kro']):
            speak("On what email address do I send sir? Please enter in the console: ")
            receiver_address = input("Enter email address: ")
            speak("What should be the subject sir?")
            subject = take_user_input().capitalize()
            speak("What is the message sir?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("I've sent the email sir.")
            else:
                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")
            exit()
        elif any(phrase in query for phrase in ["joke","ek joke sunao",'ek chutkula sunao','funny joke','make me happy','make me laugh']):
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif any(phrase in query for phrase in ["any advice","koe advice",'advice','koe salah','salah']):
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif any(phrase in query for phrase in ['ecommerce','ecommerce website','flipkart']):
            webbrowser.open('www.flipkart.com')

        elif any(phrase in query for phrase in ['play music','music','gana','gana sunao']):
            print("Playing music")
            speak("Playing music")
            play_music()
            exit()

        elif any(phrase in query for phrase in ['stop music', 'music band karo', 'music stop']):
            speak("music stopped")
            stop_music()

        elif any(phrase in query for phrase in ['screenshot', 'take screenshot', 'Screenshot lo','screenshot ligiye']):
            speak("Taking screenshot")
            take_screenshot()

        elif any(phrase in query for phrase in ['shutdown', 'laptop band karo','laptop close karo']):
            speak("Thank you ,Bye")
            shutdown()

        elif any(phrase in query for phrase in ['speed test', 'internet speed','mera internet speed batao','speed']):
            speak("Cheking,   It may take some time..please wait")
            download,upload=check_internet_speed()
            speak(f"Your downloading speed is {str(download)} Mbps and your uploading speed is {str(upload)} Mbps")
        # elif any(phrase in query for phrase in ['what you can do', 'your features','tasks you can able to perform']):
        #     speak("The following task i can perform 1. Tell you about day 2.Tell you about time 3.google search 4.searching on youtube 5.Details from wekipedia 6. opening notepad")
        

       