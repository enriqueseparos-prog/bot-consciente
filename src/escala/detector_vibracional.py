# src/escala/detector_vibracional.py
# Clasificador de vibracion - Version sin acentos

def clasificar_vibracion(texto):
    """
    Clasifica un texto en alta, baja o neutra vibracion
    Version simplificada para pruebas
    """
    texto_lower = texto.lower()
    
    # Palabras de alta vibracion
    alta = ["gracias", "amor", "paz", "alegria", "gratitud", "feliz", "bien"]
    # Palabras de baja vibracion
    baja = ["miedo", "triste", "mal", "odio", "enfado", "ira", "preocupado"]
    
    for palabra in alta:
        if palabra in texto_lower:
            return {
                "vibracion": "alta",
                "sugerencia": "Estas en sintonía. Aprovecha este estado.",
                "frase": "La gratitud eleva tu vibracion."
            }
    
    for palabra in baja:
        if palabra in texto_lower:
            return {
                "vibracion": "baja",
                "sugerencia": "Reconoce lo que sientes sin juzgarlo. Es temporal.",
                "frase": "Lo que resistes, persiste. Acéptalo para transformarlo."
            }
    
    return {
        "vibracion": "neutra",
        "sugerencia": "Todo en equilibrio. Puedes profundizar si quieres.",
        "frase": "La conciencia es el primer paso hacia la transformacion."
    }

def sugerir_accion_por_vibracion(vibracion):
    """Sugiere una accion segun la vibracion"""
    acciones = {
        "alta": "Te sugiero meditar sobre lo que hoy te hace vibrar alto.",
        "baja": "Te sugiero el protocolo de rescate de 3 minutos.",
        "neutra": "Te sugiero elegir un habito de tu lista y practicarlo."
    }
    return acciones.get(vibracion, "Observa tu estado sin juzgar.")