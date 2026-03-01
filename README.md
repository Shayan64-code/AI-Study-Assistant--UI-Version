# AI-Study-Assistant--UI Version
This is the AI-Study-Assistant with User Interface created using Streamlit.

Here’s a clean, human-style README for your project — simple, natural, and not overly corporate 😄

---

 AI Study Assistant (Streamlit + OpenRouter)

A simple AI-powered Study Assistant built with **Streamlit** and **OpenRouter API**.
It helps students revise important concepts, understand topics clearly, and solve coding problems in an easy way.

This project is beginner-friendly and perfect if you're learning how chatbots work.


## What This App Does

* Lets users ask study-related questions
* Gives clear and helpful answers
* Remembers conversation using session state
* Shows a clean chat interface
* Displays a “Thinking…” spinner while generating answers

Basically, it works like a mini ChatGPT but focused on studying.

---

## Tech Used

* **Python**
* **Streamlit** (for the web app UI)
* **OpenRouter API** (for AI model access)
* Session State (to store chat history)

---

## Project Structure

project/
│
├── app.py        # Main Streamlit app
├── Keys.py       # Stores your API key
└── README.md     # Project documentation

---

## Setup Instructions

### Clone the repository

git clone <your-repo-link>
cd <your-project-folder>

---

### Create a virtual environment (recommended)

python -m venv venv

Activate it:

**Windows**

venv\Scripts\activate


**Mac/Linux**

source venv/bin/activate

---

### Install dependencies

pip install streamlit openai

---

### add your API key

Create a file named:

Keys.py

Inside it, add:

KEY1 = "your_openrouter_api_key_here"

"Make sure you don’t upload your API key to GitHub."

---

### Run the app

streamlit run app.py

Your browser will open automatically.

---

## How It Works (Simple Explanation)

* When the app runs, it checks if chat history exists.
* If not, it creates a new message list with a system prompt.
* When the user types something:

  * It saves the message
  * Calls the AI model
  * Shows a spinner while waiting
  * Displays the AI response
  * Saves the reply in session state

Streamlit reruns the script every time you interact with it, but `st.session_state` keeps the memory safe.

---

## Why This Project Is Good for Learning

This project helps you understand:

* How chatbots work
* How to manage conversation memory
* How APIs connect to frontend apps
* How Streamlit reruns scripts
* How session state works

---

## Notes

* Don’t expose your API key.
* Free models may sometimes be slow.
* If something breaks, check the terminal for errors.

---

## Future Improvements (Optional Ideas)

* Add streaming (real-time typing effect)
* Add a "Clear Chat" button
* Limit conversation length
* Deploy on Streamlit Cloud
* Move backend to FastAPI later

---

## Author

Built as a learning project while exploring AI + Web development.

