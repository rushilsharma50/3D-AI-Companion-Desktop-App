# AURA — Desktop AI Companion (Unity + Python)

AURA is a lightweight **desktop AI companion** built with **Unity** and **Python**, designed to live on your desktop as a calm, expressive presence.  
It combines voice interaction, AI-driven conversation, and a 3D animated character — without feeling intrusive or robotic.

This project focuses on **presence over performance**: subtle animations, short natural replies, and human-like voice.

---

## ✨ Features

- 🎙️ **Voice-to-Voice Conversation**
  - Microphone input from Unity
  - Speech-to-Text using Whisper
  - AI-generated replies
  - Natural-sounding Text-to-Speech using Piper (offline)

- 🤖 **Persona-Based AI**
  - Multiple personas (Friend, Assistant, Companion)
  - Short, voice-optimized responses
  - Designed for conversational flow, not long explanations

- 🧍 **3D Desktop Companion**
  - Unity-based 3D character
  - Idle animations (standing, relaxed, sitting planned)
  - Lip sync using blendshapes (vowel-based)
  - Designed to sit on the desktop / taskbar (planned)

- ⚡ **Decoupled Architecture**
  - Unity handles UI, animation, audio playback
  - Python (Flask) handles AI, STT, and TTS
  - Keeps the Unity client responsive and lightweight

---

## 🛠️ Tech Stack

### Frontend (Client)
- **Unity 2022 LTS**
- C#
- Skinned Mesh Renderer (blendshape-based lip sync)
- Desktop transparent window (overlay-style)

### Backend (Server)
- **Python 3.10+**
- Flask (API server)
- Whisper (Speech-to-Text)
- Piper TTS (offline, natural voice)
- OpenRouter / LLM API (for AI replies)

---

## 🧠 Architecture Overview

# AURA — Desktop AI Companion (Unity + Python)

AURA is a lightweight **desktop AI companion** built with **Unity** and **Python**, designed to live on your desktop as a calm, expressive presence.  
It combines voice interaction, AI-driven conversation, and a 3D animated character — without feeling intrusive or robotic.

This project focuses on **presence over performance**: subtle animations, short natural replies, and human-like voice.

---

## ✨ Features

- 🎙️ **Voice-to-Voice Conversation**
  - Microphone input from Unity
  - Speech-to-Text using Whisper
  - AI-generated replies
  - Natural-sounding Text-to-Speech using Piper (offline)

- 🤖 **Persona-Based AI**
  - Multiple personas (Friend, Assistant, Companion)
  - Short, voice-optimized responses
  - Designed for conversational flow, not long explanations

- 🧍 **3D Desktop Companion**
  - Unity-based 3D character
  - Idle animations (standing, relaxed, sitting planned)
  - Lip sync using blendshapes (vowel-based)
  - Designed to sit on the desktop / taskbar (planned)

- ⚡ **Decoupled Architecture**
  - Unity handles UI, animation, audio playback
  - Python (Flask) handles AI, STT, and TTS
  - Keeps the Unity client responsive and lightweight

---

## 🛠️ Tech Stack

### Frontend (Client)
- **Unity 2022 LTS**
- C#
- Skinned Mesh Renderer (blendshape-based lip sync)
- Desktop transparent window (overlay-style)

### Backend (Server)
- **Python 3.10+**
- Flask (API server)
- Whisper (Speech-to-Text)
- Piper TTS (offline, natural voice)
- OpenRouter / LLM API (for AI replies)

---

## 🧠 Architecture Overview
[ Unity Client ]
├─ Records microphone input
├─ Sends audio + persona to Flask
├─ Plays returned voice
├─ Animates character (idle + lip sync)

[ Flask Server ]
├─ Whisper → transcribe audio
├─ LLM → generate short reply
├─ Piper → generate voice
└─ Returns text + audio URL


**Key idea:**  
AI logic is fully decoupled from the Unity runtime, preventing frame drops or UI freezing.

---

## 📂 Project Structure

flask-server/
│
├─ app.py # Flask API entry point
├─ whisper_module.py # Speech-to-text
├─ ai_module.py # Persona logic + reply filtering
├─ actions.py # LLM API calls
├─ tts_module.py # Piper TTS integration
├─ uploads/ # Incoming audio
├─ static/ # Generated voice output
└─ piper/ # Piper binary + voices


Unity project:
Assets/
├─ Scripts/
│ ├─ Voice/
│ ├─ Animation/
│ └─ Managers/
├─ Models/
├─ Materials/
└─ Scenes/


---

## 🚀 Current Status

✅ Voice input → AI → voice output working  
✅ Female natural voice (Piper)  
✅ Short, voice-optimized AI replies  
✅ Unity audio playback  
🚧 Idle animations (in progress)  
🚧 Lip sync refinement  
🚧 Desktop sitting / taskbar integration  

---

## 🎯 Design Philosophy

- Less UI, more presence
- Short replies > long explanations
- Calm motion over flashy animation
- Feels like someone *there*, not an app demanding attention

---

## 🧪 Future Plans

- Idle animation switching (standing / sitting)
- Taskbar & window-edge sitting
- Emotion-aware facial expressions
- Lightweight memory per persona
- Optional offline LLM support

---

## ⚠️ Disclaimer

This project is experimental and built for learning, exploration, and personal use.  
It is **not** intended to replace professional mental health support.

---

## 📌 Author

**Rushil Sharma**  
Unity Developer | AI Tools | Interactive Systems  

---

## ⭐ Why This Project Exists

This project started as an exploration of:
- AI + real-time 3D interaction
- Desktop companions that feel human, not gimmicky
- Building meaningful tools through hands-on engineering

---

If you find this interesting, feel free to explore, fork, or build on top of it.
