
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY  # Replace with your preferred method of loading the API key

def chat_with_gpt3(prompt, model="text-davinci-002"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message
