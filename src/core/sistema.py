# src/core/sistema.py
# Sistema Operativo de Encarnación Consciente v3.1

# ============================================
# FILOSOFÍA CENTRAL
# ============================================

CREADOR_SOBERANO = "Eres el creador soberano de tu realidad. Tu poder reside en la coherencia dinámica entre Pensamiento-Emoción-Acción."

PRINCIPIO_TRINITARIO = "Cuerpo, Mente y Alma están siempre presentes como tres expresiones del mismo flujo consciente."

PRINCIPIO_ESPEJO = """
INTERIOR = EXTERIOR
Cuerpo ? Salud
Mente ? Finanzas/Negocios
Alma ? Relaciones
"""

# ============================================
# VALORES PRINCIPALES
# ============================================

VALORES = [
    "DISCIPLINA: Fuerza de coherencia interna que mantiene tu rumbo",
    "RESPONSABILIDAD: Capacidad de responder creativamente ante cualquier situación",
    "EMPATÍA: Resonancia consciente con límites claros"
]

# ============================================
# TRINIDAD DE SEMILLAS
# ============================================

SEMILLAS = {
    "ORQUESTADOR": "Visión panorámica y coherencia global",
    "MEGA": "Investigación profunda y expansión",
    "CREACIÓN": "Materialización consciente"
}

# ============================================
# CUBOS CONSCIENTES (27x27)
# ============================================

CUBOS = {
    "interior_positivo": "Pensamiento-Emoción-Acción en coherencia",
    "exterior_positivo": "Salud-Negocios-Relaciones en armonía",
    "interior_negativo": "Sombras como sistema inmunológico",
    "exterior_negativo": "Conflictos como campo de maestría"
}

def estado_en_cubo(pensamiento, emocion, accion):
    """Clasifica el estado actual en un cubo"""
    if pensamiento > 7 and emocion > 7 and accion > 7:
        return "interior_positivo"
    elif pensamiento < 4 and emocion < 4 and accion < 4:
        return "interior_negativo"
    else:
        return "zona_de_crecimiento"

# ============================================
# PROTOCOLO DE RESCATE (versión texto)
# ============================================

PROTOCOLO_RESCATE_TEXTO = """
?? PROTOCOLO DE RESCATE (3 minutos)

Minuto 1 - Guerrero:
   Anclate en el cuerpo. Respirá. Sentí tus pies.

Minuto 2 - Mago:
   Soltá la emoción estancada. Exhalá profundo.

Minuto 3 - Arquero:
   Definí UNA acción concreta. Hacela.
"""

# ============================================
# SISTEMA DE POLO OPUESTO
# ============================================

def polo_opuesto(cualidad, valor):
    """Devuelve el polo opuesto de una cualidad"""
    opuestos = {
        "miedo": "amor",
        "odio": "aceptacion",
        "pereza": "disciplina",
        "duda": "certeza"
    }
    return opuestos.get(cualidad.lower(), "desconocido")

# ============================================
# DIAGNÓSTICO INICIAL
# ============================================

DIAGNOSTICO_INICIAL = {
    "alma": 3,
    "cuerpo": 2,
    "mente": 1
}

def obtener_diagnostico():
    return f"""
    ?? DIAGNÓSTICO INICIAL
    Alma: nivel {DIAGNOSTICO_INICIAL['alma']} (vibra alto)
    Cuerpo: nivel {DIAGNOSTICO_INICIAL['cuerpo']} (funcional)
    Mente: nivel {DIAGNOSTICO_INICIAL['mente']} (por entrenar)
    """