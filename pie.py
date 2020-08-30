import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

#To select the virtual assistance' voice
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#To  make the virtal assistance speak
def speak(audio):

    engine.say(audio)

    engine.runAndWait()

#wish according to the time of the day
def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
            speak("Good Morning!")
    elif hour>=12 and hour<18:
            speak("Good Afternoon!")
    else:
        speak("Good Evening!")

# To input command from user microphone
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #wait for command for 1 second 
        audio = r.listen(source)

#To conver the audio from user to text and understand
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Go ahead, I am listening...\nYou just said: {query}\n")

#If audio couldn't be understood
    except Exception as e:
        #print(e)
        speak("I am sorry!Could you please say that again?")
        print("Could you please say that again?")
        return "None"

    return query

#Function for sending email 

def sendEmail(to, content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("bhavna7132@gmail.com"," ")
    server.sendmail("bhavna7132@gmail.com",to,content)
    server.close()

if __name__=="__main__" :
    wishme()
    speak("I am Pie! your virtual assistant, How can I help you?")
    while True:
        x = takeCommand().lower()

#To search in wikipedia

        if 'wikipedia' in x:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            x = x.replace("wikipedia", "")
            results = wikipedia.summary(x, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

#Emotional intelligence

        elif ('how are you' in x):
            speak("I am absolutely good, like I am when you are around!")

        elif('joke' in x):
            speak("You mean, your life? just kidding!")

        elif('i' in x) and ('stupid' in x) or ('idiot' in x) or ('fool' in x) or ('boring' in x) or ('fail' in x) or ('sad' in x):
            speak('Remember the last time you said that? No, right! Neither do I, because no matter what, you have always got through everything!') 
            speak('You have got this!')

        elif('love you' in x):
            speak("Awe, that is so sweet of you and needless to say! I love you too and I am always there for you!")

        elif ('you' in x) and ('stupid' in x) or ('idiot' in x) or ('fool' in x) or ('boring' in x) or ('useless' in x):
            speak('Oh I am sorry, I was just trying to help!')

        elif('thank you' in x) or ('thanks' in x):
                speak('I always love to help you')

#To open google chrome

        elif ('open' in x) or ('run' in x) or ('execute' in x) or ('launch' in x) and ('chrome' in x) or ('browser' in x):
            speak("opening google chrome browser")
            os.system("chrome")

#To open youtube

        elif ('open' in x) or ('run' in x) or ('search' in x) or ('launch' in x) and ('youtube' in x):
            speak("opening youtube")
            webbrowser.open("youtube.com")

#To open google

        elif ('open' in x) or ('run' in x) or ('search' in x) or ('launch' in x) and ('google' in x):
            speak("opening google")
            webbrowser.open("google.com")

#To open facebook

        elif ('open' in x) or ('run' in x) or ('search' in x) or ('launch' in x) and ('facebook' in x):
            speak("opening facebook")
            webbrowser.open("facebook.com")
            
#To open stackoverflow

        elif ('open' in x) or ('run' in x) or ('search' in x) or ('launch' in x) and ('stackoverflow' in x):
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

#To open naukri.com

        elif ('open' in x) or ('run' in x) or ('search' in x) or ('launch' in x) and ('naukri' in x):
            speak("opening naukri.com")
            webbrowser.open("naukri.com")

#To open gmail

        elif ('open' in x) or ('run' in x) or ('search' in x) or ('launch' in x) and ('gmail' in x):
            speak("opening gmail")
            webbrowser.open("gmail.com")

#To open instagram

        elif ('open' in x) or ('run' in x) or ('search' in x) or ('launch' in x) and ('instagram' in x):
            speak("opening instagram")
            webbrowser.open("instagram.com")
            
# To open whatsapp           

        elif('whatsapp' in x):
            speak("opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")

#To play music

        elif ('play music' in x) or ('song' in x):
            music_dir = "D:\\music"
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

#To open notepad

        elif ('open' in x) or ('run' in x) or ('execute' in x) or ('launch' in x) and ('notepad' in x) or ('editor' in x):
            speak("opening notepad")
            os.system("notepad") 

#To open windows Media Player

        elif ('open' in x) or ('run' in x) or ('execute' in x) or ('launch' in x) and ('windows media player' in x):
            speak("opening windows media player")
            os.system("wmplayer")

#To know time

        elif ('time' in x) or ('clock' in x) or ('hour' in x):
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

#To know  date

        elif ('date' in x):
            strDate = datetime.datetime.today().strftime("%d/%m/%Y")
            speak(f"The date is {strDate}")        

#To know  day

        elif ('day' in x):
            strDay = datetime.datetime.now().strftime("%A")
            speak(f"The day is {strDay}") 

#To open vscode

        elif ('code' in x) or ('visual studio' in x):
            vscodepath="C:\\Users\\Bhavna\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodepath)

#To send email

        elif 'mail' in x:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "bhavna.1721cs1185@kiet.edu"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I seemed to have encounter an issue in sending email")

#To exit

        elif ('quit' in x) or ('exit' in x) or ('bye' in x) or ('go' in x):
            speak("Goodbye! Have a nice day")
            break


        