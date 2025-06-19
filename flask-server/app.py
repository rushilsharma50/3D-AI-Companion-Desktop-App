from flask import Flask, request, jsonify, send_from_directory
from ai_module import get_ai_reply
from tts_module import speak_to_file

app = Flask(__name__)

@app.route("/talk", methods=["POST"])
def talk():
    user_input = request.json.get("message", "")
    reply = get_ai_reply(user_input)
    audio_path = speak_to_file(reply)
    return jsonify({"reply": reply, "audio": audio_path})

@app.route("/static/<path:filename>")
def serve_static(filename):
    return send_from_directory("static", filename)

if __name__ == "__main__":
    app.run(port=5000)
