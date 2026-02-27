# src/confrontacion/detectores.py 
# Detecta patrones de comportamiento para confrontacion
# Versión mejorada con detector de cambio de tema

import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'bot_data.db')

def detectar_patron(texto, historial=None):
    """Detecta patrones de baja vibracion o repeticion"""
    texto_lower = texto.lower()

    # Palabras clave de baja vibracion
    palabras_baja = ["no puedo", "siempre", "nunca", "odio", "fracaso", "imposible", "culpa", "deberia"]

    for palabra in palabras_baja:
        if palabra in texto_lower:
            return {
                "tipo": "baja_vibracion", 
                "palabra": palabra,
                "intensidad": 0.7,
                "sugerencia": f"Noto que usaste '{palabra}'. ¿Que hay detras de eso?"
            }

    # Deteccion de repeticion (si hay historial)
    if historial and len(historial) > 0:
        temas_recientes = [h.get("tema", "") for h in historial[-3:]] 
        if any(tema in texto_lower for tema in temas_recientes):
            return {
                "tipo": "repeticion",
                "tema": texto_lower[:30],
                "intensidad": 0.5,
                "sugerencia": "Este tema aparece seguido. ¿Hay algo que no estes viendo?"
            }

    return None

def detectar_estado_emocional(texto):
    """Detecta el estado emocional aproximado"""
    texto_lower = texto.lower()

    estados = {
        "tristeza": ["triste", "deprimido", "bajo", "mal", "decaimiento"],
        "ansiedad": ["ansioso", "nervioso", "preocupado", "miedo", "temor"],
        "ira": ["enojado", "furioso", "rabia", "bronca", "molesto"],
        "alegria": ["feliz", "contento", "alegre", "bien", "genial"],
        "confusion": ["confundido", "no se", "duda", "incierto", "claro"]
    }

    for estado, palabras in estados.items():
        if any(p in texto_lower for p in palabras):
            return {"estado": estado, "confianza": 0.6}

    return {"estado": "neutral", "confianza": 0.3}

def obtener_ultimo_tema(user_id):
    """Obtiene el último tema hablado por el usuario"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        SELECT tema FROM conversaciones 
        WHERE user_id = ? AND tema IS NOT NULL 
        ORDER BY fecha DESC LIMIT 1
    ''', (user_id,))
    resultado = c.fetchone()
    conn.close()
    return resultado[0] if resultado else None

def detectar_cambio_de_tema(user_id, tema_actual):
    """Detecta si hubo un cambio drástico de tema"""
    ultimo_tema = obtener_ultimo_tema(user_id)
    
    if not ultimo_tema:
        return None  # No hay historial
    
    if ultimo_tema == tema_actual:
        return None  # Mismo tema
    
    # Lista de temas relacionados (para no alarmarse con cambios normales)
    relacionados = {
        "hijo": ["familia", "pareja", "hijos"],
        "pareja": ["familia", "hijo", "relaciones"],
        "cuerpo": ["salud", "entrenamiento", "habitos"],
        "mente": ["habitos", "aprendizaje"],
        "alma": ["espiritualidad", "meditacion"],
        "trabajo": ["negocios", "dinero"]
    }
    
    # Verificar si los temas están relacionados
    if tema_actual in relacionados and ultimo_tema in relacionados.get(tema_actual, []):
        return None  # Son temas relacionados, no es cambio drástico
    
    if ultimo_tema in relacionados and tema_actual in relacionados.get(ultimo_tema, []):
        return None  # Son temas relacionados
    
    # Si llegamos acá, es un cambio drástico
    return {
        "tipo": "cambio_tema",
        "desde": ultimo_tema,
        "hacia": tema_actual,
        "sugerencia": f"Pasaste de hablar de {ultimo_tema} a {tema_actual}. ¿Todo bien?"
    }