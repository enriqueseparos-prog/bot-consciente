# bot.py - Orquestador principal del Bot Consciente v6.0
# Versión con personalidad, discernimiento y 3 modos de operación

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

# ============================================
# CONFIGURACIÓN INICIAL
# ============================================

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

# ============================================
# IMPORTAR MÓDULOS DEL SISTEMA
# ============================================

# Configuración multi-IA
from src.config import ai_client

# Core
from src.core.habitos import HABITOS
from src.core.maestros import buscar_maestro, listar_maestros
from src.core.protocolos import obtener_rescate, check_valores, listar_flujos, obtener_flujo
from src.core.sistema import obtener_diagnostico
from src.core.discernimiento import resumen_discernimiento, elegir_modo_segun_complejidad, decidir_recurso

# Personalidad
from src.personalidad.temas import obtener_personalidad_para_tema

# Escala y confrontación
from src.escala.detector_vibracional import clasificar_vibracion
from src.confrontacion.detectores import detectar_patron, detectar_estado_emocional, detectar_cambio_de_tema
from src.confrontacion.modos import elegir_modo, obtener_frase as obtener_frase_confrontacion

# Memoria
from src.memoria.perfil import obtener_perfil
from src.memoria.recordatorios import SistemaRecordatorios, procesar_comando_recordatorio
from src.memoria.patrones import obtener_resumen_patrones
from src.memoria.entidades import recordar_si_corresponde, obtener_contexto_entidades

