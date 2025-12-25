import whisper

print("⏳ Loading Whisper model...")
model = whisper.load_model("medium")
print("✅ Whisper model loaded")

def transcribe_audio(audio_path: str) -> str:
    result = model.transcribe(
        audio_path,
        language="en",
        task="transcribe",
        fp16=False
    )
    return result["text"].strip()
