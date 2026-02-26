# src/core/protocolos.py
# Protocolos esenciales del sistema consciente - Version sin acentos

# ============================================
# PROTOCOLO DE RESCATE (3 minutos)
# ============================================

PROTOCOLO_RESCATE = {
    "minuto_1": {
        "nombre": "Guerrero",
        "accion": "Anclaje fisico",
        "descripcion": "Conecta con tu respiracion. Siente tus pies en el suelo. Toma conciencia de tu cuerpo aqui y ahora.",
        "comando": ">> system.anchor(physical, here_and_now)"
    },
    "minuto_2": {
        "nombre": "Mago",
        "accion": "Liberacion energetica",
        "descripcion": "Identifica la emocion estancada. Exhala profundo y sueltala. Siente como la energia fluye.",
        "comando": ">> energy.flush(stagnant, all)"
    },
    "minuto_3": {
        "nombre": "Arquero",
        "accion": "Accion concreta",
        "descripcion": "Define la proxima accion mas pequena y tangible. Una sola cosa que puedes hacer ahora.",
        "comando": ">> task.define(next_action, smallest_physical)"
    }
}

def obtener_rescate():
    """Devuelve el protocolo completo formateado"""
    texto = "🆘 *PROTOCOLO DE RESCATE (3 minutos)*\n\n"
    for minuto, datos in PROTOCOLO_RESCATE.items():
        texto += f"*{minuto.replace('_', ' ').upper()}* - {datos['nombre']}\n"
        texto += f"📌 {datos['accion']}\n"
        texto += f"💬 {datos['descripcion']}\n"
        texto += f"⚡ `{datos['comando']}`\n\n"
    return texto

# ============================================
# FLUJOS MAESTROS
# ============================================

FLUJOS_MAESTROS = {
    "manifestacion": {
        "nombre": "Manifestacion",
        "secuencia": ["Socrates", "San Francisco", "Chaman", "Tantrico", "Inca", "Bushido"],
        "descripcion": "Para llevar una idea del plano mental al mundo fisico"
    },
    "recepcion": {
        "nombre": "Recepcion",
        "secuencia": ["Socrates", "Estoico", "Inca", "Sadhu", "Chaman", "Maya"],
        "descripcion": "Para integrar una experiencia del cuerpo a la conciencia"
    },
    "integracion": {
        "nombre": "Integracion",
        "secuencia": ["Inca", "Bushido", "Estoico", "Socrates", "San Francisco", "Chaman"],
        "descripcion": "Para armonizar cuerpo, mente y alma despues de un desafio"
    },
    "expresion": {
        "nombre": "Expresion",
        "secuencia": ["Chaman", "Maya", "Tantrico", "Sadhu", "Bushido", "Inca"],
        "descripcion": "Para que el alma se exprese a traves del cuerpo en el mundo"
    }
}

def obtener_flujo(nombre):
    """Devuelve un flujo especifico"""
    return FLUJOS_MAESTROS.get(nombre.lower())

def listar_flujos():
    """Devuelve lista de flujos disponibles"""
    texto = "🌀 *FLUJOS MAESTROS DISPONIBLES*\n\n"
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
        "definicion": "Fuerza de coherencia interna que mantiene tu rumbo incluso cuando es dificil.",
        "pregunta": "¿Hoy actue con disciplina o deje que la pereza ganara?"
    },
    "responsabilidad": {
        "nombre": "RESPONSABILIDAD",
        "definicion": "Capacidad de responder creativamente (no reaccionar automaticamente) ante cualquier situacion.",
        "pregunta": "¿Hoy respondi desde la conciencia o reaccione desde el automatico?"
    },
    "empatia": {
        "nombre": "EMPATIA",
        "definicion": "Resonancia consciente con limites claros. Sentir al otro sin perder tu centro.",
        "pregunta": "¿Hoy pude sentir al otro sin perderme a mi mismo?"
    }
}

def check_valores():
    """Devuelve las tres preguntas para auto-evaluacion diaria"""
    texto = "⚖️ *TUS VALORES HOY*\n\n"
    for v in VALORES.values():
        texto += f"*{v['nombre']}*\n{v['pregunta']}\n\n"
    return texto

# ============================================
# SISTEMA DE POLO OPUESTO (-9 a +9)
# ============================================

def explicar_polo_opuesto():
    return """📊 *ESCALA DE POLO OPUESTO (-9 a +9)*

Cada cualidad tiene su opuesto. La maestria es habitar conscientemente el rango completo.

Ejemplo:
-9 Miedo ............. 0 ............. +9 Amor
-9 Odio .............. 0 ............. +9 Aceptacion
-9 Pereza ............. 0 ............. +9 Disciplina

Hoy, ¿en que numero estas? No para juzgarte, sino para observar.
"""