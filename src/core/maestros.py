# src/core/maestros.py
# Maestros externos, internos y civilizaciones - Version sin acentos

# ============================================
# MAESTROS EXTERNOS (personas reales)
# ============================================

MAESTROS_EXTERNOS = {
    # ======== SALUD ========
    "frank suarez": {
        "nombre": "Frank Suarez",
        "area": "salud",
        "frase": "El metabolismo es la base de toda energia. Sin metabolismo sano, no hay habito que sostenga.",
        "practica": "Toma un vaso de agua con una pizca de sal al despertar.",
        "logros": "Metabolismo, hormonas, sueno, higado graso"
    },
    "nathaly marcus": {
        "nombre": "Nathaly Marcus",
        "area": "salud",
        "frase": "El ciclo hormonal femenino no es un problema a resolver, sino un ritmo a comprender.",
        "practica": "Observa en que fase de tu ciclo estas y ajusta tu energia.",
        "logros": "Ciclo hormonal, adrenales, inflamacion"
    },
    "ludwig johnson": {
        "nombre": "Ludwig Johnson",
        "area": "salud",
        "frase": "La insulina es la llave maestra del metabolismo. Controlala y controlaras tu energia.",
        "practica": "Ayuna 12 horas entre cena y desayuno.",
        "logros": "Insulina, ayuno, cetosis"
    },
    "barbara onely": {
        "nombre": "Barbara Onely",
        "area": "salud",
        "frase": "La empatia es una herramienta de sanacion, no solo una emocion.",
        "practica": "Escucha a alguien sin juzgar, solo sintiendo.",
        "logros": "Empatia sanadora, escucha corporal"
    },
    
    # ======== MENTE ========
    "vishen lakhiani": {
        "nombre": "Vishen Lakhiani",
        "area": "mente",
        "frase": "Las reglas culturales no son leyes. Puedes cuestionarlas y crear las tuyas.",
        "practica": "Escribe una regla que te impusieron y decide si la quieres mantener.",
        "logros": "Cuestionar reglas, experiencias cumbre, meditacion"
    },
    "lain garcia calvo": {
        "nombre": "Lain Garcia Calvo",
        "area": "mente",
        "frase": "La resistencia es ilusion. Lo que resistes, persiste.",
        "practica": "Observa que estas resistiendo hoy y sueltalo por un momento.",
        "logros": "No-dualidad, disolucion del ego"
    },
    "jim kwik": {
        "nombre": "Jim Kwik",
        "area": "mente",
        "frase": "El conocimiento no es poder. El conocimiento aplicado es poder.",
        "practica": "Usa el dedo para guiar la lectura y aumenta velocidad.",
        "logros": "Neuroplasticidad, memoria, enfoque"
    },
    "mario alonso puig": {
        "nombre": "Mario Alonso Puig",
        "area": "mente",
        "frase": "El miedo es un mal consejero. Detras del miedo siempre hay un deseo.",
        "practica": "Cuando sientas miedo, preguntate: ?que deseo esta detras?",
        "logros": "Miedos automaticos, neurociencia aplicada"
    },
    
    # ======== RELACIONES ========
    "marshall rosenberg": {
        "nombre": "Marshall Rosenberg",
        "area": "relaciones",
        "frase": "Detras de toda critica hay una necesidad no expresada.",
        "practica": "Hoy, cuando critiques a alguien, busca la necesidad detras.",
        "logros": "Comunicacion NoViolenta (CNV)"
    },
    "john gottman": {
        "nombre": "John Gottman",
        "area": "relaciones",
        "frase": "Los 4 jinetes del apocalipsis relacional: critica, desprecio, actitud defensiva y evasion.",
        "practica": "Identifica que jinete aparecio hoy en tus relaciones.",
        "logros": "Los 4 jinetes, terapia de pareja"
    },
    "carl rogers": {
        "nombre": "Carl Rogers",
        "area": "relaciones",
        "frase": "La aceptacion positiva incondicional es la base de toda relacion sanadora.",
        "practica": "Acepta a alguien hoy sin querer cambiarlo.",
        "logros": "Aceptacion positiva, psicologia humanista"
    },
    "thich nhat hanh": {
        "nombre": "Thich Nhat Hanh",
        "area": "relaciones",
        "frase": "El mayor regalo que puedes dar a alguien es tu presencia plena.",
        "practica": "Cuando hables con alguien hoy, deja el telefono y escucha.",
        "logros": "Mindfulness en relaciones, paz interior"
    },
    "bert hellinger": {
        "nombre": "Bert Hellinger",
        "area": "relaciones",
        "frase": "En cada familia hay un orden. Cuando lo respetas, el amor fluye.",
        "practica": "Honra a tus padres aunque no sean perfectos.",
        "logros": "Constelaciones familiares"
    },
    
    # ======== UNIVERSALES ========
    "salomon": {
        "nombre": "Rey Salomon",
        "area": "universal",
        "frase": "El discernimiento es saber cuando hablar y cuando callar.",
        "practica": "Antes de hablar hoy, preguntate: ?esto suma o resta?",
        "logros": "Sabiduria, gobierno interno"
    },
    "buda": {
        "nombre": "Buda",
        "area": "universal",
        "frase": "El deseo es la causa del sufrimiento. El desapego, la causa de la paz.",
        "practica": "Observa un deseo hoy sin actuar en el.",
        "logros": "Camino medio, desapego, compasion"
    },
    "jesus": {
        "nombre": "Jesus",
        "area": "universal",
        "frase": "Amaos los unos a los otros como yo os he amado.",
        "practica": "Hoy, haz algo por alguien sin esperar nada a cambio.",
        "logros": "Amor incondicional, servicio"
    },
    "lao tzu": {
        "nombre": "Lao Tzu",
        "area": "universal",
        "frase": "El que sabe no habla. El que habla no sabe.",
        "practica": "Actua hoy sin forzar, como el agua que fluye.",
        "logros": "Taoismo, Wu Wei"
    },
    "marie kondo": {
        "nombre": "Marie Kondo",
        "area": "universal",
        "frase": "Ordena tu espacio y ordenaras tu mente.",
        "practica": "Agradecele a un objeto antes de soltarlo.",
        "logros": "Metodo KonMari"
    },
    
    # ======== INVESTIGADORES ========
    "carl jung": {
        "nombre": "Carl Jung",
        "area": "mente",
        "frase": "Hasta que no hagas consciente tu inconsciente, este dirigira tu vida y lo llamaras destino.",
        "practica": "Preguntate: ?que sombra estoy proyectando hoy en otros?",
        "logros": "Sombra, arquetipos"
    },
    "joseph campbell": {
        "nombre": "Joseph Campbell",
        "area": "universal",
        "frase": "Sigue tu felicidad y el universo te abrira puertas donde solo habia muros.",
        "practica": "?Que te haria feliz hoy, asi sea por 5 minutos? Hazlo.",
        "logros": "El viaje del heroe"
    },
    "krishnamurti": {
        "nombre": "Jiddu Krishnamurti",
        "area": "mente",
        "frase": "La verdad es una tierra sin caminos.",
        "practica": "Observa un pensamiento sin juzgarlo, solo como testigo.",
        "logros": "Libertad psicologica"
    },
    "gurdjieff": {
        "nombre": "Gurdjieff",
        "area": "mente",
        "frase": "El hombre es una maquina. Todo ocurre. Nadie hace nada.",
        "practica": "Observa hoy cuantas veces actuas en automatico.",
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
        "practica": "Hoy, siente tus pies en el suelo y agradece tu cuerpo."
    },
    "bushido": {
        "nombre": "BUSHIDO",
        "viaje": "Cuerpo ? Mente",
        "frase": "La disciplina encarnada es el puente entre intencion y accion.",
        "practica": "Hoy, haz una cosa que sabes que debes hacer aunque no tengas ganas."
    },
    "sadhu": {
        "nombre": "SADHU",
        "viaje": "Cuerpo ? Alma",
        "frase": "El cuerpo es el templo donde el alma se expresa.",
        "practica": "Hoy, mueve tu cuerpo con devocion, como un ritual."
    },
    "estoico": {
        "nombre": "ESTOICO",
        "viaje": "Mente ? Cuerpo",
        "frase": "No son las cosas las que nos perturban, sino la opinion que tenemos de ellas.",
        "practica": "Hoy, ante una molestia, preguntate: ?esto depende de mi?"
    },
    "socrates": {
        "nombre": "SOCRATES",
        "viaje": "Mente ? Mente",
        "frase": "Solo se que no se nada. El cuestionamiento es el camino.",
        "practica": "Hoy, cuestiona una creencia que das por sentada."
    },
    "san francisco": {
        "nombre": "SAN FRANCISCO",
        "viaje": "Mente ? Alma",
        "frase": "Es dando que recibimos. El amor activo transforma.",
        "practica": "Hoy, haz algo bueno por alguien en silencio."
    },
    "tantrico": {
        "nombre": "TANTRICO",
        "viaje": "Alma ? Cuerpo",
        "frase": "Lo divino se encarna. El placer es sagrado.",
        "practica": "Hoy, permitete sentir placer en algo simple."
    },
    "maya": {
        "nombre": "MAYA",
        "viaje": "Alma ? Mente",
        "frase": "Todo tiene un patron. La sincronicidad es el lenguaje del alma.",
        "practica": "Hoy, presta atencion a las casualidades significativas."
    },
    "chaman": {
        "nombre": "CHAMAN",
        "viaje": "Alma ? Alma",
        "frase": "La conexion directa con lo sagrado es posible sin intermediarios.",
        "practica": "Hoy, conecta con algo mas grande que vos (naturaleza, universo, Dios)."
    }
}

