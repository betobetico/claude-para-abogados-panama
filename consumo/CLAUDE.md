<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin se almacena en una ruta independiente de versión que sobrevive a actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/consumo/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración de esa ruta. No de este archivo.
2. Si ese archivo no existe o aún contiene marcadores [PLACEHOLDER], DETENERSE antes de hacer trabajo sustantivo. Decir: "Este plugin necesita configuración antes de generar resultados útiles. Ejecuta /consumo:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica real." NO proceder con configuración por defecto o placeholder. Los únicos skills que funcionan sin configuración son /consumo:entrevista-inicial y cualquier flag --verificar-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua de caché
   (~/.claude/plugins/cache/claude-para-abogados/consumo/<versión>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa se encuentran en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md` — un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho de Consumo

*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta entonces, es
una plantilla. Si ves valores `[PLACEHOLDER]` abajo, ejecuta `/consumo:entrevista-inicial`
para ser entrevistado.*

*Una vez poblado: edita este archivo directamente. Cada skill de este plugin lo lee
antes de hacer nada. Corrige algo aquí y queda corregido en todas partes.*

---

## Quiénes somos

[Nombre de la Empresa / Despacho] es [tipo de entidad]. El equipo encargado de derecho de consumo lo forman [N] personas. [Nombre del responsable] es el punto final de escalado. Gestionamos aproximadamente [N] reclamaciones/consultas de consumo al mes.

*(Datos de empresa proceden de perfil-empresa.md — editar allí para cambiar en todos los plugins.)*

**Lo que más duele:** [PLACEHOLDER — lo que el equipo dijo que les duele, en sus propias palabras]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Asociación de consumidores]

**Sector:** [PLACEHOLDER — ej., "E-commerce, retail, telecomunicaciones, banca, seguros, viajes, alimentación"]

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a idóneo/a | Responsable de atención al cliente con acceso a abogado | No jurista sin acceso a abogado]
**Contacto del abogado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado/a]

---

## Canales de venta

| Canal | Activo | Normativa específica | Notas |
|---|---|---|---|
| Online (web propia) | [PLACEHOLDER ✓/✗] | Ley 45 de 2007 + comercio electrónico (Ley 51 de 2008 [verificar]) | [PLACEHOLDER — ej., "Tienda Shopify / WooCommerce / desarrollo propio"] |
| Online (marketplace) | [PLACEHOLDER ✓/✗] | Ley 45 de 2007 + condiciones marketplace | [PLACEHOLDER — ej., "Amazon, MercadoLibre"] |
| Presencial (tienda física) | [PLACEHOLDER ✓/✗] | Ley 45 de 2007 | [PLACEHOLDER] |
| Teléfono | [PLACEHOLDER ✓/✗] | Ley 45 de 2007 (ventas a distancia) [verificar] | [PLACEHOLDER] |
| Mixto (click & collect) | [PLACEHOLDER ✓/✗] | Ley 45 de 2007 | [PLACEHOLDER] |

**Provincias con operaciones:** [PLACEHOLDER — ej., "Panamá, Colón, Chiriquí" — relevante por jurisdicción de las oficinas regionales de la ACODECO]

---

## Condiciones generales de contratación

### Control de inclusión (contratos de adhesión, Ley 45 de 2007) [verificar]

**Requisitos cumplidos:**
- [ ] Información previa sobre existencia de las condiciones generales
- [ ] Entrega o puesta a disposición antes de la contratación
- [ ] Redacción clara, concreta y sencilla (legibilidad del contrato de adhesión)
- [ ] Accesibilidad y legibilidad (tamaño de fuente, contraste)
- [ ] Aceptación expresa (no casillas premarcadas)
- [PLACEHOLDER — requisitos adicionales del sector]

**Estado de las CGC:** [PLACEHOLDER — ej., "Última revisión DD/MM/AAAA; redactadas por despacho X; revisión anual"]

### Control de contenido — Cláusulas abusivas (Ley 45 de 2007) [verificar]

**Cláusulas revisadas contra el régimen de cláusulas abusivas de la Ley 45 de 2007:** [verificar]
- [ ] Vinculación del contrato a la sola voluntad del proveedor
- [ ] Limitación o renuncia de derechos del consumidor
- [ ] Falta de reciprocidad entre las partes
- [ ] Garantías o penalizaciones desproporcionadas a cargo del consumidor
- [ ] Cláusulas que infringen el régimen de protección al consumidor (carácter abusivo según la Ley 45 de 2007) [verificar]
- [PLACEHOLDER — cláusulas específicas del sector bajo vigilancia]

**Posición house:** [PLACEHOLDER — ej., "Revisión semestral de CGC contra resoluciones recientes de la ACODECO y la jurisprudencia de la CSJ sobre cláusulas abusivas; consultar siempre con abogado antes de modificar"]

### Doble clic / Contratación electrónica

**Proceso de contratación online:** [PLACEHOLDER — ej., "1) Selección producto → 2) Resumen pedido → 3) Aceptación de condiciones (checkbox no premarcado) → 4) Confirmación pedido → 5) Correo de confirmación"]

**Información obligatoria al consumidor en contratos a distancia (Ley 45 de 2007):** [verificar]
- [ ] Características principales del bien/servicio
- [ ] Identidad, RUC y dirección del proveedor
- [ ] Precio total con impuestos incluidos (ITBMS)
- [ ] Gastos de envío
- [ ] Forma de pago, entrega y ejecución
- [ ] Derecho de retracto (o su exclusión motivada) [verificar]
- [ ] Garantía
- [ ] Duración del contrato y condiciones de resolución
- [ ] Funcionalidad e interoperabilidad (contenido digital)

---

## Derecho de retracto

**Plazo:** plazo legal de retracto en ventas a distancia conforme a la Ley 45 de 2007 [verificar]

**Plazo ampliado por falta de información:** plazo ampliado si no se informó del derecho de retracto, conforme a la Ley 45 de 2007 [verificar]

**Excepciones aplicables al negocio:** [verificar]
- [PLACEHOLDER — marcar las que apliquen:
  - [ ] Bienes precintados no aptos para devolución por higiene/salud
  - [ ] Bienes personalizados o confeccionados a medida
  - [ ] Contenido digital sin soporte material con ejecución comenzada con consentimiento
  - [ ] Servicios completamente ejecutados con consentimiento previo
  - [ ] Bienes que se mezclan de forma indisociable con otros
  - [ ] Prensa periódica
  - [ ] Alojamiento, transporte, comida en fecha determinada (viajes)
  - [ ] Suministro de bienes precintados que por su naturaleza no son aptos para ser devueltos]

**Formulario de retracto:** [PLACEHOLDER — ej., "Disponible en web + incluido en correo de confirmación de pedido"]

**Proceso de devolución del importe:** [PLACEHOLDER — ej., "Reembolso dentro del plazo legal desde la comunicación del retracto; mismo medio de pago; posibilidad de retener hasta recibir los bienes [verificar]"]

**Coste de devolución:** [PLACEHOLDER — ej., "A cargo del consumidor si se informó previamente; a cargo del proveedor si no se informó"]

---

## Garantías

### Garantía legal (Ley 45 de 2007) [verificar]

**Plazo:** plazo de garantía legal conforme a la Ley 45 de 2007 [verificar]

**Régimen de bienes defectuosos:** el proveedor responde por los defectos del bien o servicio conforme a la Ley 45 de 2007 [verificar]

**Remedios del consumidor:** [verificar]
1. Reparación o sustitución (primera opción del consumidor)
2. Reducción del precio
3. Resolución del contrato y devolución de lo pagado

**Posición house:** [PLACEHOLDER — ej., "Ofrecer siempre reparación/sustitución primero; aceptar resolución si no es posible o no se realiza en plazo razonable; documentar toda reclamación"]

### Garantía comercial

**¿Se ofrece garantía comercial adicional?** [PLACEHOLDER — Sí / No]
**Condiciones:** [PLACEHOLDER — ej., "Garantía adicional a la garantía legal; cubre XYZ; excluye ABC; documento de garantía conforme a la Ley 45 de 2007 [verificar]"]
**Obligaciones del documento de garantía:** [verificar]
- [ ] Indicar que no afecta a los derechos legales del consumidor
- [ ] Contenido, duración, ámbito territorial, vías de reclamación

---

## Claims de marketing — Control de legalidad

### Publicidad engañosa (Ley 45 de 2007) [verificar]

**Posición house:** [PLACEHOLDER — ej., "Toda afirmación sobre el producto debe ser verificable y documentada; claims de salud solo con respaldo científico; claims ambientales sin genéricos engañosos (greenwashing)"]

**Claims de alto riesgo que requieren revisión legal previa:**
- [PLACEHOLDER — ej., "Claims de salud/bienestar"]
- [PLACEHOLDER — ej., "Claims medioambientales/sostenibilidad (greenwashing)"]
- [PLACEHOLDER — ej., "Superlativos ('el mejor', 'el primero', 'el único')"]
- [PLACEHOLDER — ej., "Comparativas con competidores"]
- [PLACEHOLDER — ej., "Testimonios y opiniones de clientes"]

### Publicidad comparativa (Ley 45 de 2007) [verificar]

**Requisitos para que sea lícita:**
- Bienes/servicios con la misma finalidad
- Comparación objetiva y verificable
- No denigrante ni confusoria
- No aprovechamiento indebido de reputación ajena

**Posición house:** [PLACEHOLDER — ej., "Evitar publicidad comparativa directa salvo que el departamento jurídico apruebe; comparativa genérica permitida"]

### Influencers y publicidad en redes sociales

**Posición house:** [PLACEHOLDER — ej., "Identificación obligatoria como publicidad (#publi #ad); contrato escrito con cláusula de cumplimiento legal; aprobación previa del contenido; publicidad claramente identificable conforme a la Ley 45 de 2007"]

---

## Lanzamiento de producto — Checklist de riesgo

**Antes de lanzar un producto/servicio B2C, verificar:**

- [ ] Información completa al consumidor (Ley 45 de 2007 si venta a distancia) [verificar]
- [ ] CGC revisadas y actualizadas
- [ ] Política de devoluciones/retracto visible y correcta
- [ ] Etiquetado conforme a la normativa técnica panameña aplicable [verificar]
- [ ] Claims de marketing revisados por legal
- [ ] Política de privacidad y datos personales actualizada (Ley 81 de 2019)
- [ ] Precio final con impuestos visible (ITBMS incluido) (Ley 45 de 2007) [verificar]
- [ ] Desglose de gastos de envío
- [ ] Confirmación clara del pedido con obligación de pago [verificar]
- [ ] Canal de atención al cliente / reclamaciones disponible
- [ ] Libro de quejas o canal de reclamaciones disponible (si venta presencial) [verificar]
- [ ] Información de contacto y vía de reclamación ante la ACODECO
- [PLACEHOLDER — ítems adicionales específicos del sector]

**Aprobación necesaria:** [PLACEHOLDER — ej., "Checklist firmado por responsable jurídico y responsable de marketing"]

---

## Libro de quejas / Reclamaciones

**Obligatoriedad:** [PLACEHOLDER — ej., "Disponibilidad de un canal de reclamaciones en establecimiento físico [verificar]; no obligatorio online pero sí recomendable tener canal de reclamaciones"]

**Normativa aplicable:** [PLACEHOLDER — ej., "Ley 45 de 2007 y reglamentación de la ACODECO sobre atención de reclamos [verificar]"]

**Proceso interno de gestión:**
1. [PLACEHOLDER — ej., "Recepción de la queja o reclamo"]
2. [PLACEHOLDER — ej., "Registro en sistema interno (24h)"]
3. [PLACEHOLDER — ej., "Respuesta al consumidor en X días hábiles"]
4. [PLACEHOLDER — ej., "Coordinación con la ACODECO si procede"]
5. [PLACEHOLDER — ej., "Seguimiento hasta resolución"]

---

## Conciliación y arbitraje de consumo

**Participación en conciliación/arbitraje ante la ACODECO:** [PLACEHOLDER — Sí (total/limitada) / No]

**Instancia competente:** [PLACEHOLDER — ej., "Dirección de la ACODECO / juzgado competente en protección al consumidor [verificar]"]

**Limitaciones:** [PLACEHOLDER — ej., "Excluidas reclamaciones >B/.X; excluidos temas de intoxicación/lesiones; excluidos servicios financieros (Superintendencia de Bancos)"]

**Posición house:** [PLACEHOLDER — ej., "Participar activamente en la conciliación previa ante la ACODECO como señal de confianza; cumplir acuerdos y resoluciones dentro del plazo"]

---

## Acciones de clase / intereses colectivos

**Protección de intereses colectivos de consumidores (Ley 45 de 2007):** [verificar]
- Legitimación para accionar: la ACODECO y las asociaciones de consumidores [verificar]
- Acción de cesación + acción de reparación / indemnización

**Posición house ante acciones de clase:**
- [PLACEHOLDER — ej., "Escalar inmediatamente a socio/a responsable y despacho externo; revisar seguro de RC; preparar defensa proactiva"]

**Monitorización de riesgo:**
- [PLACEHOLDER — ej., "Vigilar reclamaciones recurrentes (>X reclamaciones sobre el mismo tema en Y meses = alerta)"]
- [PLACEHOLDER — ej., "Monitorizar redes sociales y plataformas de opinión"]

---

## Matriz de escalado

| Puede resolver | Sin escalar | Escala a | Vía |
|---|---|---|---|
| [Atención al cliente] | [PLACEHOLDER — ej., "Reclamaciones rutinarias, devoluciones estándar, información"] | [Responsable jurídico/consumo] | [método] |
| [Responsable jurídico/consumo] | [PLACEHOLDER — ej., "Reclamaciones complejas, hojas de reclamaciones, consultas de CGC"] | [Socio/a / dirección] | [método] |
| [Socio/a / dirección] | [PLACEHOLDER — ej., "Todo excepto acciones colectivas y sanciones administrativas"] | [Despacho externo / comité de dirección] | [método] |

**Escalados automáticos:**
- [PLACEHOLDER — ej., "Toda acción de clase, toda sanción de la ACODECO, toda inspección, reclamaciones de asociaciones de consumidores, retirada de producto"]

---

## Estilo house

**Formato de respuesta a reclamaciones:** [PLACEHOLDER — ej., "Modelo house: acuse de recibo (24h) → investigación interna → respuesta motivada (máx. 10 días hábiles)"]
**Tono en comunicaciones con consumidores:** [PLACEHOLDER — ej., "Empático, claro, sin tecnicismos; ofrecer solución concreta"]
**Citas normativas:** [PLACEHOLDER — ej., "Ley 45 de 2007, reglamentación de la ACODECO, Código de Comercio de Panamá"]
**Idioma:** [PLACEHOLDER — ej., "Español"]

---

## Legislación de referencia

Las siguientes normas son la base del análisis de este plugin:

- **Ley 45 de 2007** — sobre normas de protección al consumidor y defensa de la competencia (norma central del módulo)
- **ACODECO** — Autoridad de Protección al Consumidor y Defensa de la Competencia (autoridad de aplicación)
- **Código de Comercio de Panamá** — obligaciones de los comerciantes y régimen mercantil
- **Ley 81 de 2019** — protección de datos personales (y Decreto Ejecutivo 285 de 2021) — para políticas de privacidad
- **Reglamentación sectorial de la ACODECO** [verificar] — etiquetado, garantías, publicidad y contratos de adhesión
- **Referencia comparada internacional** (no vinculante en Panamá): directivas y prácticas de la UE/OCDE sobre protección al consumidor, citadas solo a título orientativo

---

## Postura ante juicios subjetivos

Cuando un skill de este plugin afronta un juicio subjetivo y la respuesta es incierta, el skill **prefiere el error recuperable**: marca la línea con `[revisión]` inline. Infra-marcar es una puerta de un solo sentido; sobre-marcar es una puerta de dos sentidos que un abogado cierra en 30 segundos.

---

*Para volver a ejecutar la entrevista: `/consumo:entrevista-inicial --repetir`*
