from src.config import ai_client
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

async def test():
    # Probar solo con OpenRouter (cuando tengas la clave nueva)
    response = await ai_client.get_completion(
        messages=[{"role": "user", "content": "Hola, responde OK"}],
        temperature=0.1,
        max_tokens=10
    )
    print(f"Respuesta: {response}")

asyncio.run(test())