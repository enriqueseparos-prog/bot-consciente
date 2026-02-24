import logging
import sqlite3
import matplotlib.pyplot as plt
import io
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# ============================================
# CONFIGURACIÓN (CAMBIA ESTOS VALORES)
# ============================================

TOKEN = "8781338642:AAHUVZBRvjH5oea5pQF97eO5No3qYnPTOJE"
GEMINI_KEY = "AIzaSyAvGC6NH1WkxGnmsd9Dmiyq5wduO5gA6BQ"

# Configurar Gemini
genai.configure(api_key=GEMINI_KEY)

# ============================================
# DIAGNÓSTICO DE MODELOS GEMINI
# ============================================
model = None
modelo_elegido = None

print("🔍 Consultando modelos disponibles en tu proyecto...")
try:
    modelos_disponibles = list(genai.list_models())
    print(f"✅ Se encontraron {len(modelos_disponibles)} modelos en total.")

    # Filtrar modelos que soporten 'generateContent'
    modelos_generativos = [m for m in modelos_disponibles if 'generateContent' in m.supported_generation_methods]

    if not modelos_generativos:
        print("❌ No se encontró ningún modelo que soporte generateContent.")
        print("   Posibles causas: La API no está bien habilitada o el proyecto no tiene acceso.")
    else:
        print("📚 Modelos disponibles (que soportan generateContent):")
        for m in modelos_generativos:
            print(f"   - {m.name}")

        # Intentar elegir un modelo conocido y estable
        nombres_preferidos = [
            'models/gemini-1.5-flash-001',
            'models/gemini-1.0-pro-001',
            'models/gemini-1.5-flash',
            'models/gemini-pro',
        ]

        modelo_elegido = None
        for nombre_preferido in nombres_preferidos:
            if any(m.name == nombre_preferido for m in modelos_generativos):
                modelo_elegido = nombre_preferido
                print(f"✅ Usando modelo preferido: {modelo_elegido}")
                break

        if not modelo_elegido and modelos_generativos:
            modelo_elegido = modelos_generativos[0].name
            print(f"⚠️ Usando el primer modelo disponible: {modelo_elegido}")

        if modelo_elegido:
            model = genai.GenerativeModel(modelo_elegido)
            print(f"🎯 Modelo configurado: {modelo_elegido}")
        else:
            print("❌ No se pudo configurar ningún modelo.")

except Exception as e:
    print(f"❌ Error crítico al conectar con Gemini: {e}")
    print("   Revisa que la API Key sea correcta y que la Generative Language API esté habilitada en Google Cloud.")
    model = None

