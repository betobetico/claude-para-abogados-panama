<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /fiscal:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /fiscal:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/fiscal/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Fiscal y Tributario (Panamá)
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/fiscal:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de fiscalidad se quedan aquí.*

[Empresa] es una [tipo de entidad]. Forma jurídica: [PLACEHOLDER — S.A. (Ley 32 de 1927), S. de R.L., fundación de interés privado (Ley 25 de 1995), persona natural, etc.].
Régimen fiscal: [PLACEHOLDER — régimen general del ISR / CAIR / régimen de zona especial (SEM, Ciudad del Saber, ZLC, Panamá Pacífico) / etc.].
Período fiscal: [PLACEHOLDER — año calendario / período especial autorizado]. RUC: [PLACEHOLDER]. NT/DV: [PLACEHOLDER].
Administración: DGI (Dirección General de Ingresos). El equipo fiscal cuenta con [N] personas.
[Responsable fiscal: nombre o ninguno]. Asesor fiscal externo / CPA: [PLACEHOLDER]. La escalación va a [nombre].

**Huella fiscal:** [PLACEHOLDER — tributos principales a los que está sujeta la entidad] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Asuntos fiscales abiertos:** [PLACEHOLDER — fiscalizaciones en curso, reclamos, consultas pendientes ante la DGI]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica/fiscal interna | Asesoría fiscal independiente] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a tributarista | Contador público autorizado (CPA) | Profesional no jurídico sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente |
| Software contable (SAP, QuickBooks, etc.) | [PLACEHOLDER ✓/✗] | Datos fiscales introducidos manualmente |
| e-Tax 2.0 / portal DGI | [PLACEHOLDER ✓/✗] | Consulta manual de plazos y formularios |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Alertas de calendario fiscal solo bajo demanda |

*Re-comprobar: `/fiscal:entrevista-inicial --check-integraciones`*

---

## Forma jurídica y régimen fiscal

| Campo | Valor |
|---|---|
| Forma jurídica | [PLACEHOLDER — S.A. / S. de R.L. / fundación de interés privado / persona natural / etc.] |
| Régimen del ISR | [PLACEHOLDER — general / CAIR / no contribuyente / zona especial] |
| Régimen de ITBMS | [PLACEHOLDER — contribuyente ordinario / no obligado / agente de retención] |
| Régimen de zona especial | [PLACEHOLDER — SEM (Ley 41 de 2007) / Ciudad del Saber / ZLC / Panamá Pacífico / ninguno] [verificar] |
| Agente de retención | [PLACEHOLDER — sí/no, conceptos] |
| Operaciones de fuente extranjera | [PLACEHOLDER — sí/no — recordatorio: no gravadas por territorialidad] |

---

## Obligaciones tributarias principales

| Tributo | Formulario | Periodicidad | Plazo | Notas |
|---|---|---|---|---|
| ISR — Declaración jurada de rentas | 1 (jurídicas) / 1 (naturales) [verificar] | Anual | [PLACEHOLDER — hasta 31 de marzo año calendario, con prórroga de 1 mes] [verificar] | [PLACEHOLDER] |
| ISR — Estimada | [PLACEHOLDER] | Anual / cuotas | [PLACEHOLDER] | [PLACEHOLDER — CAIR si ingresos > 1,5 millones B/.] [verificar] |
| ITBMS — Declaración | 430 [verificar] | Mensual | [PLACEHOLDER — dentro de los 15 días siguientes al mes] [verificar] | [PLACEHOLDER] |
| ISR — Retenciones sobre salarios (planilla) | 03 [verificar] | Mensual | [PLACEHOLDER] | [PLACEHOLDER] |
| Retención sobre dividendos / complementario | [PLACEHOLDER] | Según distribución | [PLACEHOLDER] | [PLACEHOLDER — 10% nominativas / 5% al portador o ZL] [verificar] |
| Retención a no residentes / servicios del exterior | [PLACEHOLDER] | Según pago | [PLACEHOLDER] | [PLACEHOLDER] |
| CSS — Planilla (cuota obrero-patronal) | [PLACEHOLDER] | Mensual | [PLACEHOLDER] | [PLACEHOLDER] |
| Tasa única (S.A. / fundaciones) | [PLACEHOLDER] | Anual | [PLACEHOLDER] | [PLACEHOLDER] |
| [Otro formulario] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Calendario fiscal DGI — Plazos clave

| Período | Obligaciones principales | Plazo presentación |
|---|---|---|
| Mensual | ITBMS (430), planilla retenciones ISR (03), planilla CSS | [PLACEHOLDER — primeros 15 días del mes siguiente] [verificar] |
| Anual | Declaración jurada del ISR, informe de no declarante si aplica | [PLACEHOLDER — hasta 31 de marzo, prórroga hasta 30 de abril] [verificar] |
| Anual | Tasa única de sociedades y fundaciones | [PLACEHOLDER] [verificar] |

**Plazos especiales:** [PLACEHOLDER — grandes contribuyentes, regímenes de zona especial, prórrogas]

---

## Tributos municipales

| Tributo | Municipio | Tasa | Notas |
|---|---|---|---|
| Impuesto de aviso de operación | [PLACEHOLDER — municipio] | [PLACEHOLDER — 2% del capital, tope B/. 60.000] [verificar] | [PLACEHOLDER] |
| Impuesto de inmuebles | ANATI / DGI [verificar] | [PLACEHOLDER — tasa progresiva] [verificar] | [PLACEHOLDER] |
| Tasas y arbitrios municipales | [PLACEHOLDER — municipio] | [PLACEHOLDER] | [PLACEHOLDER] |
| [Otro tributo municipal] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Consultas y criterios de la DGI

