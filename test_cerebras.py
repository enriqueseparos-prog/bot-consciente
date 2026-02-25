import os
import asyncio
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

cliente = AsyncOpenAI(
    api_key=os.getenv("CEREBRAS_API_KEY"),
    base_url="https://api.cerebras.ai/v1"
)

async def probar():
    try:
        response = await cliente.chat.completions.create(
            model="llama3.1-8b", # Nombre corregido
            messages=[{"role": "user", "content": "Responde OK"}],
            max_tokens=5
        )
        print("? Cerebras OK:", response.choices[0].message.content)
    except Exception as e:
        print("? Error:", e)

asyncio.run(probar())