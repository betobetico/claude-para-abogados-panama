<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /inmobiliario:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /inmobiliario:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/inmobiliario/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Inmobiliario
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/inmobiliario:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de derecho inmobiliario se quedan aquí.*

[Empresa] es una [tipo de entidad]. Operaciones inmobiliarias habituales: [PLACEHOLDER — compraventa, arrendamiento, promoción, inversión].
Zona geográfica principal: [PLACEHOLDER — provincia / distrito / corregimiento]. El equipo inmobiliario cuenta con [N] personas.
[Responsable del área: nombre o ninguno]. Notaría habitual: [PLACEHOLDER]. Sección del Registro Público habitual: [PLACEHOLDER].
La escalación va a [nombre].

**Tipología de activos:** [PLACEHOLDER — residencial / comercial / industrial / suelo / mixto] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Asuntos inmobiliarios abiertos:** [PLACEHOLDER — operaciones en curso, litigios, procedimientos registrales]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Promotora / SOCIMI / fondo] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a idóneo | Profesional jurídico no abogado con acceso a abogado | Profesional no jurídico sin acceso a abogado]
**Contacto del abogado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente |
| Registro Público en línea | [PLACEHOLDER ✓/✗] | Solicitud presencial de certificados de finca |
| Catastro / ANATI | [PLACEHOLDER ✓/✗] | Consulta manual |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Alertas de plazos solo bajo demanda |

*Re-comprobar: `/inmobiliario:entrevista-inicial --check-integraciones`*

---

## Tipos de operaciones habituales

| Operación | Frecuencia | Valor medio | Parte habitual | Notas |
|---|---|---|---|---|
| Compraventa | [PLACEHOLDER] | [PLACEHOLDER B/. o USD] | [PLACEHOLDER — comprador/vendedor/ambos] | [PLACEHOLDER] |
| Arrendamiento — vivienda | [PLACEHOLDER] | [PLACEHOLDER B/. o USD] | [PLACEHOLDER — arrendador/arrendatario] | [PLACEHOLDER] |
| Arrendamiento — comercial / uso distinto | [PLACEHOLDER] | [PLACEHOLDER B/. o USD] | [PLACEHOLDER] | [PLACEHOLDER] |
| Promoción inmobiliaria | [PLACEHOLDER] | [PLACEHOLDER B/. o USD] | [PLACEHOLDER] | [PLACEHOLDER] |
| Operaciones societarias con inmuebles | [PLACEHOLDER] | [PLACEHOLDER B/. o USD] | [PLACEHOLDER] | [PLACEHOLDER] |
| [Otra operación] | [PLACEHOLDER] | [PLACEHOLDER B/. o USD] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Compraventa de inmuebles

### Arras y precontrato

| Tipo de arras | Efecto | Uso habitual | Base legal |
|---|---|---|---|
| Penitenciales / de desistimiento | Desistimiento: comprador pierde arras / vendedor las devuelve dobladas | [PLACEHOLDER] | Art. 1224 del Código Civil de Panamá |
| Confirmatorias | Señal a cuenta del precio; no permiten desistimiento | [PLACEHOLDER] | Categoría doctrinal / jurisprudencial (sin texto legal expreso; el art. 1224 solo recoge las penitenciales; el art. 1221 regula la promesa de compraventa) |
| Penales | Pena convencional + cumplimiento forzoso | [PLACEHOLDER] | Cláusula penal — Código Civil de Panamá [verificar] |

**Importe habitual de arras:** [PLACEHOLDER — % del precio]

### Proceso de compraventa — Checklist

| Paso | Responsable | Documentación | Notas |
|---|---|---|---|
| Due diligence registral (Registro Público) | [PLACEHOLDER] | Certificado de finca del Registro Público | Gravámenes, titularidad, superficie, descripción |
| Due diligence de uso de suelo | [PLACEHOLDER] | Certificación / informe municipal | Situación urbanística, afectaciones |
| Due diligence catastral (ANATI) | [PLACEHOLDER] | Plano catastrado, certificación | Concordancia Registro Público-catastro |
| Condiciones suspensivas | [PLACEHOLDER] | Promesa de compraventa / arras | [PLACEHOLDER — financiación, permisos, etc.] |
| Gravámenes inscritos | [PLACEHOLDER] | Certificado de finca | Hipotecas, embargos, secuestros, medidas cautelares |
| Escritura pública | Notario | Escritura de compraventa | [PLACEHOLDER] |
| Liquidación de impuestos | [PLACEHOLDER] | ITBI 2% (Formulario 106, art. 701-g Código Fiscal) y ganancia de capital (retención 3%, Formulario 107) ante la DGI | [PLACEHOLDER] |
| Inscripción en el Registro Público | [PLACEHOLDER] | Copia de la escritura | Perfecciona frente a terceros (publicidad y prioridad registral); arts. 1753-1762 del Código Civil (art. 1762) |

