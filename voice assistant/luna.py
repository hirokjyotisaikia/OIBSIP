import datetime
import pyaudio
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!, Hirok")
    elif hour>=12 and hour < 18:
        speak("Good Afternoon!, Hirok")
    else:
        speak("Good Evening!, Hirok")

    speak("I am Luna, Your voice assistant, How may i help you ?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listeining....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User_said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please.")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takecommand().lower()

        #logic based for executing based task
        if "wikipedia" in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
    
        elif "youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open github" in query:
            webbrowser.open("github.com")

        elif "play music" in query:
            music_dir= 'C:\\Users\\hirok\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H %M")
            speak(f"The time is {strTime}")

        elif "the date" in query:
            strdate = datetime.datetime.now().strftime("%D")
            print(strdate)
            speak(f"The date is  {strdate}")

        elif "open vs code" in query:
            codepath = "C:\\Users\\hirok\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "open spotify" in query:
            spotify_path = "C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.242.290.0_x64__zpdnekdrzrea0\\Spotify.exe"
            os.startfile(spotify_path)

        elif "search" in query:
            search_term = query.replace("search", "").strip() #reeplaces the search
            webbrowser.open("https://www.google.com/search?q=" + search_term )