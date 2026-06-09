<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin se almacena en una ruta independiente de versión que sobrevive a actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/mercantil/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración de esa ruta. No de este archivo.
2. Si ese archivo no existe o aún contiene marcadores [PLACEHOLDER], DETENERSE antes de hacer trabajo sustantivo. Decir: "Este plugin necesita configuración antes de generar resultados útiles. Ejecuta /mercantil:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica real." NO proceder con configuración por defecto o placeholder. Los únicos skills que funcionan sin configuración son /mercantil:entrevista-inicial y cualquier flag --verificar-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua de caché
   (~/.claude/plugins/cache/claude-para-abogados/mercantil/<versión>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis, vuestra postura de riesgo, personas clave) se encuentran en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md` — un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Contratos Mercantiles

*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta entonces, es
una plantilla. Si ves valores `[PLACEHOLDER]` abajo, ejecuta `/mercantil:entrevista-inicial`
para ser entrevistado.*

*Una vez poblado: edita este archivo directamente. Cada skill de este plugin lo lee
antes de hacer nada. Corrige algo aquí y queda corregido en todas partes.*

---

## Quiénes somos

[Nombre de la Empresa] es una [tipo de entidad: S.A. (sociedad anónima), S. de R.L., fundación de interés privado, etc.]. El equipo de contratos lo forman [N] personas. [Nombre del responsable jurídico] es el punto final de escalado. Procesamos aproximadamente [N] contratos al mes, mayoritariamente [compras / ventas / mixto]. Usamos [sistema CLM] para la gestión del ciclo de vida contractual.

*(Nombre de empresa, tipo de entidad, sector y tamaño proceden de perfil-empresa.md — editar allí para cambiar en todos los plugins. Tamaño del equipo, sistema CLM y contacto de escalado son específicos de este plugin.)*

**Lo que más duele:** [PLACEHOLDER — lo que el equipo dijo que les duele, en sus propias palabras]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Administración pública/clínica jurídica] *(De perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a idóneo/a | No jurista con acceso a abogado | No jurista sin acceso a abogado]
**Contacto abogado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado/a]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| CLM (DocuSign CLM, Ironclad, etc.) | [PLACEHOLDER ✓/✗] | Registro manual; el rastreador de renovaciones funciona con registro local |
| Firma electrónica (DocuSign, Adobe Sign, firma electrónica calificada Ley 51 de 2008) | [PLACEHOLDER ✓/✗] | El usuario gestiona la firma fuera del plugin |
| Almacenamiento documental (Drive / SharePoint / Box) | [PLACEHOLDER ✓/✗] | El usuario sube los contratos directamente para cada revisión |
| Slack / Teams | [PLACEHOLDER ✓/✗] | Alertas y resúmenes para interesados se entregan inline |

*Volver a verificar: `/mercantil:entrevista-inicial --verificar-integraciones`*

---

## Playbook

**Lado activo:** [PLACEHOLDER — ventas / compras / ambos — se configura en la entrevista inicial]

*Lado ventas = la empresa vende sus productos o servicios. Somos el proveedor. Normalmente nuestro papel. Lado compras = la empresa contrata a proveedores terceros. Somos el cliente. Normalmente su papel. La respuesta cambia cada posición del playbook — apetito de riesgo, cláusulas estándar y de repliegue, umbrales de aprobación, límites de responsabilidad, dirección de la indemnización, titularidad de PI, derechos de resolución.*

> Los skills que revisan o evalúan un contrato contra este playbook determinan primero en qué lado está la empresa. Si no es obvio, preguntar. Leer la sección del playbook correspondiente. Nunca aplicar una posición de ventas a un contrato de compras ni viceversa.

### Playbook de ventas

*Aplica cuando la empresa es el proveedor. Normalmente nuestro papel.*

*[No configurado — ejecuta `/mercantil:entrevista-inicial --lado ventas` para construirlo]*

#### Limitación de responsabilidad

**Cap directo (múltiplo de honorarios/precio):** [PLACEHOLDER — ej., "12 meses de importes facturados o por facturar en USD/B/."]

**Daños indirectos / consecuenciales:** [PLACEHOLDER — excluidos / limitados a [X] / ilimitados / espejo del directo]

**Carveouts aceptables (por encima del cap):** [PLACEHOLDER — ej., "Dolo y culpa grave, infracción de confidencialidad, indemnización por PI, brecha de datos personales"]

**Base del cap que aceptamos:** [PLACEHOLDER — ej., "importes facturados en los 12 meses anteriores a la reclamación"]

**Posiciones de repliegue aceptables:**
- [PLACEHOLDER]

**Nunca aceptar:**
- [PLACEHOLDER — ej., "Responsabilidad ilimitada por daños indirectos", "base del cap sobre últimos 3 meses"]

#### Indemnización

**Posición estándar:** [PLACEHOLDER — ej., "Indemnizamos por reclamaciones de PI del servicio; el cliente indemniza por sus datos y uso"]

**Posiciones de repliegue aceptables:**
- [PLACEHOLDER]

**Nunca aceptar:**
- [PLACEHOLDER]

#### Protección de datos

**Posición estándar:** [PLACEHOLDER — ej., "Nuestro contrato de encargado del tratamiento bajo la Ley 81 de 2019; el cliente firma como responsable del tratamiento"]

**Requisitos:**
- [PLACEHOLDER — ej., "Registro de actividades de tratamiento, medidas de seguridad conforme al Decreto Ejecutivo 285 de 2021, cláusulas para transferencias internacionales de datos"]

**Posiciones de repliegue aceptables:**
- [PLACEHOLDER]

#### Propiedad intelectual

**Posición estándar:** [PLACEHOLDER — ej., "La PI preexistente de cada parte permanece con su titular; licencia limitada de uso"]

**Obra derivada / desarrollos a medida:** [PLACEHOLDER — ej., "Los desarrollos a medida se licencian al cliente; la PI subyacente permanece nuestra"]

**Nunca aceptar:**
- [PLACEHOLDER — ej., "Cesión de toda la PI al cliente sin contraprestación adicional"]

#### Duración, renovación y resolución

**Posición estándar:** [PLACEHOLDER — ej., "Duración anual, renovación tácita por períodos iguales, preaviso de 30 días para no renovar"]

**Resolución anticipada:** [PLACEHOLDER — ej., "Por incumplimiento esencial con plazo de subsanación de 30 días; por insolvencia bajo la Ley 12 de 2016"]

**Posiciones de repliegue aceptables:**
- [PLACEHOLDER]

**Nunca aceptar:**
- [PLACEHOLDER — ej., "Resolución ad nutum del cliente durante período pagado"]

#### Ley aplicable y jurisdicción

**Preferida:** [PLACEHOLDER — ej., "Ley panameña, tribunales de la Ciudad de Panamá"]
**Aceptable:** [PLACEHOLDER — ej., "Ley panameña, arbitraje del CeCAP de la Cámara de Comercio [verificar]"]
**Escalar:** [PLACEHOLDER — ej., "Ley extranjera, arbitraje institucional internacional"]
**Nunca:** [PLACEHOLDER — ej., "Jurisdicción extranjera sin posibilidad de reconocimiento del laudo o sentencia en Panamá"]

#### Lo innegociable

[PLACEHOLDER — el deal-breaker cuando vendemos. Cada revisión de ventas lo comprueba primero.]

---

### Playbook de compras

*Aplica cuando la empresa es el cliente. Normalmente su papel.*

*[No configurado — ejecuta `/mercantil:entrevista-inicial --lado compras` para construirlo]*

#### Limitación de responsabilidad

**Cap directo (múltiplo de precio):** [PLACEHOLDER — ej., "Cap del proveedor a 12 meses de importes pagados; más alto para brecha de datos y PI"]

**Daños indirectos / consecuenciales:** [PLACEHOLDER]

**Carveouts que exigimos (por encima del cap):** [PLACEHOLDER]

**Posiciones de repliegue aceptables:**
- [PLACEHOLDER]

**Nunca aceptar:**
- [PLACEHOLDER]

#### Indemnización

**Posición estándar:** [PLACEHOLDER — ej., "El proveedor indemniza por infracción de PI y brecha de datos; nosotros indemnizamos por nuestros datos"]

**Posiciones de repliegue aceptables:**
- [PLACEHOLDER]

**Nunca aceptar:**
- [PLACEHOLDER]

#### Protección de datos

**Posición estándar:** [PLACEHOLDER — ej., "El proveedor firma nuestro contrato de encargado del tratamiento"]

**Requisitos:**
- [PLACEHOLDER — ej., "Certificación de seguridad reconocida (ISO 27001) si aplica, auditoría anual, notificación de brechas conforme a la Ley 81 de 2019"]

**Posiciones de repliegue aceptables:**
- [PLACEHOLDER]

#### Duración, renovación y resolución

**Posición estándar:** [PLACEHOLDER — ej., "Resolución por conveniencia con preaviso de 30 días; renovación tácita solo con ventana de cancelación de 30 días"]

**Posiciones de repliegue aceptables:**
- [PLACEHOLDER]

**Nunca aceptar:**
- [PLACEHOLDER — ej., "Compromiso plurianual sin derecho de resolución"]

#### Ley aplicable y jurisdicción

**Preferida:** [PLACEHOLDER]
**Aceptable:** [PLACEHOLDER]
**Escalar:** [PLACEHOLDER]
**Nunca:** [PLACEHOLDER]

#### Lo innegociable

[PLACEHOLDER — el deal-breaker cuando compramos. Cada revisión de compras lo comprueba primero.]

---

## Matriz de escalado

| Puede aprobar | Sin escalar | Escala a | Vía |
|---|---|---|---|
| [Paralegal/junior] | [PLACEHOLDER umbral] | [Abogado/a] | [Slack/email] |
| [Abogado/a] | [PLACEHOLDER umbral] | [Responsable jurídico] | [método] |
| [Responsable jurídico] | [PLACEHOLDER umbral] | [Negocio/CFO/Consejero Delegado] | [método] |

**Umbrales por importe:** [PLACEHOLDER — ej., "<50K USD paralegal; 50-200K USD abogado; >200K USD responsable jurídico"]

**Escalados automáticos independientemente del importe:**
- [PLACEHOLDER — ej., "Responsabilidad ilimitada, cesión de PI al proveedor, cualquier posición en lista de Nunca"]

---

## Estilo house

**Tono en redlines:** [PLACEHOLDER — ej., "Formal pero no excesivamente técnico; justificar cada cambio"]

**Resúmenes para interesados:** [PLACEHOLDER — quién los lee, extensión, idioma]

**Dónde va el producto de trabajo:** [PLACEHOLDER — CLM, carpeta Drive, canal Slack]

**Alertas de renovación van a:** [PLACEHOLDER — canal Slack o email]

**Formato de memos:** [PLACEHOLDER — ej., "Encabezado, antecedentes, análisis, conclusión, siguientes pasos"]

**Idioma de los contratos:** [PLACEHOLDER — ej., "Español; bilingüe español-inglés para contrapartes internacionales"]

**Citas normativas:** [PLACEHOLDER — ej., "Formato: art. 985 C. Civil, art. 219 C. de Comercio, Ley 45 de 2007"]

---

## NDAs — Clasificación rápida

| Nivel | Criterio | Acción |
|---|---|---|
| 🟢 Verde | [PLACEHOLDER — ej., "NDA mutuo estándar, duración ≤3 años, ley panameña, sin cláusula penal desproporcionada"] | Firmar sin revisión adicional |
| 🟡 Amarillo | [PLACEHOLDER — ej., "NDA unilateral, ley extranjera, non-solicit, cláusula penal"] | Revisar y proponer cambios |
| 🔴 Rojo | [PLACEHOLDER — ej., "Ley extranjera de difícil ejecución en Panamá, cesión de PI en NDA, indemnización ilimitada, duración perpetua"] | Escalar a responsable jurídico |

**Posiciones específicas para NDAs:**
- **Duración de confidencialidad:** [PLACEHOLDER — ej., "Máximo 3 años; 5 años para secretos empresariales protegidos bajo la legislación panameña de propiedad industrial (Ley 35 de 1996)"]
- **Definición de información confidencial:** [PLACEHOLDER — ej., "Exigir que sea razonablemente identificable como tal; rechazar definiciones catch-all"]
- **No competencia/no solicitud en NDA:** [PLACEHOLDER — ej., "Rechazar siempre en NDA; negociar solo en contrato principal"]

---

## Contratos SaaS — Cláusulas específicas

**SLA y disponibilidad:** [PLACEHOLDER — ej., "Uptime mínimo 99,5%; créditos de servicio por incumplimiento; SLA medido mensualmente"]

**Portabilidad de datos:** [PLACEHOLDER — ej., "Exportación en formato estándar (CSV/JSON) dentro de 30 días tras resolución; sin coste adicional"]

**Subencargados del tratamiento:** [PLACEHOLDER — ej., "Notificación previa 30 días; derecho de oposición; lista actualizada accesible"]

**Modificación unilateral de condiciones:** [PLACEHOLDER — ej., "Preaviso mínimo 30 días; derecho de resolución sin penalización si el cambio es material"]

**Propiedad de los datos:** [PLACEHOLDER — ej., "Los datos del cliente son del cliente en todo momento; el proveedor solo tiene licencia de uso para prestar el servicio"]

---

## Legislación de referencia

Las siguientes normas son la base del análisis de este plugin. Cada skill las aplica según corresponda:

- **Código de Comercio de Panamá** (Ley 2 de 1916) — contratos mercantiles, obligaciones del comerciante
- **Código Civil de Panamá** (Libro IV — obligaciones y contratos [verificar]) — teoría general de obligaciones y contratos (aplicación supletoria)
- **Ley 51 de 2008** — documentos y firmas electrónicas y comercio electrónico
- **Ley 45 de 2007** — protección al consumidor y defensa de la competencia (control de cláusulas abusivas, ACODECO)
- **Ley 81 de 2019** y **Decreto Ejecutivo 285 de 2021** — protección de datos personales, en lo relativo a cláusulas de tratamiento de datos en contratos (autoridad: ANTAI)
- **Ley 35 de 1996** — propiedad industrial; confidencialidad y secretos empresariales (DIGERPI)
- **Ley 64 de 2012** — derecho de autor y derechos conexos, en lo relativo a cláusulas de PI

---

## Postura ante juicios subjetivos

Cuando un skill de este plugin afronta un juicio jurídico subjetivo y la respuesta es incierta, el skill **prefiere el error recuperable**: marca la línea específica con `[revisión]` inline y anota la incertidumbre. No decidir silenciosamente que un umbral no se cumple; no emitir un párrafo de caveat genérico. La etiqueta `[revisión]` ES el mecanismo — un abogado estrecha la lista, la IA no. Infra-marcar es una puerta de un solo sentido; sobre-marcar es una puerta de dos sentidos que un abogado cierra en 30 segundos.

---

## Documentos semilla revisados

*Poblado por la entrevista inicial. Estos son los contratos de los que se aprendió el playbook.*

| Contrato | Contraparte | Fecha de firma | Cláusulas destacadas |
|---|---|---|---|
| [PLACEHOLDER] | | | |

---

*Para volver a ejecutar la entrevista: `/mercantil:entrevista-inicial --repetir`*
