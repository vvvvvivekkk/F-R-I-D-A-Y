# F.R.I.D.A.Y — Voice Assistant in Python

F.R.I.D.A.Y is a simple voice assistant that listens to your commands and performs tasks like chatting with OpenAI, opening websites, playing YouTube videos, searching Wikipedia, and speaking responses back to you.

## Features
- Voice input using `SpeechRecognition` and `PyAudio`
- Text-to-speech with `pyttsx3`
- Chat responses via OpenAI (ChatCompletion API)
- Open websites, play YouTube videos (`pywhatkit`), and search Wikipedia
- Simple console logs and friendly voice feedback

## Requirements
- Python 3.12 (recommended)
- Windows (tested)
- Microphone enabled

## Python Packages
- `openai==0.28.0` (older API compatible with `openai.ChatCompletion.create`)
- `SpeechRecognition==3.10.0`
- `PyAudio` (0.2.14 confirmed working)
- `python-dotenv`
- `pyttsx3`, `pywhatkit`, `wikipedia`, `requests`

## Setup
1. Create a virtual environment:
   - `python -m venv .venv`
   - `./.venv/Scripts/activate` (PowerShell)

2. Install dependencies:
   - `pip install -r requirements.txt` (optional)
   - Or individually:
     - `pip install openai==0.28 SpeechRecognition==3.10.0 pyttsx3 pywhatkit wikipedia python-dotenv`
     - `pip install pyaudio` (already installed in our environment)

3. Add your OpenAI API key:
   - Create a `.env` file at the project root: `c:\myprojects\FRIDAY\.env`
   - Put your key inside:
     - `OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
   - The app reads it via `dotenv` and `os.getenv("OPENAI_API_KEY")`.

4. Run the app:
   - `cd Friday`
   - `python Friday.py`
   - You should see `🎧 Listening...` and spoken greetings.

## Usage
- Say a command like:
  - "Open YouTube"
  - "Play Despacito on YouTube"
  - "Search Wikipedia for Alan Turing"
  - "Chat: What is the capital of Japan?"

The assistant will process your voice, route the task, and speak the answer.

## Notes on OpenAI Library Version
- The code uses `openai.ChatCompletion.create(...)` and is pinned to `openai==0.28.0`.
- Newer `openai>=1.0.0` removed this interface; if you upgrade, you must migrate the code (see OpenAI’s migration guide).

## Security and Secrets
- API keys are never committed. `.env` is excluded via `.gitignore`.
- Do NOT hardcode API keys in source files. Use environment variables.

## Troubleshooting
- `ModuleNotFoundError: No module named 'distutils'` — install `setuptools` and `wheel`, and upgrade `pip`.
- `PyAudio` install errors — use prebuilt wheels or `pipwin`, or ensure you have compatible Python.
- Authentication error — ensure your `OPENAI_API_KEY` is valid and you have active billing.

## Project Structure
```
FRIDAY/
├── .env                 # NOT committed (secret)
├── .venv/               # Virtual environment (ignored)
├── Friday/
│   └── Friday.py        # Main application
├── README.md            # This file
├── .gitignore           # Excludes .env, .venv, etc.
└── chromedriver.exe/    # Optional utilities
```

## License
See `Friday/LICENSE`.

## Credits
Built by Vivek. Inspired by virtual assistants like JARVIS and Alexa.