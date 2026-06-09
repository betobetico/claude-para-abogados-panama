<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /administrativo:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /administrativo:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/administrativo/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Derecho Administrativo
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/administrativo:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de derecho administrativo se quedan aquí.*

[Empresa] es una [tipo de entidad]. Interactuamos principalmente con [PLACEHOLDER — Gobierno Central / entidades autónomas y semiautónomas / municipios].
El equipo de derecho administrativo cuenta con [N] personas. Áreas principales de actuación:
[PLACEHOLDER — contratación pública / urbanismo y construcción / regulatorio / subsidios / responsabilidad patrimonial del Estado / etc.].
[Responsable del área: nombre o ninguno]. La escalación va a [nombre].

**Administraciones con las que interactuamos habitualmente:** [PLACEHOLDER] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Asuntos administrativos abiertos:** [PLACEHOLDER — procedimientos en curso, recursos, licitaciones]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Administración pública] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a | Profesional jurídico no abogado con acceso a letrado | Profesional no jurídico sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente |
| Plataforma de contratación del sector público | [PLACEHOLDER ✓/✗] | Consulta manual |
| Sede electrónica de administraciones | [PLACEHOLDER ✓/✗] | Gestión presencial o por representante |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Alertas de plazos solo bajo demanda |

*Re-comprobar: `/administrativo:entrevista-inicial --check-integraciones`*

---

## Administraciones con las que interactuamos

| Nivel | Administración | Materias habituales | Contacto |
|---|---|---|---|
| Gobierno Central | [PLACEHOLDER — ministerios concretos] | [PLACEHOLDER] | [PLACEHOLDER] |
| Entidades autónomas y semiautónomas | [PLACEHOLDER — ASEP, ACP, ATTT, MINSA, etc.] | [PLACEHOLDER] | [PLACEHOLDER] |
| Municipios | [PLACEHOLDER — alcaldías, concejos municipales] | [PLACEHOLDER] | [PLACEHOLDER] |
| Empresas estatales / Entidades de derecho público | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Procedimiento administrativo general (Ley 38 de 2000)

### Fases del procedimiento

| Fase | Plazo legal | Consideraciones clave |
|---|---|---|
| Iniciación (de oficio o a petición de parte) | — | Derecho de petición (art. 41 de la Constitución; desarrollo en arts. 42-43 Ley 38 de 2000); deber de impulsar de oficio el procedimiento [verificar] |
| Instrucción | — | Práctica de pruebas, alegaciones del interesado y vista del expediente conforme a la Ley 38 de 2000 |
| Resolución | Plazo específico según procedimiento; en su defecto, plazo general de la Ley 38 de 2000 | Deber de decidir y notificar (principio de obligatoriedad) (arts. 34, 42 y 156 Ley 38 de 2000; art. 41 Constitución) |
| Silencio administrativo | Agotado el plazo sin resolución expresa; plazo general de 2 meses | Regla general en Panamá: silencio administrativo NEGATIVO (se entiende denegada la petición), salvo norma especial que lo disponga expresamente (arts. 156-157 Ley 38 de 2000) |

### Plazos clave

| Concepto | Plazo | Base legal |
|---|---|---|
| Resolución del derecho de petición | 30 días | Constitución (art. 41); desarrollo en arts. 42-43 Ley 38 de 2000 |
| Notificación personal del acto | Conforme a las reglas de notificación de la Ley 38 de 2000 | Ley 38 de 2000 |
| Corrección/subsanación de la petición | Plazo señalado por la entidad [verificar] | Ley 38 de 2000 |
| Período de consulta o información pública | Según norma sectorial aplicable [verificar] | Norma sectorial |

---

## Recursos administrativos (vía gubernativa — Ley 38 de 2000)

| Recurso | Contra qué actos | Plazo | Órgano | Base legal |
|---|---|---|---|---|
| Reconsideración | Actos del funcionario de primera o única instancia que los dictó | 5 días hábiles desde la notificación | Mismo funcionario que dictó el acto | Arts. 166.1 y 168 Ley 38 de 2000 |
| Apelación | Actos recurribles ante el inmediato superior | 5 días hábiles desde la notificación | Superior jerárquico (se propone ante la autoridad de primera instancia, art. 172) | Arts. 166.2 y 171 Ley 38 de 2000 |
| Hecho omisivo / silencio | Cuando la entidad no resuelve en plazo | Según régimen del silencio administrativo negativo (plazo de 2 meses) | — | Arts. 156-157 Ley 38 de 2000 |

