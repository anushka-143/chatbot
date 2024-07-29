import openai

class Chatbot:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, prompt, context):
        complete_prompt = f"{context}\n\nQuestion: {prompt}"
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": complete_prompt}
            ]
        )
        return response.choices[0].message['content'].strip()
