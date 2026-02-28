# src/config_nuevo.py - Versión con la NUEVA librería google-genai

import os
import logging
from typing import Optional
from google import genai
from google.genai import types

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class AIClient:
    def __init__(self):
        self.api_key = GEMINI_API_KEY
        self.ultimo_usado = None
        
        if self.api_key:
            # Configuración NUEVA: se crea un cliente directamente
            self.client = genai.Client(api_key=self.api_key)
            logger.info("✅ Cliente Google GenAI (nuevo) listo")
        else:
            self.client = None
            logger.error("❌ No hay key para Gemini")

    async def get_completion(self, messages, **kwargs):
        if not self.client:
            return None
        try:
            # La forma de llamar al modelo es ligeramente diferente
            # Asumiendo que el último mensaje es del usuario
            prompt = messages[-1]["content"]
            response = self.client.models.generate_content(
                model='gemini-2.0-flash-exp', # El modelo puede tener un nombre ligeramente distinto
                contents=prompt
            )
            return response.text
        except Exception as e:
            logger.error(f"Error con Gemini (nuevo SDK): {e}")
            return None

# Instancia global
ai_client = AIClient()