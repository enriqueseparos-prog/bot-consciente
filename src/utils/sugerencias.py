# src/utils/sugerencias.py - Sistema de sugerencias proactivas

import sqlite3
import os
from datetime import datetime, timedelta
import random

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'bot_data.db')

class SugerenciasProactivas:
    def __init__(self):
        self._init_db()
    
    def _init_db(self):
        """Crea la tabla de sugerencias si no existe"""
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS sugerencias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                tipo TEXT,
                sugerencia TEXT,
                respondida INTEGER DEFAULT 0,
                utilidad INTEGER
            )
        ''')
        conn.commit()
        conn.close()
    
    def detectar_momento_para_sugerir(self, user_id):
        """Detecta si es buen momento para sugerir algo"""
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        c.execute('''
            SELECT fecha FROM conversaciones 
            WHERE user_id = ? 
            ORDER BY fecha DESC LIMIT 1
        ''', (user_id,))
        
        ultima = c.fetchone()
        if not ultima:
            conn.close()
            return False
        
        ultima_fecha = datetime.strptime(ultima[0], "%Y-%m-%d %H:%M")
        horas_desde_ultima = (datetime.now() - ultima_fecha).total_seconds() / 3600
        
        conn.close()
        return horas_desde_ultima > 2
    
    def sugerir_segun_historial(self, user_id):
        """Genera una sugerencia basada en el historial"""
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        c.execute('''
            SELECT tema, COUNT(*) as frecuencia 
            FROM conversaciones 
            WHERE user_id = ? AND tema IS NOT NULL
            GROUP BY tema 
            ORDER BY frecuencia DESC 
            LIMIT 3
        ''', (user_id,))
        
        temas_frecuentes = c.fetchall()
        conn.close()
        
        if not temas_frecuentes:
            return None
        
        tema = random.choice(temas_frecuentes)[0]
        
        sugerencias = {
            "hijo": "¿Cómo va la relación con tu hijo? ¿Hay algo en lo que pueda ayudarte?",
            "pareja": "Hace un tiempo hablamos de tu pareja. ¿Cómo están ahora?",
            "cuerpo": "¿Cómo viene tu entrenamiento? ¿Necesitás ajustar algo?",
            "mente": "¿Seguís trabajando en tus hábitos mentales?",
            "alma": "¿Cómo anda tu conexión espiritual estos días?",
            "trabajo": "¿Cómo va la barbería? ¿Algún desafío nuevo?",
            "habitos": "Recordá que podés usar /microdosis para cualquier hábito"
        }
        
        return sugerencias.get(tema, "¿Cómo vienen tus días? ¿Querés retomar algún tema?")
    
    def sugerir_horario(self, user_id):
        """Sugiere según la hora del día"""
        hora = datetime.now().hour
        
        if hora < 12:
            return "🌅 Buenos días. ¿Qué tal si arrancamos con un /checkin?"
        elif hora < 19:
            return "☀️ Buenas tardes. ¿Cómo va tu día? ¿Necesitás algo?"
        else:
            return "🌙 Buenas noches. ¿Querés hacer un repaso del día con /checkin?"
    
    def obtener_sugerencia(self, user_id):
        """Obtiene una sugerencia apropiada para el usuario"""
        if self.detectar_momento_para_sugerir(user_id):
            if random.random() < 0.7:
                return self.sugerir_segun_historial(user_id)
            else:
                return self.sugerir_horario(user_id)
        return None


def obtener_sugerencia_proactiva(user_id):
    sistema = SugerenciasProactivas()
    return sistema.obtener_sugerencia(user_id)