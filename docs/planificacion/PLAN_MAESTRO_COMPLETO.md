? **PLAN MAESTRO DEFINITIVO - BOT CONSCIENTE v5.0**  
*(Versión 27/02/2026 - Incluye TODO lo hablado)*

---

## ?? **PARTE 1: ESTRUCTURA COMPLETA DEL PROYECTO**

```
?? bot-consciente/
+-- ?? src/                          # Código fuente
¦   +-- ?? core/                     # Núcleo del sistema
¦   ¦   +-- habitos.py               # 26 hábitos con prioridades
¦   ¦   +-- maestros.py              # 25+ maestros (externos, internos, civilizaciones)
¦   ¦   +-- protocolos.py            # Rescate, flujos, valores
¦   ¦   +-- sistema.py               # Filosofía v3.1 (cubos, semillas)
¦   ¦   +-- prompts.py               # 3 prompts completos
¦   +-- ?? escala/                    # Sistema de vibración
¦   ¦   +-- alta_vibracion.py
¦   ¦   +-- baja_vibracion.py
¦   ¦   +-- detector_vibracional.py
¦   +-- ?? confrontacion/             # Detectores, modos y frases
¦   ¦   +-- detectores.py
¦   ¦   +-- modos.py
¦   ¦   +-- frases.py
¦   +-- ?? puntos_14/                  # Los 14 puntos filosóficos
¦   ¦   +-- grupo1.py (puntos 1-3)
¦   ¦   +-- grupo2.py (puntos 4-6)
¦   ¦   +-- grupo3.py (puntos 7-9)
¦   ¦   +-- grupo4.py (puntos 10-12)
¦   ¦   +-- grupo5.py (puntos 13-14)
¦   +-- ?? memoria/                    # Sistema de memoria completo
¦   ¦   +-- perfil.py                  # Perfil básico de usuario (? listo)
¦   ¦   +-- entidades.py                # Memoria de relaciones (?? pendiente)
¦   ¦   +-- aprendizaje.py               # El bot mejora con feedback (?? pendiente)
¦   ¦   +-- recordatorios.py             # Recordatorios programados (?? pendiente)
¦   ¦   +-- patrones.py                   # Detecta patrones semanales (?? pendiente)
¦   ¦   +-- vectorial.py                   # Búsqueda semántica (?? pendiente)
¦   +-- ?? rag/                         # Retrieval Augmented Generation
¦   ¦   +-- vector_store.py              # ChromaDB (?? pendiente)
¦   ¦   +-- buscador.py                   # Búsqueda semántica (?? pendiente)
¦   +-- ?? web/                          # Interfaz web (futuro)
¦   ¦   +-- dashboard.html                # Visualización de progreso (?? pendiente)
¦   ¦   +-- pages/                         # Páginas estáticas por tema (?? pendiente)
¦   ¦   +-- templates/                      # Plantillas HTML (?? pendiente)
¦   +-- ?? utils/                         # Utilidades
¦   ¦   +-- microdosis.py                  # Versiones mínimas (? listo)
¦   ¦   +-- feedback.py                     # Preguntar si sirvió (?? pendiente)
¦   ¦   +-- sugerencias.py                   # Ofrecer opciones (?? pendiente)
¦   ¦   +-- buscar.py                         # Búsqueda en Google (?? pendiente)
¦   ¦   +-- voz.py                             # Procesamiento de audio (?? pendiente)
¦   ¦   +-- pdf.py                              # Generación de PDFs (?? pendiente)
¦   ¦   +-- calendario.py                        # Integración con calendarios (?? futuro)
¦   +-- ?? grupos/                         # Múltiples usuarios (?? futuro)
¦       +-- accountability.py                 # Modo grupo
¦
+-- ?? knowledge/                        # Base de conocimiento
¦   +-- ?? habitos/                      # 26 investigaciones (? listo)
¦   +-- ?? maestros/                      # 19+ biografías (? listo)
¦   +-- ?? planes/                         # Planes de 31 días (? vacío)
¦   +-- ?? prompts/                         # Prompts en .txt (? vacío)
¦   +-- ?? protocolos/                       # Protocolos guardados (? vacío)
¦   +-- ?? escala/                           # Documentación de vibración (? vacío)
¦
+-- ?? data/                              # Datos de usuario
¦   +-- bot_data.db                         # Base de datos SQLite (?)
¦   +-- ?? diarios/                          # Diarios privados por usuario (?)
¦
+-- ?? docs/                               # Documentación
¦   +-- ?? cuentas/                          # Gestión de claves (?)
¦   +-- ?? marcos_teoricos/                  # Escala, 14 puntos, confrontación (?)
¦   +-- ?? sistemas_completos/                # Respaldos de prompts y sistemas (?)
¦   +-- PLAN_MAESTRO.md                       # Este documento (?)
¦
+-- ?? scripts/                            # Herramientas
¦   +-- generar_investigaciones.py           # Generador de conocimiento (?)
¦
+-- .env                                    # Claves API (?)
+-- .gitignore                              # Archivos ignorados (?)
+-- requirements.txt                         # Dependencias (?)
+-- bot.py                                   # Orquestador principal (?)
```

---

## ?? **PARTE 2: SISTEMA DE MEMORIA COMPLETO**

