import os
from openai import OpenAI

YOUR_SITE_URL = "http://localhost:5000"
YOUR_APP_NAME = "3D AI Companion"

def get_ai_reply(user_input, history, system_prompt, max_tokens=80):
    """
    Connects to OpenRouter, using a dynamic system_prompt and max_tokens.
    """
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        print("❌ FATAL: OPENROUTER_API_KEY environment variable not set.")
        return "Sorry, my connection to my brain is not configured correctly. The API key is missing."
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "system", "content": system_prompt},
        *history,
        {"role": "user", "content": user_input}
    ]

    try:
        completion = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=messages,
            extra_headers={
              "HTTP-Referer": YOUR_SITE_URL,
              "X-Title": YOUR_APP_NAME,
            },
            temperature=0.8,
            max_tokens=max_tokens,
            top_p=1,
            stream=False,
        )

        if hasattr(completion, 'choices') and completion.choices:
            raw_response = completion.choices[0].message.content.strip()
            cleaned_response = raw_response.replace('<s>', '').replace('</s>', '').replace('[/s]', '').replace('[OUT]', '')
            return cleaned_response.strip()
        else:
            print("❌ API Error: No valid response received from OpenRouter.")
            return "Sorry, I'm having trouble thinking right now."

    except Exception as e:
        print(f"❌ Exception while calling OpenRouter API: {e}")
        return "Something went wrong while trying to connect to the AI model."