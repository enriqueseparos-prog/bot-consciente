# src/core/protocolos.py
# Protocolos esenciales del sistema consciente

# ============================================
# PROTOCOLO DE RESCATE (3 minutos)
# ============================================

PROTOCOLO_RESCATE = {
    "minuto_1": {
        "nombre": "Guerrero",
        "accion": "Anclaje físico",
        "descripcion": "Conectá con tu respiración. Sentí tus pies en el suelo. Tomá conciencia de tu cuerpo aquí y ahora.",
        "comando": ">> system.anchor(physical, here_and_now)"
    },
    "minuto_2": {
        "nombre": "Mago",
        "accion": "Liberación energética",
        "descripcion": "Identificá la emoción estancada. Exhalá profundo y soltala. Sentí cómo la energía fluye.",
        "comando": ">> energy.flush(stagnant, all)"
    },
    "minuto_3": {
        "nombre": "Arquero",
        "accion": "Acción concreta",
        "descripcion": "Definí la próxima acción más pequeña y tangible. Una sola cosa que podés hacer ahora.",
        "comando": ">> task.define(next_action, smallest_physical)"
    }
}

def obtener_rescate():
    """Devuelve el protocolo completo formateado"""
    texto = "?? *PROTOCOLO DE RESCATE (3 minutos)*\n\n"
    for minuto, datos in PROTOCOLO_RESCATE.items():
        texto += f"*{minuto.replace('_', ' ').upper()}* - {datos['nombre']}\n"
        texto += f"?? {datos['accion']}\n"
        texto += f"?? {datos['descripcion']}\n"
        texto += f"? `{datos['comando']}`\n\n"
    return texto

# ============================================
# FLUJOS MAESTROS
# ============================================

FLUJOS_MAESTROS = {
    "manifestacion": {
        "nombre": "Manifestación",
        "secuencia": ["Sócrates", "San Francisco", "Chamán", "Tántrico", "Inca", "Bushido"],
        "descripcion": "Para llevar una idea del plano mental al mundo físico"
    },
    "recepcion": {
        "nombre": "Recepción",
        "secuencia": ["Sócrates", "Estoico", "Inca", "Sadhu", "Chamán", "Maya"],
        "descripcion": "Para integrar una experiencia del cuerpo a la conciencia"
    },
    "integracion": {
        "nombre": "Integración",
        "secuencia": ["Inca", "Bushido", "Estoico", "Sócrates", "San Francisco", "Chamán"],
        "descripcion": "Para armonizar cuerpo, mente y alma después de un desafío"
    },
    "expresion": {
        "nombre": "Expresión",
        "secuencia": ["Chamán", "Maya", "Tántrico", "Sadhu", "Bushido", "Inca"],
        "descripcion": "Para que el alma se exprese a través del cuerpo en el mundo"
    }
}

def obtener_flujo(nombre):
    """Devuelve un flujo específico"""
    return FLUJOS_MAESTROS.get(nombre.lower())

def listar_flujos():
    """Devuelve lista de flujos disponibles"""
    texto = "?? *FLUJOS MAESTROS DISPONIBLES*\n\n"
    for key, flujo in FLUJOS_MAESTROS.items():
        texto += f"*{flujo['nombre']}*: {flujo['descripcion']}\n"
        texto += f"`/flujo {key}`\n\n"
    return texto

# ============================================
# SISTEMA DE VALORES
# ============================================

VALORES = {
    "disciplina": {
        "nombre": "DISCIPLINA",
        "definicion": "Fuerza de coherencia interna que mantiene tu rumbo incluso cuando es difícil.",
        "pregunta": "¿Hoy actué con disciplina o dejé que la pereza ganara?"
    },
    "responsabilidad": {
        "nombre": "RESPONSABILIDAD",
        "definicion": "Capacidad de responder creativamente (no reaccionar automáticamente) ante cualquier situación.",
        "pregunta": "¿Hoy respondí desde la conciencia o reaccioné desde el automático?"
    },
    "empatia": {
        "nombre": "EMPATÍA",
        "definicion": "Resonancia consciente con límites claros. Sentir al otro sin perder tu centro.",
        "pregunta": "¿Hoy pude sentir al otro sin perderme a mí mismo?"
    }
}

def check_valores():
    """Devuelve las tres preguntas para auto-evaluación diaria"""
    texto = "?? *TUS VALORES HOY*\n\n"
    for v in VALORES.values():
        texto += f"*{v['nombre']}*\n{v['pregunta']}\n\n"
    return texto

# ============================================
# SISTEMA DE POLO OPUESTO (-9 a +9)
# ============================================

def explicar_polo_opuesto():
    return """?? *ESCALA DE POLO OPUESTO (-9 a +9)*

Cada cualidad tiene su opuesto. La maestría es habitar conscientemente el rango completo.

Ejemplo:
-9 Miedo ............. 0 ............. +9 Amor
-9 Odio .............. 0 ............. +9 Aceptación
-9 Pereza ............. 0 ............. +9 Disciplina

Hoy, ¿en qué número estás? No para juzgarte, sino para observar.
"""