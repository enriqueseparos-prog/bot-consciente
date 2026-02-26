# src/puntos_14/grupo1.py
# Puntos 1-3: Perspectiva, Proyeccion, Desafios - Version sin acentos

def punto1_perspectiva(contexto=None):
    """Cambia la forma de ver los problemas"""
    frases = [
        "¿Y si esto no es un problema, sino una oportunidad?",
        "¿Como veria esto tu yo de 80 años?",
        "¿Que pasaria si cambiaras el lente con que miras?",
        "Todo depende del cristal con que se mire."
    ]
    import random
    return random.choice(frases)

def punto2_proyeccion(contexto=None):
    """Como manifiestas al mundo"""
    frases = [
        "Lo que proyectas, el mundo te devuelve.",
        "Tu exterior es un espejo de tu interior.",
        "¿Que estas proyectando hoy sin darte cuenta?",
        "La realidad no es lo que pasa, sino lo que interpretas."
    ]
    import random
    return random.choice(frases)

def punto3_desafios(contexto=None):
    """Los obstaculos son el camino"""
    frases = [
        "El obstaculo es el camino, decían los estoicos.",
        "Cada desafio trae una leccion escondida.",
        "No hay crecimiento sin resistencia.",
        "Lo que hoy es dificil, mañana sera tu fortaleza."
    ]
    import random
    return random.choice(frases)