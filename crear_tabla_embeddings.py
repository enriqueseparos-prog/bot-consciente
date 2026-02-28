# crear_tabla_embeddings.py - Crea la tabla de embeddings

import sqlite3
import os

DB_PATH = os.path.join('data', 'bot_data.db')

print(f"🔧 Creando tabla embeddings en {DB_PATH}")

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

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

conn.commit()
conn.close()

print("✅ Tabla 'embeddings' creada correctamente")