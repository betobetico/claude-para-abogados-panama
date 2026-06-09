<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin se almacena en una ruta independiente de versión que sobrevive a actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/procesal/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración de esa ruta. No de este archivo.
2. Si ese archivo no existe o aún contiene marcadores [PLACEHOLDER], DETENERSE antes de hacer trabajo sustantivo. Decir: "Este plugin necesita configuración antes de generar resultados útiles. Ejecuta /procesal:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica real." NO proceder con configuración por defecto o placeholder. Los únicos skills que funcionan sin configuración son /procesal:entrevista-inicial y cualquier flag --verificar-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua de caché
   (~/.claude/plugins/cache/claude-para-abogados/procesal/<versión>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa se encuentran en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md` — un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Procesal

*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta entonces, es
una plantilla. Si ves valores `[PLACEHOLDER]` abajo, ejecuta `/procesal:entrevista-inicial`
para ser entrevistado.*

*Una vez poblado: edita este archivo directamente. Cada skill de este plugin lo lee
antes de hacer nada. Corrige algo aquí y queda corregido en todas partes.*

---

## Quiénes somos

[Nombre de la Empresa / Despacho] es [tipo de entidad / despacho]. El equipo de litigación/procesal lo forman [N] personas. [Nombre del socio/a responsable] es el punto final de escalado. Llevamos aproximadamente [N] asuntos activos en [N] jurisdicciones ante el Órgano Judicial de Panamá.

*(Datos de empresa proceden de perfil-empresa.md — editar allí para cambiar en todos los plugins.)*

**Lo que más duele:** [PLACEHOLDER — lo que el equipo dijo que les duele, en sus propias palabras]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Apoderado judicial/corresponsal]

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a idóneo/a | Apoderado/a judicial | No jurista con acceso a abogado | No jurista sin acceso a abogado]
**Contacto abogado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado/a idóneo/a]

---

## Jurisdicciones activas

| Jurisdicción | Volumen | Tipos habituales | Despacho externo (si aplica) |
|---|---|---|---|
| Civil | [PLACEHOLDER — alto/medio/bajo/inactivo] | [PLACEHOLDER] | [PLACEHOLDER] |
| Comercial | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Penal | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Contencioso-administrativo | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Laboral | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

**Distritos judiciales habituales:** [PLACEHOLDER — ej., "Panamá, San Miguelito, Colón, Chiriquí (David)"]

**Plataformas telemáticas:**
- Sistema de notificaciones del Órgano Judicial: [PLACEHOLDER ✓/✗] [verificar]
- Otras plataformas del Órgano Judicial (consulta de expedientes, gestión judicial): [PLACEHOLDER] [verificar]

---

## Tipos de proceso habituales

### Jurisdicción civil

| Proceso | Cuantía/Criterio | Referencia (Código Judicial) | Uso habitual |
|---|---|---|---|
| Proceso ordinario | Según cuantía/materia | Código Judicial de Panamá [verificar] | [PLACEHOLDER] |
| Proceso sumario / oral | Materias y cuantías especiales | Código Judicial de Panamá [verificar] | [PLACEHOLDER] |
| Proceso ejecutivo | Título ejecutivo (deuda líquida y exigible) | Código Judicial de Panamá [verificar] | [PLACEHOLDER] |
| Ejecución de sentencia | Sentencia ejecutoriada | Código Judicial de Panamá [verificar] | [PLACEHOLDER] |
| Ejecución de títulos no judiciales | Escritura pública, documento de crédito | Código Judicial de Panamá [verificar] | [PLACEHOLDER] |
| Medidas cautelares (secuestro, etc.) | Periculum in mora + verosimilitud del derecho | Código Judicial de Panamá [verificar] | [PLACEHOLDER] |

### Jurisdicción comercial / societaria

| Proceso | Referencia | Uso habitual |
|---|---|---|
| Impugnación de acuerdos de junta de accionistas | Ley 32 de 1927 (sociedades anónimas) + Código Judicial | [PLACEHOLDER] |
| Responsabilidad de directores y dignatarios | Ley 32 de 1927 + Código de Comercio | [PLACEHOLDER] |
| Competencia desleal / consumo | Ley 45 de 2007 (ACODECO) [verificar] | [PLACEHOLDER] |
| Propiedad industrial / intelectual | Ley 35 de 1996 / Ley 64 de 2012 (DIGERPI) [verificar] | [PLACEHOLDER] |
| [PLACEHOLDER — otros procesos habituales] | | |

### Jurisdicción contencioso-administrativa (Sala Tercera de la CSJ)

| Proceso | Referencia | Uso habitual |
|---|---|---|
| Demanda de plena jurisdicción | Código Judicial / Ley 135 de 1943 | [PLACEHOLDER] |
| Demanda de nulidad | Código Judicial / Ley 135 de 1943 | [PLACEHOLDER] |
| Protección de derechos humanos / amparo | Constitución / Código Judicial | [PLACEHOLDER] |
| Medidas cautelares (suspensión del acto) | Código Judicial | [PLACEHOLDER] |

### Jurisdicción laboral

| Proceso | Referencia (Código de Trabajo) | Uso habitual |
|---|---|---|
| Proceso ordinario laboral | Código de Trabajo de Panamá [verificar] | [PLACEHOLDER] |
| Despido injustificado / reintegro | Código de Trabajo de Panamá [verificar] | [PLACEHOLDER] |
| Conflicto colectivo | Código de Trabajo de Panamá [verificar] | [PLACEHOLDER] |
| Recurso de apelación laboral | Código de Trabajo de Panamá [verificar] | [PLACEHOLDER] |

---

## Términos procesales — Reglas de cómputo

**Regla general (Código Judicial de Panamá):** [verificar]
- Días hábiles: lunes a viernes (excluidos sábados, domingos y días feriados o de duelo nacional declarados)
- No existe una vacancia judicial general anual equivalente al "agosto inhábil" español; los términos corren salvo declaratoria oficial de feriado o duelo nacional. Verificar el calendario del Órgano Judicial [verificar]
- Hora límite de presentación: hasta el cierre del despacho judicial del último día del término, o según el sistema de notificaciones del Órgano Judicial [verificar]

**Términos críticos:** [verificar todos los plazos concretos antes de usarlos]
| Acto procesal | Término | Norma | Notas |
|---|---|---|---|
| Contestación a la demanda (proceso ordinario) | [n] días hábiles [verificar] | Código Judicial | Desde notificación |
| Contestación a la demanda (proceso sumario/oral) | [n] días hábiles [verificar] | Código Judicial | Desde notificación |
| Recurso de reconsideración | [n] días [verificar] | Código Judicial | Desde notificación |
| Recurso de apelación (anuncio/sustentación) | [n] días [verificar] | Código Judicial | Desde notificación de resolución |
| Recurso de casación (ante la CSJ) | [n] días [verificar] | Código Judicial | Desde notificación |
| Recurso de hecho | [n] días [verificar] | Código Judicial | Tras negativa de concesión del recurso |
| Oposición en proceso ejecutivo | [n] días [verificar] | Código Judicial | Desde requerimiento/notificación |
| Demanda contencioso-administrativa de plena jurisdicción | [n] meses [verificar] | Código Judicial / Ley 135 de 1943 | Desde notificación/publicación del acto |
| Demanda por despido (laboral) | [n] días [verificar] | Código de Trabajo | Desde el despido |
| [PLACEHOLDER — términos adicionales relevantes] | | | |

**Sistema de alertas de términos:** [PLACEHOLDER — ej., "Calendario compartido con alertas 5 días antes del vencimiento; doble verificación por apoderado judicial y abogado"]

---

## Matriz de severidad de asuntos

| Severidad | Criterio | Ejemplo | Responsable mínimo |
|---|---|---|---|
| 🔴 Crítico | [PLACEHOLDER — ej., "Cuantía >B/.1M, riesgo reputacional, medidas cautelares contra nosotros, proceso penal contra directivos"] | [PLACEHOLDER] | [Socio/a director/a] |
| 🟠 Alto | [PLACEHOLDER — ej., "Cuantía B/.200K-B/.1M, asuntos con publicidad, recursos de casación ante la CSJ"] | [PLACEHOLDER] | [Socio/a responsable] |
| 🟡 Medio | [PLACEHOLDER — ej., "Cuantía B/.50K-B/.200K, procesos ordinarios"] | [PLACEHOLDER] | [Abogado/a senior] |
| 🟢 Bajo | [PLACEHOLDER — ej., "Cuantía <B/.50K, procesos sumarios rutinarios, ejecuciones sin oposición"] | [PLACEHOLDER] | [Abogado/a junior] |

---

## Estilo house de escritos

### Estructura de escritos procesales

**Encabezamiento:** [PLACEHOLDER — ej., "HONORABLE JUEZ [jurisdicción] DEL CIRCUITO DE [provincia], RAMO [civil/etc.] / Proceso [tipo] — Entrada n.º [XXX]"]

**Cuerpo:**
1. Hechos (numerados)
2. Fundamentos de derecho (numerados, con subdivisiones si es necesario)
3. Petición / parte petitoria (con peticiones numeradas)

**Peticiones accesorias / pruebas:** [PLACEHOLDER — ej., "Acompañar pruebas documentales y aducir pruebas; numerar si hay varias"]

### Citas de jurisprudencia

**Formato de cita:** [PLACEHOLDER — ej., "Fallo de la Sala Primera (de lo Civil) de la Corte Suprema de Justicia de [fecha], registro judicial [referencia]"] [verificar]

**Bases de datos utilizadas:**
- [PLACEHOLDER — ej., "Buscador de jurisprudencia del Órgano Judicial / Registro Judicial — acceso público"]
- [PLACEHOLDER — ej., "vLex — suscripción del despacho"]
- [PLACEHOLDER — ej., "otras bases de datos jurídicas panameñas"]

**Criterios de selección de jurisprudencia:**
- [PLACEHOLDER — ej., "Priorizar fallos de la Corte Suprema de Justicia sobre los de Tribunales Superiores; citar jurisprudencia reciente; incluir siempre la referencia de registro judicial"]

### Referencias normativas

**Formato:** [PLACEHOLDER — ej., "art. [X] del Código Judicial, art. [X] del Código Civil, art. [X] de la Constitución Política"] [verificar]

---

## Despachos externos — Gestión de relación

| Despacho | Especialidad | Jurisdicción | Contacto | Condiciones |
|---|---|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER — ej., "Fee cap B/.X, reporte mensual"] |

**Reporte exigido:** [PLACEHOLDER — ej., "Informe mensual de estado con: actuaciones del período, próximos hitos, estimación de costes, valoración de riesgo"]

**Aprobación de costes:** [PLACEHOLDER — ej., "Provisiones >B/.X requieren aprobación previa; minutas revisadas trimestralmente"]

---

## Medidas cautelares

**Posición como solicitante:**
- [PLACEHOLDER — ej., "Solicitar siempre que haya riesgo real de insolvencia o de frustración del fallo; ofrecer caución proporcional"]

**Posición como demandado:**
- [PLACEHOLDER — ej., "Oponerse siempre; solicitar caución sustitutoria; recurrir si se adoptan"]

**Tipos habituales solicitados/recibidos:**
- [PLACEHOLDER — ej., "Secuestro de bienes, anotación de la demanda, cesación de actos de competencia desleal, medidas de aseguramiento de prueba"]

---

## Costas procesales

**Criterio legal:** Condena en costas a la parte vencida conforme al Código Judicial de Panamá [verificar]

**Posición house:** [PLACEHOLDER — ej., "Solicitar siempre costas a la contraparte; objetar la tasación si excede los baremos de referencia"]

**Baremos de referencia:** [PLACEHOLDER — ej., "Tarifas de honorarios y costas del Colegio Nacional de Abogados de Panamá / aranceles aplicables"] [verificar]

**Límite de responsabilidad por costas:** [PLACEHOLDER — ej., "según el límite que fije el Código Judicial sobre la cuantía del proceso"] [verificar]

---

## Matriz de escalado

| Puede resolver | Sin escalar | Escala a | Vía |
|---|---|---|---|
| [Abogado/a junior] | [PLACEHOLDER — ej., "Procesos sumarios <B/.6K, ejecuciones sin oposición"] | [Abogado/a senior] | [método] |
| [Abogado/a senior] | [PLACEHOLDER — ej., "Ordinarios, apelaciones, contencioso-administrativo"] | [Socio/a responsable] | [método] |
| [Socio/a responsable] | [PLACEHOLDER — ej., "Todo lo que no sea casación ante la CSJ o asunto 🔴"] | [Socio/a director/a / despacho externo] | [método] |

**Escalados automáticos:**
- [PLACEHOLDER — ej., "Todo proceso penal, toda medida cautelar recibida, todo recurso ante la Corte Suprema de Justicia, todo asunto con publicidad en medios"]

---

## Legislación de referencia

Las siguientes normas son la base del análisis de este plugin:

- **Código Judicial de Panamá** — norma procesal general (civil, penal, contencioso) [verificar]
- **Constitución Política de la República de Panamá** — garantías del debido proceso y organización del Órgano Judicial
- **Código de Trabajo de Panamá** — proceso laboral [verificar]
- **Ley 38 de 2000** — procedimiento administrativo general [verificar]
- **Ley 12 de 2016** — proceso concursal de insolvencia [verificar]
- **Ley 135 de 1943** y reformas — jurisdicción contencioso-administrativa (Sala Tercera de la CSJ) [verificar]
- **Código de Ética y Responsabilidad Profesional del Abogado** [verificar]
- **Régimen legal de arbitraje en Panamá** (Ley 131 de 2013, arbitraje comercial) [verificar]

---

## Postura ante juicios subjetivos

Cuando un skill de este plugin afronta un juicio subjetivo y la respuesta es incierta, el skill **prefiere el error recuperable**: marca la línea con `[revisión]` inline. Infra-marcar es una puerta de un solo sentido; sobre-marcar es una puerta de dos sentidos que un abogado cierra en 30 segundos.

---

*Para volver a ejecutar la entrevista: `/procesal:entrevista-inicial --repetir`*
