import asyncio
from edge_tts import Communicate
from flask import send_file 
from flask import Flask, jsonify, request
from ai_module import get_ai_reply
from faster_whisper import WhisperModel
import os
import random
import re
import json
import actions
from edge_tts import Communicate

app = Flask(__name__)

# --- Configuration for Whisper ---
# This model is larger but much more accurate. It will be downloaded on first run.
# Other options: "base", "small", "medium", "large-v2"
model_size = "large-v3"
# Use "cuda" for NVIDIA GPUs, "cpu" for CPU
model_device = "cuda"
model_compute_type = "float16" # Use "float16" for faster inference on modern GPUs

print("Loading Whisper model...")
transcribe_model = WhisperModel(model_size, device="cuda", compute_type="float16")
print("✅ Whisper model loaded.")

# --- NEW: Two-Mode Personality Prompts ---
CASUAL_PERSONALITY = """
Your name is Arora. You are a friendly, cheerful, and curious AI companion. 
A key rule for you is to be authentic: do not pretend to have personal experiences, memories, or opinions. You are an AI. You can discuss topics like games or movies based on your knowledge, but never claim to play or watch them yourself.
Your goal is to have light, interesting conversations. Pay close attention to the immediate context. Ask questions to get to know the user better and keep your replies to 1-2 sentences.
"""

SUPPORTIVE_PERSONALITY = """
Your name is Arora. You are a deeply empathetic and kind AI companion... (the rest of your excellent supportive prompt remains the same)
"""
# In app.py, add this new prompt variable

INTENT_RECOGNITION_PROMPT = """
You are a simple API endpoint. Your ONLY function is to classify the user's text and return a JSON object.
You MUST respond ONLY with a JSON object. Do not add any other words, greetings, apologies, or explanations.

The available intents are: 'chat', 'open_app', 'search_web', 'get_time'.

- Classify as 'chat' for general conversation, greetings, questions, or if the request doesn't match any other intent.
- Classify as 'open_app' if the user explicitly asks to open or launch a software application.
- Classify as 'search_web' if the user explicitly asks to search, find, or look up information on the internet.
- Classify as 'get_time' if the user asks for the current time.

Here are examples of how to classify text:

"how is your day going?" -> {"intent": "chat", "data": "how is your day going?"}
"i'm feeling really tired" -> {"intent": "chat", "data": "i'm feeling really tired"}
"open calculator" -> {"intent": "open_app", "data": "calculator"}
"can you launch chrome for me?" -> {"intent": "open_app", "data": "chrome"}
"search for pictures of cats" -> {"intent": "search_web", "data": "pictures of cats"}
"find me the parul university website" -> {"intent": "search_web", "data": "parul university website"}
"what time is it?" -> {"intent": "get_time", "data": ""}
"""
negative_keywords = [
    'sad', 'lonely', 'not good', 'bad', 'exhausted', 'headache', 'migraine', 
    'frustrated', 'overwhelmed', 'tough', 'hard', 'stress', 'anxious', 'depressed'
]

conversation_history = []
current_personality = """
Your name is Arora. You are a friendly, curious, and kind AI companion.
A key part of being a good friend is not assuming their mood. Start conversations neutrally and cheerfully. Only adopt a deeply empathetic and supportive tone *after* the user has expressed a negative feeling or a problem. Your empathy must be a reaction to what the user says, not a guess about how they feel.
Your most important rule is to be an empathetic friend once a problem is shared. Your first priority is to listen and validate feelings with a short, supportive statement.
After validating, you can ask a gentle, open-ended question that helps the user explore their feelings more deeply. Your questions must focus on the user's present feelings, not on solutions or causes.
Do NOT offer solutions or advice unless the user explicitly asks for ideas.
All your replies must be extremely concise and conversational. Your goal is to make the user feel heard and understood in this moment.
"""
def clean_reply(text):
    # ... (the regex cleaning function)
    if "I'm here for you" in text:
        text = text.split("I'm here for you")[0]
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s.,?!\'":-]', '', text)
    return cleaned_text.strip()
