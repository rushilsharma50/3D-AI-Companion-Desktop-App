import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()
tts = pyttsx3.init()
tts.setProperty('rate', 150)  # Optional: set speech rate

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Listening...")
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Recognized: {text}")

            # TTS speaks the recognized text
            tts.say(f"You said: {text}")
            tts.runAndWait()

            if "stop" in text:
                print("Stopping program.")
                break

    except speech_recognition.UnknownValueError:
        print("Sorry, I didn’t catch that.")
        continue
