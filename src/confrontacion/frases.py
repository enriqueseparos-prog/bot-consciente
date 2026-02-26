# src/confrontacion/frases.py
# Banco de frases por modo - Version sin acentos

FRASES = {
    "acompanante": [
        "Estoy aqui contigo. ¿Como te sientes ahora?",
        "A veces solo necesitamos que nos escuchen. Te escucho.",
        "Respira profundo. No estas solo en esto.",
        "Lo que sientes es valido. ¿Quieres explorarlo?",
        "Hoy puede ser dificil, pero estas aqui. Eso ya es mucho."
    ],
    "estoico": [
        "No puedes controlar lo que pasa, pero si como respondes.",
        "La adversidad es combustible para el alma fuerte.",
        "¿Esto que te preocupa, depende de ti o no?",
        "El sufrimiento nace del deseo, no del evento.",
        "Recuerda: esto tambien pasara."
    ],
    "socratico": [
        "¿Que pasaria si lo miraras desde otra perspectiva?",
        "¿Eso que piensas es realmente cierto?",
        "Si no hubiera miedo, ¿que harías?",
        "¿Que te gustaria que pasara?",
        "¿Como seria un buen dia para ti?"
    ]
}

def obtener_frase(modo):
    import random
    return random.choice(FRASES.get(modo, FRASES["acompanante"]))