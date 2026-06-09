<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/concursal/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /concursal:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /concursal:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/concursal/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Concursal de Insolvencia (Panamá)
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/concursal:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de derecho concursal se quedan aquí.*

[Empresa] es una [tipo de entidad — despacho / asesoría interna / administrador o restructurador del proceso concursal].
Rol habitual: [PLACEHOLDER — representación del deudor / representación de acreedores / administración del proceso concursal / asesor de operaciones distressed].
Juzgados habituales: [PLACEHOLDER — Juzgados de Circuito competentes / Circuito de Panamá]. El equipo concursal cuenta con [N] personas.
[Responsable del área: nombre o ninguno]. La escalación va a [nombre].

**Experiencia concursal:** [PLACEHOLDER — número aproximado de procesos concursales gestionados, perfil de los mismos] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Procesos concursales abiertos:** [PLACEHOLDER]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Administración del proceso concursal] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a idóneo | Profesional jurídico no abogado con acceso a letrado | Administrador/restructurador del proceso concursal | Profesional no jurídico sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente |
| Órgano Judicial / Registro Judicial de Panamá | [PLACEHOLDER ✓/✗] | Consulta manual en el portal del Órgano Judicial |
| Sistema de notificaciones del Órgano Judicial | [PLACEHOLDER ✓/✗] | Presentación física ante el juzgado |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Alertas de plazos solo bajo demanda |

*Re-comprobar: `/concursal:entrevista-inicial --check-integraciones`*

---

## Rol en el proceso concursal

| Rol | Descripción | Frecuencia |
|---|---|---|
| Deudor | Representación del concursado en el proceso de reorganización o liquidación | [PLACEHOLDER] |
| Acreedor | Defensa de créditos, reconocimiento y graduación, impugnación de la lista de créditos | [PLACEHOLDER] |
| Administrador / restructurador | Designación como administrador o restructurador del proceso concursal [verificar] | [PLACEHOLDER] |
| Adquirente de unidad productiva | Asesoramiento en adquisición de activos en liquidación | [PLACEHOLDER] |
| Asesor de reorganización | Preparación del plan de reorganización (Ley 12 de 2016) | [PLACEHOLDER] |

---

## Presupuestos del proceso concursal

| Presupuesto | Descripción | Base legal |
|---|---|---|
| Subjetivo | Persona natural o jurídica comerciante / deudor sujeto a la Ley 12 de 2016 [verificar] | Ley 12 de 2016 [verificar] |
| Objetivo | Insolvencia: el deudor no puede atender el cumplimiento de sus obligaciones | Ley 12 de 2016 [verificar] |
| Cesación de pagos | El deudor ha incumplido el pago de obligaciones líquidas y exigibles | Ley 12 de 2016 [verificar] |
| Insolvencia inminente | El deudor prevé que no podrá cumplir [verificar] | Ley 12 de 2016 [verificar] |

---

## Solicitud de reorganización (proceso preventivo)

| Campo | Detalle |
|---|---|
| Finalidad | Recuperar la empresa viable mediante un plan de reorganización acordado con los acreedores |
| Legitimación | El propio deudor; en su caso, acreedores conforme a la Ley 12 de 2016 [verificar] |
| Efectos | Protección frente a ejecuciones / suspensión de procesos de ejecución durante el trámite [verificar] |
| Administrador / restructurador | Designación por el juez conforme a la Ley 12 de 2016 [verificar] |
| Desistimiento | Conversión en proceso de liquidación si no se aprueba o se incumple el plan [verificar] |

**Solicitudes de reorganización activas:** [PLACEHOLDER]

---

## Inicio del proceso concursal

| Tipo | Quién solicita | Plazo | Efectos principales |
|---|---|---|---|
| Voluntario | El propio deudor | Conforme a la Ley 12 de 2016 [verificar] | Posible mantenimiento de la administración bajo supervisión [verificar] |
| Necesario / a instancia de acreedor | Acreedor u otros legitimados | — | Posible desapoderamiento del deudor según el proceso [verificar] |

**Juzgado competente:** Juzgado de Circuito competente del domicilio del deudor [verificar]

---

## Patrimonio del deudor y masa de acreedores

### Masa activa / patrimonio del deudor

| Concepto | Descripción | Consideraciones |
|---|---|---|
| Bienes y derechos del deudor | Todo el patrimonio a la fecha de apertura del proceso | Ley 12 de 2016 [verificar] |
| Bienes de terceros | Separación de bienes que no pertenecen al deudor | Ley 12 de 2016 / Código Civil [verificar] |
| Acciones de reintegración / revocatoria | Impugnación de actos perjudiciales realizados en el periodo sospechoso | Ley 12 de 2016 [verificar] |

### Masa pasiva — Clasificación y prelación de créditos

| Categoría | Descripción | Ejemplos | Base legal |
|---|---|---|---|
| Créditos de administración del proceso | Generados tras la apertura del proceso concursal | Honorarios del administrador, gastos del proceso | Ley 12 de 2016 [verificar] |
| Créditos con garantía real / privilegio especial | Garantía sobre un bien concreto | Hipotecarios, pignoraticios | Código Civil de Panamá / Ley 12 de 2016 [verificar] |
| Créditos privilegiados / con preferencia | Preferencia legal sin afectación a bien concreto | Salarios y prestaciones laborales (incluido décimo tercer mes), créditos de la CSS, créditos fiscales (DGI) | Código de Trabajo / Código Civil / Ley 12 de 2016 [verificar] |
| Ordinarios / comunes | Sin privilegio ni subordinación | Proveedores, préstamos sin garantía | Ley 12 de 2016 / Código Civil [verificar] |
| Subordinados / postergados | Postergados por ley | Intereses, multas, créditos de personas vinculadas | Ley 12 de 2016 [verificar] |

