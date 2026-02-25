# src/core/maestros.py
# Maestros externos, internos y civilizaciones

MAESTROS_EXTERNOS = {
    "frank suarez": {
        "nombre": "Frank Suárez",
        "area": "salud",
        "frase": "El metabolismo es la base de toda energía.",
        "practica": "Tomá un vaso de agua con una pizca de sal al despertar.",
        "logros": "Metabolismo, hormonas, sueño"
    },
    "marshall rosenberg": {
        "nombre": "Marshall Rosenberg",
        "area": "relaciones",
        "frase": "Detrás de toda crítica hay una necesidad no expresada.",
        "practica": "Observá sin evaluar por 5 minutos.",
        "logros": "Comunicación NoViolenta (CNV)"
    },
    "jim kwik": {
        "nombre": "Jim Kwik",
        "area": "mente",
        "frase": "El conocimiento aplicado es poder.",
        "practica": "Usá el dedo para guiar la lectura.",
        "logros": "Memoria, neuroplasticidad, enfoque"
    }
}

MAESTROS_INTERNOS = {
    "inca": {
        "nombre": "INCA",
        "viaje": "Cuerpo ? Cuerpo",
        "frase": "Mi cuerpo es territorio sagrado.",
        "practica": "Sentí tus pies en el suelo y agradecé tu cuerpo."
    },
    "bushido": {
        "nombre": "BUSHIDO",
        "viaje": "Cuerpo ? Mente",
        "frase": "La disciplina encarnada es el puente entre intención y acción.",
        "practica": "Hacé una cosa que sabés que debés hacer aunque no tengas ganas."
    }
}

CIVILIZACIONES = {
    "filosofia china": {
        "nombre": "Filosofía China",
        "enseñanza": "El Yin-Yang nos recuerda que todo contiene su opuesto.",
        "practica": "Buscá el punto medio hoy."
    }
}

def buscar_maestro(nombre):
    """Busca un maestro por nombre (case insensitive)"""
    nombre = nombre.lower().strip()
    
    # Buscar en externos
    if nombre in MAESTROS_EXTERNOS:
        return MAESTROS_EXTERNOS[nombre]
    
    # Buscar en internos
    if nombre in MAESTROS_INTERNOS:
        return MAESTROS_INTERNOS[nombre]
    
    # Buscar en civilizaciones
    if nombre in CIVILIZACIONES:
        return CIVILIZACIONES[nombre]
    
    return None