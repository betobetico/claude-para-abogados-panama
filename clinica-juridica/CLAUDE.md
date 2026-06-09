<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin vive en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/clinica-juridica/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de generar output útil. Ejecuta
   /clinica-juridica:cold-start-interview — lleva unos 10 minutos y todos los comandos dependen de ella.
   Sin configurar, las respuestas serán genéricas y pueden no ajustarse a tu consultorio."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin setup
   son /clinica-juridica:cold-start-interview y cualquier flag --check-integrations.
3. El setup y cold-start-interview ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta
   antigua de caché (~/.claude/plugins/cache/claude-para-abogados/clinica-juridica/<version>/CLAUDE.md
   para cualquier versión) pero no en la ruta de config, copiarlo a la ruta de config antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la config. Se reemplaza en cada actualización. Nunca escribir datos de
   usuario aquí.

**Perfil de empresa compartido.** Los datos a nivel de empresa (quién eres, qué haces, dónde operas,
tu postura de riesgo, personas clave) viven en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes del perfil de
práctica de este plugin. Si no existe, el setup de este plugin lo creará.
-->

# Perfil de Práctica — Consultorio Jurídico

*Escrito por la cold-start interview. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/clinica-juridica:cold-start-interview`.*

---

## Quiénes somos

| Campo | Valor |
|---|---|
| Universidad | [PLACEHOLDER] |
| Facultad / Departamento | [PLACEHOLDER] |
| Nombre del consultorio | [PLACEHOLDER] |
| Director/a del consultorio | [PLACEHOLDER] |
| Supervisor/a académico/a | [PLACEHOLDER — nombre, área de especialización] |
| Abogado/a supervisor/a (idoneidad) | [PLACEHOLDER — nombre, número de idoneidad de la Corte Suprema de Justicia] |
| Año académico | [PLACEHOLDER] |

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Estudiante de consultorio | Supervisor/a académico/a | Abogado/a supervisor/a]
**Idoneidad:** [PLACEHOLDER — Sí (número de idoneidad de la CSJ) / No (estudiante bajo supervisión)]

---

## Áreas de práctica del consultorio

| Área | Activa | Supervisor/a |
|---|---|---|
| [PLACEHOLDER — Migración] | | |
| [PLACEHOLDER — Consumo] | | |
| [PLACEHOLDER — Vivienda / propiedad horizontal] | | |
| [PLACEHOLDER — Violencia doméstica] | | |
| [PLACEHOLDER — Derechos fundamentales / amparo de garantías] | | |
| [PLACEHOLDER — Otra] | | |

---

## Protocolo de intake

**Pasos del protocolo:**

1. **Recepción de la consulta** — Canal: [PLACEHOLDER — presencial, derivación de ONG, Órgano Judicial, Defensoría del Pueblo]
2. **Conflicto de intereses** — Verificación contra registro interno de clientes: [PLACEHOLDER — ruta/sistema]
3. **Evaluación de capacidad** — ¿El consultorio tiene competencia para este asunto? Criterios: [PLACEHOLDER]
4. **Derivación a la defensoría de oficio** — Si el asunto excede la capacidad del consultorio o requiere representación procesal que el consultorio no puede asumir
5. **Apertura de expediente** — Registro: [PLACEHOLDER — sistema/carpeta]
6. **Firma de hoja de encargo** — Modelo: [PLACEHOLDER — ruta]
7. **Consentimiento informado** — El cliente entiende que le atienden estudiantes bajo supervisión

**Criterios de derivación:** [PLACEHOLDER — cuándo se deriva a la defensoría de oficio, instituciones de asistencia social, o despacho externo]

---

## Acceso a la justicia y asistencia legal gratuita

*Garantía constitucional de acceso a la justicia (Constitución Política, art. 22) [verificar] y defensoría de oficio del Órgano Judicial.*

| Campo | Valor |
|---|---|
| Requisitos económicos | Persona de escasos recursos económicos según evaluación socioeconómica [verificar] |
| Documentación necesaria | [PLACEHOLDER — cédula / pasaporte o carné de residente, comprobante de ingresos, etc.] |
| Órgano de tramitación | Defensoría de Oficio del Órgano Judicial / Instituto de la Defensa Pública [verificar] |
| Formulario de solicitud | [PLACEHOLDER — ruta/modelo] |

**Supuestos de protección reforzada:** Víctimas de violencia doméstica, menores de edad, personas con discapacidad, personas en situación migratoria irregular (legislación panameña aplicable) [verificar].

---

## Defensoría de oficio

| Campo | Valor |
|---|---|
| Entidad de referencia | [PLACEHOLDER — Defensoría de Oficio del Órgano Judicial, Defensoría del Pueblo, Colegio Nacional de Abogados] |
| Protocolo de derivación | [PLACEHOLDER] |
| Contacto para designación de oficio | [PLACEHOLDER] |
| Sustitución de defensor de oficio | [PLACEHOLDER — procedimiento] |

*Referencia: Código Judicial de Panamá (defensoría de oficio) [verificar]; Código de Ética y Responsabilidad Profesional del Abogado [verificar].*

---

## Estructura de memo — IRAC adaptado

Todo memo del consultorio sigue esta estructura:

1. **I — Identificación del problema:** Hechos relevantes y cuestión jurídica concreta
2. **R — Regulación aplicable:** Normas, jurisprudencia y doctrina aplicables (con citas completas)
3. **A — Aplicación al caso:** Subsunción de los hechos en la norma
4. **C — Conclusión:** Respuesta a la cuestión, opciones para el cliente, recomendación

**Formato de citas:**
- Legislación: Nombre completo + artículo (ej: "art. 1644 del Código Civil de Panamá") [verificar]
- Jurisprudencia: Tribunal + Sala + fecha + referencia de Registro Judicial si disponible (ej: "Corte Suprema de Justicia, Sala Primera de lo Civil, fallo de 15 de marzo de 2023, Registro Judicial")
- Doctrina: Autor, título, editorial, año, página

**Plantilla de memo:** [PLACEHOLDER — ruta]

---

## Plazos y preclusión

**Sistema de alertas:** [PLACEHOLDER — calendario compartido, herramienta de gestión, manual]

| Tipo de plazo | Alerta previa | Responsable de control |
|---|---|---|
| Plazos procesales (Código Judicial) | [PLACEHOLDER — días antes] | [PLACEHOLDER] |
| Prescripción y caducidad | [PLACEHOLDER] | [PLACEHOLDER] |
| Plazos administrativos (Ley 38 de 2000) | [PLACEHOLDER] | [PLACEHOLDER] |
| Citas y comparecencias | [PLACEHOLDER] | [PLACEHOLDER] |

**Regla del consultorio:** Ningún plazo se deja sin verificar por el supervisor antes de que transcurran 48 horas desde su identificación.

---

## Supervisión

**Workflow de revisión:**

1. Estudiante prepara borrador del memo/escrito
2. Revisión por compañero/a del consultorio (peer review): [PLACEHOLDER — obligatorio/opcional]
3. Revisión por supervisor/a académico/a: [PLACEHOLDER — nombre]
4. Aprobación por abogado/a con idoneidad (si implica actuación procesal): [PLACEHOLDER — nombre]
5. Entrega/envío al cliente o presentación ante el tribunal/administración

**Plazo de revisión:** [PLACEHOLDER — días máximos entre borrador y aprobación]

---

## Correspondencia con cliente

**Plantillas disponibles:**

| Tipo | Ubicación |
|---|---|
| Citación para entrevista | [PLACEHOLDER] |
| Solicitud de documentos | [PLACEHOLDER] |
| Actualización de estado del caso | [PLACEHOLDER] |
| Comunicación de resultado | [PLACEHOLDER] |
| Cierre de expediente | [PLACEHOLDER] |

**Regla:** Toda comunicación con el cliente debe ser revisada por el supervisor antes de enviarla.

---

## Traspaso de semestre

**Protocolo de traspaso:**

Cuando un estudiante termina el semestre y el caso continúa:

1. **Memo de estado** — Resumen del caso, actuaciones realizadas, pendientes, plazos vivos
2. **Reunión de traspaso** — Con el estudiante entrante y el supervisor
3. **Actualización del expediente** — Documentos indexados, cronología actualizada
4. **Contacto con el cliente** — Comunicar el cambio de estudiante responsable

**Plantilla de memo de traspaso:** [PLACEHOLDER — ruta]

---

## Integraciones disponibles

| Integración | Estado | Fallback si no disponible |
|---|---|---|
| Almacenamiento (Drive / SharePoint) | [PLACEHOLDER] | Outputs guardados localmente |
| Calendario compartido | [PLACEHOLDER] | Control manual de plazos |
| Tareas programadas | [PLACEHOLDER] | Revisiones bajo demanda |

*Re-comprobar: `/clinica-juridica:cold-start-interview --check-integrations`*

---

## Outputs

**Carpeta de outputs:** [PLACEHOLDER — donde se guardan memos, escritos, correspondencia]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo]

**Cabecera de trabajo:**

`TRABAJO DE CONSULTORIO JURÍDICO — [UNIVERSIDAD] — PREPARADO BAJO SUPERVISIÓN ACADÉMICA Y LETRADA — NO CONSTITUYE ASESORAMIENTO PROFESIONAL INDEPENDIENTE`

*Nota: Los trabajos del consultorio están supervisados por un abogado con idoneidad, pero el estudiante
no actúa como abogado. La cabecera refleja esta realidad.*

---

## Legislación de referencia

| Norma | Referencia | Ámbito |
|---|---|---|
| Constitución Política de la República de Panamá | Art. 22 — garantía de defensa [verificar] | Acceso a la justicia, defensoría de oficio |
| Código Judicial de Panamá | — | Organización judicial y plazos procesales |
| Código de Ética y Responsabilidad Profesional del Abogado | — [verificar] | Ejercicio de la abogacía, secreto profesional |
| Ley de Procedimiento Administrativo General | Ley 38 de 2000 | Procedimiento administrativo |
| Ley de Protección de Datos Personales | Ley 81 de 2019 | Protección de datos del cliente |

---

*Re-ejecutar: `/clinica-juridica:cold-start-interview --redo`*
