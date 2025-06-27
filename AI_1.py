import pyttsx3
import speech_recognition as sr
import datetime
import time
import webbrowser
import os
import psutil
import pyautogui
import sys
import json
import pyjokes

def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + 0.25)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print(" Listening...", end="", flush=True)
        r.pause_threshold = 0.8
        r.energy_threshold = 4000
        try:
            print("\r",end=" ", flush=True)
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
            print("Recognizing...", end="", flush=True)
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand that. Please say it again.")
            return "None"
        except sr.RequestError as e:
            print("Request error; check your internet connection.")
            return "None"
        except Exception as e:
            print(f"Error: {str(e)}")
            return "None"

config_file = "assistant_config.json"

def load_config():
    try:
        with open(config_file, "r") as file:
            return json.load(file)  
    except FileNotFoundError:
        print(f"{config_file} not found. Ensure it exists and is properly configured.")
        sys.exit()
    except json.JSONDecodeError:
        print(f"Error decoding {config_file}. Ensure it contains valid JSON.")
        sys.exit()

config = load_config() 


def cal_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return day_dict.get(day, "Unknown Day")

def wishme():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M %p")
    day = cal_day()
    if hour >= 0 and hour < 12:
        speak(f"Good morning, Manoj! It's {day} and the time is {t}.")
    elif hour >= 12 and hour < 18:
        speak(f"Good afternoon, Manoj! It's {day} and the time is {t}.")
    else:
        speak(f"Good evening, Manoj! It's {day} and the time is {t}.")

def social_media(command):
    if 'facebook' in command:
        speak('Opening Facebook.')
        webbrowser.open("https://www.facebook.com")
    elif 'whatsapp' in command:
        speak('Opening WhatsApp.')
        webbrowser.open("https://web.whatsapp.com")
    elif 'instagram' in command:
        speak('Opening Instagram.')
        webbrowser.open("https://www.instagram.com")
    elif 'youtube' in command:
        speak('Opening YouTube.')
        webbrowser.open("https://www.youtube.com")
    else:
        speak("Sorry, no matching social media found.")

def schedule():
    day = cal_day().lower()
    week = {
        "saturday": "Boss, from 9:00 am to 9:50 am, you have a DSA class.",
    }
    speak(week.get(day, "No schedule for today."))

def openApp(command):
    if "calculator" in command:
        speak("Opening the calculator.")
        os.startfile("c:\\Windows\\System32\\calc.exe")
    elif "notepad" in command:
        speak("Opening Notepad.")
        os.startfile("c:\\Windows\\System32\\notepad.exe")
    elif "paint" in command:
        speak("Opening Paint.")
        os.startfile("c:\\Windows\\System32\\mspaint.exe")
    else:
        speak("Application not recognized.")

def closeApp(command):
    if "calculator" in command:
        speak("Closing the calculator.")
        os.system('taskkill /f /im calc.exe')
    elif "notepad" in command:
        speak("Closing Notepad.")
        os.system('taskkill /f /im notepad.exe')
    elif "point" in command:
        speak("Closing Paint.")
        os.system('taskkill /f /im mspaint.exe')
    elif 'open Google' in query:
        speak("Manoj, whats should i search on google")
        s = command().lower()
        webbrowser.open(f"{s}")
    else:
        speak("Application not recognized.")



def play_music():
    music_folder = "C:\\Users\\Dell\\Music\\musics\\musics"  
    try:
        songs = os.listdir(music_folder)
        if songs:
            song = random.choice(songs)
            os.startfile(os.path.join(music_folder, song))
            speak(f"Playing {song}.")
        else:
            speak("No music files found.")
    except Exception as e:
        speak("Sorry, an error occurred while trying to play music.")



def condition():
    usage = str(psutil.cpu_percent())
    speak(f"Manoj, the CPU is at {usage} percent usage.")
    battery = psutil.sensors_battery()
    if battery:
        percentage = battery.percent
        speak(f"The computer has {percentage} percent battery remaining.")
        if percentage >= 80:
            speak("We have enough charge to continue working.")
        elif 40 <= percentage < 80:
            speak("We should connect the system to a charging point soon.")
        else:
            speak("Battery is low. Please charge the computer.")
    else:
        speak("Battery information is not available.")


def browsing(query):
    if 'google' in query:
        speak("Manoj, what's should i search on google")
        s = command().lower()
        webbrowser.open(f"{s}")




if __name__ == "__main__":
    wishme()
    while True:
        query = command().lower()
        if query == "none":
            continue
        if any(keyword in query for keyword in ['facebook', 'whatsapp', 'instagram']):
            social_media(query)
        elif 'time table' in query or 'schedule' in query:
            schedule()
        elif "volume up" in query or " increase the volume" in query:
            pyautogui.press("volumeup")
            speak("Volume increased.")
        elif "volume down" in query or "increase the volume" in query:
            pyautogui.press("volumedown")
            speak("Volume decreased.")
        elif "volume mute" in query or "mute the volume" in query:
            pyautogui.press("volumemute")
            speak("Volume muted.")
        elif "open " in query:
            openApp(query)
        elif "Hi" in query or "Hey" in query:
            print("hi there why can i help you...")
        elif "close" in query:
            closeApp(query)
        elif "system condition" in query or "condition of the system" in query:
            condition()
        elif "play music" in query:
            play_music()
        
        elif "what is your name" in query or "what's your name" in query:
            speak("my name is ")
        elif "hey jannu" in query or "hi" in query:
            speak("hii manoj how can I help you.")
        elif "who made you " in query or "made you" in query:
            speak("I was made by, Manojarya")
        elif ("who was developed you ") in query or "developed you " in query:
            speak("I was developed by , Manojarya")
        elif "how are you " in query or "oh are you " in query:
            speak("All Good , what about you ")
        elif "joke " in query or "tell me the joke" in query:
            joke_1 = pyjokes.get_joke(language="en",category="neutral")
            speak(jake_1)
        elif ("open google" in query):
            browsing(query)

        elif "exit" in query or "you can leave now" in query or " ok bye " in query:
            speak("Goodbye, Manoj!")
            sys.exit()