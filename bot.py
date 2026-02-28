# bot.py - Orquestador principal del Bot Consciente v5.0
# Versión final con todos los módulos integrados

import logging
import sqlite3
import matplotlib.pyplot as plt
import io
import os
import asyncio
from datetime import datetime, timedelta, time
from pathlib import Path
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from src.memoria.recordatorios import SistemaRecordatorios, procesar_comando_recordatorio
from src.puntos_14 import grupo1, grupo2, grupo3, grupo4, grupo5
from src.utils.sugerencias import obtener_sugerencia_proactiva

# Configuración de logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# ============================================
# CONFIGURACIÓN - API KEYS
# ============================================

# Cargar variables de entorno desde .env
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN", "8781338642:AAHUVZBRvjH5oea5pQF97eO5No3qYnPTOJE")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")
OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY")
CEREBRAS_KEY = os.getenv("CEREBRAS_API_KEY")
DEEPSEEK_KEY = os.getenv("DEEPSEEK_API_KEY")

# ============================================
# IMPORTAR MÓDULOS DEL SISTEMA
# ============================================

from src.config import ai_client
from src.core.habitos import HABITOS, obtener_prioridades
from src.core.maestros import buscar_maestro, listar_maestros
from src.core.protocolos import obtener_rescate, check_valores, listar_flujos, obtener_flujo
from src.core.sistema import obtener_diagnostico
from src.escala.detector_vibracional import clasificar_vibracion, sugerir_accion_por_vibracion
from src.confrontacion.detectores import detectar_patron, detectar_estado_emocional
from src.confrontacion.modos import elegir_modo, obtener_frase as obtener_frase_confrontacion
from src.memoria.perfil import obtener_perfil, PERFILES
from src.utils.microdosis import obtener_microdosis, obtener_microdosis_aleatoria

# ============================================
# BASE DE DATOS
# ============================================

def init_db():
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    
    # Tabla de registros diarios (checkin)
    c.execute('''CREATE TABLE IF NOT EXISTS registros
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  fecha TEXT,
                  cuerpo INTEGER,
                  mente INTEGER,
                  alma INTEGER)''')
    
    # Tabla de conversaciones (memoria total)
    c.execute('''CREATE TABLE IF NOT EXISTS conversaciones
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  fecha TEXT,
                  mensaje TEXT,
                  respuesta TEXT,
                  tema TEXT,
                  modo TEXT)''')
    
    # Tabla de feedback
    c.execute('''CREATE TABLE IF NOT EXISTS feedback
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  fecha TEXT,
                  sugerencia TEXT,
                  respuesta TEXT,
                  utilidad INTEGER)''')
    
    conn.commit()
    conn.close()

def guardar_registro(user_id, cuerpo, mente, alma):
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    c.execute("INSERT INTO registros (user_id, fecha, cuerpo, mente, alma) VALUES (?, ?, ?, ?, ?)",
              (user_id, fecha, cuerpo, mente, alma))
    conn.commit()
    conn.close()

def guardar_conversacion(user_id, mensaje, respuesta, tema=None, modo=None):
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    c.execute("INSERT INTO conversaciones (user_id, fecha, mensaje, respuesta, tema, modo) VALUES (?, ?, ?, ?, ?, ?)",
              (user_id, fecha, mensaje, respuesta, tema, modo))
    conn.commit()
    conn.close()

def obtener_historial(user_id):
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    c.execute("SELECT fecha, cuerpo, mente, alma FROM registros WHERE user_id=? ORDER BY fecha", (user_id,))
    datos = c.fetchall()
    conn.close()
    return datos

def buscar_historial_tema(user_id, tema, limite=3):
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    c.execute('''SELECT fecha, mensaje, respuesta FROM conversaciones 
                 WHERE user_id=? AND (tema LIKE ? OR mensaje LIKE ?)
                 ORDER BY fecha DESC LIMIT ?''',
              (user_id, f'%{tema}%', f'%{tema}%', limite))
    resultados = c.fetchall()
    conn.close()
    return resultados

