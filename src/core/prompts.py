# ============================================
# PROMPT D - BIOGRAFÍA DE MAESTROS
# ============================================

PROMPT_BIOGRAFIA = """Actúa como un biógrafo especializado en sabiduría ancestral, filosofía perenne y desarrollo personal. Tu tarea es generar una BIOGRAFÍA CONSCIENTE COMPLETA sobre: {tema}

[CONTEXTO OBLIGATORIO]
Esta biografía debe servir como material de estudio para un sistema de desarrollo personal que integra cuerpo, mente y alma. Debe ser práctica, profunda y aplicable.

ESTRUCTURA OBLIGATORIA (10 PARTES):

PARTE 1: BIOGRAFÍA CONSCIENTE
- Trayectoria vital completa (fechas clave, lugares, contextos)
- Crisis transformadoras y puntos de inflexión
- Evolución de su pensamiento a lo largo de los años
- Obras principales y legado

PARTE 2: MAPA COMPLETO DEL SISTEMA
- Principios fundamentales de su enseñanza
- Conceptos clave (definiciones precisas)
- Modelos y estructuras que creó
- Vocabulario específico que utilizaba

PARTE 3: HERRAMIENTAS PRÁCTICAS
- Técnicas principales (con nombres originales)
- Protocolos paso a paso
- Ejercicios que se pueden aplicar hoy
- Prácticas diarias recomendadas

PARTE 4: PATRONES DE SUPERACIÓN
- Mecanismos de inseguridad que identificaba
- Estrategias que enseñaba para desarrollar confianza
- Cómo enfrentaba la adversidad
- Lecciones sobre la resiliencia

PARTE 5: CONEXIÓN CON EL SISTEMA CONSCIENTE
- ¿Con qué maestros internos resuena? (INCA, BUSHIDO, etc.)
- Aplicación en los 4 Cubos (interior/exterior, positivo/negativo)
- ¿En qué dominio aporta más? (Cuerpo/Mente/Alma)
- ¿Cómo integrar sus enseñanzas en la vida cotidiana?

PARTE 6: ÍNDICE AUTO-GUIADO
- Temas principales de su obra
- Ruta de aprendizaje recomendada (por dónde empezar)
- Preguntas para la reflexión personal
- Lecturas esenciales

PARTE 7: CRÍTICAS Y LIMITACIONES
- Principales críticas a su obra
- Limitaciones de su enfoque
- Contexto histórico que puede haber sesgado sus ideas
- Cómo complementar con otros maestros

PARTE 8: FRASES CLAVE Y MANTRA PERSONAL
- 10 frases fundamentales (con contexto)
- Un mantra o afirmación inspirada en su enseñanza
- Palabras que definen su legado

PARTE 9: APLICACIÓN EN EL SIGLO XXI
- ¿Cómo aplicarían sus enseñanzas hoy?
- Adaptación a la vida moderna
- Tecnología y tradición
- Relevancia actual

PARTE 10: DECISIÓN DEL ARQUITECTO
- Prioridad #1 por nivel (BRONCE/PLATA/ORO)
- Error #1 que comete la gente al estudiar este maestro
- Resolución de contradicciones aparentes

[PERFILES DE USUARIO - INCLUIR EN CADA PARTE CUANDO CORRESPONDA]
- BRONCE: Quien se acerca por primera vez a este maestro
- PLATA: Quien ya conoce lo básico y busca profundizar
- ORO: Quien quiere encarnar la maestría

[REGLAS DE FORMATO]
- Usa TABLAS para información densa (máximo 4-5 columnas)
- Incluye fechas concretas siempre que sea posible
- Prioriza NÚMEROS y RANGOS sobre descripciones vagas
- Sé directo: cada palabra debe aportar información útil

[INSTRUCCIÓN DE TONO]
Cuando generes esta biografía, hacelo con un tono respetuoso, profundo y a la vez accesible. Como si le hablaras a un discípulo que quiere aprender de este maestro. Incluye anécdotas que humanicen al personaje y que permitan conectar emocionalmente con su enseñanza.
"""
# ============================================
# FUNCIÓN PARA ELEGIR PROMPT
# ============================================

def elegir_prompt(tema, tipo="auto"):
    """Elige el prompt según el tema y tipo"""
    temas_tecnicos = ["flexibilidad", "fuerza", "dieta", "memoria", "decisiones", "lectura", "muay thai", "descanso", "hidratación", "hipertrofia", "calistenia", "cardio"]
    temas_empaticos = ["relacion", "hijo", "pareja", "familia", "emocion", "pnl", "reiki", "gestion", "meditación", "proposito", "eneagrama"]
    temas_biografia = ["frank suarez", "marshall rosenberg", "jim kwik", "buda", "jesús", "lao tzu", "carl jung", "joseph campbell", "salomon", "gurdjieff", "krishnamurti", "nathaly marcus", "ludwig johnson", "thich nhat hanh", "john gottman", "carl rogers"]
    
    if tipo == "tecnico":
        return PROMPT_TECNICO
    elif tipo == "empatico":
        return PROMPT_EMPATICO
    elif tipo == "biografia":
        return PROMPT_BIOGRAFIA
    else:
        # Auto-detección
        tema_lower = tema.lower()
        if any(t in tema_lower for t in temas_empaticos):
            return PROMPT_EMPATICO
        elif any(t in tema_lower for t in temas_biografia):
            return PROMPT_BIOGRAFIA
        else:
            return PROMPT_TECNICO