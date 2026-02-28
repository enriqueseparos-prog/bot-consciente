# src/core/discernimiento.py
# El bot decide qué hacer según el contexto

import socket
import re
from typing import Dict, Any

def hay_internet(host="8.8.8.8", port=53, timeout=3):
    """
    Detecta si hay conexión a internet.
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False

def detectar_complejidad(texto: str) -> str:
    """
    Clasifica el mensaje en: simple, normal, complejo.
    """
    texto_lower = texto.lower()
    
    # Palabras que indican complejidad
    palabras_complejas = [
        "significa", "explica", "por qué", "cómo funciona", 
        "diferencia entre", "relación entre", "filosofía", 
        "concepto", "teoría", "historia de", "origen"
    ]
    
    # Palabras que indican simplicidad
    palabras_simples = [
        "hola", "gracias", "ok", "sí", "no", "vale", 
        "listo", "entendido", "claro", "bueno"
    ]
    
    for palabra in palabras_complejas:
        if palabra in texto_lower:
            return "complejo"
    
    for palabra in palabras_simples:
        if palabra in texto_lower or len(texto.split()) < 4:
            return "simple"
    
    return "normal"

def elegir_modo_segun_complejidad(complejidad: str, estado_animo: int = 5) -> str:
    """
    Decide el modo del bot según la complejidad y el estado de ánimo.
    """
    if complejidad == "simple":
        return "acompanante"  # Modo cálido y breve
    elif complejidad == "complejo":
        if estado_animo < 4:
            return "socratico"  # Para profundizar con cuidado
        else:
            return "estoico"  # Modo desafiante
    else:
        return "guia"  # Modo equilibrado

def decidir_recurso(complejidad: str, hay_net: bool) -> Dict[str, Any]:
    """
    Decide qué recurso usar: local, api gratis o api paga.
    """
    if not hay_net:
        return {"tipo": "local", "modelo": "gemini-2.0-flash"}  # Offline
    
    if complejidad == "simple":
        return {"tipo": "api_gratis", "proveedor": "groq", "modelo": "llama-3.1-8b-instant"}
    elif complejidad == "normal":
        return {"tipo": "api_gratis", "proveedor": "gemini", "modelo": "gemini-2.0-flash"}
    else:
        return {"tipo": "api_paga", "proveedor": "openai", "modelo": "gpt-3.5-turbo"}

def resumen_discernimiento(texto: str, estado_animo: int = 5) -> Dict[str, Any]:
    """
    Devuelve un resumen con todas las decisiones.
    """
    hay_net = hay_internet()
    complejidad = detectar_complejidad(texto)
    modo = elegir_modo_segun_complejidad(complejidad, estado_animo)
    recurso = decidir_recurso(complejidad, hay_net)
    
    return {
        "texto": texto[:50],
        "internet": hay_net,
        "complejidad": complejidad,
        "modo_sugerido": modo,
        "recurso": recurso
    }