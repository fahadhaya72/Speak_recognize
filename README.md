Speak Recognizer

A powerful speech recognition assistant that listens, converts speech to text, and responds with voice feedback.

Features

Converts speech to text using Google Speech Recognition API

Uses gTTS (Google Text-to-Speech) for voice response

Continuous listening mode

Supports exit commands (exit, stop, quit)

Installation & Setup

Clone the Repository

git clone https://github.com/fahadhaya72/Speak_recognize.git
cd Speak_recognize

Create a Virtual Environment (Recommended)

python -m venv env
source env/bin/activate   # On macOS/Linux
env\Scripts\activate      # On Windows

Install Dependencies

pip install -r requirements.txt

Run the Application

python App.py

Environment Variables

Ensure you set the required environment variables before running the app:

Variable

Description

Default

LANGUAGE

Language for speech (e.g., 'en')

en

TIMEOUT

Time to wait for speech input

5

To set environment variables:

export LANGUAGE='en'
export TIMEOUT=5

(For Windows, use set instead of export.)

License

All rights reserved by fhd_hayat.

Contact Me

For questions or suggestions, feel free to reach out:

GitHub: @fahadhaya72

Email: smr69413@gmail.com

LinkedIn: Fahad Hayat

HackerRank: cyberfahad72

Portfolio: My Portfolio

Thanks for checking out Speak Recognizer!
