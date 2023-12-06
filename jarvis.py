"""
This is Jarvis program.
Jarvis is a voice assistant, similar to Apple's Siri or Google Now.
"""
# Import some modules.
import datetime
import os
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()

voices = engine.getProperty('voices')

# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
"""
    To give the own voice.

    Args:
        Say your side audio.

    Returns:
        Return to speak with me.
    """

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

"""
    Wish_me to everyone .

    Args:
       Time and name took voice.

    Returns:
       Greating  for everyone and take our suggesions.

    """

def wish_Me():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning...!")
    elif 12 <= hour < 18:
        speak("Good afternoon...!")
    else:
        speak("Good evening...!")

    speak("I am Jervis, please tell me how may I help you.")

"""
    To taking the all voices .

    Args:
        Add your work with voice.

    Returns:
       Return to all answer in giving only string.
    """
def take_Command():
    # It takes microphone input from the user and returns a string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        # return query

    except Exception:
        # print(e)
        print("Say that again, please...")
        return "None"
    return query

# This below lines are main function calling method.
if __name__ == "__main__":
    wish_Me()
    while True:
        query = take_Command().lower()

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)  # Corrected typo in 'sentences'
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('https://www.youtube.com')

        elif 'open google' in query:
            webbrowser.open('https://www.google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('https://stackoverflow.com')

        elif 'play music' in query:
            Music_Dir = 'D:\\songs\\Favorite'
            songs = os.listdir(Music_Dir)
            print(songs)
            os.startfile(os.path.join(Music_Dir, songs[0]))  # Corrected typo in 'startfile'

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")  # Corrected typo in 'strftime'
            speak(f"Sir, the time is {strTime}")
        else:
            print("think you")
            