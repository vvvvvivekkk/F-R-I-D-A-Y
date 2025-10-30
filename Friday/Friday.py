import os
import openai
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import requests
import pywhatkit
import wikipedia
from dotenv import load_dotenv

# Load API key
load_dotenv()
openai.api_key = os.getenv("sk-...Vr8A")

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print(f"Friday: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎧 Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-in')
        print(f"Vivek said: {command}\n")
    except:
        return ""
    return command.lower()

def chat_with_openai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # or gpt-4-turbo, gpt-5 if available
        messages=[{"role": "system", "content": "You are Friday, an AI assistant like Alexa."},
                  {"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def wish():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning Vivek!")
    elif 12 <= hour < 18:
        speak("Good afternoon Vivek!")
    else:
        speak("Good evening Vivek!")
    speak("I'm Friday, your AI assistant. How can I help you today?")

def weather(city="Hyderabad"):
    url = f"https://api.weatherapi.com/v1/current.json?key=637dba11db84604ad025c88b6800e0c&q={city}"
    res = requests.get(url)
    data = res.json()
    temp = data['current']['temp_c']
    condition = data['current']['condition']['text']
    speak(f"The weather in {city} is {condition} with a temperature of {temp}°C")

def open_whatsapp():
    speak("Opening WhatsApp web")
    webbrowser.open("https://web.whatsapp.com/")

def send_whatsapp_message():
    speak("Who do you want to message?")
    name = listen()
    speak("What is the message?")
    message = listen()
    pywhatkit.sendwhatmsg_instantly("+919346375528", message)
    speak("Message sent successfully!")

def perform_task(query):
    if 'open youtube' in query:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open chrome' in query:
        speak("Opening Google Chrome")
        webbrowser.open("https://www.google.com")

    elif 'open whatsapp' in query:
        open_whatsapp()

    elif 'send whatsapp' in query or 'message' in query:
        send_whatsapp_message()

    elif 'open chat' in query:
        speak("Opening Google Chat")
        webbrowser.open("https://chat.google.com")

    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {strTime}")

    elif 'weather' in query:
        speak("Which city?")
        city = listen()
        if city == "":
            city = "Hyderabad"
        weather(city)

    elif 'play music' in query:
        speak("Playing music on YouTube")
        pywhatkit.playonyt("Bollywood music")

    elif 'search' in query:
        topic = query.replace("search", "")
        speak(f"Searching {topic}")
        webbrowser.open(f"https://www.google.com/search?q={topic}")

    elif 'who is' in query or 'what is' in query:
        try:
            info = wikipedia.summary(query, 2)
            speak(info)
        except:
            speak("Let me check...")
            ans = chat_with_openai(query)
            speak(ans)

    elif 'joke' in query:
        speak(chat_with_openai("Tell me a funny joke"))

    elif 'news' in query:
        speak("Opening latest news headlines")
        webbrowser.open("https://news.google.com/")

    elif 'exit' in query or 'stop' in query:
        speak("Goodbye Vivek! Have a great day!")
        exit()

    else:
        ans = chat_with_openai(query)
        speak(ans)

if __name__ == "__main__":
    wish()
    while True:
        command = listen()
        if command:
            perform_task(command)
