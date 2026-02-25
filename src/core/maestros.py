# src/core/maestros.py
# Maestros externos, internos y civilizaciones - Versión completa

# ============================================
# MAESTROS EXTERNOS (personas reales)
# ============================================

MAESTROS_EXTERNOS = {
    # ======== SALUD ========
    "frank suarez": {
        "nombre": "Frank Suárez",
        "area": "salud",
        "frase": "El metabolismo es la base de toda energía. Sin metabolismo sano, no hay hábito que sostenga.",
        "practica": "Tomá un vaso de agua con una pizca de sal al despertar.",
        "logros": "Metabolismo, hormonas, sueño, hígado graso"
    },
    "nathaly marcus": {
        "nombre": "Nathaly Marcus",
        "area": "salud",
        "frase": "El ciclo hormonal femenino no es un problema a resolver, sino un ritmo a comprender.",
        "practica": "Observá en qué fase de tu ciclo estás y ajustá tu energía.",
        "logros": "Ciclo hormonal, adrenales, inflamación"
    },
    "ludwig johnson": {
        "nombre": "Ludwig Johnson",
        "area": "salud",
        "frase": "La insulina es la llave maestra del metabolismo. Controlala y controlarás tu energía.",
        "practica": "Ayuná 12 horas entre cena y desayuno.",
        "logros": "Insulina, ayuno, cetosis"
    },
    "barbara onely": {
        "nombre": "Barbara Onely",
        "area": "salud",
        "frase": "La empatía es una herramienta de sanación, no solo una emoción.",
        "practica": "Escuchá a alguien sin juzgar, solo sintiendo.",
        "logros": "Empatía sanadora, escucha corporal"
    },
    
    # ======== MENTE ========
    "vishen lakhiani": {
        "nombre": "Vishen Lakhiani",
        "area": "mente",
        "frase": "Las reglas culturales no son leyes. Podés cuestionarlas y crear las tuyas.",
        "practica": "Escribí una regla que te impusieron y decidí si la querés mantener.",
        "logros": "Cuestionar reglas, experiencias cumbre, meditación"
    },
    "lain garcia calvo": {
        "nombre": "Laín García Calvo",
        "area": "mente",
        "frase": "La resistencia es ilusión. Lo que resistes, persiste.",
        "practica": "Observá qué estás resistiendo hoy y soltalo por un momento.",
        "logros": "No-dualidad, disolución del ego"
    },
    "jim kwik": {
        "nombre": "Jim Kwik",
        "area": "mente",
        "frase": "El conocimiento no es poder. El conocimiento aplicado es poder.",
        "practica": "Usá el dedo para guiar la lectura y aumentá velocidad.",
        "logros": "Neuroplasticidad, memoria, enfoque"
    },
    "mario alonso puig": {
        "nombre": "Mario Alonso Puig",
        "area": "mente",
        "frase": "El miedo es un mal consejero. Detrás del miedo siempre hay un deseo.",
        "practica": "Cuando sientas miedo, preguntate: ¿qué deseo está detrás?",
        "logros": "Miedos automáticos, neurociencia aplicada"
    },
    
    # ======== RELACIONES ========
    "marshall rosenberg": {
        "nombre": "Marshall Rosenberg",
        "area": "relaciones",
        "frase": "Detrás de toda crítica hay una necesidad no expresada.",
        "practica": "Hoy, cuando critiques a alguien, buscá la necesidad detrás.",
        "logros": "Comunicación NoViolenta (CNV)"
    },
    "john gottman": {
        "nombre": "John Gottman",
        "area": "relaciones",
        "frase": "Los 4 jinetes del apocalipsis relacional: crítica, desprecio, actitud defensiva y evasión.",
        "practica": "Identificá qué jinete apareció hoy en tus relaciones.",
        "logros": "Los 4 jinetes, terapia de pareja"
    },
    "carl rogers": {
        "nombre": "Carl Rogers",
        "area": "relaciones",
        "frase": "La aceptación positiva incondicional es la base de toda relación sanadora.",
        "practica": "Aceptá a alguien hoy sin querer cambiarlo.",
        "logros": "Aceptación positiva, psicología humanista"
    },
    "thich nhat hanh": {
        "nombre": "Thich Nhat Hanh",
        "area": "relaciones",
        "frase": "El mayor regalo que puedes dar a alguien es tu presencia plena.",
        "practica": "Cuando hables con alguien hoy, dejá el teléfono y escuchá.",
        "logros": "Mindfulness en relaciones, paz interior"
    },
    "bert hellinger": {
        "nombre": "Bert Hellinger",
        "area": "relaciones",
        "frase": "En cada familia hay un orden. Cuando lo respetas, el amor fluye.",
        "practica": "Honrá a tus padres aunque no sean perfectos.",
        "logros": "Constelaciones familiares"
    },
    
    # ======== UNIVERSALES ========
    "salomon": {
        "nombre": "Rey Salomón",
        "area": "universal",
        "frase": "El discernimiento es saber cuándo hablar y cuándo callar.",
        "practica": "Antes de hablar hoy, preguntate: ¿esto suma o resta?",
        "logros": "Sabiduría, gobierno interno"
    },
    "buda": {
        "nombre": "Buda",
        "area": "universal",
        "frase": "El deseo es la causa del sufrimiento. El desapego, la causa de la paz.",
        "practica": "Observá un deseo hoy sin actuar en él.",
        "logros": "Camino medio, desapego, compasión"
    },
    "jesus": {
        "nombre": "Jesús",
        "area": "universal",
        "frase": "Amaos los unos a los otros como yo os he amado.",
        "practica": "Hoy, hacé algo por alguien sin esperar nada a cambio.",
        "logros": "Amor incondicional, servicio"
    },
    "lao tzu": {
        "nombre": "Lao Tzu",
        "area": "universal",
        "frase": "El que sabe no habla. El que habla no sabe.",
        "practica": "Actuá hoy sin forzar, como el agua que fluye.",
        "logros": "Taoísmo, Wu Wei"
    },
    "marie kondo": {
        "nombre": "Marie Kondo",
        "area": "universal",
        "frase": "Ordena tu espacio y ordenarás tu mente.",
        "practica": "Agradécele a un objeto antes de soltarlo.",
        "logros": "Método KonMari"
    },
    
    # ======== INVESTIGADORES ========
    "carl jung": {
        "nombre": "Carl Jung",
        "area": "mente",
        "frase": "Hasta que no hagas consciente tu inconsciente, este dirigirá tu vida y lo llamarás destino.",
        "practica": "Preguntate: ¿qué sombra estoy proyectando hoy en otros?",
        "logros": "Sombra, arquetipos"
    },
    "joseph campbell": {
        "nombre": "Joseph Campbell",
        "area": "universal",
        "frase": "Sigue tu felicidad y el universo te abrirá puertas donde solo había muros.",
        "practica": "¿Qué te haría feliz hoy, así sea por 5 minutos? Hacelo.",
        "logros": "El viaje del héroe"
    },
    "krishnamurti": {
        "nombre": "Jiddu Krishnamurti",
        "area": "mente",
        "frase": "La verdad es una tierra sin caminos.",
        "practica": "Observá un pensamiento sin juzgarlo, solo como testigo.",
        "logros": "Libertad psicológica"
    },
    "gurdjieff": {
        "nombre": "Gurdjieff",
        "area": "mente",
        "frase": "El hombre es una máquina. Todo ocurre. Nadie hace nada.",
        "practica": "Observá hoy cuántas veces actuás en automático.",
        "logros": "Cuarto camino"
    }
}

