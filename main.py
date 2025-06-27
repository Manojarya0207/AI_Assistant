import pyttsx3
import speech_recognition as sr
import datetime
import time
import webbrowser
import os
import psutil

def initialize_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    volume = engine.getProperty('volume')
    engine.setProperty('volume',volume+0.25)
    return engine

def speak(text):
    engine = initialize_engine()
    engine.say(text)
    engine.runAndWait()

def command():
    r = sr.Recognizer
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening...........", end="", flush=True)
        r.pause_threshold=1.0
        r.pause_threshold=0.3
        r.sample_rate = 48000
        r.dynamic_energy_threshold=True
        r.operation_timeout=5
        r.non_speaking_duration=0.5
        r.dynamic_energy_adjustment=2
        r.energy_threshold=4000
        r.phrase_time_limit = 10
        print(sr.Microphone.list_microphone_names())
        audio =r.listen(source)

    try:
        print("\r",end="", flush=True)
        print("Recognizing........", end="", flush=True)
        r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        print("Say that again please.")
        return "None"
    return query
 
def cal_day():
    day = datetime.datetime.today().weekday() + 1
    day_dict={
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"saturday",
        7:"sunday"
    }

    if day in day_dict.keys():
        day_of_week = day_dict[day]
        print(day_of_week)
    return day_of_week

def wishme():
    hour = int(datetime.datetime.now().hour)
    t = time.strftime("%I:%M:%p")
    day = cal_day()

    if(hour>=0) and (hour<=12) and ('AM' in t):
        speak(f"Good monring Manoj , it's {day} and the time is {t}.")
    elif(hour>=12) and (hour<=16) and ('PM' in t):
        speak(f"Good afternoon Manoj , it's {day} and the time is {t}.")
    else:
        speak(f"Good evening Manoj , it's {day} and the time is {t}.")

def social_media(command):
    if 'facebook' in command:
        speak('opening the facebook')
        webbrowser.open("https://www.facebook.com")
    elif 'whatsapp' in command:
        speak('opening the whatsapp')
        webbrowser.open("https://web.whatsapp.com")
    elif 'instagram' in command:
        speak('opening the instagram')
        webbrowser.open("https://www.instagram.com")
    else:
        speak("Not result found manoj")

def schedule():
    day = cal_day().lower()
    speak("Boss todays schedule is ")
    week = {
        "saturday":"Boss from 9:00 am to 9:50 am you have dsa class"
    }
    if day in week.keys():
        speak(week[day])

def openApp(command):
    if "calculator" in command:
        speak("opening the calculator")
        os.startfile("c:\\Windows\\System32\\calc.exe")
    elif "notepad" in command:
        speak("opening the notepad")
        os.startfile("c:\\Windows\\System32\\notepad.exe")
    elif "paint" in command:
        speak("opening the paint")
        os.startfile("c:\\Windows\\System32\\mspaint.exe")

def closeApp(command):
    if "calculator" in command:
        speak("closeing the calculator")
        os.system('taskkill /f /im calc.exe')
    elif "notepad" in command:
        speak("closeing the notepad")
        os.system('taskkill /f /im notepad.exe')
    elif "paint" in command:
        speak("closeing the paint")
        os.system('taskkill /f /im mspaint.exe')


def condition():
    useage = str(psutil.cpu_percent())
    speak(f" Manoj cpu is at {useage} percentage")
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"the computer have  {percentage} percentage battery.")

    if percentage>=80:
        speak("Manoj we could have enough charging to continue our work.")
    elif  percentage>=40 and percentage<=75:
        speak("Manoj we should connect our system to charging point to charging your computer. ")
    else:
        speak("Manoj we have very low battery power ,please charging the computer now.")

def play_music():
    music_folder = "C:\\Users\\Dell\\Music\\musics"  
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
        elif "volume up" in query:
            pyautogui.press("volumeup")
            speak("Volume increased.")
        elif "volume down" in query:
            pyautogui.press("volumedown")
            speak("Volume decreased.")
        elif "volume mute" in query:
            pyautogui.press("volumemute")
            speak("Volume muted.")
        elif "open" in query:
            openApp(query)
        elif "close" in query:
            closeApp(query)
        elif "system condition" in query or "condition of the system" in query:
            condition()
        elif "play music" in query:
            play_music()
        elif "exit" in query:
            speak("Goodbye, Manoj!")
            sys.exit()

#speak("hello manojarya")