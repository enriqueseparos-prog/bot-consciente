# src/memoria/embedding.py
# Sistema de embeddings híbrido: local + online (Gemini)

import os
import sqlite3
import numpy as np
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime
import json

logger = logging.getLogger(__name__)

# ============================================
# CONFIGURACIÓN
# ============================================

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'bot_data.db')

class EmbeddingManager:
    """
    Maneja embeddings usando modo local (sentence-transformers) o online (Gemini)
    """
    
    def __init__(self, modo: str = "auto"):
        """
        Args:
            modo: "local", "gemini", o "auto" (decide según disponibilidad)
        """
        self.modo = modo
        self.modelo_local = None
        self.cliente_gemini = None
        self.dimensiones = 0
        self._inicializar()
    
    def _inicializar(self):
        """Inicializa el modo correspondiente"""
        if self.modo == "local" or self.modo == "auto":
            try:
                from sentence_transformers import SentenceTransformer
                self.modelo_local = SentenceTransformer('all-MiniLM-L6-v2')
                self.dimensiones = 384
                logger.info("✅ Modelo local cargado (384 dimensiones)")
                if self.modo == "auto":
                    self.modo = "local"  # Por defecto, local
            except Exception as e:
                logger.warning(f"No se pudo cargar modelo local: {e}")
                self.modo = "gemini" if self.modo == "auto" else self.modo
        
        if self.modo == "gemini":
            try:
                import google.generativeai as genai
                api_key = os.getenv("GEMINI_API_KEY")
                if api_key:
                    genai.configure(api_key=api_key)
                    self.cliente_gemini = genai
                    self.dimensiones = 768
                    logger.info("✅ Cliente Gemini listo para embeddings (768 dimensiones)")
                else:
                    logger.error("❌ No hay API key para Gemini")
            except Exception as e:
                logger.error(f"Error inicializando Gemini: {e}")
    
    def generar_embedding(self, texto: str) -> Optional[List[float]]:
        """
        Genera embedding según el modo actual
        """
        if not texto or len(texto.strip()) == 0:
            return None
        
        try:
            if self.modo == "local" and self.modelo_local:
                # Modo local
                vector = self.modelo_local.encode(texto)
                return vector.tolist()
            
            elif self.modo == "gemini" and self.cliente_gemini:
                # Modo Gemini
                result = self.cliente_gemini.embed_content(
                    model="models/embedding-001",
                    content=texto,
                    task_type="retrieval_document"
                )
                return result['embedding']
            
            else:
                logger.error("No hay modelo disponible")
                return None
                
        except Exception as e:
            logger.error(f"Error generando embedding: {e}")
            return None
    
    def guardar_embedding(self, mensaje_id: int, texto: str, user_id: int):
        """
        Guarda el embedding de un mensaje en la BD
        """
        vector = self.generar_embedding(texto)
        if not vector:
            return False
        
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        # Crear tabla si no existe
        c.execute('''
            CREATE TABLE IF NOT EXISTS embeddings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mensaje_id INTEGER,
                user_id INTEGER,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                texto TEXT,
                vector TEXT,
                proveedor TEXT,
                dimensiones INTEGER
            )
        ''')
        
        # Guardar
        c.execute('''
            INSERT INTO embeddings (mensaje_id, user_id, texto, vector, proveedor, dimensiones)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            mensaje_id,
            user_id,
            texto[:500],  # Solo guardamos los primeros 500 chars como referencia
            json.dumps(vector),
            self.modo,
            self.dimensiones
        ))
        
        conn.commit()
        conn.close()
        return True
    
    def buscar_similares(self, texto: str, user_id: int, top_k: int = 5) -> List[Dict]:
        """
        Busca mensajes similares al texto dado
        """
        vector_q = self.generar_embedding(texto)
        if not vector_q:
            return []
        
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        
        # Obtener todos los embeddings del usuario
        c.execute('''
            SELECT id, mensaje_id, texto, vector FROM embeddings
            WHERE user_id = ?
            ORDER BY fecha DESC
            LIMIT 1000
        ''', (user_id,))
        
        resultados = []
        for row in c.fetchall():
            emb_id, mensaje_id, texto_orig, vector_json = row
            try:
                vector = json.loads(vector_json)
                # Calcular similitud coseno
                sim = self._cosine_similarity(vector_q, vector)
                resultados.append({
                    "id": emb_id,
                    "mensaje_id": mensaje_id,
                    "texto": texto_orig,
                    "similitud": sim
                })
            except:
                continue
        
        conn.close()
        
        # Ordenar por similitud y tomar top_k
        resultados.sort(key=lambda x: x["similitud"], reverse=True)
        return resultados[:top_k]
    
    def _cosine_similarity(self, a: List[float], b: List[float]) -> float:
        """Calcula similitud coseno entre dos vectores"""
        a = np.array(a)
        b = np.array(b)
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    def cambiar_modo(self, modo: str):
        """Cambia el modo de embeddings"""
        if modo in ["local", "gemini", "auto"]:
            self.modo = modo
            self._inicializar()
            logger.info(f"Modo cambiado a: {modo}")


# ============================================
# FUNCIONES DE INTEGRACIÓN PARA EL BOT
# ============================================

_embedding_manager = None

def get_embedding_manager(modo: str = "auto") -> EmbeddingManager:
    """Singleton del gestor de embeddings"""
    global _embedding_manager
    if _embedding_manager is None:
        _embedding_manager = EmbeddingManager(modo)
    return _embedding_manager

async def procesar_mensaje_para_embedding(user_id: int, mensaje_id: int, texto: str):
    """
    Procesa un mensaje para generar y guardar su embedding
    (para llamar en background desde bot.py)
    """
    try:
        manager = get_embedding_manager()
        manager.guardar_embedding(mensaje_id, texto, user_id)
    except Exception as e:
        logger.error(f"Error procesando embedding: {e}")

def obtener_contexto_semantico(user_id: int, texto: str, top_k: int = 3) -> str:
    """
    Obtiene contexto semántico para enriquecer el prompt de la IA
    """
    manager = get_embedding_manager()
    similares = manager.buscar_similares(texto, user_id, top_k)
    
    if not similares:
        return ""
    
    contexto = "\n📚 *Mensajes relacionados (por significado):*\n"
    for i, sim in enumerate(similares, 1):
        if sim["similitud"] > 0.6:  # Solo si es suficientemente similar
            contexto += f"{i}. {sim['texto'][:100]}... (similitud: {sim['similitud']:.2f})\n"
    
    return contexto