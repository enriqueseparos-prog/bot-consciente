# src/memoria/recordatorios.py
# Sistema de recordatorios para el bot consciente
# Permite programar avisos tipo: "recordame tomar agua a las 3 PM"

import json
import os
from datetime import datetime, time, timedelta
from typing import Dict, List, Optional
import threading
import time as time_module

# Archivo donde se guardan los recordatorios
RECORDATORIOS_FILE = "recordatorios.json"

class SistemaRecordatorios:
    def __init__(self, bot=None):
        self.bot = bot
        self.recordatorios = self.cargar_recordatorios()
        self.hilo_activo = False
        self.iniciar_verificador()
    
    def cargar_recordatorios(self) -> Dict:
        """Carga los recordatorios desde el archivo JSON"""
        if os.path.exists(RECORDATORIOS_FILE):
            try:
                with open(RECORDATORIOS_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {}
        return {}
    
    def guardar_recordatorios(self):
        """Guarda los recordatorios en el archivo JSON"""
        with open(RECORDATORIOS_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.recordatorios, f, ensure_ascii=False, indent=2)
    
    def programar_recordatorio(self, usuario_id: str, mensaje: str, hora_str: str, recurrente: bool = False) -> Dict:
        """
        Programa un nuevo recordatorio
        
        Args:
            usuario_id: ID del usuario
            mensaje: Qué recordar
            hora_str: "HH:MM" en formato 24h
            recurrente: True si se repite diario
        
        Returns:
            Dict con el recordatorio creado
        """
        # Validar formato de hora
        try:
            hora_obj = datetime.strptime(hora_str, "%H:%M").time()
        except ValueError:
            return {"error": "Formato de hora inválido. Usá HH:MM (ej: 15:30)"}
        
        # Crear ID único
        recordatorio_id = f"{usuario_id}_{int(datetime.now().timestamp())}"
        
        recordatorio = {
            "id": recordatorio_id,
            "usuario_id": usuario_id,
            "mensaje": mensaje,
            "hora": hora_str,
            "recurrente": recurrente,
            "activo": True,
            "creado": datetime.now().isoformat(),
            "ultimo_disparo": None
        }
        
        # Inicializar lista del usuario si no existe
        if usuario_id not in self.recordatorios:
            self.recordatorios[usuario_id] = []
        
        self.recordatorios[usuario_id].append(recordatorio)
        self.guardar_recordatorios()
        
        return recordatorio
    
    def cancelar_recordatorio(self, usuario_id: str, recordatorio_id: str) -> bool:
        """Cancela un recordatorio específico"""
        if usuario_id in self.recordatorios:
            for i, rec in enumerate(self.recordatorios[usuario_id]):
                if rec["id"] == recordatorio_id:
                    rec["activo"] = False
                    self.guardar_recordatorios()
                    return True
        return False
    
    def listar_recordatorios(self, usuario_id: str) -> List[Dict]:
        """Lista los recordatorios activos de un usuario"""
        if usuario_id in self.recordatorios:
            return [r for r in self.recordatorios[usuario_id] if r["activo"]]
        return []
    
    def verificar_recordatorios(self):
        """Verifica si hay recordatorios que disparar (se ejecuta en hilo)"""
        while self.hilo_activo:
            try:
                ahora = datetime.now()
                hora_actual = ahora.strftime("%H:%M")
                
                for usuario_id, recordatorios in self.recordatorios.items():
                    for rec in recordatorios:
                        if not rec["activo"]:
                            continue
                        
                        # Verificar si es hora de disparar
                        if rec["hora"] == hora_actual:
                            # Evitar disparar múltiples veces en el mismo minuto
                            if rec["ultimo_disparo"] != ahora.strftime("%Y-%m-%d %H:%M"):
                                self.disparar_recordatorio(usuario_id, rec)
                                rec["ultimo_disparo"] = ahora.strftime("%Y-%m-%d %H:%M")
                                
                                # Si no es recurrente, desactivar
                                if not rec["recurrente"]:
                                    rec["activo"] = False
                                
                                self.guardar_recordatorios()
                
                # Esperar 60 segundos antes de la próxima verificación
                for _ in range(60):
                    if not self.hilo_activo:
                        break
                    time_module.sleep(1)
                    
            except Exception as e:
                print(f"Error en verificador de recordatorios: {e}")
                time_module.sleep(60)
    
    def disparar_recordatorio(self, usuario_id: str, recordatorio: Dict):
        """Dispara un recordatorio (envía mensaje)"""
        if self.bot:
            try:
                mensaje = f"⏰ **RECORDATORIO**: {recordatorio['mensaje']}"
                if hasattr(self.bot, 'send_message'):
                    self.bot.send_message(chat_id=usuario_id, text=mensaje)
                print(f"Recordatorio enviado a {usuario_id}: {recordatorio['mensaje']}")
            except Exception as e:
                print(f"Error al enviar recordatorio: {e}")
    
    def iniciar_verificador(self):
        """Inicia el hilo verificador de recordatorios"""
        if not self.hilo_activo:
            self.hilo_activo = True
            hilo = threading.Thread(target=self.verificar_recordatorios, daemon=True)
            hilo.start()
    
    def detener_verificador(self):
        """Detiene el hilo verificador"""
        self.hilo_activo = False

# Funciones de utilidad para procesar comandos de recordatorios
def procesar_comando_recordatorio(texto: str, usuario_id: str, sistema: SistemaRecordatorios) -> str:
    """
    Procesa comandos de texto para crear recordatorios
    
    Ejemplos:
    - "recordame tomar agua a las 15:30"
    - "recordatorio diario meditar a las 7:00"
    - "mis recordatorios"
    - "cancelar recordatorio tomar agua"
    """
    texto = texto.lower()
    
    # Listar recordatorios
    if texto in ["mis recordatorios", "listar recordatorios", "ver recordatorios"]:
        recordatorios = sistema.listar_recordatorios(usuario_id)
        if not recordatorios:
            return "📭 No tenés recordatorios activos."
        
        respuesta = "📋 **Tus recordatorios activos:**\n\n"
        for i, rec in enumerate(recordatorios, 1):
            recurrente = "🔄 diario" if rec["recurrente"] else "⏰ única vez"
            respuesta += f"{i}. {rec['hora']} - {rec['mensaje']} {recurrente}\n"
        return respuesta
    
    # Cancelar recordatorio
    if texto.startswith("cancelar recordatorio "):
        texto_buscar = texto.replace("cancelar recordatorio ", "").strip()
        if usuario_id in sistema.recordatorios:
            for rec in sistema.recordatorios[usuario_id]:
                if rec["activo"] and texto_buscar.lower() in rec["mensaje"].lower():
                    sistema.cancelar_recordatorio(usuario_id, rec["id"])
                    return f"✅ Recordatorio cancelado: {rec['mensaje']}"
        return "❌ No encontré ese recordatorio."
    
    # Crear recordatorio
    if "recordame" in texto or "recordatorio" in texto:
        # Extraer mensaje y hora
        import re
        
        # Patrón para "a las HH:MM"
        patron_hora = r'a las (\d{1,2}:\d{2})'
        match = re.search(patron_hora, texto)
        
        if match:
            hora = match.group(1)
            # Asegurar formato HH:MM
            if len(hora.split(':')[0]) == 1:
                hora = '0' + hora
            
            # Extraer mensaje (todo lo que está entre "recordame" y "a las")
            partes = texto.split(" a las ")[0]
            if "recordame" in partes:
                mensaje = partes.replace("recordame", "").strip()
            elif "recordatorio" in partes:
                mensaje = partes.replace("recordatorio", "").strip()
            else:
                mensaje = partes
            
            # Verificar si es recurrente
            recurrente = "diario" in texto or "todos los días" in texto
            
            resultado = sistema.programar_recordatorio(usuario_id, mensaje, hora, recurrente)
            
            if "error" in resultado:
                return f"❌ {resultado['error']}"
            
            recurrente_texto = "todos los días" if recurrente else "hoy"
            return f"✅ Recordatorio programado: '{mensaje}' a las {hora} {recurrente_texto}"
    
    return None  # No es un comando de recordatorio