| Referencia | Fecha | Materia | Criterio relevante | Aplicable |
|---|---|---|---|---|
| [PLACEHOLDER — resolución o nota DGI] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER ✓/✗] |

**Política de consultas:** [PLACEHOLDER — cuándo elevamos consulta formal a la DGI, proceso interno]

---

## Procedimientos tributarios

| Procedimiento | Normativa | Plazos clave | Estado actual |
|---|---|---|---|
| Fiscalización / auditoría DGI | Código Fiscal [verificar] | [PLACEHOLDER] [verificar] | [PLACEHOLDER] |
| Resolución de alcance / liquidación adicional | Código Fiscal [verificar] | [PLACEHOLDER] [verificar] | [PLACEHOLDER] |
| Recurso de reconsideración (ante la DGI) | Código Fiscal / Ley 38 de 2000 [verificar] | [PLACEHOLDER — 15 días hábiles] [verificar] | [PLACEHOLDER] |
| Recurso de apelación (Tribunal Administrativo Tributario, TAT) | Ley 8 de 2010 [verificar] | [PLACEHOLDER — 15 días hábiles] [verificar] | [PLACEHOLDER] |
| Demanda contencioso-administrativa | Sala Tercera de la CSJ — Ley 38 de 2000 [verificar] | [PLACEHOLDER — 2 meses] [verificar] | [PLACEHOLDER] |

---

## Planificación fiscal

| Elemento | Descripción | Estado |
|---|---|---|
| Principio de territorialidad | [PLACEHOLDER — segregación de renta de fuente panameña vs extranjera] | [PLACEHOLDER] |
| Régimen de zona especial (SEM, Ciudad del Saber, ZLC, Panamá Pacífico) | [PLACEHOLDER — incentivos aplicados, requisitos de elegibilidad] | [PLACEHOLDER] |
| Precios de transferencia | [PLACEHOLDER — informe 930 / estudio de PT con partes relacionadas] [verificar] | [PLACEHOLDER] |
| Arrastre de pérdidas | [PLACEHOLDER — pérdidas pendientes de aplicar, límite anual] [verificar] | [PLACEHOLDER] |
| Incentivos sectoriales (turismo, agro, energía) | [PLACEHOLDER] | [PLACEHOLDER] |
| [Otro elemento de planificación] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Convenios para evitar la doble imposición (CDI)

| País | CDI vigente | Aspectos clave | Operaciones afectadas |
|---|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER — sí/no, referencia Gaceta Oficial] | [PLACEHOLDER — retenciones, EP, regalías] | [PLACEHOLDER] |

---

## Estilo house — Memos fiscales

**Estructura estándar de memo fiscal:**
1. [PLACEHOLDER — p.ej. Antecedentes de hecho]
2. [PLACEHOLDER — p.ej. Cuestión planteada]
3. [PLACEHOLDER — p.ej. Normativa aplicable]
4. [PLACEHOLDER — p.ej. Análisis]
5. [PLACEHOLDER — p.ej. Conclusión y recomendación]

**Tono:** [PLACEHOLDER — técnico / divulgativo / mixto]
**Extensión típica:** [PLACEHOLDER — páginas]
**Destinatario habitual:** [PLACEHOLDER — dirección financiera / cliente / archivo]

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Declaración rutinaria | Equipo fiscal | — | — |
| Consulta formal a la DGI | Equipo fiscal | Socio/Director fiscal | Siempre |
| Requerimiento de información DGI | Equipo fiscal | Dirección jurídica | Si implica posible fiscalización |
| Inicio de fiscalización | — | Dirección jurídica + Dirección General | Siempre |
| Liquidación adicional / resolución de alcance | — | Socio fiscal + Dirección | Siempre |
| Procedimiento sancionador | — | Dirección jurídica + Dirección | Siempre |

---

## Referencias legislativas principales

- **Código Fiscal de Panamá** — régimen del ISR, ITBMS y demás tributos nacionales [verificar]
- **Decreto Ejecutivo 170 de 1993** — reglamentación del Impuesto sobre la Renta [verificar]
- **Ley 8 de 2010** — reforma tributaria, ITBMS y creación del TAT [verificar]
- **Ley 41 de 2007** — régimen de Sedes de Empresas Multinacionales (SEM) [verificar]
- **Decreto Ley 6 de 1998 / régimen de la Zona Libre de Colón** [verificar]
- **Ley 41 de 2004** — régimen de Panamá Pacífico [verificar]
- **Decreto Ley 6 de 1998 — Ciudad del Saber / Ley respectiva** [verificar]
- **Ley 38 de 2000** — procedimiento administrativo general
- Resoluciones y notas interpretativas de la DGI

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Última declaración jurada del ISR | [PLACEHOLDER] | [PLACEHOLDER] | |
| Calendario fiscal vigente | [PLACEHOLDER] | [PLACEHOLDER] | |
| Memo fiscal de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan memos fiscales, análisis y calendarios]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo:**

- Si el Rol es Abogado/a tributarista: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LETRADO — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO IDÓNEO ANTES DE ACTUAR`

---

*Re-ejecutar: `/fiscal:entrevista-inicial --redo`*
