# ACE AI — Local Personal Assistant

ACE AI is an early local-chat interface powered by Ollama. The included
Modelfile creates a custom `ace-ai` model based on Gemma 3 4B.

## Requirements

- Windows 10/11
- Python 3.10 or newer
- Ollama for Windows
- Enough free RAM for the selected local model (performance depends on hardware)

## 1. Install Ollama

Download Ollama: https://ollama.com/download/windows

Open Command Prompt and download the base model:

```cmd
ollama pull gemma3:4b
```

## 2. Create the ACE AI model

Open Command Prompt in this project folder and run:

```cmd
ollama create ace-ai -f Modelfile
```

## 3. Install Python dependencies

```cmd
py -m pip install -r requirements.txt
```

## 4. Start the interface

Make sure Ollama is running, then run:

```cmd
py -m streamlit run ace_ai_app.py
```

Streamlit should open the local interface in your browser, usually at
http://localhost:8501.

## Notes

- Chat requests are sent to the Ollama service on this computer.
- The first model download requires an internet connection. After download,
  local text chat can work offline while Ollama is running.
- This starter version is text chat only. Image upload, PDF retrieval,
  voice, long-term memory, and desktop packaging are planned upgrades,
  not implemented features yet.
- The app expects an Ollama model named `ace-ai`. If you use another model,
  change `MODEL` near the top of `ace_ai_app.py`.

## GitHub

Create a new empty GitHub repository, extract this ZIP, then upload the
project files or use Git:

```cmd
git init
git add .
git commit -m "Initial ACE AI local chat app"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the remote URL with your own repository URL.
