# Speak Recognizer

A simple Python-based speech recognition assistant that listens, converts speech to text, and speaks back the detected text.

## 🛠️ Features
- Converts speech to text using Google Speech Recognition API.
- Uses `gTTS` (Google Text-to-Speech) for voice response.
- Continuous listening mode.
- Exit command support (`exit`, `stop`, `quit`).

---

## 📥 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/fahadhaya72/Speak_recognize.git
cd Speak_recognize
```

### 2️⃣ Create a Virtual Environment (Recommended)
```sh
python -m venv env
source env/bin/activate   # On macOS/Linux
env\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```sh
python App.py
```

---

## 🌎 Environment Variables
Make sure to set up the required environment variables before running the app.

| Variable         | Description                   | Default |
|-----------------|------------------------------|---------|
| `LANGUAGE`      | Language for speech (e.g., 'en') | `en`    |
| `TIMEOUT`       | Time to wait for speech input | `5`     |

To set environment variables:
```sh
export LANGUAGE='en'
export TIMEOUT=5
```
(For Windows, use `set` instead of `export`.)

---

## 📜 License
All rights reserved by **fhd_hayat**.

---

## 📞 Contact
For queries, feel free to reach out:
- GitHub: [@fahadhaya72](https://github.com/fahadhaya72)

