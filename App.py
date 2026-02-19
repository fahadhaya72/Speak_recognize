import speech_recognition as sr
from gtts import gTTS
import playsound
import os
# i got it 
def speak(text):
    """Convert text to speech and play it."""
    tts = gTTS(text=text, lang='en')
    filename = "response.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)  # Delete file after playing

def recognize_speech():
    """Listen for speech and return recognized text."""
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("🎤 Listening... Speak now.")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

        text = recognizer.recognize_google(audio).lower()
        print("📝 Detected Speech:", text)
        speak(text)
        return text

    except sr.UnknownValueError:
        print("❌ Could not understand speech")
        speak("Please speak something")
    except sr.RequestError:
        print("⚠️ Speech Recognition API is unavailable")
        speak("There is a problem with the speech recognition service")
    except KeyboardInterrupt:
        print("\n👋 Exiting...")
        return "exit"
    except Exception as e:
        print(f"⚠️ Error: {e}")

    return None

# Infinite loop to continuously listen
print("🎙️ Voice Assistant Started! Say 'exit' to stop.")

while True:
    detected_text = recognize_speech()

    if detected_text in ["exit", "stop", "quit"]:
        speak("Goodbye!")
        print("👋 Exiting program.")
        break

    print("🔄 Listening again...")
