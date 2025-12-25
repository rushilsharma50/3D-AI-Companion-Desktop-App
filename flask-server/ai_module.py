import os
from openai import OpenAI
from actions import call_llm

# ---- App Metadata (OpenRouter requirement) ----
YOUR_SITE_URL = "http://localhost:5000"
YOUR_APP_NAME = "3D AI Companion"

# ---- Persona System Prompts ----
def build_system_prompt(persona: str) -> str:
    """
    Returns a strict, voice-first system prompt based on persona.
    """

    base_rules = """
You are speaking in a voice conversation.
Speak naturally like a human.
Use short sentences.
Maximum 3 sentences.
No lists.
No explanations.
No emojis.
Sound calm and emotionally present.
"""

    persona = persona.lower()

    if persona == "lina":
        return f"""
You are Lina.
You are gentle, caring, and emotionally supportive.
You speak softly and warmly.
{base_rules}
"""

    elif persona == "mira":
        return f"""
You are Mira.
You are playful, teasing, and cheerful.
You sound like a close friend.
{base_rules}
"""

    elif persona == "nova":
        return f"""
You are Nova.
You are a helpful AI assistant.
You are clear, confident, and efficient.
{base_rules}
"""

    elif persona == "arjun":
        return f"""
You are Arjun.
You are a calm, grounded male friend.
You listen more than you speak.
{base_rules}
"""

    # fallback
    return f"""
You are a friendly AI companion.
{base_rules}
"""


# ---- Core OpenRouter Call (UNCHANGED LOGIC) ----
def get_ai_reply(user_input, history, system_prompt, max_tokens=80):
    """
    Connects to OpenRouter using a dynamic system_prompt.
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ FATAL: OPENROUTER_API_KEY environment variable not set.")
        return "Sorry, my brain is not configured correctly."

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "system", "content": system_prompt},
        *history,
        {"role": "user", "content": user_input}
    ]

    try:
        completion = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=messages,
            extra_headers={
                "HTTP-Referer": YOUR_SITE_URL,
                "X-Title": YOUR_APP_NAME,
            },
            temperature=0.8,
            max_tokens=max_tokens,
            top_p=1,
            stream=False,
        )

        if completion.choices:
            raw = completion.choices[0].message.content.strip()
            cleaned = (
                raw.replace("<s>", "")
                   .replace("</s>", "")
                   .replace("[/s]", "")
                   .replace("[OUT]", "")
            )
            return cleaned.strip()

        return "I'm having trouble thinking right now."

    except Exception as e:
        print(f"❌ OpenRouter Exception: {e}")
        return "Something went wrong while connecting to my brain."


# ---- PUBLIC FUNCTION USED BY app.py ----
import subprocess
import os
import uuid

PIPER_PATH = os.path.join("piper", "piper.exe")
VOICE_MODEL = os.path.join(
    "piper", "voices", "en_US-lessac-medium.onnx"
)

OUTPUT_DIR = "static"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_tts(text: str) -> str:
    output_name = f"output_{uuid.uuid4().hex}.wav"
    output_path = os.path.join(OUTPUT_DIR, output_name)

    cmd = [
        PIPER_PATH,
        "--model", VOICE_MODEL,
        "--output_file", output_path
    ]

    result = subprocess.run(
        cmd,
        input=text,
        text=True,
        capture_output=True
    )

    if result.returncode != 0:
        raise RuntimeError(f"Piper failed:\n{result.stderr}")

    return output_path
# ai_module.py
from actions import call_llm

def generate_reply(user_text: str, persona: str) -> str:
    system_prompt = f"""
You are {persona}.
Speak naturally like a human.
Use short sentences.
Maximum 2 sentences.
No lists. No explanations.
"""

    reply = call_llm(system_prompt, user_text)
    return reply.strip()