def obtener_ultimo_mensaje(user_id):
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    c.execute("SELECT mensaje, fecha FROM conversaciones WHERE user_id=? ORDER BY fecha DESC LIMIT 1", (user_id,))
    resultado = c.fetchone()
    conn.close()
    return resultado

def obtener_usuarios_inactivos(dias=3):
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    fecha_limite = (datetime.now() - timedelta(days=dias)).strftime("%Y-%m-%d %H:%M")
    c.execute('''SELECT DISTINCT user_id FROM conversaciones 
                 WHERE user_id NOT IN 
                 (SELECT user_id FROM conversaciones WHERE fecha > ?)''', (fecha_limite,))
    inactivos = c.fetchall()
    conn.close()
    return [u[0] for u in inactivos]

# ============================================
# FUNCIONES DE GEMINI/IA
# ============================================

async def clasificar_con_gemini(texto):
    """Clasifica el mensaje en tema y estado de ánimo aproximado"""
    try:
        prompt = f"""Del siguiente mensaje, extraé:
- Tema principal (una palabra: hijo/pareja/cuerpo/mente/alma/trabajo/otro)
- Estado de ánimo aproximado (1-10)
- Intención (ayuda/desahogo/consulta/investigacion/otro)

Formato de respuesta: tema|estado|intencion

Mensaje: {texto}"""
        
        respuesta = await ai_client.get_completion(
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=100
        )
        
        partes = respuesta.strip().split('|')
        if len(partes) == 3:
            return {
                "tema": partes[0],
                "estado": int(partes[1]) if partes[1].isdigit() else 5,
                "intencion": partes[2]
            }
        else:
            return {"tema": "otro", "estado": 5, "intencion": "otro"}
    except Exception as e:
        logging.error(f"Error en clasificación: {e}")
        return {"tema": "otro", "estado": 5, "intencion": "otro"}

async def generar_respuesta_con_ia(prompt, modo="guia"):
    system_prompts = {
        "guia": "Eres un guía breve y directo. Respondes con 1-2 frases cortas. Nada de divagaciones.",
        "acompanante": "Eres un acompañante que escucha y responde con pocas palabras. Validás y preguntás.",
        "socratico": "Hacés UNA pregunta corta que invite a reflexionar. Máximo 2 líneas."
    }
    system_content = system_prompts.get(modo, system_prompts["guia"])
    
    try:
        respuesta = await ai_client.get_completion(
            messages = [
                 {"role": "system", "content": system_content + " No inventes información. Si no hay contexto, preguntá abiertamente."},
                  {"role": "user", "content": prompt}
],
            temperature=0.7,
            max_tokens=800
        )
        return respuesta
    except Exception as e:
        logging.error(f"Error generando respuesta: {e}")
        return None

# ============================================
# FUNCIONES PARA LEER ARCHIVOS DE KNOWLEDGE
# ============================================

def leer_investigacion(carpeta, tema):
    """Lee un archivo de investigación de knowledge/"""
    nombre_archivo = tema.lower().replace(" ", "_").replace("í", "i").replace("á", "a")
    ruta = Path(f"knowledge/{carpeta}/{nombre_archivo}.txt")
    if ruta.exists():
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    return None

# ============================================
# COMANDOS PRINCIPALES
# ============================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    perfil = obtener_perfil(user_id)
    
    mensaje = (
        "🌟 *BOT CONSCIENTE v5.0*\n\n"
        "*Comandos principales:*\n"
        "• `/habitos` - Ver 26 hábitos\n"
        "• `/maestro [nombre]` - Invocar sabiduría\n"
        "• `/investigar [tema]` - Investigación de hábitos\n"
        "• `/biografia [maestro]` - Biografía de maestro\n"
        "• `/rescate` - Protocolo 3 min\n"
        "• `/valores` - Preguntas diarias\n"
        "• `/flujo [nombre]` - Flujos maestros\n"
        "• `/microdosis [hábito]` - Versión mínima\n"
        "• `/perfil` - Ver tu perfil\n\n"
        "• Mandá `7 8 9` para checkin rápido\n\n"
        f"📊 *Tu perfil:* Racha {perfil.racha_actual} días"
    )
    await update.message.reply_text(mensaje, parse_mode="Markdown")
    guardar_conversacion(user_id, "/start", mensaje, "sistema", "guia")

