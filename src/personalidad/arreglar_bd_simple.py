# arreglar_bd_simple.py - Agrega la columna proveedor
import sqlite3
import os

db_path = 'data/bot_data.db'

if not os.path.exists(db_path):
    print("No se encuentra la base de datos")
    exit(1)

conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("PRAGMA table_info(conversaciones)")
columnas = c.fetchall()
nombres = [col[1] for col in columnas]
print(f"Columnas actuales: {nombres}")

if 'proveedor' not in nombres:
    c.execute("ALTER TABLE conversaciones ADD COLUMN proveedor TEXT")
    print("Columna 'proveedor' agregada")
else:
    print("La columna 'proveedor' ya existe")

conn.commit()
conn.close()
print("Listo.")