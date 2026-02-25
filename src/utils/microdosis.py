# src/utils/microdosis.py
# Versiones mínimas de hábitos para cuando no hay tiempo

MICRODOSIS = {
    # HÁBITOS BASE
    "relación con hijo": "Mirá a tu hijo a los ojos y decile 'te quiero' o preguntale algo con genuino interés. 30 segundos.",
    "relación con pareja": "Un abrazo de 10 segundos sin hablar. Solo presencia.",
    "relación con familiares": "Envía un mensaje corto a un familiar que hace tiempo no contactas.",
    "tareas del hogar": "Ordená UNA cosa (la cama, los platos, una silla). 2 minutos.",
    
    # HÁBITOS DE CUERPO
    "flexibilidad": "Estirá un brazo 10 segundos mientras respirás. Cambiá de lado.",
    "muay thai": "Sombra boxing 1 minuto. Sin técnica, solo mover el cuerpo.",
    "descanso": "Cerrá los ojos 60 segundos. Respirá profundo.",
    "hidratación": "Tomá un vaso de agua AHORA.",
    "dieta proteica": "En tu próxima comida, asegurate de que haya proteína.",
    "hipertrofia": "5 flexiones de brazos. Sin excusas.",
    "calistenia": "3 sentadillas. Sentí las piernas.",
    "medición": "Pesate o tomate una medida rápida.",
    "cardio": "Subí y bajá una escalera o caminá rápido 2 minutos.",
    
    # HÁBITOS DE MENTE
    "estoicismo": "Preguntate: ¿esto que me preocupa depende de mí?",
    "memoria": "Intentá recordar 3 cosas que hiciste ayer.",
    "eneagrama": "Observá una reacción tuya y preguntate: ¿qué tipo se activó?",
    "sombra": "Escribí una emoción que hoy escondiste.",
    "estructura": "Hacé una lista de 3 cosas pendientes. Ordenalas.",
    "toma de decisiones": "Elegí entre A o B en 10 segundos. No pienses.",
    "lectura veloz": "Leé un párrafo con el dedo guía.",
    
    # HÁBITOS DE ALMA
    "reiki": "Poné las manos en tu corazón y respirá. 1 minuto.",
    "gestión emocional": "Identificá la emoción del momento y nombrala.",
    "meditación": "3 respiraciones conscientes. Ahora.",
    "propósito": "Preguntate: ¿qué quiero hoy? Una palabra.",
    "pnl": "Cambiá tu postura física por 30 segundos. Notá cómo cambia tu ánimo.",
    "gratitud": "Nombra UNA cosa que hoy no salió mal.",
    "disciplina": "Hacé una cosa que postergabas. 2 minutos.",
    "desapego": "Soltá una expectativa. Solo por hoy."
}

def obtener_microdosis(habito):
    """Devuelve la microdosis para un hábito específico"""
    habito_lower = habito.lower()
    
    # Búsqueda directa
    if habito_lower in MICRODOSIS:
        return MICRODOSIS[habito_lower]
    
    # Búsqueda aproximada (por si el nombre no coincide exactamente)
    for clave, valor in MICRODOSIS.items():
        if clave in habito_lower or habito_lower in clave:
            return valor
    
    return "Respirá profundo 3 veces y preguntate: ¿qué necesito ahora?"

def obtener_microdosis_aleatoria():
    """Devuelve una microdosis al azar"""
    import random
    habito = random.choice(list(MICRODOSIS.keys()))
    return f"?? *Microdosis para '{habito}':*\n{MICRODOSIS[habito]}"