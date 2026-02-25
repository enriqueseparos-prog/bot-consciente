# src/confrontacion/frases.py
# Banco de frases por modo

FRASES = {
    "acompanante": [
        "Estoy aquí contigo. ¿Cómo te sientes ahora?",
        "A veces solo necesitamos que nos escuchen. Te escucho.",
        "Respira profundo. No estás solo en esto.",
        "Lo que sientes es válido. ¿Quieres explorarlo?",
        "Hoy puede ser difícil, pero estás aquí. Eso ya es mucho."
    ],
    "estoico": [
        "No puedes controlar lo que pasa, pero sí cómo respondes.",
        "La adversidad es combustible para el alma fuerte.",
        "¿Esto que te preocupa, depende de ti o no?",
        "El sufrimiento nace del deseo, no del evento.",
        "Recuerda: esto también pasará."
    ],
    "socratico": [
        "¿Qué pasaría si lo miraras desde otra perspectiva?",
        "¿Eso que piensas es realmente cierto?",
        "Si no hubiera miedo, ¿qué harías?",
        "¿Qué te gustaría que pasara?",
        "¿Cómo sería un buen día para ti?"
    ]
}

def obtener_frase(modo):
    import random
    return random.choice(FRASES.get(modo, FRASES["acompanante"]))

def obtener_frase_por_contexto(modo, contexto):
    """Versión más avanzada (por implementar)"""
    return obtener_frase(modo)