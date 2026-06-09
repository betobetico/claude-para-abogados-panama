<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin vive en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de generar output útil. Ejecuta
   /estudiante-derecho:cold-start-interview — lleva unos 10 minutos y todos los comandos dependen de ella.
   Sin configurar, las respuestas serán genéricas y pueden no ajustarse a tus necesidades."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin setup
   son /estudiante-derecho:cold-start-interview y cualquier flag --check-integrations.
3. El setup y cold-start-interview ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta
   antigua de caché (~/.claude/plugins/cache/claude-para-abogados/estudiante-derecho/<version>/CLAUDE.md
   para cualquier versión) pero no en la ruta de config, copiarlo a la ruta de config antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la config. Se reemplaza en cada actualización. Nunca escribir datos de
   usuario aquí.

**Perfil de empresa compartido.** Los datos a nivel de empresa (quién eres, qué haces, dónde operas,
tu postura de riesgo, personas clave) viven en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes del perfil de
práctica de este plugin. Si no existe, el setup de este plugin lo creará.
-->

# Perfil de Práctica — Estudiante de Derecho

*Escrito por la cold-start interview. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/estudiante-derecho:cold-start-interview`.*

---

## Quiénes somos

| Campo | Valor |
|---|---|
| Universidad | [PLACEHOLDER — Universidad de Panamá / USMA / Universidad Latina / ULACIT / Universidad Católica / otra] |
| Licenciatura / Doble titulación | [PLACEHOLDER — Licenciatura en Derecho y Ciencias Políticas / Derecho + Relaciones Internacionales / otra] |
| Año actual | [PLACEHOLDER — 1.o a 5.o de Licenciatura, o posgrado/maestría] |
| Especialización o mención | [PLACEHOLDER — si aplica] |
| Objetivo profesional | [PLACEHOLDER — ejercicio libre, empresa, carrera judicial, Ministerio Público, academia] |

---

## Quién usa esto

**Rol:** Estudiante de Derecho
**Supervisor/a académico/a:** [PLACEHOLDER — nombre del tutor si aplica]

---

## Plan de estudios

*Asignaturas de la Licenciatura en Derecho y Ciencias Políticas — adaptar al plan de estudios de tu universidad.*

| Año | Asignaturas clave | Estado |
|---|---|---|
| 1.o | [PLACEHOLDER — Derecho Romano, Derecho Constitucional, Introducción al Derecho Civil, etc.] | [PLACEHOLDER] |
| 2.o | [PLACEHOLDER — Derecho Penal I, Derecho Administrativo I, Obligaciones y Contratos, etc.] | [PLACEHOLDER] |
| 3.o | [PLACEHOLDER — Derecho Comercial I, Derecho del Trabajo, Derecho Procesal Civil, etc.] | [PLACEHOLDER] |
| 4.o-5.o | [PLACEHOLDER — Derecho Internacional, Derecho Tributario, optativas, tesis/práctica] | [PLACEHOLDER] |

**Asignaturas en curso este semestre:** [PLACEHOLDER]

---

## Método socrático

**Reglas para este plugin cuando el estudiante pide ayuda con un problema jurídico:**

1. **Pregunta** — Plantea una pregunta que dirija al estudiante hacia el concepto relevante
2. **Respuesta** — Espera la respuesta del estudiante
3. **Desafío** — Cuestiona la respuesta: ¿en qué norma se basa? ¿Qué pasa si cambiamos un hecho? ¿Hay excepciones?
4. **NUNCA des la respuesta directamente** — El objetivo es que el estudiante razone y llegue a la conclusión

**Excepciones al método socrático:**
- Si el estudiante pide explícitamente la respuesta ("dime la respuesta", "no quiero pistas")
- Si se trata de un dato puntual (fecha, número de artículo, nombre de tribunal)
- Si el estudiante lleva 3+ intentos sin avanzar — dar una pista más directa

---

## Evaluación IRAC

**Rúbrica para evaluar respuestas del estudiante:**

| Criterio | Peso | Descripción |
|---|---|---|
| **I — Identificación del problema** | [PLACEHOLDER — %] | ¿Identifica correctamente la cuestión jurídica? |
| **R — Regulación aplicable** | [PLACEHOLDER — %] | ¿Cita la norma panameña correcta con artículo preciso? |
| **A — Aplicación al caso** | [PLACEHOLDER — %] | ¿Subsume los hechos en la norma de forma lógica? |
| **C — Conclusión** | [PLACEHOLDER — %] | ¿Llega a una conclusión coherente con el razonamiento? |
| **Citas** | [PLACEHOLDER — %] | ¿Formato correcto de citas legales y jurisprudenciales (Registro Judicial)? |

---

## Esquemas

**Formato de esquemas de estudio:**

| Campo | Valor |
|---|---|
| Nivel de detalle | [PLACEHOLDER — resumen / intermedio / exhaustivo] |
| Formato preferido | [PLACEHOLDER — bullet points / mapa conceptual / tabla / mixto] |
| Fuentes principales | [PLACEHOLDER — manuales, apuntes de clase, legislación] |
| Manuales de referencia | [PLACEHOLDER — editorial, autor, edición] |

---

## Concursos de la carrera judicial

**Preparación de concursos de méritos para la carrera judicial o el Ministerio Público — solo si aplica.**

| Campo | Valor |
|---|---|
| Cargo objetivo | [PLACEHOLDER — Juez de Circuito / Juez Municipal / Magistrado / Fiscal / Personero / Defensor de Oficio / otro] [verificar] |
| Academia/preparador | [PLACEHOLDER] |
| Temario oficial | [PLACEHOLDER — número de temas, fuente del temario] |
| Tipo de ejercicios | [PLACEHOLDER — oral / escrito / dictamen / caso práctico / prueba de conocimientos] |
| Temas estudiados | [PLACEHOLDER — rango] |
| Planificación semanal | [PLACEHOLDER — horas/día, vueltas al temario] |

*Referencia: bases y temarios de los concursos de méritos publicados por el Órgano Judicial / Procuraduría en la Gaceta Oficial [verificar].*

---

## Idoneidad para el ejercicio de la abogacía

*En Panamá el ejercicio de la abogacía requiere el certificado de idoneidad expedido por la
Corte Suprema de Justicia (Sala Cuarta de Negocios Generales), conforme a la legislación que regula
la profesión de abogado [verificar].*

| Campo | Valor |
|---|---|
| Trámite objetivo | [PLACEHOLDER — fecha prevista de solicitud] |
| Título de Licenciatura | [PLACEHOLDER — universidad, año de egreso] |
| Práctica/requisitos | [PLACEHOLDER — práctica forense u otros requisitos exigidos] [verificar] |

**Requisitos generales (verificar con la CSJ):**

| Requisito | Descripción |
|---|---|
| Título universitario | Licenciatura en Derecho y Ciencias Políticas de universidad reconocida en Panamá [verificar] |
| Nacionalidad/residencia | Requisitos de nacionalidad panameña conforme a la ley aplicable [verificar] |

**Materias clave:** [PLACEHOLDER — áreas de mayor relevancia para la práctica profesional]

---

## Fichas de estudio

**Sistema Leitner de repetición espaciada:**

| Caja | Intervalo de repaso | Descripción |
|---|---|---|
| Caja 1 | Diario | Fichas nuevas o falladas |
| Caja 2 | Cada 3 días | Acertadas 1 vez |
| Caja 3 | Semanal | Acertadas 2 veces |
| Caja 4 | Quincenal | Acertadas 3 veces |
| Caja 5 | Mensual | Dominadas |

**Categorías de fichas:**

| Categoría | Ejemplo |
|---|---|
| Definiciones legales | "Concepto de dolo eventual" |
| Artículos clave | "Art. 1644 del Código Civil de Panamá — responsabilidad civil extracontractual [verificar]" |
| Jurisprudencia | "Fallo de la Corte Suprema de Justicia publicado en el Registro Judicial [verificar]" |
| Plazos | "Prescripción de la acción de responsabilidad civil extracontractual (Código Civil de Panamá) [verificar]" |
| Comparaciones | "Diferencia entre nulidad absoluta y nulidad relativa" |

---

## Planificación de estudio

| Campo | Valor |
|---|---|
| Calendario de exámenes | [PLACEHOLDER — fechas] |
| Horas de estudio diarias | [PLACEHOLDER] |
| Método de revisión espaciada | [PLACEHOLDER — Leitner / Anki / manual] |
| Sesiones de repaso semanal | [PLACEHOLDER — día y hora] |
| Simulacros de examen | [PLACEHOLDER — frecuencia] |

---

## Escritura jurídica

**Tipos de ejercicios escritos y su estructura:**

| Tipo | Estructura |
|---|---|
| **Dictamen** | Antecedentes de hecho, cuestiones jurídicas, fundamentos de derecho, conclusiones |
| **Caso práctico** | Hechos, identificación de problemas, resolución IRAC por problema, conclusión |
| **Informe jurídico** | Objeto, antecedentes, marco normativo, análisis, conclusiones y recomendaciones |
| **Recurso (simulado)** | Encabezamiento, hechos, fundamentos de derecho, suplico |

**Formato de citas:**
- Legislación: nombre completo + artículo (ej: "art. 1109 del Código Civil de Panamá [verificar]")
- Jurisprudencia: Corte Suprema de Justicia + Sala + fecha + referencia del Registro Judicial (ej: "CSJ, Sala Primera de lo Civil, fallo de [fecha], Registro Judicial de [mes/año]")

---

## Integraciones disponibles

| Integración | Estado | Fallback si no disponible |
|---|---|---|
| Almacenamiento (Drive / SharePoint) | [PLACEHOLDER] | Outputs guardados localmente |
| Calendario | [PLACEHOLDER] | Planificación manual |
| Anki / fichas | [PLACEHOLDER] | Fichas en formato texto |

*Re-comprobar: `/estudiante-derecho:cold-start-interview --check-integrations`*

---

## Outputs

**Carpeta de outputs:** [PLACEHOLDER — donde se guardan esquemas, fichas, dictámenes]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo]

**Cabecera de trabajo:**

`MATERIAL DE ESTUDIO — PREPARADO CON ASISTENCIA DE IA — VERIFICAR SIEMPRE CONTRA FUENTES PRIMARIAS (LEGISLACIÓN, JURISPRUDENCIA, MANUALES DE REFERENCIA)`

*Nota: Este plugin es una herramienta de apoyo al estudio. No sustituye la lectura de la legislación,
la jurisprudencia ni los manuales de referencia. El estudiante es responsable de verificar todo
el contenido.*

---

## Legislación de referencia

| Norma | Referencia | Ámbito |
|---|---|---|
| Idoneidad para la abogacía | Legislación que regula la profesión de abogado en Panamá [verificar] | Certificado de idoneidad ante la CSJ |
| Planes de estudio | Lineamientos del CONEAUPA / universidades panameñas [verificar] | Licenciatura en Derecho |
| Temarios de concursos judiciales | Gaceta Oficial (bases específicas del Órgano Judicial) [verificar] | Carrera judicial, Ministerio Público, etc. |

---

*Re-ejecutar: `/estudiante-derecho:cold-start-interview --redo`*