# ============================================
# BASE DE DATOS
# ============================================
def init_db():
    conn = sqlite3.connect('bot_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS usuarios
                 (user_id INTEGER PRIMARY KEY, 
                  nombre TEXT,
                  primera_vez TIMESTAMP)''')
    c.execute('''CREATE TABLE IF NOT EXISTS registros
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  fecha DATE,
                  mente INTEGER,
                  alma INTEGER,
                  cuerpo INTEGER,
                  notas TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS conversaciones
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  user_id INTEGER,
                  timestamp TIMESTAMP,
                  mensaje_usuario TEXT,
                  respuesta_bot TEXT)''')
    conn.commit()
    conn.close()

def guardar_registro(user_id, mente, alma, cuerpo, notas=""):
    conn = sqlite3.connect('bot_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO registros (user_id, fecha, mente, alma, cuerpo, notas) VALUES (?, date('now'), ?, ?, ?, ?)",
              (user_id, mente, alma, cuerpo, notas))
    conn.commit()
    conn.close()

def guardar_conversacion(user_id, mensaje, respuesta):
    conn = sqlite3.connect('bot_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO conversaciones (user_id, timestamp, mensaje_usuario, respuesta_bot) VALUES (?, datetime('now'), ?, ?)",
              (user_id, mensaje, respuesta))
    conn.commit()
    conn.close()

def obtener_ultimos_registros(user_id, dias=7):
    conn = sqlite3.connect('bot_data.db')
    c = conn.cursor()
    c.execute("SELECT fecha, mente, alma, cuerpo FROM registros WHERE user_id = ? ORDER BY fecha DESC LIMIT ?",
              (user_id, dias))
    resultados = c.fetchall()
    conn.close()
    return resultados

# ============================================
# COMANDOS DEL BOT
# ============================================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    conn = sqlite3.connect('bot_data.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO usuarios (user_id, nombre, primera_vez) VALUES (?, ?, datetime('now'))",
              (user.id, user.first_name))
    conn.commit()
    conn.close()
    await update.message.reply_text(
        f"🌟 *Hola {user.first_name}!*\n\n"
        "Soy tu *Entrenador Consciente*. Puedes hablarme como a un amigo.\n\n"
        "📌 *Comandos:*\n"
        "/checkin - Registro rápido de mente/alma/cuerpo\n"
        "/stats - Ver tus últimos registros\n"
        "/grafica - Ver gráfica de evolución\n"
        "/reset - Reiniciar conversación\n\n"
        "✨ *O simplemente háblame*: cuéntame cómo estás.",
        parse_mode="Markdown"
    )

async def checkin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['checkin_paso'] = 'mente'
    await update.message.reply_text(
        "🌅 *CHECK-IN*\n\n1. *MENTE*: ¿Cómo está tu claridad hoy? (1-10)",
        parse_mode="Markdown"
    )

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    registros = obtener_ultimos_registros(user_id, 7)
    if not registros:
        await update.message.reply_text("Aún no tienes registros. Usa /checkin para empezar.")
        return
    mensaje = "📊 *TUS ÚLTIMOS REGISTROS*\n\n"
    for fecha, mente, alma, cuerpo in registros:
        mensaje += f"📅 {fecha}\n🧠 {mente} | ❤️ {alma} | 💪 {cuerpo}\n\n"
    await update.message.reply_text(mensaje, parse_mode="Markdown")

async def grafica(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    registros = obtener_ultimos_registros(user_id, 14)
    if len(registros) < 2:
        await update.message.reply_text("Necesito al menos 2 registros para graficar.")
        return
    fechas = [r[0] for r in reversed(registros)]
    mente = [r[1] for r in reversed(registros)]
    alma = [r[2] for r in reversed(registros)]
    cuerpo = [r[3] for r in reversed(registros)]
    plt.figure(figsize=(10, 5))
    plt.plot(fechas, mente, marker='o', label='Mente', color='blue')
    plt.plot(fechas, alma, marker='o', label='Alma', color='red')
    plt.plot(fechas, cuerpo, marker='o', label='Cuerpo', color='green')
    plt.title('Evolución Mente-Alma-Cuerpo')
    plt.xlabel('Fecha')
    plt.ylabel('Nivel (1-10)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    await update.message.reply_photo(photo=buf, caption="📈 Tu evolución")

async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await update.message.reply_text("🔄 Conversación reiniciada.")

async def manejar_mensaje(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    texto = update.message.text
    user = update.effective_user

    # Verificar checkin
    if 'checkin_paso' in context.user_data:
        paso = context.user_data['checkin_paso']
        try:
            numero = int(texto)
            if numero < 1 or numero > 10:
                raise ValueError
        except:
            await update.message.reply_text("Responde con un número del 1 al 10.")
            return
        if paso == 'mente':
            context.user_data['mente_temp'] = numero
            context.user_data['checkin_paso'] = 'alma'
            await update.message.reply_text("2. *ALMA*: ¿Cómo está tu energía emocional? (1-10)", parse_mode="Markdown")
        elif paso == 'alma':
            context.user_data['alma_temp'] = numero
            context.user_data['checkin_paso'] = 'cuerpo'
            await update.message.reply_text("3. *CUERPO*: ¿Cómo está tu vitalidad física? (1-10)", parse_mode="Markdown")
        elif paso == 'cuerpo':
            guardar_registro(user_id, 
                           context.user_data['mente_temp'],
                           context.user_data['alma_temp'],
                           numero)
            context.user_data.pop('checkin_paso')
            await update.message.reply_text("✅ *¡Registro completado!*", parse_mode="Markdown")
        return

    # Si no es checkin, usar Gemini (si está disponible)
    if model is None:
        await update.message.reply_text("La IA no está disponible en este momento. Puedes usar /checkin para registrar.")
        return

    try:
        ultimos = obtener_ultimos_registros(user_id, 3)
        contexto = ""
        if ultimos:
            contexto = "\nRegistros recientes:\n"
            for fecha, mente, alma, cuerpo in ultimos:
                contexto += f"- {fecha}: Mente {mente}, Alma {alma}, Cuerpo {cuerpo}\n"
        prompt = f"""Eres un entrenador consciente, empático pero sincero.
Nombre del usuario: {user.first_name}
{contexto}
Instrucciones:
- Responde en el MISMO IDIOMA que el usuario use
- Máximo 3 oraciones
- Sé cálido pero directo
- Haz preguntas que inviten a reflexionar
Mensaje: {texto}
Respuesta:"""
        respuesta = model.generate_content(prompt)
        respuesta_texto = respuesta.text
        guardar_conversacion(user_id, texto, respuesta_texto)
        await update.message.reply_text(respuesta_texto)
    except Exception as e:
        await update.message.reply_text("Perdón, tuve un problema. ¿Puedes repetir?")
        print(f"Error: {e}")

# ============================================
# INICIAR BOT
# ============================================
def main():
    init_db()
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("checkin", checkin))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("grafica", grafica))
    app.add_handler(CommandHandler("reset", reset))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, manejar_mensaje))
    print("🤖 BOT INICIADO! Busca tu bot en Telegram.")
    app.run_polling()

if __name__ == "__main__":
    main()