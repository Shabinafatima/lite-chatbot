# Lite Chatbot

A simple Python-based AI chatbot built with OpenAI API and LangChain.  
Designed for easy local setup, safe handling of API keys with `.env`, and a clean virtual environment.

## Quick Setup & Run (Copy-Paste)

```powershell
# 1️⃣ Clone the repository
git clone https://github.com/Shabinafatima/lite-chatbot.git
cd lite-chatbot

# 2️⃣ Create a Python virtual environment (isolated environment for dependencies)
python -m venv venv

# 3️⃣ Activate the virtual environment
# PowerShell:
.\venv\Scripts\Activate.ps1
# CMD (if using Command Prompt):
# .\venv\Scripts\activate.bat
# Linux/macOS:
# source venv/bin/activate

# 4️⃣ Install required Python packages
pip install -r requirements.txt

# 5️⃣ Prepare environment variables
# Copy the example file to a real .env file
copy .env.example .env

# 6️⃣ Open the .env file and add your OpenAI API key
# Example:
# OPENAI_API_KEY=your_actual_api_key_here

# 7️⃣ Run the chatbot
python main.py

## License
This project is licensed under the Apache License 2.0.
