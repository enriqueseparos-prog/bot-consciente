# verificar_bd.py - Verifica y arregla la base de datos

import sqlite3
import os

db_path = 'data/bot_data.db'

print("🔍 VERIFICANDO BASE DE DATOS")
print("===========================")

# 1. Verificar que la BD existe
if not os.path.exists(db_path):
    print(f"❌ No existe la BD en {db_path}")
    exit(1)
else:
    print(f"✅ BD encontrada: {db_path}")

# 2. Conectar
conn = sqlite3.connect(db_path)
c = conn.cursor()

# 3. Ver tablas existentes
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tablas = c.fetchall()
print(f"\n📋 Tablas en la BD: {[t[0] for t in tablas]}")

# 4. Verificar tabla conversaciones
if ('conversaciones',) in tablas:
    print("\n✅ Tabla 'conversaciones' existe")
    
    # Ver columnas actuales
    c.execute("PRAGMA table_info(conversaciones)")
    columnas = c.fetchall()
    nombres = [col[1] for col in columnas]
    print(f"   Columnas actuales: {nombres}")
    
    # Agregar columna proveedor si no existe
    if 'proveedor' not in nombres:
        try:
            c.execute("ALTER TABLE conversaciones ADD COLUMN proveedor TEXT")
            print("   ✅ Columna 'proveedor' AGREGADA")
        except Exception as e:
            print(f"   ❌ Error al agregar: {e}")
    else:
        print("   ✅ Columna 'proveedor' YA EXISTE")
    
    # Verificar nuevamente
    c.execute("PRAGMA table_info(conversaciones)")
    columnas = c.fetchall()
    nombres = [col[1] for col in columnas]
    print(f"   Columnas finales: {nombres}")
    
else:
    print("\n❌ Tabla 'conversaciones' NO existe")
    # Crear la tabla si no existe
    c.execute('''
        CREATE TABLE IF NOT EXISTS conversaciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            fecha TEXT,
            mensaje TEXT,
            respuesta TEXT,
            tema TEXT,
            modo TEXT,
            proveedor TEXT
        )
    ''')
    print("   ✅ Tabla 'conversaciones' CREADA")

# 5. Verificar tabla registros
if ('registros',) in tablas:
    c.execute("PRAGMA table_info(registros)")
    columnas = c.fetchall()
    nombres = [col[1] for col in columnas]
    print(f"\n✅ Tabla 'registros' tiene columnas: {nombres}")
else:
    print("\n❌ Tabla 'registros' NO existe")
    c.execute('''
        CREATE TABLE IF NOT EXISTS registros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            fecha TEXT,
            cuerpo INTEGER,
            mente INTEGER,
            alma INTEGER
        )
    ''')
    print("   ✅ Tabla 'registros' CREADA")

# 6. Verificar tabla feedback
if ('feedback',) in tablas:
    c.execute("PRAGMA table_info(feedback)")
    columnas = c.fetchall()
    nombres = [col[1] for col in columnas]
    print(f"\n✅ Tabla 'feedback' tiene columnas: {nombres}")
else:
    print("\n❌ Tabla 'feedback' NO existe")
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            fecha TEXT,
            sugerencia TEXT,
            respuesta TEXT,
            utilidad INTEGER
        )
    ''')
    print("   ✅ Tabla 'feedback' CREADA")

# Guardar cambios y cerrar
conn.commit()
conn.close()

print("\n🎯 VERIFICACION COMPLETADA")
print("Ahora ejecuta: python bot.py")