> Con la resolución del recurso de apelación (o cuando contra el acto no quepa apelación) se entiende **agotada la vía gubernativa**, requisito para acudir a la Sala Tercera de lo Contencioso-Administrativo de la CSJ (art. 200 Ley 38 de 2000).

**Política interna sobre recursos:** [PLACEHOLDER — cuándo recurrimos, criterio de coste-beneficio]

---

## Contratación pública (Ley 22 de 2006 y sus reformas)

### Tipos de contrato habituales

| Tipo | Frecuencia | Valor medio | Notas |
|---|---|---|---|
| Obras | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Servicios | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Suministros | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Concesiones de servicios | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Contratación menor | [PLACEHOLDER] | [PLACEHOLDER] | Límite de cuantía según la Ley 22 de 2006 y reglamentación de la DGCP [verificar] |

### Procedimientos de selección de contratista

| Procedimiento | Cuándo se usa | Plazos clave |
|---|---|---|
| Licitación pública | Regla general por encima de los umbrales [verificar] | Según pliego de cargos [verificar] |
| Licitación por mejor valor (y con evaluación separada) | Cuando se ponderan factores además del precio (Texto Único de la Ley 22 de 2006) | Según pliego de cargos [verificar] |
| Licitación abreviada | Supuestos previstos en el Texto Único de la Ley 22 de 2006 | Según pliego de cargos [verificar] |
| Contratación menor | Por debajo del umbral legal [verificar] | Según pliego/cotización [verificar] |
| Subasta en reversa | Bienes y servicios estandarizados (Texto Único de la Ley 22 de 2006) | Según pliego de cargos [verificar] |
| Subasta de bienes públicos | Venta de bienes del Estado (Texto Único de la Ley 22 de 2006) | Variable |
| Licitación para convenio marco / Catálogo electrónico | Compras a través de PanamaCompra (Texto Único de la Ley 22 de 2006) | Variable |
| Procedimiento excepcional / contratación directa | Figura aparte, sin concurrencia; supuestos tasados (urgencia, único proveedor, etc.) [verificar] | Según resolución motivada |

### Pliego de cargos — Estilo house

**Revisión estándar del pliego de cargos incluye:** [PLACEHOLDER — checklist de revisión del pliego de cargos]
**Cláusulas críticas:** [PLACEHOLDER — multas, modificación, resolución administrativa, ajuste de precios]

### Recursos en materia de contratación pública

| Campo | Detalle |
|---|---|
| Órgano | Tribunal Administrativo de Contrataciones Públicas (TACP), que resuelve el recurso de impugnación (art. 125 del Texto Único de la Ley 22 de 2006) |
| Plazo | 5 días hábiles desde la notificación del acto; requiere fianza de impugnación del 10% (bienes/servicios) o 15% (obras) (art. 125 del Texto Único de la Ley 22 de 2006) |
| Actos recurribles | Adjudicación, declaratoria de deserción, rechazo de propuestas y actos que afecten la selección objetiva (art. 125 del Texto Único de la Ley 22 de 2006) |
| Efecto | Según lo previsto en el Texto Único de la Ley 22 de 2006 |
| Vía posterior | Demanda contencioso-administrativa ante la Sala Tercera de la CSJ |

---

## Responsabilidad patrimonial del Estado

| Campo | Detalle | Base legal |
|---|---|---|
| Plazo de reclamación | Plazo de prescripción aplicable a la acción de indemnización [verificar] | Código Judicial / Código Civil |
| Requisitos | Daño efectivo, evaluable, individualizable y antijurídico; nexo causal con la actuación administrativa | Doctrina de la Sala Tercera de la CSJ [verificar] |
| Procedimiento | Demanda de plena jurisdicción ante la Sala Tercera de lo Contencioso-Administrativo de la CSJ | Código Judicial |
| Dictamen previo | Concepto de la Procuraduría de la Administración en el proceso contencioso | Art. 5 Ley 38 de 2000 |

**Asuntos de responsabilidad patrimonial abiertos:** [PLACEHOLDER]

---

## Subsidios y ayudas públicas