| Tipo de Memoria | Función | Archivo | Estado |
|-----------------|---------|---------|--------|
| **Conversación** | Guarda cada interacción | `conversaciones` en BD | ? |
| **Perfil** | Datos del usuario (rachas, hábitos) | `src/memoria/perfil.py` | ? |
| **Entidades** | Relaciona conceptos ("Mike" = "Mike Mentzer") | `src/memoria/entidades.py` | ?? Pendiente |
| **Temas** | Frecuencia de temas hablados | `src/memoria/perfil.py` | ?? Mejorable |
| **Aprendizaje** | El bot mejora con feedback | `src/memoria/aprendizaje.py` | ?? Pendiente |
| **Patrones** | Detecta "los lunes tu mente baja" | `src/memoria/patrones.py` | ?? Pendiente |
| **Vectorial** | Búsqueda semántica en knowledge | `src/rag/vector_store.py` | ?? Pendiente |
| **Recordatorios** | Mensajes programados | `src/memoria/recordatorios.py` | ?? Pendiente |

---

## ?? **PARTE 3: PLAN DE ACCIÓN POR PRIORIDAD**

### ?? **PRIORIDAD 1 - COHERENCIA (Esta semana)**

| # | Tarea | Archivo | Tiempo |
|---|-------|---------|--------|
| 1 | **Integrar 14 puntos** en `manejar_mensaje` | `bot.py` | 30 min |
| 2 | **Activar confrontación** según vibración | `manejar_mensaje` | 30 min |
| 3 | **Crear memoria de entidades** | `src/memoria/entidades.py` | 30 min |
| 4 | **Mejorar detector de cambio de tema** | `src/confrontacion/detectores.py` | 30 min |
| 5 | **Implementar feedback loop** | `src/utils/feedback.py` | 1 hora |
| 6 | **Probar todo en Telegram** | - | 1 hora |

### ?? **PRIORIDAD 2 - FUNCIONALIDAD (Próxima semana)**

| # | Tarea | Archivo | Tiempo |
|---|-------|---------|--------|
| 7 | **Recordatorios programados** | `src/memoria/recordatorios.py` | 1 hora |
| 8 | **Sugerencias proactivas** | `src/utils/sugerencias.py` | 1 hora |
| 9 | **Detector de patrones semanales** | `src/memoria/patrones.py` | 1.5 horas |
| 10 | **Dashboard web básico** | `web/dashboard.html` | 2 horas |
| 11 | **Páginas estáticas para investigaciones** | `web/pages/` | 2 horas |

### ?? **PRIORIDAD 3 - EXPANSIÓN (Mes 1)**

| # | Tarea | Archivo | Tiempo |
|---|-------|---------|--------|
| 12 | **RAG vectorial con ChromaDB** | `src/rag/vector_store.py` | 2 horas |
| 13 | **Búsqueda en Google** | `src/utils/buscar.py` | 2 horas |
| 14 | **Generación de PDFs** | `scripts/generar_pdf.py` | 2 horas |
| 15 | **Aprendizaje automático (feedback)** | `src/memoria/aprendizaje.py` | 2 horas |
| 16 | **Estadísticas avanzadas** | `src/utils/estadisticas.py` | 2 horas |

### ?? **PRIORIDAD 4 - FUTURO (Mes 2-3)**

| # | Tarea | Archivo |
|---|-------|---------|
| 17 | **Voz a texto** | `src/utils/voz.py` |
| 18 | **Múltiples usuarios** | `src/grupos/` |
| 19 | **Exportar informes** | `scripts/generar_informe.py` |
| 20 | **Integración con Google Calendar** | `src/utils/calendario.py` |
| 21 | **Modo grupo / accountability** | `src/grupos/accountability.py` |
| 22 | **Web app completa** | `web/app.py` |
| 23 | **Hosting 24/7 en Railway** | `railway.json` |

---

## ?? **PARTE 4: CONTEXTO PARA OTROS CHATS**

Para no saturar este chat, podés usar este mensaje en otro:

```
--- CONTEXTO MAESTRO - BOT CONSCIENTE v5.0 ---

CREADOR: Kike
FECHA: 27/02/2026
PROPÓSITO: Bot de Telegram para desarrollo personal con 26 hábitos, 25+ maestros, 14 puntos, escala Hawking y confrontación adaptativa.

ESTADO ACTUAL:
? Estructura completa (ver árbol abajo)
? 5 proveedores IA (Groq, Gemini, Cerebras, DeepSeek, OpenRouter)
? 26 investigaciones en knowledge/habitos/
? 19+ biografías en knowledge/maestros/
? Bot funcional con Python 3.11

PENDIENTE PRIORIDAD 1:
- Integrar 14 puntos en conversación
- Activar confrontación
- Crear memoria de entidades
- Implementar feedback loop
- Recordatorios programados

ESTRUCTURA:
[pegar el árbol de carpetas de la Parte 1]

INSTRUCCIÓN: Trabajar con coherencia. Todo el código debe integrarse sin romper lo existente. Las decisiones ya están tomadas: modularidad, multi-IA, conocimiento en knowledge/, prioridad en experiencia de usuario.
```

**Elegí UNA y arrancamos.**
