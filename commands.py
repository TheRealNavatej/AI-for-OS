import os
import psutil
import webbrowser
import pyautogui
import datetime
from speak import speak

def open_app(app):
    paths = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "notepad": "notepad.exe",
        "calculator": "calc.exe"
    }
    if app in paths:
        os.startfile(paths[app])
        speak(f"Opening {app}")
    else:
        speak("I don't know that app yet.")

def system_stats():
    cpu = psutil.cpu_percent()
    battery = psutil.sensors_battery()
    speak(f"CPU usage is {cpu} percent.")
    if battery:
        speak(f"Battery is at {battery.percent} percent.")

def take_screenshot():
    img = pyautogui.screenshot()
    img.save("screenshot.png")
    speak("Screenshot taken and saved.")

def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")

def open_website(site):
    webbrowser.open(f"https://{site}")
    speak(f"Opening {site}")
