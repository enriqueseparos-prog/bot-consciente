import os
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

cliente = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

async def probar():
    try:
        response = await cliente.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "user", "content": "Hola"}],
            temperature=0.1,
            max_tokens=10
        )
        print("? FUNCIONA:", response.choices[0].message.content)
    except Exception as e:
        print("? ERROR:", str(e))

asyncio.run(probar())