import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    # query = gt.translate(audio,dest="hi")
    # audio = query.text
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am jarvis Please tell me how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(sourse)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server=smtplib.SMTP('samtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abhishektyagi2307@gmail.com','ABHISHEK2138433@')
    server.sendmail('abhishektyagi2307@gmail.com',to, content)
    server.close()

def hello():
    speak('ji beta ji')

if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
       

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query=query.replace("wikipedia", "")
            results= wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
                     
        elif 'open youtube' in query:
            speak('ok sir')

            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak('Ok sir')

            webbrowser.open("google.com")

        elif 'hello' in query:
            hello()
            

        elif 'What r u doing' in query:
            speak('Nothing Special')

        elif 'say hello' in query:
            speak('Hello every one')

        elif 'are you listen me ' in query:
            speak('yes Sir')

        elif 'play music' in query:
            speak('ok sir')
            music_dir="E:\\study\\music2"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[4]))

        elif 'play jarvis' in query:
            speak('ok sir')
            music_dir="E:\\study\\music2"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[1]))
        
        elif 'time batao' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif 'open vs code' in query:
            codepath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email to vishal' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to = "abhishektyagi2307@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            
            except Exception as e:
                print(e)
                speak("Soory Abhishek, I am not able to send this email")
