# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
Script para generar investigaciones de habitos usando multiples IAs
Uso: python scripts/generar_investigaciones.py --tema "flexibilidad" --tipo "tecnico"
     python scripts/generar_investigaciones.py --lista "flexibilidad,decisiones,pnl" --tipo "empatico"
"""

import asyncio
import argparse
import os
import sys
from pathlib import Path

# Agregar el directorio raiz al path para poder importar config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from src.config import ai_client
except ImportError as e:
    print(f"? Error importando config: {e}")
    print("Asegurate de que el archivo src/config.py existe")
    sys.exit(1)

# Prompts para investigacion
PROMPT_TECNICO = """Actua como un Arquitecto de Sistemas de Alto Rendimiento y Cientifico de la Encarnacion.

Tu tarea es generar una INVESTIGACION EXHAUSTIVA sobre el habito: {tema}

[MARCO OBLIGATORIO: FORMULA DE SOBERANIA]
B = P(T + M3 + XR)C

DONDE:
- B (Beneficio): El resultado soberano, la transformacion obtenida.
- P (Precio): El sacrificio consciente, el "por que" profundo.
- T (Tiempo): La metodologia exacta, la cronometria, los ciclos optimos.
- M3 (Tridimensionalidad): Mente, Cuerpo, Alma.
- XR (Recursos): Material, Economico, Energia, Espacial.
- C (Constancia): El multiplicador ritmico.

[PERFILES DE USUARIO - INCLUIR]
- BRONCE: Principiante, parte de cero, busca orden y disciplina
- PLATA: Intermedio, tiene base, busca optimizacion
- ORO: Avanzado, domina lo tecnico, busca trascendencia

ESTRUCTURA OBLIGATORIA:
PARTE 1: FUNDACIONES DEL HABITO (Contexto y Filosofia)
PARTE 2: INGENIERIA TECNICA (El Como)
PARTE 3: CAPACIDADES Y RENDIMIENTO
PARTE 4: NEUROCIENCIA Y FISIOLOGIA
PARTE 5: COMBUSTIBLE Y RECUPERACION
PARTE 6: HERRAMIENTAS Y ENTORNO
PARTE 7: INTERFERENCIAS (Ruido de Sistema)
PARTE 8: INTEGRACION Y TRASCENDENCIA
PARTE 9: ANALISIS POR FORMULA DE SOBERANIA
PARTE 10: DECISION DEL ARQUITECTO

Inclui TABLAS donde sea relevante. Se directo, practico y profundo.
"""

PROMPT_EMPATICO = """Actua como un Arquitecto de Sistemas de Alto Rendimiento, con especializacion en Psicologia Humanista, Relaciones Conscientes y Filosofia del Disfrute.

Tu tarea es generar una INVESTIGACION EXHAUSTIVA Y EMPATICA sobre: {tema}

[MARCO OBLIGATORIO: FORMULA DE SOBERANIA APLICADA A LA VIDA COTIDIANA]
B = P(T + M3 + XR)C

DONDE:
- B (Beneficio): Paz interior, conexion genuina, disfrute del proceso.
- P (Precio): El sacrificio consciente de la queja, la culpa, la reactividad.
- T (Tiempo): La calidad del tiempo, momentos de presencia plena.
- M3: Mente (comunicacion), Cuerpo (presencia fisica), Alma (conexion genuina).
- XR: Recursos emocionales y practicos.
- C (Constancia): La frecuencia de la presencia consciente.

[PERFILES DE USUARIO - ADAPTADOS]
- BRONCE: Sobrevive, reacciona, actua por obligacion
- PLATA: Gestiona con conciencia, elige estar presente
- ORO: Encarna, disfruta, conecta desde el alma

