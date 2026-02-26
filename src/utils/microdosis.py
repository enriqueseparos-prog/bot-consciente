# -*- coding: utf-8 -*-
# src/utils/microdosis.py
# Versiones minimas de habitos para cuando no hay tiempo - Version sin acentos

MICRODOSIS = {
    # HABITOS BASE
    "relacion con hijo": "Mira a tu hijo a los ojos y dile 'te quiero' o preguntale algo con genuino interes. 30 segundos.",
    "relacion con pareja": "Un abrazo de 10 segundos sin hablar. Solo presencia.",
    "relacion con familiares": "Envia un mensaje corto a un familiar que hace tiempo no contactas.",
    "tareas del hogar": "Ordena UNA cosa (la cama, los platos, una silla). 2 minutos.",
    
    # HABITOS DE CUERPO
    "flexibilidad": "Estira un brazo 10 segundos mientras respiras. Cambia de lado.",
    "muay thai": "Sombra boxing 1 minuto. Sin tecnica, solo mover el cuerpo.",
    "descanso": "Cierra los ojos 60 segundos. Respira profundo.",
    "hidratacion": "Toma un vaso de agua AHORA.",
    "dieta proteica": "En tu proxima comida, asegurate de que haya proteina.",
    "hipertrofia": "5 flexiones de brazos. Sin excusas.",
    "calistenia": "3 sentadillas. Siente las piernas.",
    "medicion": "Pesate o tomate una medida rapida.",
    "cardio": "Sube y baja una escalera o camina rapido 2 minutos.",
    
    # HABITOS DE MENTE
    "estoicismo": "Preguntate: ¿esto que me preocupa depende de mi?",
    "memoria": "Intenta recordar 3 cosas que hiciste ayer.",
    "eneagrama": "Observa una reaccion tuya y preguntate: ¿que tipo se activo?",
    "sombra": "Escribe una emocion que hoy escondiste.",
    "estructura": "Haz una lista de 3 cosas pendientes. Ordenalas.",
    "toma de decisiones": "Elige entre A o B en 10 segundos. No pienses.",
    "lectura veloz": "Lee un parrafo con el dedo guia.",
    
    # HABITOS DE ALMA
    "reiki": "Pon las manos en tu corazon y respira. 1 minuto.",
    "gestion emocional": "Identifica la emocion del momento y nombrala.",
    "meditacion": "3 respiraciones conscientes. Ahora.",
    "proposito": "Preguntate: ¿que quiero hoy? Una palabra.",
    "pnl": "Cambia tu postura fisica por 30 segundos. Nota como cambia tu animo.",
    "gratitud": "Nombra UNA cosa que hoy no salio mal.",
    "disciplina": "Haz una cosa que postergabas. 2 minutos.",
    "desapego": "Suelta una expectativa. Solo por hoy."
}

def obtener_microdosis(habito):
    """Devuelve la microdosis para un habito especifico"""
    habito_lower = habito.lower()
    
    # Busqueda directa
    if habito_lower in MICRODOSIS:
        return MICRODOSIS[habito_lower]
    
    # Busqueda aproximada (por si el nombre no coincide exactamente)
    for clave, valor in MICRODOSIS.items():
        if clave in habito_lower or habito_lower in clave:
            return valor
    
    return "Respira profundo 3 veces y preguntate: ¿que necesito ahora?"

def obtener_microdosis_aleatoria():
    """Devuelve una microdosis al azar"""
    import random
    habito = random.choice(list(MICRODOSIS.keys()))
    return f"🧠 *Microdosis para '{habito}':*\n{MICRODOSIS[habito]}"