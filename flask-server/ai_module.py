import requests

def get_ai_reply(user_input):
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://openrouter.ai"
    }

    data = {
        "model": "deepseek/deepseek-r1-0528-qwen3-8b:free",  # ✅ make sure this is valid!
        "messages": [
            {"role": "system", "content": "You are a kind and calm therapist who helps users explore their emotions."},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    try:
        result = response.json()
        if "choices" in result:
            return result['choices'][0]['message']['content']
        else:
            print("❌ API Error: ", result)
            return "Sorry, I'm having trouble thinking right now."
    except Exception as e:
        print("❌ Exception while parsing AI response:", e)
        return "Something went wrong with the AI model."