**Tratamiento habitual de créditos:** [PLACEHOLDER — política de reconocimiento, impugnación del inventario y la lista de créditos]

---

## Plan de reorganización (Ley 12 de 2016)

| Aspecto | Detalle | Base legal |
|---|---|---|
| Contenido mínimo | Descripción de la situación, medidas propuestas, plan de viabilidad | Ley 12 de 2016 [verificar] |
| Clases de créditos afectados | Agrupación de acreedores por categoría de créditos | Ley 12 de 2016 [verificar] |
| Mayorías | Mayoría del pasivo conforme a la Ley 12 de 2016 [verificar] | Ley 12 de 2016 [verificar] |
| Aprobación / confirmación judicial | El juez confirma el plan aprobado por los acreedores | Ley 12 de 2016 [verificar] |
| Impugnación | Plazo conforme a la Ley 12 de 2016 [verificar] | Ley 12 de 2016 [verificar] |

---

## Acuerdo con los acreedores (reorganización)

| Aspecto | Detalle | Base legal |
|---|---|---|
| Contenido | Quitas y/o esperas, capitalización de deuda, dación en pago | Ley 12 de 2016 [verificar] |
| Mayorías | Según la Ley 12 de 2016 [verificar] | Variable |
| Aprobación judicial | Control de legalidad y confirmación | Ley 12 de 2016 [verificar] |
| Incumplimiento | Apertura del proceso de liquidación | Ley 12 de 2016 [verificar] |

---

## Liquidación

| Aspecto | Detalle | Base legal |
|---|---|---|
| Apertura | A solicitud del deudor, de acreedores o por fracaso/incumplimiento de la reorganización | Ley 12 de 2016 [verificar] |
| Liquidador | Designación del liquidador del proceso concursal | Ley 12 de 2016 [verificar] |
| Venta de unidad productiva | Posibilidad de enajenación como unidad en marcha | Ley 12 de 2016 [verificar] |
| Sucesión laboral | Riesgo de sucesión laboral conforme al Código de Trabajo de Panamá | Código de Trabajo [verificar] |
| Pago de créditos | Orden de prelación según clasificación | Ley 12 de 2016 / Código Civil [verificar] |

---

## Responsabilidad de administradores y conducta del deudor

| Supuesto | Consecuencias | Base legal |
|---|---|---|
| Conducta de buena fe | Sin consecuencias personales ni patrimoniales adicionales | Ley 12 de 2016 [verificar] |
| Conducta dolosa o fraudulenta | Responsabilidad patrimonial; posibles consecuencias penales (alzamiento de bienes, quiebra fraudulenta) | Ley 12 de 2016 / Código Penal de Panamá [verificar] |

**Indicios de conducta sancionable [verificar]:** incumplimiento del deber de solicitar el proceso a tiempo, irregularidades contables graves, ocultación o alzamiento de bienes.

---

## Insolvencia de persona natural

| Aspecto | Consideraciones especiales |
|---|---|
| Bienes inembargables | Excluidos conforme al Código Judicial de Panamá [verificar] |
| Prestaciones laborales | Protección especial de salarios y prestaciones (incluido décimo tercer mes) |
| Aplicabilidad de la Ley 12 de 2016 a la persona natural | Verificar el ámbito subjetivo de la Ley 12 de 2016 [verificar] |

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Reconocimiento de créditos | Equipo concursal | — | — |
| Impugnación de la lista de créditos / inventario | Equipo concursal | Socio/Director | Si crédito > [PLACEHOLDER] |
| Solicitud de reorganización (voluntaria) | — | Socio/Director + Dirección | Siempre |
| Solicitud de liquidación | — | Socio/Director | Siempre |
| Indicios de conducta dolosa o fraudulenta | — | Socio/Director + Dirección General | Siempre |
| Adquisición de unidad productiva | — | Socio/Director + Dirección + Laboral + Fiscal | Siempre |
| Plan de reorganización | — | Socio/Director + Dirección | Siempre |

---

## Referencias legislativas principales

- **Ley 12 de 2016** — por la cual se establece el proceso concursal de insolvencia (reorganización y liquidación) en Panamá [verificar]
- **Código de Comercio de Panamá** — régimen mercantil general (supletorio)
- **Código Civil de Panamá** — prelación y graduación de créditos; obligaciones y contratos
- **Código Judicial de Panamá** — normas procesales supletorias
- **Código de Trabajo de Panamá** — prelación de créditos laborales, sucesión de empresa
- **Ley 51 de 2005** [verificar] — régimen de la Caja de Seguro Social (CSS), créditos por cuotas

*Nota: la normativa de la Unión Europea (p. ej. la Directiva 2019/1023 de reestructuración) no es derecho aplicable en Panamá; solo se cita, en su caso, como referencia comparada internacional.*

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Solicitud de reorganización/liquidación de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |
| Comunicación/reconocimiento de créditos tipo | [PLACEHOLDER] | [PLACEHOLDER] | |
| Plan de reorganización de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan solicitudes, reconocimientos de créditos, informes y planes]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo:**

- Si el Rol es Abogado/a: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LETRADO — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO IDÓNEO ANTES DE ACTUAR`

---

*Re-ejecutar: `/concursal:entrevista-inicial --redo`*
