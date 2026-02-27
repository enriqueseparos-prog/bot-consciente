"""
entidades.py - Memoria de relaciones semánticas
"""

import sqlite3
import os
from typing import Optional, List, Tuple

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'bot_data.db')

class EntidadesMemory:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self._init_db()
    
    def _init_db(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS entidades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                clave TEXT NOT NULL,
                valor TEXT NOT NULL,
                contexto TEXT,
                veces_usado INTEGER DEFAULT 1,
                ultima_vez TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(user_id, clave, valor)
            )
        ''')
        conn.commit()
        conn.close()
    
    def recordar(self, clave: str, valor: str, contexto: Optional[str] = None):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        c.execute('''
            SELECT veces_usado FROM entidades 
            WHERE user_id = ? AND clave = ? AND valor = ?
        ''', (self.user_id, clave.lower().strip(), valor))
        
        resultado = c.fetchone()
        
        if resultado:
            c.execute('''
                UPDATE entidades 
                SET veces_usado = ?, ultima_vez = CURRENT_TIMESTAMP
                WHERE user_id = ? AND clave = ? AND valor = ?
            ''', (resultado[0] + 1, self.user_id, clave.lower().strip(), valor))
        else:
            c.execute('''
                INSERT INTO entidades (user_id, clave, valor, contexto)
                VALUES (?, ?, ?, ?)
            ''', (self.user_id, clave.lower().strip(), valor, contexto))
        
        conn.commit()
        conn.close()
    
    def buscar(self, clave: str) -> Optional[str]:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        c.execute('''
            SELECT valor FROM entidades 
            WHERE user_id = ? AND clave = ?
            ORDER BY veces_usado DESC, ultima_vez DESC
            LIMIT 1
        ''', (self.user_id, clave.lower().strip()))
        
        resultado = c.fetchone()
        conn.close()
        
        if resultado:
            return resultado[0]
        return None
    
    def detectar_entidades_en_texto(self, texto: str) -> List[Tuple[str, str]]:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        c.execute('''
            SELECT DISTINCT clave, valor FROM entidades 
            WHERE user_id = ?
        ''', (self.user_id,))
        
        entidades = c.fetchall()
        conn.close()
        
        texto_lower = texto.lower()
        encontradas = []
        
        for clave, valor in entidades:
            if clave in texto_lower:
                encontradas.append((clave, valor))
        
        return encontradas


def recordar_si_corresponde(user_id: int, texto: str, respuesta: str):
    memoria = EntidadesMemory(user_id)
    
    texto_lower = texto.lower()
    
    if ' es ' in texto_lower:
        partes = texto_lower.split(' es ')
        if len(partes) == 2:
            clave = partes[0].strip()
            valor = partes[1].strip()
            if len(clave) < 30 and len(valor) < 100:
                memoria.recordar(clave, valor, contexto="conversacion")


def obtener_contexto_entidades(user_id: int, texto: str) -> str:
    memoria = EntidadesMemory(user_id)
    entidades = memoria.detectar_entidades_en_texto(texto)
    
    if not entidades:
        return ""
    
    contexto = "\n[CONTEXTO DE ENTIDADES RECORDADAS:\n"
    for clave, valor in entidades:
        contexto += f"- Cuando el usuario dice '{clave}', se refiere a: {valor}\n"
    contexto += "]"
    
    return contexto