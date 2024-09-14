import os
import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import time
import wikipedia
import threading
import requests
import subprocess
import random
import psutil
import platform
import pygame  # Import pygame for audio playback

# Initialize pygame mixer
pygame.mixer.init()

# Sample questions and answers for the quiz
quiz_questions = [
    {"question": "What is the capital of France?", "answer": "paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "jupiter"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "harper lee"},
    {"question": "What is the chemical symbol for gold?", "answer": "au"},
    {"question": "Who painted the Mona Lisa?", "answer": "leonardo da vinci"},
    {"question": "Who is called as the God of Cricket?", "answer": "Sachin Tendulkar"}
]

# Voice / Language options
voices = {
    'es-mx': r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0',
    'en-us': r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0',
    'en-us-zira': r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0',
    'es-es': r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0',
    'en-gb': r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
}

# Initialize pyttsx3 engine
def init_speech_engine(voice_id):
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_id)
    return engine

# Hear the microphone and return the audio as text
def transform_audio_into_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        print("You can now speak")
        audio = r.listen(source)

        try:
            request = r.recognize_google(audio, language="en-gb")
            print("You said " + request)
            return request
        except sr.UnknownValueError:
            print("Ups! I didn't understand audio")
            return "I am still waiting"
        except sr.RequestError:
            print("Ups! There is no service")
            return "I am still waiting"
        except Exception as e:
            print(f"Ups! Something went wrong: {e}")
            return "I am still waiting"

# Function so the assistant can be heard
def speak(message, voice_id='en-gb'):
    engine = init_speech_engine(voices[voice_id])
    engine.say(message)
    engine.runAndWait()

# Inform day of the week
def ask_day():
    today = datetime.date.today()
    week_day = today.weekday()
    calendar = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}
    speak(f'Today is {calendar[week_day]}')

# Inform what time it is
def ask_time():
    now = datetime.datetime.now()
    time_message = f'At this moment it is {now.hour} hours and {now.minute} minutes'
    speak(time_message)

# Inform what month it is
def ask_month():
    now = datetime.datetime.now()
    month_message = f'This month is {now.strftime("%B")}'
    speak(month_message)

# Inform what year it is
def ask_year():
    now = datetime.datetime.now()
    year_message = f'This year is {now.year}'
    speak(year_message)

# Create initial greeting
def initial_greeting():
    speak('Hello I am John. How can I help you?')

# Function to set an alarm
def set_alarm(alarm_time):
    speak(f'Alarm set for {alarm_time}')
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            speak('Alarm ringing! Time to wake up!')
            pygame.mixer.music.load('alram_sound.mp3')  # Load your alarm sound
            pygame.mixer.music.play()  # Play the alarm sound
            while pygame.mixer.music.get_busy():  # Wait until the sound finishes
                time.sleep(1)
            break
        time.sleep(60)  # Check every minute

# Thread function for alarm
def alarm_thread(alarm_time):
    alarm_thread = threading.Thread(target=set_alarm, args=(alarm_time,))
    alarm_thread.start()

# Function to open WhatsApp
def open_whatsapp():
    speak('Opening WhatsApp')
    os.system('start whatsapp:')

# Function to ask a quiz question and check the answer
def ask_quiz():
    question = random.choice(quiz_questions)
    correct_answer = question["answer"]
    speak(question["question"])
    user_answer = transform_audio_into_text().lower()

    if user_answer == correct_answer:
        speak("Correct! Well done.")
    else:
        speak(f"Incorrect. The correct answer is {correct_answer}.")


# Function to get system information
def get_system_info():
    uname = platform.uname()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    system_info = (
        f"System: {uname.system} {uname.release} ({uname.version})\n"
        f"Node Name: {uname.node}\n"
        f"Machine: {uname.machine}\n"
        f"Processor: {uname.processor}\n"
        f"CPU Usage: {cpu_usage}%\n"
        f"Memory Usage: {memory_info.percent}%\n"
        f"Disk Usage: {disk_info.percent}%"
    )

    speak(system_info)


