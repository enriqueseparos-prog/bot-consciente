# src/puntos_14/grupo4.py
# Puntos 10-12: Gratitud, Disciplina, Desapego - Version sin acentos

def punto10_gratitud(contexto=None):
    """Combustible del alma"""
    frases = [
        "La gratitud transforma lo que tienes en suficiente.",
        "Agradece hasta lo pequeño, y crecera.",
        "Un corazon agradecido atrae bendiciones.",
        "Hoy, ¿que tres cosas agradeces?"
    ]
    import random
    return random.choice(frases)

def punto11_disciplina(contexto=None):
    """Cuerpo diciendo si"""
    frases = [
        "La disciplina es el puente entre metas y logros.",
        "Haz lo que debes, cuando debes, estes como estes.",
        "La motivacion va y viene. La disciplina permanece.",
        "Un poco de disciplina cada dia, mucho resultado cada mes."
    ]
    import random
    return random.choice(frases)

def punto12_desapego(contexto=None):
    """No depender del resultado"""
    frases = [
        "Hazlo por amor, no por el resultado.",
        "El desapego no es indiferencia, es libertad.",
        "Suelta el fruto y cuida la raiz.",
        "Lo que esperas, te ata. Lo que vives, te libera."
    ]
    import random
    return random.choice(frases)