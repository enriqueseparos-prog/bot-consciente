# src/confrontacion/modos.py 
# Modos de confrontacion con integracion de vibracion

MODOS = {
    "acompanante": {
        "nombre": "Acompanante",
        "tono": "suave, empatico, calido",
        "objetivo": "Contener y sostener",
        "frases_clave": [ 
            "Te escucho, ¿quieres contarme mas?",
            "Esta bien sentirse asi. ¿Que necesitas ahora?",        
            "No estas solo en esto. Estoy aqui."
        ]
    },
    "estoico": {
        "nombre": "Estoico",
        "tono": "directo, filosofico, desafiante",
        "objetivo": "Confrontar patrones",
        "frases_clave": [
            "Si no puedes cambiar lo que pasa, cambia como lo interpretas.",
            "El obstaculo es el camino.", 
            "No son las cosas las que te perturban, sino tu juicio sobre ellas."
        ]
    },
    "socratico": {
        "nombre": "Socratico",
        "tono": "pregunton, indagador, profundo",
        "objetivo": "Hacer pensar",
        "frases_clave": [
            "¿Que crees que pasaria si...?",
            "¿Que evidencia tienes de eso?",
            "Si un amigo estuviera en tu lugar, ¿que le dirias?"    
        ]
    },
    "confrontativo": {
        "nombre": "Confrontativo",
        "tono": "directo, sin rodeos, desafiante",
        "objetivo": "Sacudir al usuario de su estado",
        "frases_clave": [
            "¿Y si seguir asi no es una opcion?",
            "¿Cuanto tiempo mas vas a permitirte esto?",
            "El cambio no espera. ¿Que vas a hacer hoy distinto?",
            "La queja no construye. ¿Que accion concreta vas a tomar?"
        ]
    }
}

def elegir_modo(estado_usuario, patron_detectado, vibracion=None):
    """Elige el modo segun el estado, patron y vibracion"""
    
    # Si la vibracion es baja, usar modo confrontativo
    if vibracion and vibracion.get("vibracion") == "baja":
        return "confrontativo"
    
    # Logica original
    if patron_detectado and patron_detectado.get("tipo") == "baja_vibracion":
        if estado_usuario.get("estado") in ["tristeza", "ansiedad"]: 
            return "acompanante" 
        else:
            return "estoico"
    elif patron_detectado and patron_detectado.get("tipo") == "repeticion":
        return "socratico"
    else:
        return "acompanante"

def obtener_frase(modo):
    """Devuelve una frase aleatoria del modo elegido"""
    import random
    if modo in MODOS:
        frases = MODOS[modo]["frases_clave"]
        return random.choice(frases)
    else:
        return "Te escucho. ¿Que necesitas?"