# src/utils/feedback.py - Sistema de feedback loop

import sqlite3
import os
from datetime import datetime, timedelta

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'bot_data.db')

def init_feedback_table():
    """Crea la tabla de feedback si no existe"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
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

def guardar_sugerencia(user_id, sugerencia):
    """Guarda una sugerencia para preguntar después si sirvió"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        INSERT INTO feedback (user_id, fecha_envio, sugerencia)
        VALUES (?, ?, ?)
    ''', (user_id, datetime.now(), sugerencia))
    conn.commit()
    conn.close()

def obtener_pendientes(horas=2):
    """Obtiene feedbacks pendientes de responder después de X horas"""
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

def registrar_respuesta(feedback_id, respuesta_texto, utilidad):
    """Registra la respuesta del usuario"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        UPDATE feedback
        SET fecha_respuesta = ?, respuesta = ?, utilidad = ?, contestado = 1
        WHERE id = ?
    ''', (datetime.now(), respuesta_texto, utilidad, feedback_id))
    conn.commit()
    conn.close()

def obtener_estadisticas(user_id):
    """Obtiene estadísticas de feedback para un usuario"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        SELECT COUNT(*), AVG(utilidad) FROM feedback
        WHERE user_id = ? AND contestado = 1
    ''', (user_id,))
    total, promedio = c.fetchone()
    conn.close()
    return {
        "total": total or 0,
        "promedio": round(promedio, 1) if promedio else 0
    }

def ajustar_frecuencia_segun_feedback(user_id):
    """Sugiere si hay que aumentar o disminuir frecuencia de sugerencias"""
    stats = obtener_estadisticas(user_id)
    if stats["total"] < 5:
        return "normal"  # Pocos datos, mantener frecuencia
    if stats["promedio"] >= 8:
        return "aumentar"  # Le sirve mucho, podemos sugerir más
    if stats["promedio"] <= 3:
        return "disminuir"  # No le sirve, mejor menos
    return "normal"

# Inicializar tabla al importar
init_feedback_table()