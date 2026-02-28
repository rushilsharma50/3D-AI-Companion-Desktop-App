# AURA — Desktop AI Companion (Unity + Python)

AURA (**Adaptive User Response Assistant**) is a lightweight desktop AI companion built with **Unity** and **Python**. It is designed to live on your desktop as a calm, expressive presence, combining voice interaction, AI-driven conversation, and a 3D animated character.

This project focuses on **presence over performance**: subtle animations, short natural replies, and human-like voice interaction.

![AURA Desktop Overlay](Images/Screenshot (1338).png)
> *AURA running as a non-intrusive desktop overlay alongside system tasks on an RTX 4060 system.*

---

## ✨ Features

* 🎙️ **Voice-to-Voice Conversation**: Real-time microphone input from Unity with natural-sounding TTS via Piper.
* 🤖 **Persona-Based AI**: Multiple personas (Friend, Assistant, Companion) with short, voice-optimized responses.
* 🧍 **3D Desktop Companion**: Unity-based character with automated head tracking and idle animations.
* 🎭 **Emotion Controller**: Integrated blendshapes for Neutral, Happy, Sad, Angry, and Surprised states.
* 👄 **Lip Sync**: Skinned Mesh Renderer utilizing vowel-based blendshapes for natural speech movement.
* ⚡ **Decoupled Architecture**: Python Flask backend handles heavy AI processing to keep the Unity client lightweight.

---

## 🛠️ Tech Stack

### Frontend (Client)
* **Unity 2022.3.62f1**
* **C#**
* **Desktop Transparent Window**: Overlay-style integration.

### Backend (Server)
* **Python 3.10+ (Flask)**: Serving as the API bridge.
* **Whisper**: For local Speech-to-Text transcription.
* **Piper TTS**: High-quality, offline text-to-speech.
* **OpenRouter/LLM**: For generating emotionally intelligent replies.

---

## 🧠 System Architecture

![Emotion Controller and Logic](Images/Screenshot (1330).png)
> *The Unity Inspector showing the Emotion Controller setup and real-time backend communication logs.*

---

## 🚀 Project Status

* ✅ Voice input → AI → Voice output loop
* ✅ Offline Natural Voice (Piper)
* ✅ Emotion-aware facial expressions
* ✅ Unity audio playback & JSON parsing
* 🚧 Taskbar and window-edge sitting
* 🚧 Idle animation switching (standing/sitting)

![Character Preview](Images/Screenshot (1333).png)

---

## 📜 Model License & Credits

The 3D character used in this project is **Chisa (鸣潮_千咲)** created by **1010浣 / 鸣潮**. 

According to the original `read me.txt` provided with the model:

### ⚠️ Forbidden Actions
- **Redistribution:** Redistribution of this model data is strictly prohibited.
- **Commercial Use:** Any use involving money transactions or commercial gain is forbidden.
- **Prohibited Content:** Use involving R-18 (pornography, blood, violence), politics, religion, or illegal activities is strictly prohibited.
- **Harmful Use:** Must not be used to insult or show contempt toward other people, countries, or regions.

### 🛠️ Editing & Redistribution
- **Editing:** Allowed, provided the character is not changed to a different character.
- **Part Transfer:** You may NOT transplant parts of this model onto other models.
- **Finality:** Redistribution is prohibited regardless of whether the model is edited or not.

### ⚖️ Disclaimer & Copyright
- This file is intended for **FAN ART** purposes only and differs from the original game content.
- The author/editor is not responsible for any damage caused by using this model.
- **The final copyright of this model material belongs to Guangzhou Kuluo Technology Co., Ltd.**

---

## 📌 Author

**Rushil Sharma** *Unity Developer | AI Tools | Interactive Systems*

---

## ⭐ Why This Project Exists

This project is an exploration of AI-driven real-time 3D interaction, aiming to build desktop companions that feel like a genuine presence rather than just a robotic utility.
