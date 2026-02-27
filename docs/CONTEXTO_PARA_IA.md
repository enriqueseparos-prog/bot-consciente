 # CONTEXTO COMPLETO PARA IAS - BOT CONSCIENTE v5.0

## 📋 INFORMACIÓN GENERAL
- **Proyecto:** Bot de Telegram para desarrollo personal
- **Creador:** Kike
- **Fecha:** 27/02/2026
- **Repositorio:** https://github.com/enriqueseparos-prog/bot-consciente

## 🏗️ ESTRUCTURA COMPLETA DEL PROYECTO

📁 bot-consciente/
├── 📁 src/ # Código fuente
│ ├── 📁 core/ # Núcleo del sistema
│ │ ├── habitos.py # 26 hábitos con prioridades
│ │ ├── maestros.py # 25+ maestros (externos, internos, civilizaciones)
│ │ ├── protocolos.py # Rescate, flujos, valores
│ │ ├── sistema.py # Filosofía v3.1 (cubos, semillas)
│ │ └── prompts.py # 3 prompts completos (técnico, empático, biografía)
│ ├── 📁 escala/ # Sistema de vibración
│ │ ├── alta_vibracion.py
│ │ ├── baja_vibracion.py
│ │ └── detector_vibracional.py
│ ├── 📁 confrontacion/ # Detectores, modos y frases
│ │ ├── detectores.py
│ │ ├── modos.py
│ │ └── frases.py
│ ├── 📁 puntos_14/ # Los 14 puntos filosóficos
│ │ ├── grupo1.py (puntos 1-3)
│ │ ├── grupo2.py (puntos 4-6)
│ │ ├── grupo3.py (puntos 7-9)
│ │ ├── grupo4.py (puntos 10-12)
│ │ └── grupo5.py (puntos 13-14)
│ ├── 📁 memoria/ # Sistema de memoria
│ │ ├── perfil.py # ✅ Perfil básico de usuario
│ │ ├── entidades.py # 🔴 Pendiente - Relaciona conceptos
│ │ ├── aprendizaje.py # 🔴 Pendiente - El bot mejora con feedback
│ │ ├── recordatorios.py # 🔴 Pendiente - Mensajes programados
│ │ ├── patrones.py # 🟠 Pendiente - Detecta patrones semanales
│ │ └── vectorial.py # 🟡 Pendiente - Búsqueda semántica
│ ├── 📁 rag/ # Retrieval Augmented Generation
│ │ ├── vector_store.py # 🟡 Pendiente - ChromaDB
│ │ └── buscador.py # 🟡 Pendiente - Búsqueda semántica
│ ├── 📁 web/ # Interfaz web
│ │ ├── dashboard.html # 🟡 Pendiente - Visualización de progreso
│ │ └── pages/ # 🟡 Pendiente - Páginas estáticas por tema
│ ├── 📁 utils/ # Utilidades
│ │ ├── microdosis.py # ✅ Listo - Versiones mínimas de hábitos
│ │ ├── feedback.py # 🔴 Pendiente - Preguntar si sirvió
│ │ ├── sugerencias.py # 🟠 Pendiente - Ofrecer opciones
│ │ ├── buscar.py # 🟡 Pendiente - Búsqueda en Google
│ │ ├── voz.py # 🟡 Pendiente - Procesamiento de audio
│ │ ├── pdf.py # 🟡 Pendiente - Generación de PDFs
│ │ └── calendario.py # 🟢 Futuro - Integración con calendarios
│ └── 📁 grupos/ # Múltiples usuarios
│ └── accountability.py # 🟢 Futuro - Modo grupo
│
├── 📁 knowledge/ # Base de conocimiento
│ ├── 📁 habitos/ # 26 investigaciones (✅ completas)
│ ├── 📁 maestros/ # 19+ biografías (✅ completas)
│ ├── 📁 planes/ # Planes de 31 días (⚪ vacío)
│ ├── 📁 prompts/ # Prompts en .txt (⚪ vacío)
│ ├── 📁 protocolos/ # Protocolos guardados (⚪ vacío)
│ └── 📁 escala/ # Documentación de vibración (⚪ vacío)
│
├── 📁 data/ # Datos de usuario
│ ├── bot_data.db # Base de datos SQLite (✅)
│ └── 📁 diarios/ # Diarios privados por usuario (✅)
│
├── 📁 docs/ # Documentación
│ ├── 📁 cuentas/ # Gestión de claves (✅)
│ ├── 📁 marcos_teoricos/ # Escala, 14 puntos, confrontación (✅)
│ ├── 📁 sistemas_completos/ # Respaldos de prompts y sistemas (✅)
│ ├── 📁 planificacion/ # Planes maestros (✅)
│ └── CONTEXTO_PARA_IA.md # Este archivo (✅)
│
├── 📁 scripts/ # Herramientas
│ └── generar_investigaciones.py # Generador de conocimiento (✅)
│
├── .env # Claves API (✅)
├── .gitignore # Archivos ignorados (✅)
├── requirements.txt # Dependencias (✅)
└── bot.py # Orquestador principal (✅)