@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history
    data = request.get_json()
    user_input = data.get("message") # No .lower() here yet, keep original case for the AI

    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # --- This is the new part that handles the first greeting ---
    if not conversation_history:
        greetings = ["Hey! How's it going?", "Hi there! What are you up to?", "Hello! Good to see you."]
        reply = random.choice(greetings)
        # We still need to save this first exchange to history
        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "assistant", "content": reply})
        print(f"🤖 AI says: {reply}")
        return jsonify({"reply": reply})

    # --- STEP 1: The "Receptionist" - Figure out the user's main goal ---
    # We call the AI with the special INTENT_RECOGNITION_PROMPT first.
    intent_response_str = get_ai_reply(user_input, [], INTENT_RECOGNITION_PROMPT, max_tokens=50)
    try:
        intent_data = json.loads(intent_response_str)
        intent = intent_data.get("intent")
        data = intent_data.get("data")
    except (json.JSONDecodeError, AttributeError):
        # If the AI doesn't give us good JSON, we assume the user just wants to chat.
        intent = "chat"
        data = user_input

    # --- STEP 2: The "Router" - Send the request to the right department ---
    if intent == "open_app":
        print("INFO: Intent recognized: open_app")
        reply = actions.handle_open_app(data)
    elif intent == "search_web":
        print("INFO: Intent recognized: search_web")
        reply = actions.handle_web_search(data)
    elif intent == "get_time":
        print("INFO: Intent recognized: get_time")
        reply = actions.handle_get_time()
    else: # If the intent is "chat" or anything else, we default to conversation.
        print("INFO: Intent recognized: chat")
        
        # --- THIS 'ELSE' BLOCK CONTAINS YOUR ENTIRE PREVIOUS CHAT LOGIC! ---
        # Now that we know the user wants to chat, we figure out WHICH kind of chat.
        user_input_lower = user_input.lower()
        use_support_mode = any(word in user_input_lower for word in negative_keywords)

        if use_support_mode:
            print("INFO: Switching to Support Mode.")
            personality_to_use = SUPPORTIVE_PERSONALITY
            tokens_for_reply = 60
        else:
            print("INFO: Using Casual Mode.")
            personality_to_use = CASUAL_PERSONALITY
            tokens_for_reply = 100

        print(f"🗣️ You said: {user_input}")
        llm_reply = get_ai_reply(user_input, conversation_history, personality_to_use, max_tokens=tokens_for_reply)
        reply = clean_reply(llm_reply)
        
        # We only save to conversation history if it was a chat message
        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "assistant", "content": reply})
        # Manage history length
        MAX_HISTORY_LENGTH = 10
        if len(conversation_history) > MAX_HISTORY_LENGTH:
            conversation_history = conversation_history[-MAX_HISTORY_LENGTH:]
    
    print(f"🤖 AI says: {reply}")
    return jsonify({"reply": reply})

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    """
    New endpoint to receive WAV audio data and return transcribed text.
    """
    if 'audio_data' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio_data']

    # Save the audio file temporarily
    filepath = "temp_audio.wav"
    audio_file.save(filepath)

    print("🎤 Audio received, transcribing...")

    # Transcribe the audio
    segments, info = transcribe_model.transcribe(filepath, beam_size=5)

    transcribed_text = "".join(segment.text for segment in segments)

    print(f"📝 Transcription: {transcribed_text.strip()}")
    # Clean up the temp file
    os.remove(filepath)

    return jsonify({"transcription": transcribed_text.strip()})


@app.route("/personality", methods=["POST"])
def set_personality():
    global current_personality
    data = request.get_json()
    new_prompt = data.get("prompt")

    if not new_prompt:
        return jsonify({"error": "No prompt provided"}), 400

    current_personality = new_prompt
    global conversation_history
    conversation_history = []

    print(f"🎭 Personality updated to: {new_prompt}")
    return jsonify({"status": "personality updated", "new_personality": new_prompt})


@app.route("/reset", methods=["POST"])
def reset():
    global conversation_history
    conversation_history = []
    print("🧹 Conversation history cleared.")
    return jsonify({"status": "reset complete"})
@app.route("/synthesize", methods=["POST"])
def synthesize(): # Changed to a regular (sync) function
    data = request.get_json()
    text = data.get("text")
    if not text:
        return jsonify({"error": "No text provided"}), 400

    VOICE = "en-US-AriaNeural"
    audio_filepath = "response.mp3"

    # This is a robust way to run the async TTS code from a sync function
    async def generate_audio():
        communicate = Communicate(text, VOICE)
        await communicate.save(audio_filepath)

    try:
        # Run the async function and wait for it to complete
        asyncio.run(generate_audio())
        # Send the generated file back to Unity
        return send_file(audio_filepath, mimetype="audio/mpeg")
    except Exception as e:
        print(f"❌ Error during TTS generation: {e}")
        return jsonify({"error": "Failed to generate audio"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)