# 🧠 AURA - Desktop AI Companion

![Unity](https://img.shields.io/badge/Unity-2022.3%2B-black?style=for-the-badge&logo=unity)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)
![Status](https://img.shields.io/badge/Status-Prototype-orange?style=for-the-badge)

> **AURA** is a desktop companion application designed to bridge the gap between static chatbots and emotionally intelligent digital presence. It combines a **Unity-based 3D interface** with a decoupled **Flask AI backend** to create a lightweight, voice-interactive character that lives on your desktop.

---

## ✨ Key Features

- **🎙️ Real-time Voice Interaction:** Speak naturally using microphone input; the system handles STT (Whisper) and TTS (Piper) locally or via API.
- **Iy 3D Desktop Overlay:** A non-intrusive 3D character (Unity URP) that sits on your screen, capable of idle animations and lip-syncing.
- **🧠 Decoupled Architecture:** Heavy AI processing (LLM, Audio generation) is offloaded to a Python Flask server, keeping the Unity client buttery smooth.
- **🎭 Multi-Persona Support:** Switch between different personality prompts (Friend, Assistant, Stoic) dynamically.
- **🔒 Privacy-Focused Design:** Prioritizes local execution for TTS and STT to minimize data leakage and latency.

---

## 🏗️ Architecture

The system follows a **Client-Server** model to ensure performance:

```mermaid
graph LR
    A[User Voice] -->|Mic Input| B(Unity Client)
    B -->|WAV + Persona Data| C{Flask Backend}
    C -->|Whisper| D[STT]
    D -->|Text| E[LLM / OpenRouter]
    E -->|Reply Text| F[Piper TTS]
    F -->|Audio URL| B
    B -->|Playback & Animation| G[User Output]

Tech Stack
Component,Technology,Purpose
Frontend,Unity 2022 (C#),"UI, Animation, Audio Capture, Network Requests"
Backend,Python 3.10 + Flask,"API Server, Logic Handling"
STT,OpenAI Whisper,Converting user speech to text
TTS,Piper (Local),"Generating low-latency, natural voice audio"
Intelligence,OpenRouter / Local LLM,Brains behind the conversation

#📂 Project Structure
root/
├── flask-server/            # The Brain
│   ├── app.py               # Main API entry point
│   ├── whisper_module.py    # Speech-to-Text logic
│   ├── tts_module.py        # Piper TTS integration
│   ├── ai_module.py         # Context & Persona management
│   ├── piper/               # Local TTS binaries
│   └── static/              # Generated audio cache
│
└── unity-client/            # The Body
    ├── Assets/
    │   ├── Scripts/         # NetworkManager, VoiceRecorder, LipSync
    │   ├── Models/          # 3D Character (VRM/FBX)
    │   └── Scenes/          # Main Desktop Overlay Scene
#🚀 Getting Started
Prerequisites
   Python 3.10+
   Unity 2022.3 (LTS) or higher
   A microphone
1. Setup Backend (Flask)
cd flask-server
pip install -r requirements.txt
# Download Piper voice model and place in /piper folder
python app.py

