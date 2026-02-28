print("=" * 50)
print("🔍 INICIANDO TEST RAPIDO")
print("=" * 50)

import os
from dotenv import load_dotenv

print("1. Cargando .env...")
load_dotenv()
print("2. .env cargado")

print("3. Leyendo variables...")
gemini = os.getenv("GEMINI_API_KEY")
groq = os.getenv("GROQ_API_KEY")
cerebras = os.getenv("CEREBRAS_API_KEY")
deepseek = os.getenv("DEEPSEEK_API_KEY")

print(f"4. GEMINI: {'✅' if gemini else '❌'}")
print(f"5. GROQ: {'✅' if groq else '❌'}")
print(f"6. CEREBRAS: {'✅' if cerebras else '❌'}")
print(f"7. DEEPSEEK: {'✅' if deepseek else '❌'}")

print("8. TEST COMPLETADO")
print("=" * 50)

# Pequeña pausa para que alcances a leer
input("Presiona ENTER para salir...")