async def habitos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = "📋 *TUS 26 HÁBITOS*\n\n"
    
    for dominio, lista in HABITOS.items():
        mensaje += f"🔹 *{dominio.upper()}*\n"
        for habito in lista:
            estrella = " ⭐" if habito["prioridad"] == 3 else ""
            mensaje += f"  • {habito['nombre']}{estrella}\n"
        mensaje += "\n"
    
    mensaje += "⭐ = Prioridad actual"
    await update.message.reply_text(mensaje, parse_mode="Markdown")
    guardar_conversacion(update.effective_user.id, "/habitos", mensaje, "sistema", "guia")

async def grafica(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    datos = obtener_historial(user_id)
    
    if len(datos) < 2:
        await update.message.reply_text("Necesito al menos 2 registros para hacer una gráfica.")
        return
    
    fechas = [d[0][5:16] for d in datos]
    cuerpos = [d[1] for d in datos]
    mentes = [d[2] for d in datos]
    almas = [d[3] for d in datos]
    
    plt.figure(figsize=(10, 5))
    plt.plot(fechas, cuerpos, marker='o', label='Cuerpo', linewidth=2)
    plt.plot(fechas, mentes, marker='s', label='Mente', linewidth=2)
    plt.plot(fechas, almas, marker='^', label='Alma', linewidth=2)
    plt.xlabel('Fecha')
    plt.ylabel('Nivel (1-10)')
    plt.title('Tu evolución')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100)
    buf.seek(0)
    plt.close()
    
    await update.message.reply_photo(photo=buf, caption="📊 Tu evolución")
    guardar_conversacion(user_id, "/grafica", "Gráfica enviada", "sistema", "guia")

async def maestro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usá: /maestro [nombre]\nEj: /maestro frank suarez")
        return
    
    nombre = " ".join(context.args).lower()
    
    if nombre == "lista":
        texto = listar_maestros()
        await update.message.reply_text(texto, parse_mode="Markdown")
        return
    
    maestro_info = buscar_maestro(nombre)
    
    if maestro_info:
        respuesta = f"🧠 *{maestro_info['nombre']}*\n\n"
        respuesta += f"📌 {maestro_info['frase']}\n\n"
        respuesta += f"✨ *Práctica:* {maestro_info['practica']}\n"
        if 'area' in maestro_info:
            respuesta += f"\nÁrea: {maestro_info['area']}"
        if 'viaje' in maestro_info:
            respuesta += f"\nViaje: {maestro_info['viaje']}"
        
        await update.message.reply_text(respuesta, parse_mode="Markdown")
        guardar_conversacion(update.effective_user.id, f"/maestro {nombre}", "Maestro invocado", "maestro", "guia")
    else:
        await update.message.reply_text("No encontré ese maestro. Probá con /maestro lista")

async def investigar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usá: /investigar [tema] (ej: /investigar flexibilidad)")
        return
    
    tema = " ".join(context.args)
    
    # Buscar en knowledge/habitos/
    contenido = leer_investigacion("habitos", tema)
    
    if contenido:
        with open(f"knowledge/habitos/{tema}.txt", "rb") as f:
            await update.message.reply_document(
                document=f,
                filename=f"{tema}.txt",
                caption=f"📚 Investigación sobre {tema}"
            )
    else:
        await update.message.reply_text(f"No encontré investigación para '{tema}'. Usá el script para generarla.")
    
    guardar_conversacion(update.effective_user.id, f"/investigar {tema}", "Investigación solicitada", tema, "guia")

async def biografia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usá: /biografia [maestro] (ej: /biografia frank suarez)")
        return
    
    tema = " ".join(context.args)
    
    # Buscar en knowledge/maestros/
    contenido = leer_investigacion("maestros", tema)
    
    if contenido:
        with open(f"knowledge/maestros/{tema}.txt", "rb") as f:
            await update.message.reply_document(
                document=f,
                filename=f"{tema}_biografia.txt",
                caption=f"📚 Biografía de {tema}"
            )
    else:
        await update.message.reply_text(f"No encontré biografía para '{tema}'. Usá el script para generarla.")
    
    guardar_conversacion(update.effective_user.id, f"/biografia {tema}", "Biografía solicitada", tema, "guia")

