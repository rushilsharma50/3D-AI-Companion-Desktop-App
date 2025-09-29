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
* **3D Assets & Animation:** Blender (for animation rigging/cleanup), Sketchfab (for the base model).
* **Platform:** Windows Desktop

---

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Unity Hub with Unity Editor version `2022.3.x` or later.
* Python `3.10` or later.
* Git for cloning the repository.

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```
2.  **Setup the Python Backend:**
    ```bash
    cd backend
    pip install -r requirements.txt
    ```
3.  **Setup the Unity Frontend:**
    * Open Unity Hub and click "Add project from disk".
    * Select the `UnityProject` folder from the cloned repository.
    * Let Unity import the project.

4.  **Run the Application:**
    * First, start the Flask server from your terminal:
        ```bash
        cd backend
        python app.py
        ```
    * Once the server is running, go to the Unity Editor and press the **Play** button.

---

## 🧠 Challenges & Learnings

This project was a significant learning experience in system design and applied AI.

* **Challenge 1: Real-Time Frontend-Backend Communication:**
    * **Problem:** Establishing a low-latency, two-way communication channel between a C# Unity application and a Python backend.
    * **Solution:** I implemented a WebSocket connection. This allowed the backend to stream TTS audio data and animation commands to Unity in real-time, while Unity could send transcribed user speech to the backend with minimal delay.

* **Challenge 2: Performance Optimization:**
    * **Problem:** Running a local STT model like Whisper can be resource-intensive. It was crucial to prevent it from causing frame drops or freezing the Unity application.
    * **Solution:** I ran the AI model processing in a separate thread on the Python backend. For the model itself, I experimented with different quantized versions to find the best balance between transcription accuracy and performance on my hardware (RTX 4060).

* **Challenge 3: Mapping AI to Animation:**
    * **Problem:** Making the character's animations feel natural and not repetitive or random.
    * **Solution:** I developed a simple intent-detection system in the backend. Based on keywords and sentiment from the conversation, the backend sends a corresponding animation state (e.g., `thinking`, `listening`, `happy`, `confused`) to Unity, which then triggers the appropriate animation from the character's Animator Controller.

---

## 📈 Future Roadmap

* [ ] **Long-Term Memory:** Implement a vector database (e.g., ChromaDB) to give Arora memory of past conversations.
* [ ] **Dynamic Personality:** Develop a mood system that changes based on interactions over time.
* [ ] **API Integrations:** Connect Arora to external APIs to fetch real-time data like weather, news, or calendar events.