# ============================================
# CIVILIZACIONES Y TRADICIONES
# ============================================

CIVILIZACIONES = {
    "filosofia china": {
        "nombre": "Filosofia China",
        "ensenanza": "El Yin-Yang, el I Ching y el Tao nos recuerdan que todo contiene su opuesto.",
        "practica": "Hoy, cuando enfrentes un conflicto, busca el punto medio."
    },
    "sabiduria andina": {
        "nombre": "Sabiduria Andina",
        "ensenanza": "El Ayni es la reciprocidad: dar y recibir en equilibrio con la vida.",
        "practica": "Hoy, agradece a la tierra (Pachamama) por lo que te da."
    },
    "cosmologia maya": {
        "nombre": "Cosmologia Maya",
        "ensenanza": "El tiempo es sagrado y ciclico. Cada dia tiene una energia unica.",
        "practica": "Observa que energia trae hoy para vos."
    },
    "tradicion hindu": {
        "nombre": "Tradicion Hindu",
        "ensenanza": "Los chakras son centros de energia que conectan cuerpo y espiritu.",
        "practica": "Hoy, enfocate en un chakra que sientas bloqueado."
    },
    "filosofia griega": {
        "nombre": "Filosofia Griega",
        "ensenanza": "El estoicismo nos ensena a distinguir lo que controlamos de lo que no.",
        "practica": "Hoy, acepta lo que no puedes cambiar y actua en lo que si."
    },
    "cristianismo mistico": {
        "nombre": "Cristianismo Mistico",
        "ensenanza": "La Trinidad es un reflejo de cuerpo, mente y alma en unidad.",
        "practica": "Hoy, busca coherencia entre lo que piensas, sientes y haces."
    },
    "budismo tibetano": {
        "nombre": "Budismo Tibetano",
        "ensenanza": "La compasion es el deseo de que todos los seres se liberen del sufrimiento.",
        "practica": "Hoy, desea bienestar a alguien que te cuesta."
    },
    "chamanismo": {
        "nombre": "Chamanismo",
        "ensenanza": "Todo tiene espiritu y todo esta conectado.",
        "practica": "Hoy, conecta con la naturaleza aunque sea 5 minutos."
    }
}

# ============================================
# FUNCION DE BUSQUEDA
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
    
    # Busqueda aproximada (contiene)
    for key, valor in {**MAESTROS_EXTERNOS, **MAESTROS_INTERNOS, **CIVILIZACIONES}.items():
        if nombre in key or key in nombre:
            return valor
    
    return None

def listar_maestros():
    """Devuelve listado de todos los maestros disponibles"""
    externos = list(MAESTROS_EXTERNOS.keys())
    internos = list(MAESTROS_INTERNOS.keys())
    civs = list(CIVILIZACIONES.keys())
    
    texto = "📚 *MAESTROS DISPONIBLES*\n\n"
    texto += "*Externos:*\n" + "\n".join([f"• {m.title()}" for m in externos[:10]]) + "\n\n"
    texto += "*Internos:*\n" + "\n".join([f"• {m.upper()}" for m in internos]) + "\n\n"
    texto += "*Civilizaciones:*\n" + "\n".join([f"• {c.title()}" for c in civs]) + "\n"
    return texto