# ============================================
# MAESTROS INTERNOS (9 arquetipos)
# ============================================

MAESTROS_INTERNOS = {
    "inca": {
        "nombre": "INCA",
        "viaje": "Cuerpo ? Cuerpo",
        "frase": "Mi cuerpo es territorio sagrado. Lo honro con presencia.",
        "practica": "Hoy, sentí tus pies en el suelo y agradecé tu cuerpo."
    },
    "bushido": {
        "nombre": "BUSHIDO",
        "viaje": "Cuerpo ? Mente",
        "frase": "La disciplina encarnada es el puente entre intención y acción.",
        "practica": "Hoy, hacé una cosa que sabés que debés hacer aunque no tengas ganas."
    },
    "sadhu": {
        "nombre": "SADHU",
        "viaje": "Cuerpo ? Alma",
        "frase": "El cuerpo es el templo donde el alma se expresa.",
        "practica": "Hoy, mové tu cuerpo con devoción, como un ritual."
    },
    "estoico": {
        "nombre": "ESTOICO",
        "viaje": "Mente ? Cuerpo",
        "frase": "No son las cosas las que nos perturban, sino la opinión que tenemos de ellas.",
        "practica": "Hoy, ante una molestia, preguntate: ¿esto depende de mí?"
    },
    "socrates": {
        "nombre": "SÓCRATES",
        "viaje": "Mente ? Mente",
        "frase": "Solo sé que no sé nada. El cuestionamiento es el camino.",
        "practica": "Hoy, cuestioná una creencia que das por sentada."
    },
    "san francisco": {
        "nombre": "SAN FRANCISCO",
        "viaje": "Mente ? Alma",
        "frase": "Es dando que recibimos. El amor activo transforma.",
        "practica": "Hoy, hacé algo bueno por alguien en silencio."
    },
    "tantrico": {
        "nombre": "TÁNTRICO",
        "viaje": "Alma ? Cuerpo",
        "frase": "Lo divino se encarna. El placer es sagrado.",
        "practica": "Hoy, permitite sentir placer en algo simple."
    },
    "maya": {
        "nombre": "MAYA",
        "viaje": "Alma ? Mente",
        "frase": "Todo tiene un patrón. La sincronicidad es el lenguaje del alma.",
        "practica": "Hoy, prestá atención a las casualidades significativas."
    },
    "chaman": {
        "nombre": "CHAMÁN",
        "viaje": "Alma ? Alma",
        "frase": "La conexión directa con lo sagrado es posible sin intermediarios.",
        "practica": "Hoy, conectá con algo más grande que vos (naturaleza, universo, Dios)."
    }
}