# Utilidades
from src.utils.microdosis import obtener_microdosis, obtener_microdosis_aleatoria
from src.utils.sugerencias import obtener_sugerencia_proactiva

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
                  modo TEXT,
                  proveedor TEXT)''')

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

def guardar_conversacion(user_id, mensaje, respuesta, tema=None, modo=None, proveedor=None):
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
    c.execute("INSERT INTO conversaciones (user_id, fecha, mensaje, respuesta, tema, modo, proveedor) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (user_id, fecha, mensaje, respuesta, tema, modo, proveedor))
    conn.commit()
    conn.close()

def obtener_historial(user_id):
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    c.execute("SELECT fecha, cuerpo, mente, alma FROM registros WHERE user_id=? ORDER BY fecha", (user_id,))
    datos = c.fetchall()
    conn.close()
    return datos

def obtener_ultimas_conversaciones(user_id, limite=5):
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    c.execute('''SELECT mensaje, respuesta FROM conversaciones
                 WHERE user_id=? ORDER BY fecha DESC LIMIT ?''', (user_id, limite))
    resultados = c.fetchall()
    conn.close()
    return resultados

# ============================================
# FUNCIONES DE IA CON CONTEXTO
# ============================================

async def generar_respuesta_con_contexto(texto, user_id, tema, estado, modo_bot, recurso):
    """
    Genera una respuesta usando:
    - Personalidad según tema
    - Contexto de conversaciones recientes
    - Entidades recordadas
    - Modo elegido por discernimiento
    """
    
    # 1. Obtener personalidad para el tema
    personalidad = obtener_personalidad_para_tema(tema, estado)
    
    # 2. Obtener historial reciente
    historial = obtener_ultimas_conversaciones(user_id, 5)
    contexto_historial = ""
    if historial:
        contexto_historial = "Conversación reciente:\n"
        for msg, resp in reversed(historial):
            contexto_historial += f"Usuario: {msg}\nElypson: {resp}\n"
    
    # 3. Obtener entidades relevantes
    entidades = obtener_contexto_entidades(user_id, texto)
    
    # 4. Construir prompt completo
    system_prompt = f"{personalidad}\n\n{contexto_historial}{entidades}"
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": texto}
    ]
    
    # 5. Llamar a la IA según el recurso elegido
    proveedor = recurso.get("proveedor", "gemini")
    modelo = recurso.get("modelo", "gemini-2.0-flash")
    
    respuesta = await ai_client.get_completion(
        messages=messages,
        modo=recurso["tipo"],
        modelo_preferido=modelo,
        temperature=0.7,
        max_tokens=800
    )
    
    return respuesta, recurso["tipo"], f"{proveedor}/{modelo}"

# ============================================
# COMANDOS PRINCIPALES
# ============================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    perfil = obtener_perfil(user_id)

    mensaje = (
        "🌱 *BOT CONSCIENTE v6.0*\n\n"
        "*Comandos principales:*\n"
        "• `/habitos` - Ver 26 hábitos\n"
        "• `/maestro [nombre]` - Invocar sabiduría\n"
        "• `/investigar [tema]` - Investigación de hábitos\n"
        "• `/biografia [maestro]` - Biografía de maestro\n"
        "• `/rescate` - Protocolo 3 min\n"
        "• `/valores` - Preguntas diarias\n"
        "• `/flujo [nombre]` - Flujos maestros\n"
        "• `/microdosis [hábito]` - Versión mínima\n"
        "• `/perfil` - Ver tu perfil\n"
        "• `/patrones` - Ver patrones semanales\n\n"
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
            mensaje += f"  • {habito['nombre']}\n"
        mensaje += "\n"

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

        await update.message.reply_text(respuesta, parse_mode="Markdown")
        guardar_conversacion(update.effective_user.id, f"/maestro {nombre}", respuesta, "maestro", "guia")
    else:
        await update.message.reply_text("No encontré ese maestro. Probá con /maestro lista")

async def investigar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usá: /investigar [tema] (ej: /investigar flexibilidad)")
        return

    tema = " ".join(context.args)
    ruta = Path(f"knowledge/habitos/{tema}.txt")
    
    if ruta.exists():
        with open(ruta, "rb") as f:
            await update.message.reply_document(
                document=f,
                filename=f"{tema}.txt",
                caption=f"📚 Investigación sobre {tema}"
            )
    else:
        await update.message.reply_text(f"No encontré investigación para '{tema}'.")

    guardar_conversacion(update.effective_user.id, f"/investigar {tema}", "Investigación solicitada", tema, "guia")

async def biografia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usá: /biografia [maestro] (ej: /biografia frank suarez)")
        return

    tema = " ".join(context.args)
    ruta = Path(f"knowledge/maestros/{tema}.txt")
    
    if ruta.exists():
        with open(ruta, "rb") as f:
            await update.message.reply_document(
                document=f,
                filename=f"{tema}_biografia.txt",
                caption=f"📚 Biografía de {tema}"
            )
    else:
        await update.message.reply_text(f"No encontré biografía para '{tema}'.")

    guardar_conversacion(update.effective_user.id, f"/biografia {tema}", "Biografía solicitada", tema, "guia")

async def rescate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(obtener_rescate(), parse_mode="Markdown")
    guardar_conversacion(update.effective_user.id, "/rescate", "Protocolo enviado", "sistema", "guia")

async def valores(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(check_valores(), parse_mode="Markdown")
    guardar_conversacion(update.effective_user.id, "/valores", "Valores enviados", "sistema", "guia")

async def flujo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(listar_flujos(), parse_mode="Markdown")
        return

    nombre = context.args[0].lower()
    flujo = obtener_flujo(nombre)

    if flujo:
        texto = f"🌊 *{flujo['nombre']}*\n{flujo['descripcion']}\n\n"
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

async def patrones(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    resumen = obtener_resumen_patrones(user_id)
    await update.message.reply_text(resumen, parse_mode="Markdown")
    guardar_conversacion(user_id, "/patrones", resumen, "patrones", "guia")

# ============================================
# TAREAS PROGRAMADAS
# ============================================

async def enviar_sugerencias_proactivas(context: ContextTypes.DEFAULT_TYPE):
    """Envía sugerencias proactivas a usuarios activos"""
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

async def verificar_inactividad(context: ContextTypes.DEFAULT_TYPE):
    """Verifica usuarios inactivos"""
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    fecha_limite = (datetime.now() - timedelta(days=3)).strftime("%Y-%m-%d %H:%M")
    c.execute('''SELECT DISTINCT user_id FROM conversaciones
                 WHERE user_id NOT IN
                 (SELECT user_id FROM conversaciones WHERE fecha > ?)''', (fecha_limite,))
    inactivos = c.fetchall()
    conn.close()
    
    for (user_id,) in inactivos:
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text="🌱 Hace días que no hablamos. ¿Todo bien? ¿Querés retomar algún tema?"
            )
        except:
            pass

async def recordatorio_proposito(context: ContextTypes.DEFAULT_TYPE):
    """Recordatorio diario de propósito"""
    conn = sqlite3.connect('data/bot_data.db')
    c = conn.cursor()
    c.execute("SELECT DISTINCT user_id FROM conversaciones")
    usuarios = c.fetchall()
    conn.close()

    for (user_id,) in usuarios:
        try:
            await context.bot.send_message(
                chat_id=user_id,
                text="🌅 *Buenos días*\n\nRecordá que cada decisión que tomás hoy construye la vida que querés. ¿Cuál va a ser tu primera decisión consciente?",
                parse_mode="Markdown"
            )
        except:
            pass

# ============================================
# MANEJO DE MENSAJES (EL CORAZÓN DEL BOT)
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

                def emoji(valor):
                    if valor >= 8: return "😊"
                    elif valor >= 5: return "😐"
                    else: return "😔"

                respuesta = (
                    f"✅ *Registro guardado*\n\n"
                    f"Cuerpo: {cuerpo}/10 {emoji(cuerpo)}\n"
                    f"Mente: {mente}/10 {emoji(mente)}\n"
                    f"Alma: {alma}/10 {emoji(alma)}"
                )

                await update.message.reply_text(respuesta, parse_mode="Markdown")
                guardar_conversacion(user_id, texto, respuesta, "checkin", "guia")
                return
        except:
            pass
    
    # ========================================
    # COMANDOS DE RECORDATORIO
    # ========================================
    respuesta_recordatorio = procesar_comando_recordatorio(texto, str(user_id), sistema_recordatorios)
    if respuesta_recordatorio:
        await update.message.reply_text(respuesta_recordatorio, parse_mode="Markdown")
        guardar_conversacion(user_id, texto, respuesta_recordatorio, "recordatorio", "guia")
        return
    
    # ========================================
    # DISCERNIMIENTO: EL BOT DECIDE
    # ========================================
    # Clasificar vibración
    vibracion = clasificar_vibracion(texto)
    estado = vibracion.get("estado", 5)
    
    # Detectar tema (simplificado por ahora)
    if any(p in texto.lower() for p in ["hijo", "hija", "papá", "mamá"]):
        tema = "hijo"
    elif any(p in texto.lower() for p in ["pareja", "novia", "esposa", "mujer"]):
        tema = "pareja"
    elif any(p in texto.lower() for p in ["cuerpo", "entreno", "gimnasio", "muay thai"]):
        tema = "cuerpo"
    elif any(p in texto.lower() for p in ["mente", "pienso", "cabeza", "aprender"]):
        tema = "mente"
    elif any(p in texto.lower() for p in ["alma", "espíritu", "meditar", "reiki"]):
        tema = "alma"
    elif any(p in texto.lower() for p in ["trabajo", "barbería", "negocio", "cliente"]):
        tema = "trabajo"
    else:
        tema = "otro"
    
    perfil.registrar_tema(tema)
    
    # Usar discernimiento para decidir modo y recursos
    decision = resumen_discernimiento(texto, estado)
    modo_bot = decision["modo_sugerido"]
    recurso = decision["recurso"]
    
    # Detectar patrones para confrontación
    historial = []  # Podríamos mejorarlo después
    patron = detectar_patron(texto, historial)
    estado_emo = detectar_estado_emocional(texto)
    
    # Elegir modo de confrontación (ahora usando vibración)
    modo_confrontacion = elegir_modo(estado_emo, patron, vibracion)
    
    # ========================================
    # GENERAR RESPUESTA CON IA
    # ========================================
    respuesta_ia, tipo_recurso, proveedor_usado = await generar_respuesta_con_contexto(
        texto, user_id, tema, estado, modo_bot, recurso
    )
    
    if not respuesta_ia:
        respuesta_final = "🌱 No pude generar una respuesta en este momento. ¿Querés hacer un checkin o usar algún comando?"
    else:
        respuesta_final = respuesta_ia
    
    # Agregar frase de confrontación si aplica
    if patron:
        frase_confrontacion = obtener_frase_confrontacion(modo_confrontacion)
        respuesta_final = f"{frase_confrontacion}\n\n{respuesta_final}"
    
    # Enviar respuesta
    await update.message.reply_text(respuesta_final)
    
    # Guardar en base de datos
    guardar_conversacion(user_id, texto, respuesta_final, tema, modo_bot, proveedor_usado)
    
    # Recordar entidades si corresponde
    recordar_si_corresponde(user_id, texto, respuesta_final)

# ============================================
# INICIAR BOT
# ============================================

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
    app.bot_data['sistema_recordatorios'] = sistema_recordatorios
    
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
    app.add_handler(CommandHandler("patrones", patrones))
    
    # Manejar mensajes
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))
    
    # Tareas programadas
    job_queue = app.job_queue
    if job_queue:
        job_queue.run_daily(verificar_inactividad, time=time(10, 0))
        job_queue.run_daily(recordatorio_proposito, time=time(8, 0))
        job_queue.run_repeating(enviar_sugerencias_proactivas, interval=10800, first=10)
    
    print("🤖 BOT CONSCIENTE v6.0 INICIADO")
    app.run_polling()

if __name__ == "__main__":
    main()