text

## ✅ LO QUE YA ESTÁ LISTO
- ✅ 26 hábitos con prioridades (`habitos.py`)
- ✅ 25+ maestros (externos, internos, civilizaciones) (`maestros.py`)
- ✅ 14 puntos filosóficos (5 archivos en `puntos_14/`)
- ✅ Escala Hawking (alta/baja vibración) (`escala/`)
- ✅ Confrontación (detectores, modos, frases) (`confrontacion/`)
- ✅ Perfil de usuario básico (`memoria/perfil.py`)
- ✅ Microdosis (`utils/microdosis.py`)
- ✅ 26 investigaciones en `knowledge/habitos/`
- ✅ 19+ biografías en `knowledge/maestros/`
- ✅ 5 proveedores IA (Groq, Gemini, Cerebras, DeepSeek, OpenRouter)
- ✅ Bot funcional con Python 3.11

## 🔴 PRIORIDAD 1 (PENDIENTE INMEDIATO)
1. **Integrar 14 puntos** en `manejar_mensaje` (`bot.py`)
2. **Activar confrontación** según vibración
3. **Crear memoria de entidades** (`src/memoria/entidades.py`)
4. **Implementar feedback loop** (`src/utils/feedback.py`)
5. **Recordatorios programados** (`src/memoria/recordatorios.py`)
6. **Mejorar detector de cambio de tema** (`confrontacion/detectores.py`)

## 🟠 PRIORIDAD 2
7. **Sugerencias proactivas** (`utils/sugerencias.py`)
8. **Detector de patrones semanales** (`memoria/patrones.py`)
9. **Dashboard web básico** (`web/dashboard.html`)
10. **Páginas estáticas para investigaciones** (`web/pages/`)

## 🟡 PRIORIDAD 3
11. **RAG vectorial con ChromaDB** (`rag/vector_store.py`)
12. **Búsqueda en Google** (`utils/buscar.py`)
13. **Generación de PDFs** (`scripts/generar_pdf.py`)
14. **Aprendizaje automático (feedback)** (`memoria/aprendizaje.py`)
15. **Estadísticas avanzadas** (`utils/estadisticas.py`)

## 🟢 PRIORIDAD 4 (FUTURO)
16. **Voz a texto** (`utils/voz.py`)
17. **Múltiples usuarios** (`grupos/`)
18. **Exportar informes** (`scripts/generar_informe.py`)
19. **Integración con Google Calendar** (`utils/calendario.py`)
20. **Modo grupo / accountability** (`grupos/accountability.py`)
21. **Web app completa** (`web/app.py`)
22. **Hosting 24/7 en Railway** (`railway.json`)

## 🧠 SISTEMA DE MEMORIA COMPLETO
| Tipo | Función | Archivo | Estado |
|------|---------|---------|--------|
| Conversación | Guarda cada interacción | BD (`conversaciones`) | ✅ |
| Perfil | Datos del usuario | `perfil.py` | ✅ |
| Entidades | Relaciona conceptos | `entidades.py` | 🔴 |
| Temas | Frecuencia de temas | `perfil.py` | ⚠️ |
| Aprendizaje | El bot mejora | `aprendizaje.py` | 🔴 |
| Patrones | Detecta tendencias | `patrones.py` | 🟠 |
| Vectorial | Búsqueda semántica | `vectorial.py` | 🟡 |
| Recordatorios | Mensajes programados | `recordatorios.py` | 🔴 |

## 🎯 FILOSOFÍA CENTRAL DEL BOT
- El bot debe **PREGUNTAR, no ordenar**
- Textos largos van a **archivos .txt**
- Prioridad: **coherencia > velocidad**
- Usar los **14 puntos** para profundidad filosófica
- Usar **escala Hawking** para detectar estado
- **Confrontación adaptativa** según contexto

## 📚 DOCUMENTACIÓN ADICIONAL
- **Sistema completo:** `docs/sistemas_completos/`
- **Marcos teóricos:** `docs/marcos_teoricos/`
- **Planificación maestra:** `docs/planificacion/PLAN_MAESTRO_COMPLETO.md`
- **Contexto para IAs:** `docs/CONTEXTO_PARA_IA.md` (este archivo)

## 🚀 INSTRUCCIÓN PARA LA IA
Trabajar con **coherencia total**. Todo el código debe integrarse sin romper lo existente. Las decisiones ya están tomadas:

✅ Modularidad (cada cosa en su archivo)
✅ Multi-IA (5 proveedores con fallback)
✅ Conocimiento en `knowledge/` (archivos .txt)
✅ Prioridad en experiencia de usuario
✅ Sistema filosófico propio (14 puntos, escala Hawking)

**Preguntar si hay dudas antes de generar código. Mantener el estilo y las convenciones del proyecto.**