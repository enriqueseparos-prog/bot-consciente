print("🔍 INICIANDO TEST DE PROVEEDORES")
print("================================")

import os
from dotenv import load_dotenv

load_dotenv()

print("1. Leyendo variables de entorno...")
gemini = os.getenv("GEMINI_API_KEY")
groq = os.getenv("GROQ_API_KEY")
cerebras = os.getenv("CEREBRAS_API_KEY")
deepseek = os.getenv("DEEPSEEK_API_KEY")

print(f"2. GEMINI: {'✅' if gemini else '❌'}")
print(f"3. GROQ: {'✅' if groq else '❌'}")
print(f"4. CEREBRAS: {'✅' if cerebras else '❌'}")
print(f"5. DEEPSEEK: {'✅' if deepseek else '❌'}")

print("6. TEST COMPLETADO")