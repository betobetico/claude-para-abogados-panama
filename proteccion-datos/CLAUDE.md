<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin vive en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de generar output útil. Ejecuta
   /proteccion-datos:cold-start-interview — lleva unos 10 minutos y todos los comandos dependen de ella.
   Sin configurar, las respuestas serán genéricas y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin setup
   son /proteccion-datos:cold-start-interview y cualquier flag --check-integrations.
3. El setup y cold-start-interview ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta
   antigua de caché (~/.claude/plugins/cache/claude-para-abogados/proteccion-datos/<version>/CLAUDE.md
   para cualquier versión) pero no en la ruta de config, copiarlo a la ruta de config antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la config. Se reemplaza en cada actualización. Nunca escribir datos de
   usuario aquí.

**Perfil de empresa compartido.** Los datos a nivel de empresa (quién eres, qué haces, dónde operas,
tu postura de riesgo, personas clave) viven en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes del perfil de
práctica de este plugin. Si no existe, el setup de este plugin lo creará.
-->

# Perfil de Práctica — Protección de Datos (Operativo)

*Escrito por la cold-start interview. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/proteccion-datos:cold-start-interview`.*

---

## Quiénes somos

*El nombre de la empresa, sector, tamaño y jurisdicciones vienen de `perfil-empresa.md` — edita allí
para cambiar en todos los plugins. Los campos específicos de protección de datos van aquí.*

[Empresa] es una [tipo de entidad]. Tratamos datos personales como [responsable / custodio o encargado / ambos]
respecto a [de quién son los datos]. Los datos se alojan en [regiones/países]. El equipo de protección
de datos tiene [N] personas.

**Marco normativo aplicable:** [PLACEHOLDER — Ley 81 de 2019, Decreto Ejecutivo 285 de 2021, normativa sectorial]
*(Desde perfil-empresa.md — edita allí para cambiar en todos los plugins)*

**Expedientes abiertos con ANTAI:** [PLACEHOLDER]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual | Despacho mediano/grande | In-house | Administración pública | Clínica jurídica]
*(Desde perfil-empresa.md — edita allí para cambiar en todos los plugins)*

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a | Profesional jurídico | No jurista con acceso a abogado | No jurista sin acceso a abogado]
**Contacto de abogado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Encargado / Responsable de Protección de Datos

**Responsable de protección de datos designado:** [PLACEHOLDER — Sí (obligatorio) / Sí (voluntario) / No] [verificar]
**Nombre y contacto:** [PLACEHOLDER]
**Comunicación con ANTAI:** [PLACEHOLDER — canal de comunicación registrado ante la ANTAI]
**Inscripción en registro público:** [PLACEHOLDER — Sí/No, fecha]

*Referencia: Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021.*

---

## Registro de Actividades de Tratamiento (RAT)

*Obligatorio para responsables y custodios o encargados según la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021.*

| Campo | Valor |
|---|---|
| Ubicación del RAT | [PLACEHOLDER — ruta o sistema] |
| Número de tratamientos registrados | [PLACEHOLDER] |
| Última actualización | [PLACEHOLDER — fecha] |
| Responsable del mantenimiento | [PLACEHOLDER] |

**Categorías de datos habituales:** [PLACEHOLDER — identificativos, contacto, financieros, salud, etc.]
**Bases jurídicas más utilizadas:** [PLACEHOLDER — consentimiento, ejecución contractual, interés legítimo, obligación legal]
**Plazos de conservación estándar:** [PLACEHOLDER — por categoría]
**Cesiones habituales:** [PLACEHOLDER — a quién, base jurídica]
**Transferencias internacionales:** [PLACEHOLDER — destinos, mecanismo: nivel adecuado de protección, cláusulas contractuales, consentimiento del titular] [verificar]

*Referencia: Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021.*

---

## Evaluación de Impacto (EIPD)

**Cuándo es obligatoria:** Según los criterios de la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021 para tratamientos que entrañen probablemente un alto riesgo para los titulares.

| Campo | Valor |
|---|---|
| Metodología utilizada | [PLACEHOLDER — guía ANTAI, ISO 29134, propia] |
| Plantilla de EIPD | [PLACEHOLDER — ruta] |
| Umbral interno para EIPD | [PLACEHOLDER — criterios propios además de los obligatorios] |
| Consulta previa a la ANTAI | [PLACEHOLDER — se ha realizado alguna vez: Sí/No] [verificar] |

*Referencia: Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021.*

---

## Brechas de seguridad

**Protocolo de gestión de brechas:**

1. **Detección** — Canales de notificación interna: [PLACEHOLDER]
2. **Evaluación de riesgo** — Responsable de evaluación: [PLACEHOLDER]. Metodología: [PLACEHOLDER — propia]
3. **Notificación a la ANTAI** — Plazo: [PLACEHOLDER — plazo legal desde el conocimiento] [verificar]. Canal: ANTAI.
4. **Comunicación a titulares** — Cuándo: si riesgo alto para los derechos de los titulares [verificar]. Plantilla: [PLACEHOLDER]

| Campo | Valor |
|---|---|
| Registro de brechas | [PLACEHOLDER — ubicación] |
| Brechas notificadas a ANTAI | [PLACEHOLDER — número, última fecha] |
| Equipo de respuesta | [PLACEHOLDER — nombres/roles] |
| Seguro de ciberriesgo | [PLACEHOLDER — Sí/No, cobertura] |

*Referencia: Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021 sobre gestión y notificación de incidentes de seguridad [verificar].*

---

## Auditorías y compliance

| Campo | Valor |
|---|---|
| Programa de auditoría | [PLACEHOLDER — frecuencia, alcance] |
| Última auditoría interna | [PLACEHOLDER — fecha, resultado] |
| Última auditoría externa | [PLACEHOLDER — fecha, auditor, resultado] |
| Checklist de cumplimiento | [PLACEHOLDER — ruta al checklist] |

**Áreas auditadas:** [PLACEHOLDER — RAT, consentimientos, ejercicio de derechos, medidas de seguridad, custodios o encargados, transferencias internacionales]

---

## Relación con la ANTAI

| Tipo de procedimiento | Estado | Referencia |
|---|---|---|
| Reclamaciones recibidas | [PLACEHOLDER] | |
| Actuaciones previas de investigación | [PLACEHOLDER] | |
| Procedimiento sancionador | [PLACEHOLDER] | |
| Recursos ante la Sala Tercera de lo Contencioso-Administrativo de la CSJ | [PLACEHOLDER] | |

**Interlocutor habitual con ANTAI:** [PLACEHOLDER]
**Apercibimientos recibidos:** [PLACEHOLDER]

*Referencia: Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021 (régimen sancionador) [verificar].*

---

## Formación y concienciación

| Campo | Valor |
|---|---|
| Plan de formación | [PLACEHOLDER — frecuencia, destinatarios] |
| Última formación impartida | [PLACEHOLDER — fecha, tema] |
| Material formativo | [PLACEHOLDER — ruta] |
| Test de concienciación | [PLACEHOLDER — frecuencia, resultados] |

---

## Custodios o encargados de tratamiento

| Custodio/Encargado | Servicio | Contrato de tratamiento | Última auditoría | Próxima revisión |
|---|---|---|---|---|
| [PLACEHOLDER] | | | | |

**Modelo de contrato de custodio o encargado:** [PLACEHOLDER — ruta]
**Proceso de homologación de custodios o encargados:** [PLACEHOLDER]

*Referencia: Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021.*

---

## Medidas de seguridad de la información

**Marco de seguridad aplicado:** [PLACEHOLDER — ISO 27001, marco propio, normativa sectorial]
**Categoría del sistema:** [PLACEHOLDER — Básica / Media / Alta]
**Certificación de seguridad:** [PLACEHOLDER — Sí/No, fecha, entidad certificadora]
**Declaración de aplicabilidad:** [PLACEHOLDER — ruta]

*Referencia: deber de seguridad y confidencialidad de la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021.*

---

## Integraciones disponibles

| Integración | Estado | Fallback si no disponible |
|---|---|---|
| Almacenamiento (Drive / SharePoint) | [PLACEHOLDER] | Outputs guardados localmente |
| Slack / Teams | [PLACEHOLDER] | Notificaciones de brechas entregadas inline |
| Tareas programadas | [PLACEHOLDER] | Auditorías y revisiones bajo demanda |
| Canal de la ANTAI | [PLACEHOLDER] | Notificaciones manuales |

*Re-comprobar: `/proteccion-datos:cold-start-interview --check-integrations`*

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| RAT completo | [PLACEHOLDER] | | |
| Plantilla EIPD | [PLACEHOLDER] | | |
| Protocolo de brechas | [PLACEHOLDER] | | |
| Contrato tipo custodio o encargado | [PLACEHOLDER] | | |
| Política de protección de datos | [PLACEHOLDER] | | |

---

## Outputs

**Carpeta de outputs:** [PLACEHOLDER — donde se guardan EIPD, informes de auditoría, notificaciones]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Cabecera de trabajo:**

- Si el Rol es Abogado/a o profesional jurídico: `CONFIDENCIAL — TRABAJO PROFESIONAL — PREPARADO BAJO DIRECCIÓN LETRADA`
- Si el Rol es No jurista: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON ABOGADO ANTES DE ACTUAR`

*Nota: en Derecho panameño no existe la doctrina de "attorney work product" estadounidense. La cabecera
"Confidencial" tiene valor como marcado de confidencialidad. El secreto profesional del abogado se rige
por el Código de Ética y Responsabilidad Profesional del Abogado y por la legislación panameña aplicable [verificar].*

---

## Legislación de referencia

| Norma | Referencia | Ámbito |
|---|---|---|
| Ley 81 de 2019 | Protección de datos personales [verificar] | Protección de datos — norma principal aplicable |
| Decreto Ejecutivo 285 de 2021 | Reglamento de la Ley 81 de 2019 | Desarrollo reglamentario |
| Guías ANTAI | antai.gob.pa | Criterios interpretativos y buenas prácticas |
| RGPD (referencia comparada) | Reglamento (UE) 2016/679 | No aplicable en Panamá; solo buena práctica internacional |

---

*Re-ejecutar: `/proteccion-datos:cold-start-interview --redo`*
