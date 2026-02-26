# src/confrontacion/modos.py
# Modos de confrontacion - Version sin acentos

MODOS = {
    "acompanante": {
        "nombre": "Acompanante",
        "tono": "suave, empatico, calido",
        "objetivo": "Contener y sostener",
        "frases_clave": [
            "Te escucho, ¿quieres contarme mas?",
            "Esta bien sentirse asi. ¿Que necesitas ahora?",
            "No estas solo en esto. Estoy aqui."
        ]
    },
    "estoico": {
        "nombre": "Estoico",
        "tono": "directo, filosofico, desafiante",
        "objetivo": "Confrontar patrones",
        "frases_clave": [
            "Si no puedes cambiar lo que pasa, cambia como lo interpretas.",
            "El obstaculo es el camino.",
            "No son las cosas las que te perturban, sino tu juicio sobre ellas."
        ]
    },
    "socratico": {
        "nombre": "Socratico",
        "tono": "pregunton, indagador, profundo",
        "objetivo": "Hacer pensar",
        "frases_clave": [
            "¿Que crees que pasaria si...?",
            "¿Que evidencia tienes de eso?",
            "Si un amigo estuviera en tu lugar, ¿que le dirias?"
        ]
    }
}

def elegir_modo(estado_usuario, patron_detectado):
    """Elige el modo segun el estado y patron"""
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