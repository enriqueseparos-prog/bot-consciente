# src/utils/feedback.py - Sistema de feedback loop

import sqlite3
import os
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'bot_data.db')

class FeedbackLoop:
    def __init__(self):
        self._init_db()
    
    def _init_db(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS feedback (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                fecha_respuesta TIMESTAMP,
                sugerencia TEXT,
                respuesta TEXT,
                utilidad INTEGER,
                contestado INTEGER DEFAULT 0
            )
        ''')
        conn.commit()
        conn.close()
    
    def guardar_sugerencia(self, user_id, sugerencia):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            INSERT INTO feedback (user_id, fecha_envio, sugerencia)
            VALUES (?, ?, ?)
        ''', (user_id, datetime.now(), sugerencia))
        conn.commit()
        conn.close()
    
    def obtener_pendientes(self, horas=2):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        fecha_limite = (datetime.now() - timedelta(hours=horas)).strftime("%Y-%m-%d %H:%M:%S")
        c.execute('''
            SELECT id, user_id, sugerencia FROM feedback
            WHERE contestado = 0 AND fecha_envio < ?
        ''', (fecha_limite,))
        pendientes = c.fetchall()
        conn.close()
        return pendientes
    
    def registrar_respuesta(self, feedback_id, respuesta_texto, utilidad):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            UPDATE feedback
            SET fecha_respuesta = ?, respuesta = ?, utilidad = ?, contestado = 1
            WHERE id = ?
        ''', (datetime.now(), respuesta_texto, utilidad, feedback_id))
        conn.commit()
        conn.close()

feedback_loop = FeedbackLoop()