# Geminin-chatbot-2.0-update

A Python-based chatbot powered by Gemini API, featuring a Tkinter GUI and .env file integration for secure API management. This project provides a conversational AI experience with a clean and interactive interface.

<br>

Features
	•	Tkinter GUI: User-friendly graphical interface for chatting.
	•	Secure .env Configuration: Safely store API keys and sensitive data.
	•	Interactive Conversations: Generates responses in real-time.
	•	Exit Functionality: Easily close the chatbot using the GUI.
 
<br>

## Installation
1.	Clone the repository
         ``` https://github.com/KGP-Pramodith/Geminin-chatbot-2.0-update.git ```

2.	Create and activate a virtual environment
        ```
        python -m venv env
        # Windows
        env\Scripts\activate
        # macOS/Linux
        source env/bin/activate ```

3.	Install dependencies
         ` pip install -r requirements.txt`
    	
5.	Set up your .env file
     Create a .env file in the root directory and add your Gemini API key:
    	  `GEMINI_API_KEY=your_api_key_here`

## Usage

Run the chatbot GUI:
    `python main.py`

	•	Enter your message in the input box.
	•	The chatbot responds in real-time using Gemini API.
	•	Click the Exit button to close the application.

 ## Technologies Used
	•	Python 3.10
	•	Tkinter – For GUI development
	•	Gemini API – Conversational AI engine
	•	dotenv – Environment variable management

