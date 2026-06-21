from openai import OpenAI
import os
from dotenv import load_dotenv
from src.learning.memory import get_recent_feedback

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_section(text, instruction):

    feedback = get_recent_feedback()

    feedback_text = ""
    for f in feedback:
        feedback_text += f"\nMistake:\n{f['draft']}\nFix:\n{f['edited']}\n"

    prompt = f"""
    You are a clinical AI.

    Avoid mistakes:
    {feedback_text}

    Extract {instruction}.
    DO NOT GUESS.
    If missing return NOT_FOUND.

    Context:
    {text}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

    except:
        return "FAILED"