ESTRUCTURA OBLIGATORIA:
PARTE 1: FUNDACIONES DEL HABITO (Contexto y Filosofia)
PARTE 2: INGENIERIA DE LA PRESENCIA
PARTE 3: CAPACIDADES EMOCIONALES Y RELACIONALES
PARTE 4: NEUROCIENCIA Y FISIOLOGIA DE LA CONEXION
PARTE 5: COMBUSTIBLE PARA LA PRESENCIA
PARTE 6: HERRAMIENTAS Y ENTORNO
PARTE 7: INTERFERENCIAS (Ruido de Sistema)
PARTE 8: INTEGRACION Y TRASCENDENCIA
PARTE 9: ANALISIS POR FORMULA DE SOBERANIA
PARTE 10: DECISION DEL ARQUITECTO

Inclui TABLAS. Se calido, humano, como si le hablaras a un amigo.
"""

async def generar_investigacion(tema, tipo="tecnico"):
    """Genera una investigacion usando el sistema multi-IA"""
    
    # Elegir prompt segun tipo
    if tipo == "tecnico":
        prompt = PROMPT_TECNICO.format(tema=tema)
        print(f"?? Usando prompt TECNICO para: {tema}")
    else:
        prompt = PROMPT_EMPATICO.format(tema=tema)
        print(f"?? Usando prompt EMPATICO para: {tema}")
    
    print(f"?? Enviando solicitud a IA...")
    
    try:
        respuesta = await ai_client.get_completion(
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=4000
        )
        print(f"? Respuesta recibida ({len(respuesta)} caracteres)")
        return respuesta
    except Exception as e:
        print(f"? Error generando investigacion: {e}")
        return None

def guardar_investigacion(tema, contenido, tipo):
    """Guarda la investigacion en la carpeta knowledge/habitos/"""
    
    # Crear nombre de archivo (ej: flexibilidad.txt)
    nombre_archivo = tema.lower().replace(" ", "_").replace("(", "").replace(")", "")
    ruta = Path(f"knowledge/habitos/{nombre_archivo}.txt")
    
    # Asegurar que la carpeta existe
    ruta.parent.mkdir(parents=True, exist_ok=True)
    
    # Guardar
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(f"# INVESTIGACION: {tema.upper()}\n")
        f.write(f"# Tipo: {tipo}\n")
        f.write(f"# Generado: {asyncio.get_event_loop().time()}\n\n")
        f.write(contenido)
    
    print(f"? Investigacion guardada en: {ruta}")
    return ruta

async def main():
    parser = argparse.ArgumentParser(description="Generar investigaciones de habitos")
    parser.add_argument("--tema", help="Tema especifico a investigar")
    parser.add_argument("--lista", help="Lista de temas separados por comas")
    parser.add_argument("--tipo", default="tecnico", choices=["tecnico", "empatico"], 
                       help="Tipo de investigacion (tecnico o empatico)")
    
    args = parser.parse_args()
    
    if not args.tema and not args.lista:
        print("? Debes especificar --tema o --lista")
        print("Ejemplo: python scripts/generar_investigaciones.py --tema 'flexibilidad'")
        print("Ejemplo: python scripts/generar_investigaciones.py --lista 'flexibilidad,decisiones,pnl'")
        return
    
    temas = []
    if args.lista:
        temas = [t.strip() for t in args.lista.split(",")]
    else:
        temas = [args.tema]
    
    print(f"\n?? Iniciando generacion de {len(temas)} investigacion(es)...")
    print(f"?? Tipo: {args.tipo}")
    print(f"?? Temas: {temas}")
    
    print(f"\n{'='*50}")
    print(f"?? Usando proveedor: {ai_client.default_provider if hasattr(ai_client, 'default_provider') else 'desconocido'}")
    print(f"{'='*50}")
    
    for tema in temas:
        print(f"\n{'='*50}")
        print(f"?? Procesando: {tema}")
        contenido = await generar_investigacion(tema, args.tipo)
        
        if contenido:
            guardar_investigacion(tema, contenido, args.tipo)
            print(f"? {tema} completado")
        else:
            print(f"? No se pudo generar investigacion para: {tema}")
        
        # Pequena pausa entre investigaciones para no saturar
        if len(temas) > 1:
            print("? Esperando 2 segundos antes de la siguiente...")
            await asyncio.sleep(2)
    
    print("\n? Proceso completado!")

if __name__ == "__main__":
    asyncio.run(main())