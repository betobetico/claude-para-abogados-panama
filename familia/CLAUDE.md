<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/familia/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /familia:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /familia:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/familia/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho de Familia
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/familia:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de derecho de familia se quedan aquí.*

[Empresa] es un [tipo de entidad — firma de abogados / servicio de mediación / consultorio jurídico].
Circuito / juzgado seccional de familia principal: [PLACEHOLDER]. Provincia: [PLACEHOLDER].
El equipo de familia cuenta con [N] personas. Mediadores familiares: [PLACEHOLDER — sí/no, acreditación].
[Responsable del área: nombre o ninguno]. La escalación va a [nombre].

**Perfil de asuntos:** [PLACEHOLDER — divorcios por mutuo consentimiento / por causal / modificación de medidas / ejecución / internacional] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Asuntos de familia abiertos:** [PLACEHOLDER]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Firma mediana/grande | Consultorio jurídico | Servicio de mediación] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a idóneo/a | Mediador/a familiar | Profesional no jurídico sin acceso a abogado]
**Contacto de abogado idóneo:** [PLACEHOLDER — Nombre / equipo / firma externa / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente |
| Sistema de notificaciones del Órgano Judicial | [PLACEHOLDER ✓/✗] | Presentación física en secretaría |
| Calculadora de pensiones (criterio de proporcionalidad) | [PLACEHOLDER ✓/✗] | Cálculo manual |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Alertas de plazos solo bajo demanda |

*Re-comprobar: `/familia:entrevista-inicial --check-integraciones`*

---

## Tipos de procedimiento

| Procedimiento | Frecuencia | Parte habitual | Juzgado competente |
|---|---|---|---|
| Divorcio por mutuo consentimiento | [PLACEHOLDER] | [PLACEHOLDER — ambas partes / una parte] | Juzgado Seccional de Familia del domicilio conyugal [verificar] |
| Divorcio por causal (contencioso) | [PLACEHOLDER] | [PLACEHOLDER — demandante / demandado] | Juzgado Seccional de Familia del domicilio del demandado [verificar] |
| Guarda, crianza y comunicación (padres no casados) | [PLACEHOLDER] | [PLACEHOLDER] | Juzgado Seccional de Familia / de Niñez y Adolescencia [verificar] |
| Modificación de medidas | [PLACEHOLDER] | [PLACEHOLDER] | Juzgado que dictó la sentencia originaria |
| Ejecución de sentencia de familia | [PLACEHOLDER] | [PLACEHOLDER] | Juzgado que dictó la sentencia |
| Liquidación del régimen patrimonial | [PLACEHOLDER] | [PLACEHOLDER] | Juzgado Seccional de Familia |
| Sustracción internacional de menores | [PLACEHOLDER] | [PLACEHOLDER] | Autoridad competente (Convenio de La Haya 1980) [verificar] |

---

## Convenio de divorcio

### Contenido habitual (Código de la Familia de Panamá)

| Materia | Posición habitual de la firma | Consideraciones |
|---|---|---|
| Guarda y crianza | [PLACEHOLDER — guarda compartida / exclusiva como preferencia] | Interés superior del menor (Código de la Familia [verificar]); criterio de la jurisdicción de familia |
| Régimen de comunicación y visitas | [PLACEHOLDER — modelo estándar: fines de semana alternos + mitad vacaciones] | [PLACEHOLDER] |
| Uso de vivienda familiar | [PLACEHOLDER — criterio: atribución al progenitor guardador / interés del menor] | Código de la Familia [verificar art.] |
| Pensión alimenticia a los hijos | [PLACEHOLDER — criterio de proporcionalidad] | Código de la Familia [verificar arts.]; gastos ordinarios vs extraordinarios |
| Pensión alimenticia entre cónyuges | [PLACEHOLDER — criterio: necesidad, duración, cuantía] | Código de la Familia [verificar art.] |
| Liquidación del régimen patrimonial | [PLACEHOLDER — se incluye en convenio o proceso aparte] | Según régimen patrimonial aplicable |

### Gastos extraordinarios

| Tipo | Consensuados / judicialmente autorizados | Reparto habitual |
|---|---|---|
| Sanitarios no cubiertos por la CSS / seguro | [PLACEHOLDER] | [PLACEHOLDER — 50/50 o proporcional] |
| Actividades extraescolares | [PLACEHOLDER] | [PLACEHOLDER] |
| Educación especial / refuerzo | [PLACEHOLDER] | [PLACEHOLDER] |
| Otros (licencia de conducir, viajes, etc.) | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Regímenes patrimoniales del matrimonio

### Código de la Familia de Panamá

| Régimen | Descripción | Liquidación | Base legal |
|---|---|---|---|
| Sociedad de gananciales | Bienes comunes los adquiridos durante el matrimonio a título oneroso | Inventario → avalúo → liquidación → adjudicación | Código de la Familia [verificar arts.] |
| Separación de bienes | Cada cónyuge conserva la propiedad de sus bienes | No hay masa común que liquidar (salvo bienes en copropiedad) | Código de la Familia [verificar arts.] |
| Participación en las ganancias | Cada cónyuge adquiere derecho a participar en las ganancias del otro | Cálculo de ganancias y derecho de crédito | Código de la Familia [verificar arts.] |

**Régimen legal supletorio:** [verificar — confirmar el régimen aplicable a falta de capitulaciones según el Código de la Familia y la fecha del matrimonio]

**Régimen aplicable habitualmente:** [PLACEHOLDER — según los clientes de la firma]

---

## Uniones de hecho

| Campo | Detalle | Base legal |
|---|---|---|
| Reconocimiento | Unión de hecho con efectos de matrimonio tras cumplir los requisitos legales | Código de la Familia [verificar arts.] |
| Requisitos | [PLACEHOLDER — convivencia estable, singular, por el tiempo legal; ausencia de impedimentos] | [verificar] |
| Efectos patrimoniales | [PLACEHOLDER — aplicación del régimen patrimonial del matrimonio una vez reconocida] | Código de la Familia [verificar] |

**Nota:** La unión de hecho reconocida produce, en su caso, efectos análogos al matrimonio conforme al Código de la Familia. [verificar]

---

## Mediación familiar

| Campo | Detalle | Base legal |
|---|---|---|
| Marco legal | Mediación y métodos alternos de solución de conflictos | Decreto Ley 5 de 1999 [verificar] |
| Centros / acreditación | [PLACEHOLDER — centros de métodos alternos del Órgano Judicial / privados] | [verificar] |
| Mediadores acreditados en el equipo | [PLACEHOLDER — sí/no, nombres, número de registro] | |
| Derivación judicial a mediación | [PLACEHOLDER — frecuencia, juzgados que derivan habitualmente] | [verificar] |

---

## Medidas cautelares y de protección

| Tipo | Cuándo | Plazo | Base legal |
|---|---|---|---|
| Medidas de protección (violencia doméstica) | Urgencia: riesgo para la víctima | [PLACEHOLDER — plazo] | Ley 82 de 2013 [verificar] |
| Medidas provisionales (con la demanda) | Con la admisión de la demanda | Vigentes hasta sentencia firme | Código Judicial / Código de la Familia [verificar] |
| Medidas definitivas | En sentencia | Hasta modificación judicial | Código de la Familia [verificar] |

---

## Ejecución de sentencias de familia

| Incumplimiento | Mecanismo | Plazo | Base legal |
|---|---|---|---|
| Impago de pensión alimenticia | Ejecución; posible apremio corporal / responsabilidad penal por incumplimiento de deberes de familia | [verificar] | Código de la Familia / Código Penal [verificar arts.] |
| Incumplimiento de régimen de comunicación y visitas | Ejecución no dineraria; medidas coercitivas; revisión de la guarda en casos graves | — | Código de la Familia [verificar art.] |
| Incumplimiento de uso de vivienda | Lanzamiento / desalojo | — | Código Judicial [verificar] |

---

## Sustracción internacional de menores

| Campo | Detalle | Base legal |
|---|---|---|
| Marco legal | Convenio de La Haya de 25 de octubre de 1980 sobre los Aspectos Civiles de la Sustracción Internacional de Menores (Panamá es parte) | Convenio de La Haya 1980 [verificar ratificación] |
| Autoridad Central panameña | [PLACEHOLDER — autoridad central designada en Panamá] | [verificar] |
| Marco regional | Convención Interamericana sobre Restitución Internacional de Menores (CIDIP) [verificar aplicabilidad] | [verificar] |
| Plazo de resolución | 6 semanas (objetivo del Convenio) | Art. 11 Convenio de La Haya |
| Excepciones a la restitución | Art. 13 Convenio: grave riesgo, oposición del menor con madurez suficiente, integración en nuevo medio | Art. 13 Convenio |

*Referencia comparada internacional: el Convenio de La Haya y la CIDIP son tratados aplicables en Panamá si están ratificados; verificar el estado de ratificación.*

---

## Violencia doméstica — Aspectos civiles

| Campo | Detalle | Base legal |
|---|---|---|
| Marco legal | Femicidio y violencia contra la mujer; violencia doméstica | Ley 82 de 2013 [verificar] |
| Medidas de protección | Medidas cautelares a favor de la víctima | Ley 82 de 2013 [verificar art.] |
| Medidas civiles asociadas | Atribución de vivienda, guarda, régimen de comunicación, pensión alimenticia | Código de la Familia / Ley 82 de 2013 [verificar] |
| Suspensión de régimen de comunicación y visitas | Posible si el menor es víctima directa o indirecta | Código de la Familia [verificar art.] |

**Nota sensible:** Los asuntos de violencia doméstica requieren especial cuidado en la confidencialidad y protección de datos de la víctima (Ley 81 de 2019 de protección de datos personales).

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Divorcio por mutuo consentimiento | Equipo de familia | — | — |
| Divorcio por causal (contencioso) | Equipo de familia | Socio/Director | Si patrimonio > [PLACEHOLDER en B/.] o guarda disputada |
| Sustracción internacional | — | Socio/Director + Internacional | Siempre |
| Violencia doméstica | — | Socio/Director + Penal | Siempre |
| Liquidación de régimen patrimonial complejo | — | Socio/Director + Patrimonial | Si patrimonio > [PLACEHOLDER en B/.] |
| Ejecución con indicios de insolvencia | Equipo de familia | Socio/Director | Si impago > 6 meses |

---

## Referencias legislativas principales

- **Código de la Familia de Panamá** (Ley 3 de 1994 [verificar]) — matrimonio, filiación, patria potestad, guarda y crianza, alimentos, régimen patrimonial del matrimonio, uniones de hecho
- **Código Judicial de Panamá** — procesos de familia y jurisdicción de familia (Ley 42 de 1999 [verificar])
- **Ley 82 de 2013** [verificar] — femicidio y violencia contra la mujer
- **Ley 46 de 2013** [verificar] — adopciones
- **Decreto Ley 5 de 1999** [verificar] — métodos alternos de solución de conflictos (mediación, arbitraje)
- **Ley 81 de 2019** — protección de datos personales (víctimas y menores)
- **Convenio de La Haya 1980** — sobre Aspectos Civiles de la Sustracción Internacional de Menores [verificar ratificación]
- **Código de Derecho Internacional Privado de Panamá** (Ley 7 de 2014 [verificar]) y Código de Bustamante — efectos del matrimonio con elemento internacional

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Convenio de divorcio tipo | [PLACEHOLDER] | [PLACEHOLDER] | |
| Demanda de divorcio por causal de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |
| Modelo de solicitud de medidas provisionales | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan convenios, demandas, informes y dictámenes]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo:**

- Si el Rol es Abogado/a idóneo/a: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LEGAL — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO IDÓNEO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO IDÓNEO ANTES DE ACTUAR`

---

*Re-ejecutar: `/familia:entrevista-inicial --redo`*
