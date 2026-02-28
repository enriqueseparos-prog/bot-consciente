# src/memoria/patrones.py - Detector de patrones semanales

import sqlite3
import os
from datetime import datetime, timedelta
from collections import Counter
import statistics

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'bot_data.db')

class DetectorPatrones:
    def __init__(self, user_id):
        self.user_id = user_id
    
    def _get_connection(self):
        return sqlite3.connect(DB_PATH)
    
    def patron_temas_semanales(self, dias=7):
        """Detecta qué temas se repiten en los últimos X días"""
        conn = self._get_connection()
        c = conn.cursor()
        
        fecha_limite = (datetime.now() - timedelta(days=dias)).strftime("%Y-%m-%d %H:%M:%S")
        
        c.execute('''
            SELECT tema, COUNT(*) as frecuencia
            FROM conversaciones
            WHERE user_id = ? AND fecha > ? AND tema IS NOT NULL
            GROUP BY tema
            ORDER BY frecuencia DESC
        ''', (self.user_id, fecha_limite))
        
        resultados = c.fetchall()
        conn.close()
        
        if not resultados:
            return None
        
        return {
            "top_temas": resultados[:3],
            "total_mensajes": sum(r[1] for r in resultados),
            "periodo": f"últimos {dias} días"
        }
    
    def patron_horario(self, dias=7):
        """Detecta a qué horas habla más el usuario"""
        conn = self._get_connection()
        c = conn.cursor()
        
        fecha_limite = (datetime.now() - timedelta(days=dias)).strftime("%Y-%m-%d %H:%M:%S")
        
        c.execute('''
            SELECT fecha FROM conversaciones
            WHERE user_id = ? AND fecha > ?
        ''', (self.user_id, fecha_limite))
        
        fechas = c.fetchall()
        conn.close()
        
        if not fechas:
            return None
        
        horas = []
        for (fecha_str,) in fechas:
            try:
                hora = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M").hour
                horas.append(hora)
            except:
                continue
        
        if not horas:
            return None
        
        # Agrupar por rangos
        rangos = {
            "madrugada (0-6)": 0,
            "mañana (6-12)": 0,
            "tarde (12-18)": 0,
            "noche (18-24)": 0
        }
        
        for h in horas:
            if h < 6:
                rangos["madrugada (0-6)"] += 1
            elif h < 12:
                rangos["mañana (6-12)"] += 1
            elif h < 18:
                rangos["tarde (12-18)"] += 1
            else:
                rangos["noche (18-24)"] += 1
        
        # Encontrar el rango más activo
        rango_activo = max(rangos, key=rangos.get)
        
        return {
            "horas": horas,
            "rango_mas_activo": rango_activo,
            "total_mensajes": len(horas)
        }
    
    def patron_estado_animo(self, dias=7):
        """Detecta tendencias en el estado de ánimo (checkins)"""
        conn = self._get_connection()
        c = conn.cursor()
        
        fecha_limite = (datetime.now() - timedelta(days=dias)).strftime("%Y-%m-%d %H:%M:%S")
        
        c.execute('''
            SELECT fecha, cuerpo, mente, alma FROM registros
            WHERE user_id = ? AND fecha > ?
            ORDER BY fecha
        ''', (self.user_id, fecha_limite))
        
        registros = c.fetchall()
        conn.close()
        
        if len(registros) < 3:
            return None
        
        # Calcular promedios
        cuerpos = [r[1] for r in registros]
        mentes = [r[2] for r in registros]
        almas = [r[3] for r in registros]
        
        # Detectar tendencia (si está mejorando o empeorando)
        def tendencia(valores):
            if len(valores) < 2:
                return "estable"
            if valores[-1] > valores[0]:
                return "mejorando"
            elif valores[-1] < valores[0]:
                return "empeorando"
            else:
                return "estable"
        
        return {
            "promedios": {
                "cuerpo": round(statistics.mean(cuerpos), 1),
                "mente": round(statistics.mean(mentes), 1),
                "alma": round(statistics.mean(almas), 1)
            },
            "tendencia": {
                "cuerpo": tendencia(cuerpos),
                "mente": tendencia(mentes),
                "alma": tendencia(almas)
            },
            "total_registros": len(registros)
        }
    
    def obtener_resumen_semanal(self):
        """Genera un resumen completo de patrones"""
        temas = self.patron_temas_semanales()
        horario = self.patron_horario()
        animo = self.patron_estado_animo()
        
        resumen = "📊 *RESUMEN DE PATRONES*\n\n"
        
        if temas:
            resumen += f"*Temas más hablados:*\n"
            for tema, freq in temas["top_temas"]:
                resumen += f"  • {tema}: {freq} veces\n"
            resumen += "\n"
        
        if horario:
            resumen += f"*Horario más activo:* {horario['rango_mas_activo']}\n"
            resumen += "\n"
        
        if animo:
            resumen += f"*Promedios:*\n"
            resumen += f"  • Cuerpo: {animo['promedios']['cuerpo']}/10 ({animo['tendencia']['cuerpo']})\n"
            resumen += f"  • Mente: {animo['promedios']['mente']}/10 ({animo['tendencia']['mente']})\n"
            resumen += f"  • Alma: {animo['promedios']['alma']}/10 ({animo['tendencia']['alma']})\n"
        
        return resumen


def obtener_resumen_patrones(user_id):
    """Función de acceso rápido para el bot"""
    detector = DetectorPatrones(user_id)
    return detector.obtener_resumen_semanal()