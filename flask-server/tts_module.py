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
