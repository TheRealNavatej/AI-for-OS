from speak import listen, speak
from commands import *
from extras import *

def process_command(command):
    if "open" in command:
        if "chrome" in command:
            open_app("chrome")
        elif "notepad" in command:
            open_app("notepad")
        elif "calculator" in command:
            open_app("calculator")
        elif "youtube" in command:
            open_website("youtube.com")
        else:
            speak("Sorry, I can't open that yet.")
    elif "cpu" in command or "battery" in command:
        system_stats()
    elif "time" in command:
        tell_time()
    elif "screenshot" in command:
        take_screenshot()
    elif "joke" in command:
        tell_joke()
    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        search_wikipedia(query)
    elif "weather" in command:
        weather_info("Hyderabad")
    elif "stop" in command or "exit" in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I don’t know that command yet.")

if __name__ == "__main__":
    speak("Hello, I am NeuraDesk. How can I help you?")
    while True:
        command = listen()
        if command:
            process_command(command)
import os
import psutil
import webbrowser
import pyautogui
import datetime
from speak import speak