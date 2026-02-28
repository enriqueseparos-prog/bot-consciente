import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GEMINI_API_KEY")
print(f"Key encontrada: {'✅' if key else '❌'}")

if key:
    genai.configure(api_key=key)
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content("Decí hola")
    print("Respuesta:", response.text)