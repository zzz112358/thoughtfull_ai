import os
import logging

from openai import OpenAI

logging.basicConfig(level=logging.ERROR)

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def call_openai(user_question, model="gpt-3.5-turbo"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an AI assistant for Thoughtful AI."},
                {"role": "user", "content": user_question}
            ],
        )
        return response.choices[0].message.content.strip()
    # todo: different handler for specific error
    except Exception as e:
        logging.error("Failed to generate response from OpenAI", exc_info=e)
        return "sorry, the agent is not able to respond now, please retry later"  # or return a default fallback string
