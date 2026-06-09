<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin se almacena en una ruta independiente de versión que sobrevive a actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/laboral/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración de esa ruta. No de este archivo.
2. Si ese archivo no existe o aún contiene marcadores [PLACEHOLDER], DETENERSE antes de hacer trabajo sustantivo. Decir: "Este plugin necesita configuración antes de generar resultados útiles. Ejecuta /laboral:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica real." NO proceder con configuración por defecto o placeholder. Los únicos skills que funcionan sin configuración son /laboral:entrevista-inicial y cualquier flag --verificar-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua de caché
   (~/.claude/plugins/cache/claude-para-abogados/laboral/<versión>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa se encuentran en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md` — un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Laboral

*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta entonces, es
una plantilla. Si ves valores `[PLACEHOLDER]` abajo, ejecuta `/laboral:entrevista-inicial`
para ser entrevistado.*

*Una vez poblado: edita este archivo directamente. Cada skill de este plugin lo lee
antes de hacer nada. Corrige algo aquí y queda corregido en todas partes.*

---

## Quiénes somos

[Nombre de la Empresa / Despacho] es [tipo de entidad]. El equipo de derecho laboral lo forman [N] personas. [Nombre del responsable] es el punto final de escalado. Gestionamos aproximadamente [N] consultas/expedientes laborales al mes.

*(Datos de empresa proceden de perfil-empresa.md — editar allí para cambiar en todos los plugins.)*

**Lo que más duele:** [PLACEHOLDER — lo que el equipo dijo que les duele, en sus propias palabras]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna / RRHH | Asesor laboral]

**Tamaño de plantilla (si asesoría interna):** [PLACEHOLDER — ej., "<50 / 50-250 / >250 trabajadores"]

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a laboralista idóneo/a | RRHH con acceso a abogado | RRHH sin acceso a abogado]
**Contacto del abogado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado/a]

---

## Convención colectiva aplicable

**Convención:** [PLACEHOLDER — ej., "Convención colectiva de trabajo entre [empresa] y [sindicato], registrada en MITRADEL el XX/XX/XXXX"]
**Vigencia:** [PLACEHOLDER — ej., "2023-2027"]
**Régimen especial aplicable:** [PLACEHOLDER — ej., "Zona Libre de Colón / Ciudad del Saber / Panamá Pacífico / régimen SEM / ninguno"]

**Convenciones adicionales si hay varios centros o sindicatos:**
- [PLACEHOLDER]

**Posición ante ausencia de convención:** [PLACEHOLDER — ej., "Aplicar los mínimos del Código de Trabajo; escalar a abogado si hay duda"]

---

## Tipos de contrato — Referencia y posición

| Tipo de contrato | Referencia legal | Uso habitual | Posición house |
|---|---|---|---|
| Por tiempo indefinido | Código de Trabajo | [PLACEHOLDER] | [PLACEHOLDER — ej., "Tipo por defecto"] |
| Por tiempo definido | Código de Trabajo | [PLACEHOLDER] | [PLACEHOLDER — ej., "Solo con causa real; vigilar la conversión a indefinido"] |
| Por obra determinada | Código de Trabajo | [PLACEHOLDER] | [PLACEHOLDER] |
| De aprendizaje / formación | Código de Trabajo / INADEH [verificar] | [PLACEHOLDER] | [PLACEHOLDER] |

**Modelos house de contrato:** [PLACEHOLDER — ej., "Repositorio en Drive/carpeta X; usar siempre modelo house"]

**Cláusulas adicionales habituales en contratos:**
- [PLACEHOLDER — ej., "Período de prueba, dedicación exclusiva, teletrabajo, protección de datos del empleado"]

---

## Despido — Tipos y requisitos

### Despido por causa económica o de operación de la empresa (Código de Trabajo, art. 213 [verificar])

**Causas:** Pérdidas económicas comprobadas, reducción de operaciones, cierre de la empresa o de unidades de producción [verificar]

**Requisitos formales:**
- Aviso de despido por escrito con causa concreta y fecha de efectos
- Trámite ante MITRADEL cuando aplique (autorización o notificación) [verificar]
- Pago de la indemnización por despido injustificado cuando proceda y de la prima de antigüedad [verificar]
- [PLACEHOLDER — requisitos adicionales de la convención aplicable]

**Posición house:** [PLACEHOLDER — ej., "Siempre revisar el aviso con abogado antes de entregar; documentar la causa con evidencia objetiva"]

### Despido por causa justificada disciplinaria (Código de Trabajo, art. 213 [verificar])

**Causas:** Faltas repetidas de asistencia, indisciplina, ofensas, abuso de confianza, bajo rendimiento, embriaguez/toxicomanía en el trabajo, acoso [verificar]

**Requisitos formales:**
- Aviso de despido por escrito con hechos concretos, fechas y causal legal invocada
- Plazo de caducidad para invocar la causa desde su conocimiento [verificar]
- No pueden alegarse posteriormente causas distintas a las indicadas en el aviso
- [PLACEHOLDER — requisitos de la convención: sanciones previas, graduación de faltas]

**Posición house:** [PLACEHOLDER — ej., "Documentar siempre con amonestaciones previas escritas cuando sea posible; consultar abogado antes del despido disciplinario"]

### Despido de trabajador con fuero (maternidad, sindical, dirigente)

**Requisito esencial:**
- Autorización judicial previa ante el Juzgado de Trabajo o la Junta de Conciliación y Decisión competente [verificar]
- Sin autorización previa, el despido es ineficaz y procede el reintegro con salarios caídos [verificar]

**Posición house:** [PLACEHOLDER — ej., "Nunca despedir a trabajador con fuero sin autorización judicial previa; acompañamiento de abogado especializado"]

---

## Período de prueba

**Duración máxima legal (Código de Trabajo):**
- Confirmar el límite máximo de período de prueba aplicable bajo el Código de Trabajo

**Duración según convención aplicable:** [PLACEHOLDER]

**Posición house:** [PLACEHOLDER — ej., "Pactar siempre el período de prueba por escrito; documentar causa de no superación"]

---

## Cláusulas especiales

### No competencia post-contractual

**Posición house:** [PLACEHOLDER — ej., "Incluir solo en contratos de personal clave; pactar contraprestación e interés legítimo del empleador; duración razonable [verificar]"]

**Contraprestación económica:** [PLACEHOLDER]

**Interés legítimo del empleador:** [PLACEHOLDER — ej., "Documentar siempre el interés empresarial legítimo"]

### Cláusula de confidencialidad

**Posición house:** [PLACEHOLDER — ej., "Incluir en todos los contratos; referenciar la normativa panameña de secretos empresariales y la Ley 81 de 2019 de datos personales [verificar]"]

### Pacto de dedicación exclusiva / plena dedicación

**Posición house:** [PLACEHOLDER — ej., "Solo para puestos de dirección o con acceso a información estratégica; contraprestación económica expresa"]

---

## Jornada y salario

**Salario mínimo vigente (MITRADEL):** [PLACEHOLDER — ej., "B/. X.XX por hora según región y actividad; verificar el decreto de salario mínimo vigente"] [verificar]

**Jornada máxima legal:** confirmar la jornada máxima diurna, mixta y nocturna del Código de Trabajo
**Jornada según convención:** [PLACEHOLDER]

**Registro de jornada y asistencia:** [PLACEHOLDER]

**Sobretiempo (horas extraordinarias):**
- Recargos según el Código de Trabajo
- Compensación: [PLACEHOLDER]

**Décimo tercer mes:**
- Tres partidas al año (15 de abril, 15 de agosto y 15 de diciembre) [verificar]
- Equivalente a un día de salario por cada once días trabajados [verificar]
- [PLACEHOLDER — observaciones house]

**Prima de antigüedad:**
- Una semana de salario por cada año de servicio en contratos por tiempo indefinido [verificar]
- [PLACEHOLDER — observaciones house]

**Complementos salariales habituales:** [PLACEHOLDER — ej., "Bono de transporte, comisiones, viáticos, variable por objetivos"]

**Teletrabajo (Ley 126 de 2020):**
- Acuerdo escrito de teletrabajo
- [PLACEHOLDER — política house de teletrabajo]

---

## Licencias y permisos

| Tipo | Duración | Referencia | Posición house |
|---|---|---|---|
| Licencia de maternidad | 14 semanas (6 prenatales, 8 posnatales) [verificar] | Código de Trabajo / CSS [verificar] | [PLACEHOLDER — fuero de maternidad] |
| Licencia de paternidad | [verificar] | Ley aplicable [verificar] | [PLACEHOLDER] |
| Licencia por duelo | [verificar] | Código de Trabajo | [PLACEHOLDER] |
| Licencia no remunerada | Según acuerdo | Código de Trabajo | [PLACEHOLDER] |
| Incapacidad por enfermedad / riesgo profesional | Según certificación de la CSS | Régimen de la CSS [verificar] | [PLACEHOLDER] |
| [PLACEHOLDER — permisos adicionales de la convención] | | | |

---

## Matriz de escalado

| Puede resolver | Sin escalar | Escala a | Vía |
|---|---|---|---|
| [RRHH/paralegal] | [PLACEHOLDER — ej., "Consultas rutinarias, permisos, certificados"] | [Abogado/a laboralista] | [método] |
| [Abogado/a laboralista] | [PLACEHOLDER — ej., "Despidos individuales, sanciones, reclamos <B/. X"] | [Socio/a / responsable] | [método] |
| [Socio/a / responsable] | [PLACEHOLDER — ej., "Despidos colectivos por causa económica, conflictos colectivos, inspecciones de MITRADEL"] | [Comité dirección / despacho externo] | [método] |

**Escalados automáticos:**
- [PLACEHOLDER — ej., "Todo despido de trabajador con fuero, toda demanda ante Junta de Conciliación y Decisión o Juzgado de Trabajo, toda inspección de MITRADEL, hostigamiento laboral"]

---

## Estilo house

**Formato de avisos de despido:** [PLACEHOLDER — ej., "Modelo house obligatorio; siempre revisar por abogado"]
**Formato de informes laborales:** [PLACEHOLDER — ej., "Encabezado, antecedentes, normativa aplicable, análisis, recomendación"]
**Citas normativas:** [PLACEHOLDER — ej., "art. 213 del Código de Trabajo; fallo de la Sala de lo Laboral de la CSJ de DD/MM/AAAA [verificar]"]
**Idioma:** [PLACEHOLDER — ej., "Español; traducciones para trabajadores extranjeros si es necesario"]

---

## Legislación de referencia

Las siguientes normas son la base del análisis de este plugin:

- **Código de Trabajo de Panamá** — norma principal del derecho laboral [verificar]
- **Régimen del décimo tercer mes** — Decreto de Gabinete sobre el XIII mes [verificar]
- **Ley Orgánica de la CSS** — Ley 51 de 2005 (seguridad social y riesgos profesionales) [verificar]
- **Ley 126 de 2020** — Teletrabajo [verificar]
- **Ley 7 de 2018** — Prevención del hostigamiento, acoso y discriminación [verificar]
- **Ley 81 de 2019** — Protección de datos personales (datos del trabajador); autoridad: ANTAI [verificar]
- **MITRADEL** — Resoluciones, salario mínimo y procedimientos administrativos laborales
- **Convención colectiva aplicable** (ver sección específica arriba)

---

## Postura ante juicios subjetivos

Cuando un skill de este plugin afronta un juicio jurídico subjetivo y la respuesta es incierta, el skill **prefiere el error recuperable**: marca la línea específica con `[revisión]` inline. La etiqueta `[revisión]` ES el mecanismo. Infra-marcar es una puerta de un solo sentido; sobre-marcar es una puerta de dos sentidos que un letrado cierra en 30 segundos.

---

*Para volver a ejecutar la entrevista: `/laboral:entrevista-inicial --repetir`*
