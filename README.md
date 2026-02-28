# AURA — Desktop AI Companion (Unity + Python)

AURA (**Adaptive User Response Assistant**) is a lightweight desktop AI companion built with **Unity** and **Python**. It is designed to live on your desktop as a calm, expressive presence, combining voice interaction, AI-driven conversation, and a 3D animated character.

This project focuses on **presence over performance**: subtle animations, short natural replies, and human-like voice interaction.

![AURA Desktop Overlay](https://github.com/user-attachments/assets/screenshot_1338)
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

![Emotion Controller and Logic](https://github.com/user-attachments/assets/screenshot_1330)
> *The Unity Inspector showing the Emotion Controller setup and real-time backend communication logs.*

**Key logic flow:**
1.  **Unity** records microphone input and sends audio to **Flask**.
2.  **Flask** transcribes via **Whisper**, generates a reply via **LLM**, and converts to voice via **Piper**.
3.  **Unity** receives the audio URL and text, plays the response, and triggers corresponding **Blendshape** animations.

---

## 🚀 Project Status

* ✅ Voice input → AI → Voice output loop
* ✅ Offline Natural Voice (Piper)
* ✅ Emotion-aware facial expressions
* ✅ Unity audio playback & JSON parsing
* 🚧 Taskbar and window-edge sitting
* 🚧 Idle animation switching (standing/sitting)

![Character Preview](https://github.com/user-attachments/assets/screenshot_1333)

---

## ⚖️ Model Credits & License

The 3D character used in this project is **Chisa (鸣潮_千咲)** created by **1010浣 / Guangzhou Kuluo Technology Co., Ltd**.

* **Usage**: This project is intended for **FAN ART** and experimental purposes only.
* **Restrictions**: 
    * No commercial use or money-related transactions.
    * No redistribution of the model data.
    * No usage involving R-18 content, politics, or religion.
* **Copyright**: The final copyright belongs to **Guangzhou Kuluo Technology Co., Ltd**.

---

## 📌 Author

**Rushil Sharma** *B.Tech CSE Student @ Parul University* Unity Developer | AI Tools | Interactive Systems

---

## ⭐ Why This Project Exists

This project is an exploration of AI-driven real-time 3D interaction, aiming to build desktop companions that feel like a genuine presence rather than just a robotic utility.