| Campo | Detalle |
|---|---|
| Subsidios habituales | [PLACEHOLDER — programas a los que se solicita habitualmente] |
| Obligaciones como beneficiario | Justificación del gasto, cumplimiento de fines, rendición de cuentas |
| Plazo de justificación | Según las bases reguladoras del programa [verificar] |
| Procedimiento de reintegro / glosa | Según norma del programa y fiscalización de la Contraloría General de la República [verificar] |

---

## Contencioso-administrativo (Código Judicial — Sala Tercera de la CSJ)

| Campo | Detalle |
|---|---|
| Plazo para interponer la demanda | Plena jurisdicción: 2 meses desde la publicación, notificación o ejecución del acto (art. 42-B Ley 135 de 1943). Nulidad: en cualquier tiempo, no sujeta a caducidad (art. 42-A Ley 135 de 1943) |
| Tipos de demanda | Plena jurisdicción (restablecimiento de derecho subjetivo lesionado; arts. 42-B y 43-A Ley 135 de 1943) y nulidad (control objetivo de legalidad; art. 43-B Ley 135 de 1943) |
| Legitimación | Plena jurisdicción: titular de derecho subjetivo lesionado (art. 43-A Ley 135 de 1943). Nulidad: cualquier persona (acción pública de legalidad; art. 43-B Ley 135 de 1943) |
| Medidas cautelares | Suspensión provisional de los efectos del acto acusado para evitar un perjuicio notoriamente grave (art. 73 Ley 135 de 1943; el art. 74 enumera los casos en que no procede) |
| Órgano | Sala Tercera de lo Contencioso-Administrativo de la Corte Suprema de Justicia (instancia única; art. 97 Código Judicial) |
| Intervención obligatoria | La Procuraduría de la Administración emite concepto en el proceso (art. 5 Ley 38 de 2000) |

**Criterio de litigación:** [PLACEHOLDER — cuándo se recomienda acudir a la Sala Tercera, análisis coste-beneficio]

---

## Expropiación

| Campo | Detalle | Base legal |
|---|---|---|
| Procedimiento general | Declaratoria de utilidad pública → avalúo/indemnización → pago o consignación → ocupación | Constitución (art. 48 [verificar]) y legislación de expropiación panameña [verificar] |
| Avalúo | Fijación del valor de la indemnización; intervención de ANATI / avaluadores oficiales [verificar] | Legislación de expropiación [verificar] |
| Impugnación | Demanda contencioso-administrativa ante la Sala Tercera de la CSJ | Código Judicial |
| Urgencia / extrema urgencia | Ocupación anticipada por causa de utilidad pública o interés social [verificar] | Legislación de expropiación [verificar] |

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Petición / instancia administrativa rutinaria | Equipo administrativo | — | — |
| Recurso de reconsideración o apelación | Equipo administrativo | Socio/Director | Si cuantía > [PLACEHOLDER] |
| Recurso ante el Tribunal Administrativo de Contrataciones Públicas (TACP) | — | Socio/Director + Dirección | Siempre |
| Contencioso-administrativo (Sala Tercera CSJ) | — | Socio/Director + Dirección | Siempre |
| Procedimiento sancionador | — | Dirección jurídica + Dirección General | Siempre |
| Expropiación | — | Dirección jurídica + Dirección | Siempre |

---

## Referencias legislativas principales

- **Ley 38 de 2000** — Estatuto Orgánico de la Procuraduría de la Administración y Procedimiento Administrativo General
- **Código Judicial de Panamá** — jurisdicción contencioso-administrativa y atribuciones de la Sala Tercera de la CSJ
- **Ley 22 de 2006** — Contratación pública (y sus reformas, incluida la Ley 153 de 2020)
- **Constitución Política de la República de Panamá** — control de legalidad de los actos administrativos
- **Ley de expropiación panameña** [verificar] — régimen de la expropiación por causa de utilidad pública
- **Ley 106 de 1973** [verificar] — régimen municipal

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Modelo de recurso administrativo (reconsideración/apelación) | [PLACEHOLDER] | [PLACEHOLDER] | |
| Checklist de revisión del pliego de cargos | [PLACEHOLDER] | [PLACEHOLDER] | |
| Demanda contencioso-administrativa de referencia (Sala Tercera) | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan recursos, demandas, análisis de pliegos y dictámenes]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo:**

- Si el Rol es Abogado/a: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LETRADO — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO IDÓNEO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO IDÓNEO ANTES DE ACTUAR`

---

*Re-ejecutar: `/administrativo:entrevista-inicial --redo`*
