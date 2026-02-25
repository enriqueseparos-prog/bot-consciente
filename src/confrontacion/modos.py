# src/confrontacion/modos.py
# Modos de confrontación

MODOS = {
    "acompanante": {
        "nombre": "Acompañante",
        "tono": "suave, empático, cálido",
        "objetivo": "Contener y sostener",
        "frases_clave": [
            "Te escucho, ¿quieres contarme más?",
            "Está bien sentirse así. ¿Qué necesitas ahora?",
            "No estás solo en esto. Estoy aquí."
        ]
    },
    "estoico": {
        "nombre": "Estoico",
        "tono": "directo, filosófico, desafiante",
        "objetivo": "Confrentar patrones",
        "frases_clave": [
            "Si no puedes cambiar lo que pasa, cambia cómo lo interpretas.",
            "El obstáculo es el camino.",
            "No son las cosas las que te perturban, sino tu juicio sobre ellas."
        ]
    },
    "socratico": {
        "nombre": "Socrático",
        "tono": "preguntón, indagador, profundo",
        "objetivo": "Hacer pensar",
        "frases_clave": [
            "¿Qué crees que pasaría si...?",
            "¿Qué evidencia tienes de eso?",
            "Si un amigo estuviera en tu lugar, ¿qué le dirías?"
        ]
    }
}

def elegir_modo(estado_usuario, patron_detectado):
    """Elige el modo según el estado y patrón"""
    if patron_detectado and patron_detectado.get("tipo") == "baja_vibracion":
        if estado_usuario.get("estado") in ["tristeza", "ansiedad"]:
            return "acompanante"
        else:
            return "estoico"
    elif patron_detectado and patron_detectado.get("tipo") == "repeticion":
        return "socratico"
    else:
        return "acompanante"

def obtener_frase(modo):
    """Devuelve una frase aleatoria del modo elegido"""
    import random
    frases = MODOS[modo]["frases_clave"]
    return random.choice(frases)