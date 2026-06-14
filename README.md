# Claude para Abogados (Panamá)

Agentes, skills y conectores de referencia para los flujos de trabajo jurídicos más habituales en Panamá — societario, mercantil, laboral, propiedad intelectual, procesal, privacidad, consumo, regulatorio, gobernanza de IA, fiscal, administrativo, inmobiliario, concursal, familia, protección de datos, startups, clínica jurídica y estudiantes de Derecho.

> **¿Primera vez aquí?** Empieza por [QUICKSTART.md](QUICKSTART.md) — instalación en 60 segundos. Este README es la referencia completa.

> [!NOTE]
> **Atribución** — Este proyecto es una adaptación al **derecho panameño** de [claude-para-abogados](https://github.com/betobetico/claude-para-abogados) (la adaptación al derecho español), que a su vez deriva de [claude-for-legal](https://github.com/anthropics/claude-for-legal), el repositorio original creado por [Anthropic](https://www.anthropic.com). Toda la arquitectura de plugins, los patrones de diseño, la estructura de cold-start interviews y el concepto de perfiles de práctica son mérito del equipo de Anthropic. Este repositorio toma ese trabajo como base, parte de la versión española y reescribe las referencias normativas al ordenamiento jurídico de la **República de Panamá**. **El crédito del diseño original corresponde íntegramente a Anthropic.**

> [!CAUTION]
> **Descargo de responsabilidad**
>
> **Este proyecto NO ha sido testado con casos reales.** Los skills, agentes y perfiles de práctica han sido diseñados conforme a la legislación panameña, pero no han sido validados en producción con documentos jurídicos reales. Pueden contener errores, omisiones o interpretaciones incorrectas. Muchas citas concretas (números de ley, artículos, plazos) están marcadas con `[verificar]` y deben confirmarse contra la fuente oficial (Gaceta Oficial, Órgano Judicial, DGI, etc.) antes de cualquier uso.
>
> **Esto es una herramienta, no un sustituto del criterio profesional.** La inteligencia artificial asiste, pero no piensa por ti. Todo resultado generado por estos agentes requiere:
> - **Revisión humana** por un profesional cualificado antes de cualquier uso
> - **Pensamiento crítico** — no aceptes ningún resultado sin verificarlo
> - **Criterio profesional** — el abogado que usa la herramienta es quien decide, no la herramienta
>
> Este proyecto se proporciona "tal cual" (*as is*), sin garantías de ningún tipo, expresas o implícitas. **No constituye asesoramiento jurídico, ni sustituye el criterio de un abogado idóneo.**
>
> Los autores y colaboradores de este proyecto **no se hacen responsables** de ningún daño, perjuicio, pérdida económica o consecuencia de cualquier naturaleza derivados del uso, mal uso o imposibilidad de uso de estas herramientas. Esto incluye, sin limitación:
> - Errores en el contenido legal o referencias normativas incorrectas
> - Interpretaciones incorrectas de la legislación
> - Cambios normativos no reflejados en el proyecto
> - Decisiones tomadas basándose en los resultados generados
> - Plazos, cálculos o importes incorrectos
>
> **Todo resultado generado es un borrador para revisión profesional** — no es un dictamen, no es una conclusión jurídica, no sustituye a un abogado. Un abogado idóneo debe revisar, verificar y asumir la responsabilidad profesional de cualquier documento antes de su uso.
>
> El uso de este proyecto implica la aceptación de estas condiciones.

> [!IMPORTANT]
> **Estos plugins no representan posiciones jurídicas de Anthropic, ni de los autores de esta adaptación, ni de ninguna otra entidad.** Son herramientas que ayudan a los profesionales del Derecho a analizar cuestiones jurídicas. Cuando un skill incluye un checklist, un marco de análisis, una señal de riesgo o una caracterización de jurisprudencia o normativa, se trata de una ayuda al análisis del abogado, no de una opinión jurídica vinculante. La legislación en muchas de estas áreas está en evolución y sujeta a interpretación. El abogado que utiliza el plugin — no el plugin, y no los autores — es responsable de las posiciones jurídicas adoptadas en su trabajo.

---

## Agentes

Cada agente lleva el nombre del flujo de trabajo que ejecuta. Son el punto de entrada más habitual — empieza por los que encajan con tu práctica y ajusta el skill, el perfil de práctica y los conectores a cómo trabaja tu equipo.

### Societario

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Revisor de due diligence** | Revisión tabular de data room con una fila por documento y cada celda citada | `societario` | `/societario:revision-tabular` |
| **Extractor de incidencias** | Lee documentos del VDR y extrae incidencias por categoría y materialidad | `societario` | `/societario:extraccion-incidencias` |
| **Redactor de acuerdos sociales** | Redacta acuerdos de junta y junta directiva en formato del despacho | `societario` | `/societario:acuerdo-social` |
| **Tracker de cumplimiento societario** | Tasa única anual, agente residente, libros sociales, registros en el Registro Público | `societario` | `/societario:cumplimiento` |
| **Checklist de cierre** | Seguimiento de condiciones, consentimientos y documentos pendientes de cierre | `societario` | `/societario:checklist-cierre` |
| **Vigilante de data room** | Monitoriza el VDR para nuevas subidas y actualiza el estado del cierre | `societario` | agente programado |

### Mercantil

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Revisor de contratos mercantiles** | Revisa un contrato contra tu playbook y genera un memo de observaciones | `mercantil` | `/mercantil:revision` |
| **Triaje de NDAs** | VERDE/AMARILLO/ROJO — solo los complicados llegan al abogado | `mercantil` | `/mercantil:revision` |
| **Trazador de adendas** | Traza cómo ha cambiado un contrato a lo largo de sus modificaciones | `mercantil` | `/mercantil:historial-adendas` |
| **Vigilante de renovaciones** | Escanea el registro de contratos buscando vencimientos y renovaciones | `mercantil` | agente programado |
| **Debrief semanal** | Revisión semanal de contratos firmados con desviaciones del playbook | `mercantil` | agente programado |
| **Router de escalado** | Deriva cuestiones contractuales al aprobador correcto | `mercantil` | `/mercantil:escalado` |

### Laboral

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Revisor de despidos** | Analiza un despido propuesto contra el Código de Trabajo y la causa justificada | `laboral` | `/laboral:revision-despido` |
| **Revisor de contratación** | Revisa contratos de trabajo, cláusulas de no competencia, período de prueba | `laboral` | `/laboral:revision-contratacion` |
| **Clasificador de relación laboral** | Test de subordinación: relación laboral vs. servicios profesionales | `laboral` | `/laboral:clasificacion` |
| **Redactor de políticas** | Redacta políticas laborales conforme al Código de Trabajo | `laboral` | `/laboral:politica` |
| **Calculadora de prestaciones** | Cálculo de prima de antigüedad, indemnización y décimo tercer mes | `laboral` | `/laboral:indemnizacion` |
| **Q&A laboral** | Respuesta rápida a consultas laborales con referencia al Código de Trabajo | `laboral` | `/laboral:consulta` |

### Propiedad Intelectual

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Screening de marca** | Primera búsqueda de disponibilidad con heurísticas de confusión (DIGERPI) | `propiedad-intelectual` | `/pi:busqueda-marca` |
| **Redactor de requerimiento** | Redacta o triaja un requerimiento extrajudicial de cese | `propiedad-intelectual` | `/pi:burofax` |
| **Revisor de licencias OSS** | Clasifica licencias open source según tu modelo de distribución | `propiedad-intelectual` | `/pi:oss` |
| **Triaje de infracción** | Triaje de marca/copyright/patente/secreto empresarial — factores, no dictamen | `propiedad-intelectual` | `/pi:triaje-infraccion` |
| **Revisor de cláusulas de PI** | Revisa cesión, titularidad, licencia, garantías e indemnizaciones | `propiedad-intelectual` | `/pi:clausulas` |
| **Tracker de portfolio** | Registros, renovaciones, tasas de mantenimiento (DIGERPI) | `propiedad-intelectual` | `/pi:portfolio` |

### Procesal

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Cronología** | Construye o actualiza una cronología de hechos desde fuentes declaradas | `procesal` | `/procesal:cronologia` |
| **Redactor de demanda** | Borrador de sección de demanda en estilo del despacho | `procesal` | `/procesal:demanda` |
| **Triaje de notificación recibida** | Analiza una demanda/notificación entrante — opciones, términos, derivación | `procesal` | `/procesal:requerimiento-recibido` |
| **Calculadora de términos** | Términos procesales según el Código Judicial con días hábiles | `procesal` | `/procesal:plazos` |
| **Intake de asunto** | Alta de nuevo asunto — ficha, cronología inicial, log | `procesal` | `/procesal:intake` |
| **Briefing de asunto** | Briefing en profundidad de un asunto para reunión con socio o cliente | `procesal` | `/procesal:briefing` |
| **Estado del portfolio** | Distribución de riesgo, próximos términos, asuntos sin actividad | `procesal` | `/procesal:portfolio` |

### Privacidad

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Respondedor de derechos del titular** | Redacta acuse y respuesta sustantiva dentro del plazo legal (Ley 81 de 2019) | `privacidad` | `/privacidad:derechos` |
| **Revisor de encargos de tratamiento** | Revisa un contrato de custodio/encargado del tratamiento contra tu playbook | `privacidad` | `/privacidad:encargo` |
| **Generador de evaluación de impacto** | Genera evaluación de impacto en protección de datos en formato del despacho | `privacidad` | `/privacidad:eipd` |
| **Triaje de tratamiento** | Decide si un tratamiento necesita evaluación de impacto o puede proceder | `privacidad` | `/privacidad:triaje` |
| **Gap regulatorio de privacidad** | Compara un cambio normativo contra tu política de privacidad actual | `privacidad` | `/privacidad:gap` |

### Consumo

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Revisor de lanzamiento** | Revisa un lanzamiento de producto contra tu calibración de riesgo | `consumo` | `/consumo:lanzamiento` |
| **Checker de claims de marketing** | Señala claims que necesitan sustanciación o retirada (Ley 45 de 2007) | `consumo` | `/consumo:claims` |
| **Revisor de condiciones generales** | Analiza cláusulas abusivas en contratos de adhesión con consumidores | `consumo` | `/consumo:condiciones-generales` |
| **¿Esto es un problema?** | Respuesta rápida al "¿podemos hacer esto?" con tu calibración | `consumo` | `/consumo:consulta` |

### Regulatorio

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Vigilante de normativa** | Monitoriza la Gaceta Oficial y boletines de reguladores y genera resumen | `regulatorio` | agente programado |
| **Diff de política** | Compara un cambio normativo contra tu biblioteca de políticas internas | `regulatorio` | `/regulatorio:diff` |
| **Tracker de gaps** | Gaps abiertos — qué se ha señalado y aún no se ha cerrado | `regulatorio` | `/regulatorio:gaps` |
| **Redactor de política** | Propuesta de redacción de política para cerrar un gap (incl. antiblanqueo Ley 23 de 2015) | `regulatorio` | `/regulatorio:redaccion` |

### Gobernanza de IA

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Triaje de caso de uso IA** | Clasifica usos de IA propuestos contra marcos de referencia y tu registro interno | `gobernanza-ia` | `/gobernanza-ia:triaje` |
| **Evaluador de impacto IA** | Evaluación de impacto de IA según los regímenes aplicables | `gobernanza-ia` | `/gobernanza-ia:evaluacion` |
| **Revisor de IA de proveedor** | Revisa cláusulas de IA de proveedores (entrenamiento, responsabilidad, cambios de modelo) | `gobernanza-ia` | `/gobernanza-ia:proveedor` |
| **Gap regulatorio de IA** | Compara nueva regulación de IA contra tu postura de gobernanza actual | `gobernanza-ia` | `/gobernanza-ia:gap` |

### Fiscal

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Calendario fiscal** | Plazos de la DGI por tipo de obligación y forma jurídica | `fiscal` | `/fiscal:calendario` |
| **Revisor de declaraciones** | Revisión de coherencia de declaraciones de ISR e ITBMS | `fiscal` | `/fiscal:revision` |
| **Consulta tributaria** | Respuesta rápida a consultas fiscales con referencia al Código Fiscal y el principio de territorialidad | `fiscal` | `/fiscal:consulta` |
| **Triaje de procedimiento** | Fiscalización, sancionador, reclamación ante el TAT — términos y opciones | `fiscal` | `/fiscal:procedimiento` |

### Administrativo

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Procedimiento administrativo** | Términos, silencio administrativo, recursos (reconsideración, apelación) — Ley 38 de 2000 | `administrativo` | `/administrativo:procedimiento` |
| **Contratación pública** | Revisión de pliegos, criterios de adjudicación, recursos (Ley 22 de 2006) | `administrativo` | `/administrativo:contratacion` |
| **Contencioso-administrativo** | Términos, legitimación y estrategia ante la Sala Tercera de la CSJ | `administrativo` | `/administrativo:contencioso` |

### Inmobiliario

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Revisor de arrendamiento** | Revisa contrato de alquiler contra la ley de arrendamientos y cláusulas habituales | `inmobiliario` | `/inmobiliario:arrendamiento` |
| **Compraventa** | Revisión de contrato de compraventa, promesa, condiciones suspensivas | `inmobiliario` | `/inmobiliario:compraventa` |
| **Propiedad horizontal** | Revisión de reglamento de copropiedad, actas de asamblea, cuotas (Ley 284 de 2022) | `inmobiliario` | `/inmobiliario:comunidad` |

### Concursal

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Diagnóstico de insolvencia** | Análisis de la situación del deudor según la Ley 12 de 2016 | `concursal` | `/concursal:diagnostico` |
| **Plan de reorganización** | Estructura básica de plan de reorganización | `concursal` | `/concursal:plan` |
| **Calificación de créditos** | Clasificación de créditos (privilegiados, ordinarios, subordinados) | `concursal` | `/concursal:creditos` |

### Familia

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Convenio / acuerdo** | Borrador de acuerdo de divorcio/separación con los pactos habituales | `familia` | `/familia:convenio` |
| **Régimen económico** | Análisis del régimen económico matrimonial aplicable (Código de la Familia) | `familia` | `/familia:regimen-economico` |
| **Pensiones** | Cálculo orientativo de pensión alimenticia | `familia` | `/familia:pensiones` |

### Protección de datos

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Registro de actividades** | Genera o actualiza el registro de actividades de tratamiento | `proteccion-datos` | `/proteccion-datos:rat` |
| **Evaluación de impacto** | Evaluación de impacto completa conforme a la Ley 81 de 2019 | `proteccion-datos` | `/proteccion-datos:eipd` |
| **Gestión de brechas** | Protocolo de notificación de brecha ante la ANTAI y a los titulares | `proteccion-datos` | `/proteccion-datos:brecha` |
| **Relación con la ANTAI** | Reclamaciones, fiscalizaciones, procedimiento sancionador | `proteccion-datos` | `/proteccion-datos:antai` |

### Startups

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Constitución de sociedad** | Checklist y borradores de pacto social y acuerdo de accionistas (S.A. / S. de R.L.) | `startups` | `/startups:constitucion` |
| **Stock options** | Estructura de stock options/phantom shares con tratamiento fiscal | `startups` | `/startups:stock-options` |
| **Ronda de inversión** | Revisión de term sheet y SHA con señales de riesgo | `startups` | `/startups:ronda` |
| **Incentivos fiscales** | Mapa de incentivos disponibles (SEM, Ciudad del Saber, zonas especiales) | `startups` | `/startups:incentivos` |
| **Primeras contrataciones** | Guía para contratar los primeros empleados (tipo de contrato, CSS, coste) | `startups` | `/startups:contratacion` |

### Clínica jurídica

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Intake de cliente** | Recepción estructurada con detección de áreas y conflictos | `clinica-juridica` | `/clinica:intake` |
| **Memo de caso** | Memo con estructura IRAC adaptada con gaps de investigación señalados | `clinica-juridica` | `/clinica:memo` |
| **Hoja de ruta de investigación** | Legislación a consultar, jurisprudencia relevante, términos de búsqueda | `clinica-juridica` | `/clinica:investigacion` |
| **Tracker de términos** | Términos del caso con alertas de preclusión | `clinica-juridica` | `/clinica:plazos` |
| **Carta al cliente** | Correspondencia rutinaria — citaciones, solicitud de documentos, actualizaciones | `clinica-juridica` | `/clinica:carta` |

### Estudiante de Derecho

| Agente | Qué hace | Plugin | Comando |
|---|---|---|---|
| **Método socrático** | Pregunta, tú respondes, te desafía — no te da la respuesta | `estudiante-derecho` | `/estudiante:socratico` |
| **Evaluador IRAC** | Evalúa tu caso práctico en estructura, identificación del problema, normas, análisis | `estudiante-derecho` | `/estudiante:irac` |
| **Esquematizador** | Construye o amplía un esquema desde tus apuntes y manual | `estudiante-derecho` | `/estudiante:esquema` |
| **Preparación de concursos / cátedra** | Temas, test y casos prácticos por especialidad | `estudiante-derecho` | `/estudiante:oposiciones` |
| **Preparación de idoneidad** | Práctica para el examen de idoneidad profesional con retroalimentación | `estudiante-derecho` | `/estudiante:acceso` |
| **Fichas de estudio** | Genera o repasa fichas estilo Leitner | `estudiante-derecho` | `/estudiante:fichas` |
| **Planificador de estudio** | Plan a largo plazo con sesiones programadas | `estudiante-derecho` | `/estudiante:plan` |

---

## Estructura del repositorio

```
societario/               # sociedades anónimas, fundaciones de interés privado, due diligence, gobierno corporativo
mercantil/                # contratos mercantiles, NDAs, SaaS, renovaciones
laboral/                  # contratación, despido, prestaciones, clasificación laboral
propiedad-intelectual/    # marcas, patentes, derecho de autor, OSS, cláusulas de PI
procesal/                 # portfolio de asuntos, demandas, términos, cronologías
privacidad/               # encargos de tratamiento, derechos del titular, evaluaciones de impacto
consumo/                  # lanzamientos, claims de marketing, cláusulas abusivas
regulatorio/              # vigilancia Gaceta Oficial, antiblanqueo, diff de políticas, gaps
gobernanza-ia/            # triaje de casos de uso IA, evaluaciones de impacto IA, proveedores
fiscal/                   # calendario DGI, ISR/ITBMS, territorialidad, procedimientos tributarios
administrativo/           # procedimiento administrativo, contratación pública, contencioso
inmobiliario/             # arrendamientos, compraventa, propiedad horizontal
concursal/                # insolvencia, reorganización, calificación de créditos
familia/                  # acuerdos de divorcio, régimen económico, pensiones
proteccion-datos/         # registro de actividades, evaluaciones, brechas, relación con ANTAI
startups/                 # constitución, stock options, rondas, incentivos (SEM/Ciudad del Saber)
clinica-juridica/         # intake, memos, términos, correspondencia
estudiante-derecho/       # socrático, IRAC, idoneidad, fichas
hub-constructor/          # descubrimiento e instalación de skills comunitarios
recetas-agentes/          # cookbooks de agentes programados
references/               # materiales de referencia
scripts/                  # scripts de despliegue y validación
```

Cada directorio de plugin tiene la misma estructura:

```
<plugin>/
  .claude-plugin/plugin.json
  CLAUDE.md               # perfil de práctica — se rellena con /<plugin>:entrevista-inicial
  README.md
  skills/                 # skills — cada uno es un comando /<plugin>:<skill>
  agents/                 # agentes programados (si los hay)
  hooks/                  # hooks pre y post herramienta (si los hay)
```

---

## Conectores MCP

Los plugins alcanzan su máximo potencial cuando están conectados a fuentes de datos autorizadas. Consulta [CONNECTORS.md](CONNECTORS.md) para la lista completa de conectores actuales y deseados.

### MCPs por desarrollar

Estos conectores MCP no existen aún pero multiplicarían el valor de los plugins. Son candidatos naturales para desarrollo:

| MCP | Fuente | Plugins beneficiados | Prioridad |
|---|---|---|---|
| **Gaceta Oficial** | Gaceta Oficial de la República de Panamá (legislación y disposiciones) | regulatorio, fiscal, administrativo, laboral, todos | Alta |
| **Órgano Judicial** | Registro Judicial y jurisprudencia de la CSJ | procesal, clinica-juridica, estudiante-derecho, laboral, familia | Alta |
| **Registro Público** | Información registral de sociedades, fundaciones e inmuebles | societario, mercantil, concursal, inmobiliario | Alta |
| **DGI** | Dirección General de Ingresos (calendario y obligaciones tributarias) | fiscal, startups | Alta |
| **ANTAI** | Resoluciones y guías de la Autoridad Nacional de Transparencia y Acceso a la Información | privacidad, proteccion-datos | Alta |
| **SMV** | Superintendencia del Mercado de Valores | societario, startups, regulatorio | Media |
| **DIGERPI** | Dirección General del Registro de la Propiedad Industrial | propiedad-intelectual | Media |
| **UAF** | Unidad de Análisis Financiero (guías y tipologías) | regulatorio, societario | Media |
| **MITRADEL** | Ministerio de Trabajo y Desarrollo Laboral | laboral, startups | Media |
| **PanamaCompra** | Sistema de contrataciones públicas | administrativo | Media |
| **ACODECO** | Autoridad de Protección al Consumidor y Defensa de la Competencia | consumo | Baja |
| **ANATI** | Autoridad Nacional de Administración de Tierras (catastro) | inmobiliario | Baja |
| **Superintendencia de Bancos** | Normativa y acuerdos del regulador bancario | regulatorio | Baja |
| **AMP** | Autoridad Marítima de Panamá (registro de naves) | societario, mercantil | Baja |

Si desarrollas alguno de estos MCPs o conoces uno existente, abre un issue o un PR.

---

## Estado del proyecto

Este proyecto está en fase inicial. Los skills han sido diseñados pero **no han sido testados con casos reales**. Las referencias legislativas deben verificarse — muchas citas concretas se han marcado con `[verificar]` precisamente para señalar que requieren confirmación contra la fuente oficial.

La **identidad de las normas de base** (qué ley es cada una y de qué trata) ha sido verificada contra fuentes oficiales — ver [VERIFICACION.md](VERIFICACION.md). Los marcadores `[verificar]` que permanecen señalan **artículos, plazos e importes concretos** pendientes de confirmar contra el texto vigente de cada ley.

Se agradecen contribuciones, especialmente:

- Correcciones de referencias normativas y resolución de marcadores `[verificar]`
- Tests con documentos jurídicos reales
- Desarrollo de conectores MCP a fuentes panameñas
- Nuevos skills para áreas no cubiertas

---

## Créditos

Este proyecto es una **adaptación al derecho panameño** de [claude-para-abogados](https://github.com/betobetico/claude-para-abogados) (adaptación al derecho español), que deriva de [claude-for-legal](https://github.com/anthropics/claude-for-legal), creado por [Anthropic](https://www.anthropic.com) y publicado bajo la licencia Apache 2.0.

Todo el mérito del diseño original — la arquitectura de plugins, el sistema de cold-start interviews, los perfiles de práctica, los patrones de agentes programados y el concepto de skills jurídicos — corresponde al equipo de Anthropic. Este repositorio reescribe ese trabajo para el ordenamiento jurídico de la República de Panamá, reenfocando las áreas de práctica hacia el régimen panameño (sociedades anónimas y fundaciones de interés privado, fiscalidad territorial, compliance/antiblanqueo, inmigración, zonas económicas especiales y derecho marítimo).

## Licencia

[Apache 2.0](LICENSE) — la misma licencia que el proyecto original.