# ============================================
# CIVILIZACIONES Y TRADICIONES
# ============================================

CIVILIZACIONES = {
    "filosofia china": {
        "nombre": "Filosofía China",
        "enseñanza": "El Yin-Yang, el I Ching y el Tao nos recuerdan que todo contiene su opuesto.",
        "practica": "Hoy, cuando enfrentes un conflicto, buscá el punto medio."
    },
    "sabiduria andina": {
        "nombre": "Sabiduría Andina",
        "enseñanza": "El Ayni es la reciprocidad: dar y recibir en equilibrio con la vida.",
        "practica": "Hoy, agradecé a la tierra (Pachamama) por lo que te da."
    },
    "cosmologia maya": {
        "nombre": "Cosmología Maya",
        "enseñanza": "El tiempo es sagrado y cíclico. Cada día tiene una energía única.",
        "practica": "Observá qué energía trae hoy para vos."
    },
    "tradicion hindu": {
        "nombre": "Tradición Hindú",
        "enseñanza": "Los chakras son centros de energía que conectan cuerpo y espíritu.",
        "practica": "Hoy, enfocate en un chakra que sientas bloqueado."
    },
    "filosofia griega": {
        "nombre": "Filosofía Griega",
        "enseñanza": "El estoicismo nos enseña a distinguir lo que controlamos de lo que no.",
        "practica": "Hoy, aceptá lo que no podés cambiar y actuá en lo que sí."
    },
    "cristianismo místico": {
        "nombre": "Cristianismo Místico",
        "enseñanza": "La Trinidad es un reflejo de cuerpo, mente y alma en unidad.",
        "practica": "Hoy, buscá coherencia entre lo que pensás, sentís y hacés."
    },
    "budismo tibetano": {
        "nombre": "Budismo Tibetano",
        "enseñanza": "La compasión es el deseo de que todos los seres se liberen del sufrimiento.",
        "practica": "Hoy, deseale bienestar a alguien que te cuesta."
    },
    "chamanismo": {
        "nombre": "Chamanismo",
        "enseñanza": "Todo tiene espíritu y todo está conectado.",
        "practica": "Hoy, conectá con la naturaleza aunque sea 5 minutos."
    }
}

# ============================================
# FUNCIÓN DE BÚSQUEDA
# ============================================

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
    
    # Búsqueda aproximada (contiene)
    for key, valor in {**MAESTROS_EXTERNOS, **MAESTROS_INTERNOS, **CIVILIZACIONES}.items():
        if nombre in key or key in nombre:
            return valor
    
    return None

def listar_maestros():
    """Devuelve listado de todos los maestros disponibles"""
    externos = list(MAESTROS_EXTERNOS.keys())
    internos = list(MAESTROS_INTERNOS.keys())
    civs = list(CIVILIZACIONES.keys())
    
    texto = "?? *MAESTROS DISPONIBLES*\n\n"
    texto += "*Externos:*\n" + "\n".join([f"• {m.title()}" for m in externos[:10]]) + "\n\n"
    texto += "*Internos:*\n" + "\n".join([f"• {m.upper()}" for m in internos]) + "\n\n"
    texto += "*Civilizaciones:*\n" + "\n".join([f"• {c.title()}" for c in civs]) + "\n"
    return texto