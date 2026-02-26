# src/core/habitos.py
# 26 habitos organizados por dominio

HABITOS = {
    "base": [
        {"nombre": "Relacion con hijo", "nivel": "bronce", "prioridad": 2},
        {"nombre": "Relacion con pareja", "nivel": "bronce", "prioridad": 2},
        {"nombre": "Relacion con familiares", "nivel": "bronce", "prioridad": 1},
        {"nombre": "Tareas del hogar", "nivel": "bronce", "prioridad": 2}
    ],
    "cuerpo": [
        {"nombre": "Muay Thai", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Descanso", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Hidratacion", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Dieta proteica", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Hipertrofia (Mentzer)", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Calistenia", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Flexibilidad Funcional", "nivel": "bronce", "prioridad": 3},
        {"nombre": "Medicion y Seguimiento", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Cardio", "nivel": "bronce", "prioridad": 0}
    ],
    "mente": [
        {"nombre": "Estoicismo", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Memoria (Jim Kwik)", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Eneagrama + Lectura de Personas", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Integracion de la Sombra (Jung)", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Estructura del Pensamiento", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Toma de Decisiones", "nivel": "bronce", "prioridad": 3},
        {"nombre": "Lectura Veloz", "nivel": "bronce", "prioridad": 0}
    ],
    "alma": [
        {"nombre": "Reiki", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Gestion Emocional", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Meditacion Profunda (Silva)", "nivel": "bronce", "prioridad": 0},
        {"nombre": "Proposito y Valores", "nivel": "bronce", "prioridad": 0},
        {"nombre": "PNL", "nivel": "bronce", "prioridad": 3},
        {"nombre": "Eneagrama", "nivel": "bronce", "prioridad": 0}
    ]
}

def obtener_prioridades():
    """Devuelve los habitos con prioridad maxima (3)"""
    prioritarios = []
    for dominio, habitos in HABITOS.items():
        for h in habitos:
            if h["prioridad"] == 3:
                prioritarios.append(h["nombre"])
    return prioritarios

def obtener_por_dominio(dominio):
    """Devuelve los habitos de un dominio especifico"""
    return HABITOS.get(dominio, [])