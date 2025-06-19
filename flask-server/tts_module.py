import pyttsx3

def speak_to_file(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    filepath = "static/output.wav"
    engine.save_to_file(text, filepath)
    engine.runAndWait()
    return "output.wav"
