import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

key = os.getenv("OPENROUTER_API_KEY")
print(f"Clave cargada: {key[:10]}...{key[-5:] if key else 'NO KEY'}")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=key
)

try:
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hola, respondé OK"}],
        max_tokens=10
    )
    print("✅ OpenRouter funciona:", response.choices[0].message.content)
except Exception as e:
    print(f"❌ Error: {e}")