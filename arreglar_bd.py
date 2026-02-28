# arreglar_bd.py - Agrega la columna proveedor a la tabla conversaciones

import sqlite3
import os

# Ruta a la base de datos
db_path = 'data/bot_data.db'

# Verificar que la base de datos existe
if not os.path.exists(db_path):
    print(f"? No se encuentra la base de datos en {db_path}")
    exit(1)

# Conectar a la base de datos
conn = sqlite3.connect(db_path)
c = conn.cursor()

# Ver qué columnas tiene actualmente
c.execute("PRAGMA table_info(conversaciones)")
columnas = c.fetchall()
nombres = [col[1] for col in columnas]
print(f"?? Columnas actuales: {', '.join(nombres)}")

# Agregar la columna proveedor si no existe
if 'proveedor' not in nombres:
    try:
        c.execute("ALTER TABLE conversaciones ADD COLUMN proveedor TEXT")
        print("? Columna 'proveedor' agregada correctamente")
    except sqlite3.OperationalError as e:
        print(f"? Error: {e}")
else:
    print("? La columna 'proveedor' ya existe")

# Verificar que ahora está
c.execute("PRAGMA table_info(conversaciones)")
columnas = c.fetchall()
nombres = [col[1] for col in columnas]
print(f"?? Columnas finales: {', '.join(nombres)}")

conn.close()
print("\n?? Listo. Ya podés ejecutar el bot.")