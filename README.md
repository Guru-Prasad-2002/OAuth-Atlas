# OAuth Guide

A starting point for the Composio take-home assignment: a Flask application that will help developers research OAuth app setup and approval.

## Setup (Windows Command Prompt)

Open Command Prompt in the project folder, then create and activate a virtual environment:

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
```

Install the dependencies and start the app:

```cmd
python -m pip install -r requirements.txt
python -m flask --app app run --debug
```

Before starting the app, add your Gemini API key to `.env` as described below.

## Alternative: Windows PowerShell

From the project folder, create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned` and then repeat the activation command. This change applies only to the current PowerShell session.

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

The packages are Flask (web app), python-dotenv (load local environment variables), and google-genai (Gemini API client).

Add your key to `.env`:

```text
GEMINI_API_KEY=your_key_here
```

The `.env` file is ignored by Git. Never commit your API key. For a fresh checkout, copy `.env.example` to `.env` and add the key.

Run the starter app:

```powershell
python -m flask --app app run --debug
```

Open http://127.0.0.1:5000/. Stop the server with Ctrl+C and leave the virtual environment with `deactivate`.

## Deploy on Render

Push the project to GitHub, keeping `.env` out of the repository. Create a Render Web Service from the repository and select the Free instance. Set the build command to `pip install -r requirements.txt` and the start command to `gunicorn --timeout 240 app:app`. In Render's Environment settings, add `GEMINI_API_KEY` and `TAVILY_API_KEY` with your own values; optionally add `GEMINI_MODEL`. Deploy and test the public URL. The longer worker timeout accommodates slow research calls and retries. Free services can take about a minute to wake after inactivity. Generated guides are not saved on the server.

## Current status

Add `TAVILY_API_KEY=your_key_here` to `.env` for web search. Enter an app name or website to generate a guide using Tavily search and Gemini. The default model is `gemini-3.5-flash-lite`; set `GEMINI_MODEL` in `.env` to use another available model. The normal flow uses one search and one model request; temporary model server and network failures may trigger up to two retries, each of which can consume quota. Rate-limit errors are not automatically retried. Search results may include third-party sources and are not independent verification of every claim. Guides are not saved and disappear on refresh. Review the result and sources before relying on it. This workflow researches public material; it does not register an OAuth app or test a provider's setup flow.
