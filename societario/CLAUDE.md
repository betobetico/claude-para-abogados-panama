<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin se almacena en una ruta independiente de versión que sobrevive a actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/societario/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración de esa ruta. No de este archivo.
2. Si ese archivo no existe o aún contiene marcadores [PLACEHOLDER], DETENERSE antes de hacer trabajo sustantivo. Decir: "Este plugin necesita configuración antes de generar resultados útiles. Ejecuta /societario:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica real." NO proceder con configuración por defecto o placeholder. Los únicos skills que funcionan sin configuración son /societario:entrevista-inicial y cualquier flag --verificar-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua de caché
   (~/.claude/plugins/cache/claude-para-abogados/societario/<versión>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis, vuestra postura de riesgo, personas clave) se encuentran en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md` — un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Societario

*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta entonces, es
una plantilla. Si ves valores `[PLACEHOLDER]` abajo, ejecuta `/societario:entrevista-inicial`
para ser entrevistado.*

*Una vez poblado: edita este archivo directamente. Cada skill de este plugin lo lee
antes de hacer nada. Corrige algo aquí y queda corregido en todas partes.*

---

## Quiénes somos

[Nombre de la Empresa / Firma] es [tipo de entidad / firma de abogados]. El equipo de derecho societario lo forman [N] personas. [Nombre del socio/a responsable] es el punto final de escalado. Gestionamos aproximadamente [N] operaciones/consultas societarias al mes. Usamos [herramienta de gestión de entidades] para el seguimiento de obligaciones registrales.

*(Nombre de empresa, tipo de entidad, sector y tamaño proceden de perfil-empresa.md — editar allí para cambiar en todos los plugins.)*

**Lo que más duele:** [PLACEHOLDER — lo que el equipo dijo que les duele, en sus propias palabras]

**Entorno de práctica:** [PLACEHOLDER — Firma individual/pequeña | Firma mediana/grande | Asesoría jurídica interna | Administración pública/clínica jurídica]

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a idóneo/a | No jurista con acceso a abogado | No jurista sin acceso a abogado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / firma externa / N/A si es abogado/a]

---

## Áreas de práctica activas

| Área | Estado | Responsable |
|---|---|---|
| M&A (fusiones y adquisiciones) | [PLACEHOLDER ✓/✗] | [PLACEHOLDER] |
| Secretaría de la Junta Directiva / Accionistas | [PLACEHOLDER ✓/✗] | [PLACEHOLDER] |
| Cumplimiento registral | [PLACEHOLDER ✓/✗] | [PLACEHOLDER] |
| Gestión de entidades (grupo) | [PLACEHOLDER ✓/✗] | [PLACEHOLDER] |
| Fundaciones de interés privado | [PLACEHOLDER ✓/✗] | [PLACEHOLDER] |
| Reestructuraciones societarias | [PLACEHOLDER ✓/✗] | [PLACEHOLDER] |
| Capital de riesgo / financiación | [PLACEHOLDER ✓/✗] | [PLACEHOLDER] |

---

## Due diligence — Checklist por categoría

*Checklist estándar para operaciones de M&A. Adaptar según tipo y tamaño de la operación.*

### Societario

- [ ] Pacto social y reformas vigentes (escritura pública)
- [ ] Certificaciones actualizadas del Registro Público
- [ ] Registro de acciones / cuotas de participación
- [ ] Actas de juntas de accionistas (últimos [N] años)
- [ ] Actas de junta directiva (últimos [N] años)
- [ ] Poderes vigentes y revocados
- [ ] Pactos de accionistas (shareholders' agreements)
- [ ] Estructura del grupo (organigrama societario)
- [ ] Participaciones en otras sociedades
- [ ] [PLACEHOLDER — ítems adicionales específicos de la firma/empresa]

### Contratos

- [ ] Contratos materiales vigentes (>USD/B/. [PLACEHOLDER] de valor)
- [ ] Cláusulas de cambio de control
- [ ] Contratos con partes relacionadas
- [ ] Contratos de financiación y garantías
- [ ] [PLACEHOLDER]

### Laboral

- [ ] Convención colectiva aplicable
- [ ] Planilla y categorías ocupacionales
- [ ] Contratos de alta dirección / personal de confianza
- [ ] Litigios laborales pendientes (Ministerio de Trabajo / MITRADEL)
- [ ] Cumplimiento de cuotas a la CSS (Caja de Seguro Social)
- [ ] [PLACEHOLDER]

### Fiscal

- [ ] Declaraciones de renta de los últimos [N] períodos (ISR, ITBMS)
- [ ] Requerimientos y fiscalizaciones de la DGI
- [ ] Pérdidas fiscales acumuladas pendientes de aplicar
- [ ] Operaciones con partes relacionadas (documentación de precios de transferencia)
- [ ] Paz y salvo de la DGI
- [ ] [PLACEHOLDER]

### Regulatorio

- [ ] Licencias y autorizaciones administrativas
- [ ] Cumplimiento sectorial específico
- [ ] [PLACEHOLDER]

### Litigios

- [ ] Procedimientos judiciales activos
- [ ] Procedimientos arbitrales
- [ ] Reclamaciones administrativas
- [ ] Contingencias no provisionadas
- [ ] [PLACEHOLDER]

### Propiedad intelectual e industrial

- [ ] Marcas registradas y solicitudes pendientes (DIGERPI)
- [ ] Patentes y modelos de utilidad (Ley 35 de 1996)
- [ ] Nombres de dominio
- [ ] Contratos de licencia de PI (derecho de autor — Ley 64 de 2012)
- [ ] [PLACEHOLDER]

### Inmobiliario

- [ ] Inmuebles en propiedad (certificaciones del Registro Público actualizadas)
- [ ] Contratos de arrendamiento
- [ ] Permisos de construcción y de operación
- [ ] [PLACEHOLDER]

---

## Gobierno corporativo

### Tipos de acuerdos

**Junta de Accionistas:**
- [PLACEHOLDER — ej., "Ordinaria anual (aprobación de estados financieros, aplicación de utilidades), Extraordinaria (reforma del pacto social, aumento/reducción de capital, transformación, fusión, escisión)"]

**Junta Directiva / Órgano de administración:**
- [PLACEHOLDER — ej., "Junta directiva (presidente, secretario, tesorero) — frecuencia de reuniones, quórum, sistema de voto"]

### Libro de actas

**Formato:** [PLACEHOLDER — ej., "Libro de actas físico / formato electrónico con firma digital"]
**Responsable de custodia:** [PLACEHOLDER — ej., "agente residente / secretario"]
**Mantenimiento:** [PLACEHOLDER — ej., "Libro de actas y registro de acciones conforme al Código de Comercio de Panamá"]

### Certificaciones

**Modelo house de certificación del secretario:** [PLACEHOLDER — ej., "Certificación del acta con transcripción literal del acuerdo, datos de asistencia, quórum"]
**Certificaciones del Registro Público habituales:** [PLACEHOLDER — ej., "Certificación de existencia y vigencia, certificación de dignatarios y directores"]

---

## Cumplimiento registral — Plazos y obligaciones

| Obligación | Plazo legal | Alerta interna | Referencia |
|---|---|---|---|
| Tasa única anual | Anual [verificar] | [PLACEHOLDER] | Registro Público [verificar] |
| Declaración jurada de renta (ISR) | Hasta 31 de marzo siguiente al cierre [verificar] | [PLACEHOLDER] | Código Fiscal |
| Mantenimiento del agente residente | Continuo | [PLACEHOLDER] | Ley 32 de 1927 |
| Libros sociales (actas y registro de acciones) | Permanente | [PLACEHOLDER] | Código de Comercio |
| Inscripción de nombramientos/remociones | Tras protocolización en escritura pública [verificar] | [PLACEHOLDER] | Registro Público [verificar] |
| Declaración de beneficiario final | Según normativa de transparencia vigente | [PLACEHOLDER] | Normativa de transparencia [verificar] |
| [PLACEHOLDER — otras obligaciones periódicas] | | | |

**Consecuencias del incumplimiento:**
- Suspensión de derechos corporativos y eventual disolución por falta de pago de la tasa única anual [verificar]
- Multas y recargos por presentación tardía de declaraciones ante la DGI [verificar]
- Responsabilidad de directores y dignatarios por incumplimiento de sus deberes [verificar]

---

## Tipos societarios — Referencia rápida

| Tipo | Capital mínimo | Norma principal | Notas |
|---|---|---|---|
| S.A. (Sociedad Anónima) | Sin mínimo legal fijo [verificar] | Ley 32 de 1927 | Tipo más común; acciones nominativas o al portador (con restricciones) [verificar] |
| S. de R.L. (Sociedad de Responsabilidad Limitada) | Según pacto social [verificar] | Ley 4 de 2009 | Cuotas de participación; régimen flexible |
| Fundación de interés privado | USD 10.000 de patrimonio inicial [verificar] | Ley 25 de 1995 | Fines no lucrativos; sin accionistas; usada en planificación patrimonial |
| Sociedad Civil | Sin mínimo | Código Civil de Panamá [verificar] | Para ejercicio de profesiones |
| Sociedad en Comandita | Según tipo | Código de Comercio de Panamá [verificar] | Socios gestores y comanditarios |
| Empresa Individual | Según patrimonio afectado [verificar] | Ley específica [verificar] | Limitación de responsabilidad del comerciante individual |

**Tipo societario del cliente / entidades del grupo:**
- [PLACEHOLDER — listar cada entidad con su tipo, RUC, folio del Registro Público]

---

## Operaciones M&A — Posiciones estándar

**Tipo de operaciones habituales:** [PLACEHOLDER — ej., "Compraventas de acciones, fusiones por absorción, escisiones"]

**Posición en representaciones y garantías (R&W):**
- [PLACEHOLDER — ej., "Exigir catálogo completo; limitar temporalmente a 2 años (3 para fiscal y laboral); cap al precio de compra"]

**Cláusula de ajuste de precio:** [PLACEHOLDER — ej., "Locked box vs. completion accounts — preferencia"]

**Cláusula de no competencia:** [PLACEHOLDER — ej., "Duración máxima 2 años; ámbito geográfico acotado a Panamá/Centroamérica"]

**Indemnización:** [PLACEHOLDER — ej., "Basket/de minimis, cap global, supervivencia de reclamaciones"]

**Condiciones precedentes habituales:** [PLACEHOLDER — ej., "Due diligence satisfactoria, autorizaciones regulatorias, renuncia a derechos de adquisición preferente"]

---

## Pactos de accionistas — Cláusulas clave

- **Derecho de acompañamiento (tag-along):** [PLACEHOLDER]
- **Derecho de arrastre (drag-along):** [PLACEHOLDER]
- **Derecho de adquisición preferente:** [PLACEHOLDER]
- **Cláusulas antidilución:** [PLACEHOLDER]
- **Governance / composición del órgano de administración:** [PLACEHOLDER]
- **Materias reservadas:** [PLACEHOLDER — ej., "Operaciones >USD/B/. X, endeudamiento >USD/B/. Y, contratación de directivos clave"]
- **Deadlock y mecanismos de resolución:** [PLACEHOLDER — ej., "Mediación → arbitraje; put/call de última oferta"]

---

## Matriz de escalado

| Puede resolver | Sin escalar | Escala a | Vía |
|---|---|---|---|
| [Junior/paralegal] | [PLACEHOLDER — ej., "Certificaciones rutinarias, mantenimiento de libros"] | [Abogado/a senior] | [método] |
| [Abogado/a senior] | [PLACEHOLDER — ej., "Operaciones <USD/B/. 500K, juntas ordinarias"] | [Socio/a responsable] | [método] |
| [Socio/a responsable] | [PLACEHOLDER — ej., "Operaciones <USD/B/. 5M"] | [Comité de dirección / cliente] | [método] |

**Escalados automáticos:**
- [PLACEHOLDER — ej., "Cualquier operación de M&A, reformas estructurales, operaciones con partes relacionadas"]

---

## Estilo house

**Formato de escrituras y actas:** [PLACEHOLDER — ej., "Seguir modelo de la firma; siempre incluir datos de inscripción en el Registro Público"]
**Formato de informes de due diligence:** [PLACEHOLDER — ej., "Resumen ejecutivo + hallazgos por categoría con semáforo + anexos documentales"]
**Citas normativas:** [PLACEHOLDER — ej., "Ley 32 de 1927, Ley 25 de 1995, Código de Comercio de Panamá"]
**Idioma:** [PLACEHOLDER — ej., "Español; documentos bilingües para operaciones internacionales"]

---

## Legislación de referencia

Las siguientes normas son la base del análisis de este plugin:

- **Ley 32 de 1927** — sobre sociedades anónimas
- **Ley 25 de 1995** — sobre fundaciones de interés privado
- **Ley 4 de 2009** — sobre sociedades de responsabilidad limitada
- **Código de Comercio de Panamá** — comerciantes, libros y obligaciones mercantiles
- **Código Civil de Panamá** — en lo relativo a obligaciones, contratos y personalidad jurídica
- **Código Fiscal de Panamá** [verificar] — Impuesto sobre la Renta (ISR) e ITBMS, bajo principio de territorialidad
- **Ley 23 de 2015** — prevención de blanqueo de capitales (sujetos obligados, UAF) y régimen de beneficiario final
- **Ley 45 de 2007** — protección al consumidor y defensa de la competencia (ACODECO) — control de concentraciones [verificar]
- **Ley 81 de 2019** — protección de datos personales (ANTAI)

---

## Postura ante juicios subjetivos

Cuando un skill de este plugin afronta un juicio jurídico subjetivo y la respuesta es incierta, el skill **prefiere el error recuperable**: marca la línea específica con `[revisión]` inline. Infra-marcar es una puerta de un solo sentido; sobre-marcar es una puerta de dos sentidos que un abogado idóneo cierra en 30 segundos.

---

*Para volver a ejecutar la entrevista: `/societario:entrevista-inicial --repetir`*
