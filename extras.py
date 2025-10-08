import wikipedia
import pyjokes
import requests
from speak import speak

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        speak(summary)
    except:
        speak("Sorry, I couldn't find that on Wikipedia.")

def weather_info(city="Hyderabad"):
    api_key = "YOUR_OPENWEATHER_API_KEY"  # Optional
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        data = requests.get(url).json()
        if data["cod"] == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            speak(f"The temperature in {city} is {temp}°C with {desc}.")
        else:
            speak("City not found.")
    except:
        speak("Error fetching weather data.")
