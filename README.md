# John the voice assistant
# Table of Contents
* [Intrduction](#Introduction)
* [Features](#Features)
* [Installation](#Installation)
* [Libraries](#Libraries)
* [Operations](#Operations)
* [Future Enhancements](#Future Enhancements)
* [Conclusion](#Conclusion)
## Introduction
The voice assistant script is a Python-based application designed to provide a variety of functionalities through voice commands. It leverages speech recognition and synthesis to interact with users, offering a range of features from setting alarms to retrieving stock prices and playing media. The assistant is designed to be both interactive and informative, making it a versatile tool for managing daily tasks and obtaining information.

## Features
### ->Voice Interaction
Speech Recognition: Converts spoken language into text using Google's Web Speech API. Text-to-Speech: Provides auditory responses to user queries using pyttsx3.

### ->Information Retrieval
Date and Time: Reports the current day, time, month, and year. Wikipedia Search: Retrieves and reads out summaries from Wikipedia. Stock Prices: Provides current stock prices for predefined stocks using yfinance. System Information: Reports on system performance metrics like CPU usage, memory usage, and disk space.

### ->Entertainment
Jokes: Tells jokes using pyjokes. Music: Plays music on YouTube based on user requests.

### ->Productivity
Set Alarms: Allows users to set alarms with customizable times. Open Websites: Opens various websites like YouTube, Google, LinkedIn, and others. Quiz Game: Engages users with a quiz game asking trivia questions.

### ->Additional Utilities
Weather Information: Fetches current weather details for a specified city (although this feature has been disabled in the current version). Log Off: Logs off the user from the system upon request.

## Installation
Clone the repository:

git clone https://github.com/yourusername/Voice-Assistant.git
cd Voice-Assistant
Install Pygame:

pip install pygame
pip install request
pip install pyaudio
pip install SpeechRecognition
pip install pyttsx3
pip install pyjokes
pip install requests
pip install pywhatkit
pip install subprocess
pip install psutil
pip install webbrowser
pip install wikipedia
pip install yfinance
Run the game:

python Voice_Assistant.py
## Libraries
os: Provides functions for interacting with the operating system, such as opening applications and logging off the user.

pyttsx3: Enables text-to-speech capabilities for providing vocal responses.

speech_recognition: Handles speech-to-text conversion for understanding user commands.

pywhatkit: Facilitates interactions with YouTube, WhatsApp, and internet searches.

yfinance: Fetches stock market data.

pyjokes: Generates jokes for entertainment.

webbrowser: Opens URLs in a web browser.

datetime: Handles date and time operations.

time: Manages time-related tasks such as setting alarms.

wikipedia: Retrieves summaries from Wikipedia.

requests: Makes HTTP requests to fetch data from web APIs.

pygame: Manages audio playback for alarm sounds.

psutil: Provides system and process utilities.

platform: Retrieves system information.

## Operations
Voice Commands: The assistant listens for specific commands and performs corresponding actions. Response Generation: Converts responses into speech and plays them back to the user. Alarm Functionality: Monitors the system clock and plays an alarm sound when the set time is reached. Information Fetching: Retrieves and presents information from various sources, including stock prices and Wikipedia.

## Future Enhancements
Enhanced Natural Language Processing: Implement more sophisticated NLP techniques to understand and process a wider variety of user commands. Integration with Other APIs: Incorporate additional APIs for extended functionalities, such as flight tracking or news updates. Customizable Responses: Allow users to customize the voice assistant’s responses and behavior. Improved Error Handling: Implement more robust error handling to manage unforeseen issues or unsupported commands. User Authentication: Add security features to restrict certain actions based on user authentication.

## Conclusion
The voice assistant script is a well-rounded tool that combines various functionalities to assist users with daily tasks and provide information. Its use of speech recognition and synthesis enables seamless interaction, while its diverse set of features caters to various needs ranging from entertainment to productivity. With potential enhancements, the assistant can become an even more powerful tool, offering a broader range of capabilities and improved user experience.

Overall, the voice assistant is a practical and engaging solution for automating tasks and retrieving information, showcasing the power of Python in developing interactive applications.
