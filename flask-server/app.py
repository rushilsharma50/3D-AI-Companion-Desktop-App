from flask import Flask, request, jsonify
from whisper_module import transcribe_audio
from ai_module import generate_reply
from tts_module import generate_tts
import os

app = Flask(__name__)

@app.route("/voice-input", methods=["POST"])
def voice_input():
    persona = request.form.get("persona", "Lina")
    audio_file = request.files["audio"]

    os.makedirs("uploads", exist_ok=True)
    input_path = "uploads/input.wav"
    audio_file.save(input_path)

    print("🎤 Audio received")

    user_text = transcribe_audio(input_path)
    print("📝 User said:", user_text)

    reply_text = generate_reply(user_text, persona)
    print("🤖 AI reply:", reply_text)

    audio_path = generate_tts(reply_text)
    print("🔊 Audio generated:", audio_path)

    return jsonify({
        "user_text": user_text,
        "reply_text": reply_text,
        "audio_url": f"/{audio_path.replace(os.sep, '/')}"
    })

if __name__ == "__main__":
    print("🚀 Starting Flask server...")
    app.run(host="0.0.0.0", port=5000, debug=True)
