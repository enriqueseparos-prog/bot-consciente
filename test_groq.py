import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

key = os.getenv("GROQ_API_KEY")
print(f"🔑 Groq key: {key[:10]}...{key[-5:] if key else 'NO KEY'}")

if not key:
    print("❌ No hay clave de Groq")
    exit()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=key
)

try:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": "Hola, respondé con una palabra: OK"}],
        max_tokens=10
    )
    print("✅ Groq funciona:", response.choices[0].message.content)
except Exception as e:
    print(f"❌ Error: {e}")