async def rescate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from src.core.protocolos import obtener_rescate
    await update.message.reply_text(obtener_rescate(), parse_mode="Markdown")
    guardar_conversacion(update.effective_user.id, "/rescate", "Protocolo enviado", "sistema", "guia")

async def valores(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from src.core.protocolos import check_valores
    await update.message.reply_text(check_valores(), parse_mode="Markdown")
    guardar_conversacion(update.effective_user.id, "/valores", "Valores enviados", "sistema", "guia")

async def flujo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    from src.core.protocolos import listar_flujos, obtener_flujo
    
    if not context.args:
        await update.message.reply_text(listar_flujos(), parse_mode="Markdown")
        return
    
    nombre = context.args[0].lower()
    flujo = obtener_flujo(nombre)
    
    if flujo:
        texto = f"🌀 *{flujo['nombre']}*\n{flujo['descripcion']}\n\n"
        texto += "🔹 *Secuencia:*\n"
        for i, m in enumerate(flujo['secuencia'], 1):
            texto += f"{i}. {m}\n"
        await update.message.reply_text(texto, parse_mode="Markdown")
    else:
        await update.message.reply_text("Flujo no encontrado. Usá /flujo para ver opciones.")
    
    guardar_conversacion(update.effective_user.id, f"/flujo {nombre}", "Flujo enviado", "sistema", "guia")

async def microdosis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        texto = obtener_microdosis_aleatoria()
        await update.message.reply_text(texto, parse_mode="Markdown")
        return
    
    habito = " ".join(context.args)
    texto = obtener_microdosis(habito)
    await update.message.reply_text(f"🧠 *Microdosis para '{habito}':*\n{texto}", parse_mode="Markdown")
    guardar_conversacion(update.effective_user.id, f"/microdosis {habito}", texto, "microdosis", "guia")

async def perfil(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    perfil = obtener_perfil(user_id)
    await update.message.reply_text(perfil.obtener_resumen(), parse_mode="Markdown")
    guardar_conversacion(user_id, "/perfil", "Perfil mostrado", "sistema", "guia")

# ============================================
# FUNCIÓN PARA LOS 14 PUNTOS
# ============================================

def aplicar_punto_segun_contexto(texto, tema, estado):
    """Elige un punto de los 14 según el contexto"""
    import random
    
    # Puntos de perspectiva (1-3) para problemas
    if "problema" in texto or "difícil" in texto or "no puedo" in texto:
        punto = random.choice([grupo1.punto1_perspectiva, grupo1.punto2_proyeccion, grupo1.punto3_desafios])
        return punto()
    
    # Puntos de identidad (4-6) para crecimiento
    if "quién" in texto or "soy" in texto or "identidad" in texto:
        punto = random.choice([grupo2.punto4_identidad, grupo2.punto5_tiempo, grupo2.punto6_encarnar])
        return punto()
    
    # Puntos de alineación (7-9) para confusión
    if "no sé" in texto or "confundido" in texto or "duda" in texto:
        punto = random.choice([grupo3.punto7_campo_cuantico, grupo3.punto8_alineacion, grupo3.punto9_ritmo_rendicion])
        return punto()
    
    # Puntos de gratitud (10-12) para momentos bajos
    if estado < 4 or "mal" in texto or "triste" in texto:
        punto = random.choice([grupo4.punto10_gratitud, grupo4.punto11_disciplina, grupo4.punto12_desapego])
        return punto()
    
    # Puntos de propósito (13-14) para inspiración
    if "propósito" in texto or "sentido" in texto or "para qué" in texto:
        punto = random.choice([grupo5.punto13_proposito, grupo5.punto14_expansion])
        return punto()
    
    return None

# ============================================
# MANEJO DE MENSAJES
# ============================================

async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    texto = update.message.text
    perfil = obtener_perfil(user_id)
    
        # Obtener sistema de recordatorios
    sistema_recordatorios = context.bot_data.get('sistema_recordatorios')
    if not sistema_recordatorios:
        sistema_recordatorios = SistemaRecordatorios(context.bot)
        context.bot_data['sistema_recordatorios'] = sistema_recordatorios

    # ========================================
    # CHECKIN RÁPIDO (formato "7 8 9")
    # ========================================
    partes = texto.split()
    if len(partes) == 3 and all(p.isdigit() for p in partes):
        try:
            cuerpo, mente, alma = map(int, partes)
            if 1 <= cuerpo <= 10 and 1 <= mente <= 10 and 1 <= alma <= 10:
                guardar_registro(user_id, cuerpo, mente, alma)
                perfil.actualizar_por_checkin(cuerpo, mente, alma)
                
                # Emojis según valores
                def emoji(valor):
                    if valor >= 8: return "😊"
                    elif valor >= 5: return "😐"
                    else: return "😞"
                
                # Mensaje según vibración
                vibracion = clasificar_vibracion(texto)
                
                respuesta = (
                    f"✅ *Registro guardado*\n\n"
                    f"Cuerpo: {cuerpo}/10 {emoji(cuerpo)}\n"
                    f"Mente: {mente}/10 {emoji(mente)}\n"
                    f"Alma: {alma}/10 {emoji(alma)}\n\n"
                    f"💬 {vibracion['sugerencia']}\n"
                    f"✨ {vibracion['frase']}"
                )
                
                await update.message.reply_text(respuesta, parse_mode="Markdown")
                guardar_conversacion(user_id, texto, respuesta, "checkin", "guia")
                return
        except:
            pass
    
    # ========================================
        # CLASIFICAR MENSAJE
    # ========================================
    clasificacion = await clasificar_con_gemini(texto)
    tema = clasificacion.get("tema", "otro")
    estado = clasificacion.get("estado", 5)
    intencion = clasificacion.get("intencion", "otro")
    
    perfil.registrar_tema(tema)
    
    # Clasificar vibración
    vibracion = clasificar_vibracion(texto)
    
    # Verificar si es un comando de recordatorio
    respuesta_recordatorio = procesar_comando_recordatorio(texto, str(user_id), sistema_recordatorios)
    if respuesta_recordatorio:
        await update.message.reply_text(respuesta_recordatorio, parse_mode="Markdown")
        guardar_conversacion(user_id, texto, respuesta_recordatorio, "recordatorio", "guia")
        return
        
    # Detectar patrones
    historial = []  # Aquí iría historial de BD
    patron = detectar_patron(texto, historial)
    estado_emo = detectar_estado_emocional(texto)
    
    # Elegir modo
    modo = elegir_modo(estado_emo, patron, vibracion)
    
    # ========================================
    # APLICAR 14 PUNTOS SI CORRESPONDE
    # ========================================
    frase_punto = aplicar_punto_segun_contexto(texto, tema, estado)
    
    if frase_punto:
        # Si hay un punto, lo agregamos como sugerencia
        contexto_punto = f"\n\n💭 *Reflexión:* {frase_punto}"
    else:
        contexto_punto = ""

    # ========================================
    # GENERAR RESPUESTA
    # ========================================
    prompt = f"El usuario dice: '{texto}'. Tema: {tema}. Estado: {estado}/10. Vibración: {vibracion['vibracion']}. {vibracion['sugerencia']}"
    
    respuesta_ia = await generar_respuesta_con_ia(prompt, modo)
    
    if respuesta_ia:
        respuesta_final = respuesta_ia
    else:
        respuesta_final = "La IA no está disponible. Podés usar /checkin para registrar."

    # Agregar el punto de los 14 si corresponde
    if frase_punto:
        respuesta_final = f"{respuesta_final}\n\n💭 *Reflexión:* {frase_punto}"    
   
    # Si hay patrón, agregar frase de confrontación
    if patron:
        frase_confrontacion = obtener_frase_confrontacion(modo)
        respuesta_final = f"{frase_confrontacion}\n\n{respuesta_final}"
    
    await update.message.reply_text(respuesta_final)
    guardar_conversacion(user_id, texto, respuesta_final, tema, modo)

# ============================================
# TAREAS PROGRAMADAS
# ============================================

async def verificar_inactividad(context: ContextTypes.DEFAULT_TYPE):
    inactivos = obtener_usuarios_inactivos(dias=3)
    def buscar_historial_reciente(user_id, limite=5):
        """Busca las últimas conversaciones del usuario"""
        conn = sqlite3.connect('data/bot_data.db')
        c = conn.cursor()
        c.execute('''SELECT mensaje, respuesta FROM conversaciones 
                 WHERE user_id=? ORDER BY fecha DESC LIMIT ?''', (user_id, limite))
        resultados = c.fetchall()
        conn.close()
        return resultados

    for user_id in inactivos:
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text="Hace días que no hablamos. ¿Todo bien? ¿Quieres retomar algún hábito?"
            )
        except:
            pass

async def recordatorio_proposito(context: ContextTypes.DEFAULT_TYPE):
    # Obtener usuarios activos
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT user_id FROM conversaciones")
    usuarios = c.fetchall()
    conn.close()
    
    from src.core.protocolos import VALORES
    import random
    
    for (user_id,) in usuarios:
        try:
            valor = random.choice(list(VALORES.values()))
            mensaje = f"🌅 *Buenos días*\n\n*{valor['nombre']}*: {valor['definicion']}\n\n{valor['pregunta']}"
            await context.bot.send_message(chat_id=user_id, text=mensaje, parse_mode="Markdown")
        except:
            pass

# ============================================
# INICIAR BOT
# ============================================

async def enviar_sugerencias_proactivas(context: ContextTypes.DEFAULT_TYPE):
    """Envía sugerencias proactivas a usuarios activos"""
    import sqlite3
    from src.utils.sugerencias import obtener_sugerencia_proactiva
    
    # Obtener usuarios que han hablado en las últimas 24h
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    c.execute('''
        SELECT DISTINCT user_id FROM conversaciones 
        WHERE fecha > datetime('now', '-1 day')
    ''')
    usuarios = c.fetchall()
    conn.close()
    
    for (user_id,) in usuarios:
        try:
            sugerencia = obtener_sugerencia_proactiva(user_id)
            if sugerencia:
                await context.bot.send_message(
                    chat_id=user_id,
                    text=f"💭 *Sugerencia:* {sugerencia}",
                    parse_mode="Markdown"
                )
        except Exception as e:
            print(f"Error enviando sugerencia a {user_id}: {e}")

def main():
    # Inicializar base de datos
    init_db()
    
    # Crear carpetas necesarias
    os.makedirs("knowledge/habitos", exist_ok=True)
    os.makedirs("knowledge/maestros", exist_ok=True)
    os.makedirs("data", exist_ok=True)
    
    # Crear aplicación
    app = Application.builder().token(TOKEN).build()
        # Inicializar sistema de recordatorios
    sistema_recordatorios = SistemaRecordatorios(app.bot)

    # Agregar comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("habitos", habitos))
    app.add_handler(CommandHandler("grafica", grafica))
    app.add_handler(CommandHandler("maestro", maestro))
    app.add_handler(CommandHandler("investigar", investigar))
    app.add_handler(CommandHandler("biografia", biografia))
    app.add_handler(CommandHandler("rescate", rescate))
    app.add_handler(CommandHandler("valores", valores))
    app.add_handler(CommandHandler("flujo", flujo))
    app.add_handler(CommandHandler("microdosis", microdosis))
    app.add_handler(CommandHandler("perfil", perfil))
    
    # Manejar mensajes
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))
    
    # Tareas programadas
    job_queue = app.job_queue
    if job_queue:
        job_queue.run_daily(verificar_inactividad, time=time(10, 0))
        job_queue.run_daily(recordatorio_proposito, time=time(8, 0))
            # Sugerencias proactivas cada 3 horas
        job_queue.run_repeating(enviar_sugerencias_proactivas, interval=10800, first=10)
    
        print("🤖 BOT CONSCIENTE v5.0 INICIADO")
    app.run_polling()

if __name__ == "__main__":
    main()