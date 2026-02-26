# src/confrontacion/detectores.py
# Detecta patrones de comportamiento para confrontacion - Version sin acentos

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