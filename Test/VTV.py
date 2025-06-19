import speech_recognition
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = speech_recognition.Recognizer()
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 150)  # You can slow/speed the speech

print("Say something... (say 'stop' to quit)")

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio)
            text = text.lower()
            print(f"Recognized: {text}")

            if "stop" in text:
                response = "Okay, stopping the program."
                print(response)
                tts_engine.say(response)
                tts_engine.runAndWait()
                break

            # Basic response logic — can replace with AI/NLP later
            if "how are you" in text:
                response = "I'm just a virtual voice, but I'm doing great! How about you?"
            elif "hello" in text:
                response = "Hello there! I’m listening."
            elif "what is your name" in text:
                response = "I’m your AI voice companion. You can name me if you'd like!"
            else:
                response = f"You said: {text}"

            # Speak the response
            tts_engine.say(response)
            tts_engine.runAndWait()

    except speech_recognition.UnknownValueError:
        print("Sorry, I didn’t catch that.")
        continue
