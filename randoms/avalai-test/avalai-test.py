from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api = os.getenv("avalai")

client = OpenAI(
    api_key=api,
    base_url="https://api.avalai.ir/v1",
)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn.",
        }
    ],
)

print(completion.choices[0].message.content)
