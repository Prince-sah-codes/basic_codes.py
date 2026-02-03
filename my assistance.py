import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser


# ========== CONFIG ==========
ASSISTANT_NAME = "Jarvis"
# ============================

engine = pyttsx3.init()
engine.setProperty('rate', 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_me():
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good morning Prince sir")
    elif hour < 18:
        speak("Good afternoon Prince sir")
    else:
        speak("Good evening Prince sir")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except:
        speak("Sorry, I didn't understand")
        return ""



# ========== MAIN ==========
wish_me()
speak(f"I am jarvis your personal assistance. How can I help you sir?")

while True:
    query = take_command()

    if "what's the time jarvis" in query:
        time = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {time}")

    elif "what is the date today" in query:
        date = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {date}")

    elif "tell me about srk jarvis" or "tell me about shahrukh khan" in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    elif "open youtube" in query:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open google" in query:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "exit" in query or "quit" in query:
        speak("Goodbye Prince sir")
        break

 