---

## Arrendamiento (régimen panameño)

### Vivienda (régimen tutelado)

| Aspecto | Régimen legal | Posición habitual |
|---|---|---|
| Duración mínima / prórroga | Ley 93 de 1973 (verificar en el texto oficial) | [PLACEHOLDER] |
| Canon inicial | Libre fijación, salvo límites del régimen tutelado [verificar] | [PLACEHOLDER] |
| Actualización del canon | Según pacto y límite legal [verificar] | [PLACEHOLDER] |
| Régimen tutelado por cuantía | El umbral histórico de B/.150/mes (DE 294 de 1994) quedó suspendido por el DE 145 de 2020; el MIVIOT conoce de todos los contratos sin distinción de monto (verificar en el texto oficial) | [PLACEHOLDER — dentro/fuera sí/no] |
| Depósito de garantía | Un (1) mes de canon; consignación ante la Dirección General de Arrendamientos del MIVIOT (art. 13 Ley 93 de 1973, mod. Ley 259 de 2021) | [PLACEHOLDER] |
| Obras del arrendatario | Consentimiento del arrendador [verificar] | [PLACEHOLDER] |
| Resolución / desalojo | Vía gubernativa ante la Dirección General de Arrendamientos del MIVIOT (reconsideración y apelación ante el Ministro) — Ley 93 de 1973 | [PLACEHOLDER] |

### Comercial / uso distinto de vivienda

| Aspecto | Régimen legal | Posición habitual |
|---|---|---|
| Duración | Libre pacto — Código Civil de Panamá | [PLACEHOLDER] |
| Canon y actualización | Libre pacto — Código Civil de Panamá | [PLACEHOLDER] |
| Depósito de garantía | Libre pacto | [PLACEHOLDER] |
| Cesión y subarriendo | Según pacto — Código Civil de Panamá | [PLACEHOLDER] |
| Mejoras del local | Según pacto; reversión / remoción | [PLACEHOLDER] |

---

## Propiedad horizontal (Ley 284 de 2022)

| Aspecto | Normativa | Consideraciones |
|---|---|---|
| Reglamento de copropiedad | Ley 284 de 2022 (Dirección de PH del MIVIOT) | [PLACEHOLDER — restricciones habituales, uso de corto plazo] |
| Actas y acuerdos de asamblea | Ley 284 de 2022 | Un voto por unidad; morosas inhabilitadas para votar (solo voz). Ordinarios: mayoría de unidades presentes/al día. Calificadas (verificar en el texto oficial): 51% para cuota/coeficiente y mejoras adicionales; 66% para fachadas; 66% de unidades que representen ≥75% del valor para reformar el Reglamento. Los acuerdos vinculan a presentes y ausentes (sin plazo de adhesión) |
| Cuotas y gastos extraordinarios | Ley 284 de 2022 | Gastos urgentes vía Desembolso Extraordinario y Fondo para Imprevistos (art. 46) [PLACEHOLDER — política habitual] |
| Impugnación de acuerdos | Ley 284 de 2022 | Plazo según la ley [verificar] |
| Morosos | Ley 284 de 2022 | Proceso ejecutivo (título = estado de cuenta, a partir de 2 meses de mora); obligación de carácter real sobre la unidad; recargo de hasta 20% |
| Fondo para Imprevistos | Art. 46 de la Ley 284 de 2022 | Obligatorio, mínimo 1% de los ingresos anuales; cuenta separada (art. 82); embargo limitado al 20% (art. 47) |
| Alquiler de corto plazo / turístico | Reglamento de copropiedad + Ley 284 de 2022 | Mayoría para limitar o condicionar [verificar] |

---

## Registro Público de Panamá

| Principio registral | Descripción | Base legal |
|---|---|---|
| Legitimación | Lo inscrito se presume exacto e íntegro | Código Civil de Panamá / normativa del Registro Público [verificar] |
| Fe pública registral | Tercero de buena fe que adquiere confiando en el Registro queda protegido | Código Civil de Panamá [verificar] |
| Prioridad | Primer título inscrito prevalece | Normativa del Registro Público [verificar] |
| Tracto sucesivo | Para inscribir un derecho, debe estar inscrito el del transmitente | Normativa del Registro Público [verificar] |
| Calificación | El registrador califica la legalidad de los documentos | Normativa del Registro Público [verificar] |

**Operaciones registrales habituales:** [PLACEHOLDER — inscripciones, marginales, cancelaciones, medidas cautelares]

---

## Uso de suelo y construcción

