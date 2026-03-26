import speech_recognition as sr
import pyttsx3
from datetime import datetime
import wikipedia


# Initialize engine (Windows)
engine = pyttsx3.init('sapi5')


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_time():
    time=datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {time}")
    print("current time :",time)

def search_wikipedia(query):
    try:
        result=wikipedia.summary(query,sentences=2)
        speak(result)
        print(result)
    except wikipedia.exceptions.DisambiguationError:
        speak("there are multiple result, please specify")
    except wikipedia.exceptions.PageError:
        speak("no results found")
        
def recognize_speech():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    
    except sr.UnknownValueError:
        print("Could not understand")
        return None
    
    except sr.RequestError:
        print("API error")
        return None


def process_command(command):
    if "time" in command:
        get_time()
    elif "wikipedia" in command :
        speak("what do you want to search on wikipedia ?")
        query=recognize_speech()
        if query:
            print("Searching Wikipedia for:", query)
            speak(f"Searching Wikipedia for {query}")
            search_wikipedia(query)
        else:
            speak("sorry i dont understand that command")
    elif "exit" in command or "stop" in command or "quit" in command:
        speak("Goodbye!")
        return False

def start_voice_assistant():
    speak("hello! i am your voice assistant . how can i help you ?")
    while True:
        command=recognize_speech()
        if command:
            process_command(command)
            
            
# Run assistant
start_voice_assistant()
