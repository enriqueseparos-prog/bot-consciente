# src/confrontacion/detectores.py
# Detecta patrones de comportamiento para confrontación

def detectar_patron(texto, historial=None):
    """Detecta patrones de baja vibración o repetición"""
    texto_lower = texto.lower()
    
    palabras_baja = ["no puedo", "siempre", "nunca", "odio", "fracaso", "imposible", "culpa", "debería"]
    
    for palabra in palabras_baja:
        if palabra in texto_lower:
            return {
                "tipo": "baja_vibracion",
                "palabra": palabra,
                "intensidad": 0.7,
                "sugerencia": f"Noto que usaste '{palabra}'. ¿Qué hay detrás de eso?"
            }
    
    if historial and len(historial) > 0:
        temas_recientes = [h.get("tema", "") for h in historial[-3:]]
        if any(tema in texto_lower for tema in temas_recientes):
            return {
                "tipo": "repeticion",
                "tema": texto_lower[:30],
                "intensidad": 0.5,
                "sugerencia": "Este tema aparece seguido. ¿Hay algo que no estés viendo?"
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
        "confusion": ["confundido", "no sé", "duda", "incierto", "claro"]
    }
    
    for estado, palabras in estados.items():
        if any(p in texto_lower for p in palabras):
            return {"estado": estado, "confianza": 0.6}
    
    return {"estado": "neutral", "confianza": 0.3}