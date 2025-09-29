# 🤖 Project: Arora - Your AI Desktop Companion

[![LinkedIn](https://img.shields.io/badge/LinkedIn-RushilSharma-blue?style=for-the-badge&logo=linkedin)]([https://www.linkedin.com/in/your-linkedin-url/](https://www.linkedin.com/in/rushilkumar-sharma-0679b9305/))
[![GitHub](https://img.shields.io/badge/GitHub-rushilsharma50-lightgrey?style=for-the-badge&logo=github)](https://github.com/rushilsharma50)
![Python](https://img.shields.io/badge/Python-3.10-blue.svg?style=for-the-badge&logo=python)
![Unity](https://img.shields.io/badge/Unity-2022.3-black.svg?style=for-the-badge&logo=unity)
![Flask](https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask)


> An emotionally intelligent 3D AI companion that lives on your desktop, offering natural voice-based conversation and perspective, powered by a local Python backend.

![Arora AI Desktop Companion in Action](https://github.com/your-username/your-repo-name/blob/main/docs/demo.gif)
---

## 🎯 About The Project

Traditional AI assistants are confined to a window or a smart speaker, feeling more like a utility than a companion. They often lack personality and require an internet connection, raising privacy concerns.

**Project: Arora** is my attempt to solve this. It's a lightweight, non-intrusive 3D character that exists as a desktop overlay, providing companionship and assistance without getting in the way. The entire AI pipeline, from voice recognition to response generation, runs locally, ensuring privacy and offline functionality.

This project was built to explore the technical challenges of integrating a real-time 3D application (Unity) with a powerful and flexible AI backend (Python/Flask), with a focus on creating a believable, emotionally aware character.

---

## ✨ Key Features

* **Real-time, Offline Voice Conversation:** Utilizes local, high-performance Speech-to-Text (Whisper) and expressive Text-to-Speech (Edge-TTS) for natural, private conversations.
* **Expressive 3D Animated Character:** Features a fully animated 3D character (Scifi Girl v.01) that uses context-aware animations to convey emotion and react to the conversation.
* **Seamless Desktop Overlay:** Renders as a transparent, click-through window that sits on your desktop, making the character feel truly integrated with your workspace.
* **Powerful Python & Flask Backend:** All heavy AI processing is offloaded to a local Flask server, keeping the Unity frontend lightweight and responsive.
* **Modular and Extensible:** The architecture is designed to be easily extendable, with plans for adding new skills, memories, and integrations.

---

## 🛠️ Tech Stack & Tools

This project brings together a variety of technologies to create a cohesive experience:

* **Frontend:** Unity, C#
* **Backend:** Python, Flask
* **AI / Machine Learning:**
    * **Speech-to-Text (STT):** Local Whisper model implementation.
    * **Text-to-Speech (TTS):** Microsoft's Edge-TTS for natural and expressive voices.
    * **Natural Language Processing (NLP):** [Specify library, e.g., SpaCy for intent recognition or NLTK for text processing]
* **3
