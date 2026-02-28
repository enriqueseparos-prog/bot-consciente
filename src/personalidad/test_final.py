# test_final.py - Test con pausa para ver resultados

import os
import sys
from dotenv import load_dotenv

print("🔍 TEST DE PROVEEDORES")
print("=====================")
print("Presioná CTRL+C para salir")
print("-" * 30)

# Cargar variables
load_dotenv()
print("✅ Archivo .env cargado")

# Verificar cada clave
gemini = os.getenv("GEMINI_API_KEY")
groq = os.getenv("GROQ_API_KEY")
cerebras = os.getenv("CEREBRAS_API_KEY")
deepseek = os.getenv("DEEPSEEK_API_KEY")

print(f"\n📌 GEMINI: {'✅' if gemini else '❌'} {gemini[:10] if gemini else 'no encontrada'}")
print(f"📌 GROQ: {'✅' if groq else '❌'} {groq[:10] if groq else 'no encontrada'}")
print(f"📌 CEREBRAS: {'✅' if cerebras else '❌'} {cerebras[:10] if cerebras else 'no encontrada'}")
print(f"📌 DEEPSEEK: {'✅' if deepseek else '❌'} {deepseek[:10] if deepseek else 'no encontrada'}")

print("\n" + "="*30)
print("✅ TEST COMPLETADO")
print("Esta ventana se cerrará en 30 segundos...")

# Esperar 30 segundos para que puedas leer
import time
time.sleep(30)