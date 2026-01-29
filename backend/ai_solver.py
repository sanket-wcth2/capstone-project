import os
import requests
from dotenv import load_dotenv
from topic_detector import detect_topic
from prompts import get_prompt
from syllabus import is_supported

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL = "mistralai/mistral-7b-instruct"


def solve_math(question: str) -> str:
    if not OPENROUTER_API_KEY:
        return "Error: OpenRouter API key not found."

    if not is_supported(question):
        return "This question is outside the supported syllabus."

    topic = detect_topic(question)
    prompt = get_prompt(topic, question)

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "AI Math Solver"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2
    }

    response = requests.post(
        OPENROUTER_URL,
        headers=headers,
        json=payload,
        timeout=60
    )

    if response.status_code != 200:
        return f"OpenRouter error ({response.status_code}): {response.text}"

    data = response.json()
    return data["choices"][0]["message"]["content"]
