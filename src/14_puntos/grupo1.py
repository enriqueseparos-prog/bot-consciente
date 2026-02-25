# src/14_puntos/grupo1.py
# Puntos 1-3: Perspectiva, Proyección, Desafíos

def punto1_perspectiva(contexto=None):
    """Cambia la forma de ver los problemas"""
    frases = [
        "¿Y si esto no es un problema, sino una oportunidad?",
        "¿Cómo vería esto tu yo de 80 años?",
        "¿Qué pasaría si cambiaras el lente con que miras?",
        "Todo depende del cristal con que se mire."
    ]
    import random
    return random.choice(frases)

def punto2_proyeccion(contexto=None):
    """Cómo manifiestas al mundo"""
    frases = [
        "Lo que proyectas, el mundo te devuelve.",
        "Tu exterior es un espejo de tu interior.",
        "¿Qué estás proyectando hoy sin darte cuenta?",
        "La realidad no es lo que pasa, sino lo que interpretas."
    ]
    import random
    return random.choice(frases)

def punto3_desafios(contexto=None):
    """Los obstáculos son el camino"""
    frases = [
        "El obstáculo es el camino, decían los estoicos.",
        "Cada desafío trae una lección escondida.",
        "No hay crecimiento sin resistencia.",
        "Lo que hoy es difícil, mañana será tu fortaleza."
    ]
    import random
    return random.choice(frases)