# Main function of the assistant
def my_assistant():
    initial_greeting()
    go_on = True

    while go_on:
        request = transform_audio_into_text().lower()

        if 'set an alarm for' in request:
            time_str = request.replace('set an alarm for', '').strip()
            try:
                # Check if the time is in correct format
                datetime.datetime.strptime(time_str, '%H:%M')
                speak(f'Setting an alarm for {time_str}')
                alarm_thread(time_str)
            except ValueError:
                speak('Sorry, I did not understand the time format. Please use HH:MM.')


        elif 'weather' in request:

            api_key = "8ef61edcf1c576d65d836254e11ea420"

            base_url = "https://api.openweathermap.org/data/2.5/weather?"

            speak("What's the city name?")

            city_name = transform_audio_into_text()

            complete_url = base_url + "appid=" + api_key + "&q=" + city_name

            response = requests.get(complete_url)

            x = response.json()

            if x["cod"] != "404":

                y = x["main"]

                current_temperature_kelvin = y["temp"]

                current_humidity = y["humidity"]

                z = x["weather"]

                weather_description = z[0]["description"]

                # Convert temperature from Kelvin to Celsius

                current_temperature_celsius = current_temperature_kelvin - 273.15

                speak(f"Temperature in Celsius is {current_temperature_celsius:.2f}."

                      f" Humidity in percentage is {current_humidity}."

                      f" Description is {weather_description}.")

                print(f"Temperature in Celsius = {current_temperature_celsius:.2f}."

                      f" Humidity (in percentage) = {current_humidity}."

                      f" Description = {weather_description}.")

            else:

                speak("City not found.")

        elif 'quiz' in request:
            ask_quiz()

        elif 'system info' in request or 'system information' in request:
            get_system_info()

        elif 'open youtube' in request:
            speak('Sure, I am opening YouTube')
            webbrowser.open('https://www.youtube.com')

        elif 'open browser' in request:
            speak('Of course, I am opening Google')
            webbrowser.open('https://www.google.com')

        elif 'open linkedin' in request:
            speak('Sure, I am opening LinkedIn')
            webbrowser.open('https://www.linkedin.com/in/aditya-ranjan-sahu-07a2b7235/')

        elif 'what day is today' in request:
            ask_day()

        elif 'what time is it' in request:
            ask_time()

        elif 'what month is it' in request:
            ask_month()

        elif 'what year is it' in request:
            ask_year()

        elif 'do a wikipedia search for' in request:
            search_term = request.replace('do a wikipedia search for', '').strip()
            speak('I am looking for it')
            try:
                answer = wikipedia.summary(search_term, sentences=1)
                speak(f'According to Wikipedia: {answer}')
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f'There are multiple results for {search_term}. Please be more specific.')
            except wikipedia.exceptions.PageError:
                speak('I couldn’t find a page for your search term.')

        elif 'search the internet for' in request:
            search_term = request.replace('search the internet for', '').strip()
            speak('Searching the internet')
            pywhatkit.search(search_term)
            speak('This is what I found')

        elif 'play' in request:
            song = request.replace('play', '').strip()
            speak(f'Playing {song}')
            pywhatkit.playonyt(song)

        elif 'joke' in request:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'stock price' in request:
            stock = request.split()[-2].strip()
            portfolio = {'apple': 'AAPL', 'amazon': 'AMZN', 'google': 'GOOGL'}
            if stock in portfolio:
                try:
                    ticker = portfolio[stock]
                    stock_info = yf.Ticker(ticker).info
                    price = stock_info.get('regularMarketPrice', 'Price not available')
                    speak(f'The price of {stock} is {price}')
                except Exception as e:
                    speak('I am sorry, but I didn’t find the stock price.')
            else:
                speak('I am sorry, I don’t have information for that stock.')

        elif 'open espncricinfo' in request:
            speak('Of course, I am opening ESPN Cric Info')
            webbrowser.open('https://www.espncricinfo.com/')

        elif 'open aaj tak news' in request:
            speak('Of course, I am opening Aaj Tak News')
            webbrowser.open('https://www.indiatoday.in/aajtak-livetv')

        elif 'open flipkart' in request:
            speak('Of course, I am opening Flipkart')
            webbrowser.open('https://www.flipkart.com/')

        elif 'open amazon' in request:
            speak('Of course, I am opening Amazon')
            webbrowser.open(
                'https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_5szpgfto9i_e&adgrpid=155259813593&hvpone=&hvptwo=&hvadid=674893540034&hvpos=&hvnetw=g&hvrand=13150601451261614019&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007799&hvtargid=kwd-64107830&hydadcr=14452_2316413&gad_source=1')

        elif 'open nike' in request:
            speak('Of course, I am opening Nike store')
            webbrowser.open('https://www.nike.com/in/w/jordan-shoes-37eefzy7ok')

        elif 'open website' in request:
            website = request.replace('open website', '').strip()
            if not website.startswith(('http://', 'https://')):
                website = 'http://' + website
            speak(f'Opening {website}')
            webbrowser.open(website)

        elif 'open github' in request:
            speak('Of course, I am opening Github')
            webbrowser.open('https://github.com/AdityaOm6603')

        elif 'open l code' in request:
            speak('Yes I am open Leetcode')
            webbrowser.open('https://leetcode.com/problemset/')

        elif 'open udemy' in request:
            speak('Yes I"m opening Udemy')
            webbrowser.open('https://www.udemy.com/home/my-courses/learning/')

        elif 'open gmail' in request:
            speak('Opening your Google Mail')
            webbrowser.open('https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox')

        elif 'open whatsapp' in request:
            open_whatsapp()

        elif 'goodbye' in request:
            speak('I am going to rest. Let me know if you need anything')
            go_on = False

        elif "log off" in request or "sign out" in request:
            speak("Okay, your PC will log off in 20 seconds. Please make sure you exit all applications.")
            time.sleep(20)  # Wait for 20 seconds before logging off
            subprocess.call(["shutdown", "/l"])  # Log off the user

my_assistant()
