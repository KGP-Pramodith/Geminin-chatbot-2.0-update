from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_gemini_response(question: str) -> str:
    """Send a message to Gemini and return the response text."""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        ),
    )
    return response.text.strip()

# Optional: keep terminal chat mode if you run app.py directly
if __name__ == "__main__":
    while True:
        question = input("USER : ")
        if question.lower() == "bye":
            print("Bye...!")
            break
        else:
            print(get_gemini_response(question))