| Aspecto | Normativa | Consideraciones |
|---|---|---|
| Uso de suelo / zonificación | Normativa de ordenamiento territorial (MIVIOT) y municipal [verificar] | Residencial, comercial, industrial, mixto, rural |
| Permisos de construcción | Reglamentación municipal y de construcción [verificar] | [PLACEHOLDER — permiso de construcción, ocupación] |
| Permiso de ocupación | Municipio / autoridad competente [verificar] | [PLACEHOLDER — obra nueva] |
| Disciplina urbanística | Normativa municipal [verificar] | Plazos variables por municipio [verificar] |
| Planes de ordenamiento territorial | MIVIOT + municipio [verificar] | [PLACEHOLDER — plan vigente, revisiones en curso] |

**Provincia/distrito principal de actuación:** [PLACEHOLDER — normativa municipal aplicable]

---

## Fiscalidad inmobiliaria

| Operación | Impuesto | Tarifa | Notas |
|---|---|---|---|
| Compraventa — transferencia | ITBI (Impuesto de Transferencia de Bienes Inmuebles) | 2% sobre el mayor entre (i) el valor de la escritura y (ii) el valor catastral de adquisición + mejoras + 5% del catastral por año transcurrido (art. 701-g Código Fiscal, Ley 106 de 1974; Formulario 106) | A cargo del vendedor; requisito para inscribir |
| Compraventa — ganancia | Impuesto sobre la ganancia de capital | 10% sobre la ganancia; retención anticipada del 3% del mayor entre valor de venta y catastral (Formulario 107; art. 701 Código Fiscal y DE 170 de 1993) | Retiene el comprador, entera ante la DGI; el vendedor puede optar por el 3% como definitivo o pedir devolución |
| Operación de promotor / giro ordinario | Ganancia de capital — régimen de promotor | 3,75% único y definitivo sobre el mayor entre valor de enajenación y catastral; vivienda nueva escala 0,5%-2,5% (4,5% comercial) | Régimen específico de promotores |
| Operación de promotor | ITBMS (si aplica) | [PLACEHOLDER — verificar incidencia] | El ITBMS no grava la transferencia de inmueble (art. 1057-V Código Fiscal) |
| Impuesto de inmueble | Impuesto de inmueble | Según valor catastral [verificar] | Verificar exoneraciones (p. ej. patrimonio familiar tributario) y paz y salvo [verificar] |
| Renta del arrendador | ISR (Impuesto sobre la Renta) | Según régimen del arrendador [verificar] | Principio de territorialidad |
| Arrendamiento | ITBMS (si comercial) + ISR | [PLACEHOLDER] | [PLACEHOLDER — verificar incidencia del ITBMS] |

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Compraventa rutinaria | Equipo inmobiliario | — | — |
| Gravámenes inscritos complejos | Equipo inmobiliario | Socio/Director | Si afectan a viabilidad de operación |
| Arrendamiento con cláusulas no estándar | Equipo inmobiliario | Socio/Director | Si canon > [PLACEHOLDER] o duración > [PLACEHOLDER] |
| Litigio de arrendamiento (desalojo, resolución) | — | Procesal + Dirección | Siempre |
| Operación con componente de uso de suelo complejo | — | Socio/Director + especialista | Siempre |
| Promoción inmobiliaria | — | Socio/Director + Dirección | Siempre |

---

## Referencias legislativas principales

- **Código Civil de Panamá** — derechos reales, compraventa, arras (art. 1224), promesa (art. 1221), hipoteca, inscripción (arts. 1753-1762); supletorio en arrendamiento
- **Ley 93 de 1973** (mod. Ley 28 de 1974 y Ley 259 de 2021) — medidas sobre los arrendamientos; Dirección General de Arrendamientos del MIVIOT; DE 145 de 2020 (suspensión del umbral de canon)
- **Ley 284 de 2022** — Régimen de propiedad horizontal (subroga la Ley 31 de 2010); art. 46 (Fondo para Imprevistos); Dirección de PH del MIVIOT
- **Normativa del Registro Público de Panamá** — inscripción de la propiedad y gravámenes [verificar]
- **ANATI** — administración de tierras y catastro
- **Código Fiscal (Ley 106 de 1974)** — ITBI (art. 701-g, Formulario 106), ganancia de capital (art. 701, DE 170 de 1993, Formulario 107), ITBMS no grava inmuebles (art. 1057-V)
- **Ley 23 de 2015** (arts. 22 y ss.) — prevención de blanqueo; promotores y agentes/corredores como sujetos obligados no financieros (Superintendencia de Sujetos No Financieros, UAF)
- **Normativa municipal de uso de suelo y construcción** — según provincia/distrito de actuación

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Promesa de compraventa / arras de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |
| Contrato de arrendamiento tipo | [PLACEHOLDER] | [PLACEHOLDER] | |
| Reglamento de copropiedad de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |
| Checklist de due diligence inmobiliaria | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan contratos, informes de due diligence y dictámenes]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo:**

- Si el Rol es Abogado/a: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LEGAL — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO IDÓNEO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO IDÓNEO ANTES DE ACTUAR`

---

*Re-ejecutar: `/inmobiliario:entrevista-inicial --redo`*
