---
name: contencioso
description: >
  Contencioso-administrativo — guía a través de la demanda contencioso-
  administrativa ante la Sala Tercera de la CSJ contra actos de la
  Administración. Demandas de plena jurisdicción y de nulidad, plazos,
  legitimación, suspensión provisional. Usar cuando el usuario diga "demanda
  contenciosa", "Sala Tercera", "impugnar ante la Corte", "la Administración
  no cumple", "me han denegado" o tras agotar la vía gubernativa.
argument-hint: "[describir el acto administrativo a impugnar o pegar la resolución]"
---

# /contencioso

1. Cargar `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md` → sector, tipo de administración, letrados.
2. Identificar el acto impugnado y la vía administrativa agotada.
3. Analizar legitimación, plazos, órgano competente y viabilidad.
4. Generar informe con estrategia procesal.

```
/administrativo:contencioso
La DGI confirmó en apelación la liquidación de impuesto de inmueble.
Queremos demandar ante la Sala Tercera.
```

---

## Propósito

La demanda contencioso-administrativa ante la Sala Tercera de lo Contencioso-Administrativo de la Corte Suprema de Justicia es la vía judicial de control de la actividad administrativa en Panamá. Es el paso siguiente cuando la vía gubernativa se ha agotado o cuando el acto pone fin directamente a dicha vía. La Sala Tercera conoce en instancia única. Este skill guía la evaluación de viabilidad, plazos y estrategia de la demanda.

---

## Presupuestos de la demanda

### 1. Actividad administrativa impugnable

| Tipo | Ejemplo |
|---|---|
| Actos administrativos (expresos o presuntos por silencio) | Resoluciones, liquidaciones, sanciones |
| Reglamentos y demás disposiciones de carácter general | Decretos ejecutivos, resueltos, acuerdos municipales [verificar] |
| Omisión o no ejecución de actos administrativos | Inactividad de la Administración [verificar] |
| Actuación de la Administración sin sustento jurídico | Actuación material irregular [verificar] |

### 2. Agotamiento de la vía gubernativa

La demanda solo procede una vez agotada la vía gubernativa (salvo excepciones legales) [verificar]:

- Cuando se ha resuelto el recurso de apelación
- Cuando contra el acto no procede apelación por carecer de superior jerárquico la autoridad que lo dictó
- Cuando opera el silencio administrativo negativo respecto del recurso interpuesto

### 3. Tipos de demanda y legitimación

| Tipo de demanda | Objeto | Legitimación |
|---|---|---|
| **Plena jurisdicción** | Restablecer un derecho subjetivo lesionado por el acto y, en su caso, indemnización | Quien sea titular del derecho subjetivo lesionado [verificar] |
| **Nulidad** | Control objetivo de legalidad del acto o disposición (interés general) | Cualquier persona — acción pública de legalidad [verificar] |
| **Protección de derechos humanos** | Tutela de derechos consagrados en la ley frente a actos administrativos [verificar] | El afectado [verificar] |
| **Interpretación prejudicial** | Aclarar el sentido y alcance de un acto administrativo [verificar] | — |

### 4. Plazos

| Supuesto | Plazo |
|---|---|
| **Demanda de plena jurisdicción (acto notificado)** | Plazo del Código Judicial — referido frecuentemente como **2 meses** desde la notificación o ejecutoria del acto [verificar] |
| **Demanda de nulidad** | No sujeta a término de caducidad (puede presentarse en cualquier tiempo) [verificar] |
| **Silencio administrativo negativo** | A partir del vencimiento del plazo para resolver el recurso [verificar] |

**Los plazos de la demanda de plena jurisdicción son de caducidad — improrrogables.**

---

## Órgano competente

| Órgano | Competencia |
|---|---|
| **Sala Tercera de lo Contencioso-Administrativo de la CSJ** | Conoce, en instancia única, de las demandas contra los actos, resoluciones, órdenes y disposiciones de las autoridades administrativas nacionales, autónomas, semiautónomas y municipales [verificar] |
| **Procuraduría de la Administración** | Interviene obligatoriamente como representante del interés de la ley emitiendo concepto en el proceso (Ley 38 de 2000) |

> A diferencia de España, en Panamá no existen juzgados o salas territoriales de lo contencioso: la competencia se concentra en la Sala Tercera de la CSJ.

---

## Suspensión provisional del acto (medida cautelar)

| Aspecto | Detalle |
|---|---|
| **Regla general** | El demandante puede solicitar la suspensión provisional de los efectos del acto acusado para evitar un perjuicio notoriamente grave [verificar] |
| **Criterio** | Apariencia de buen derecho y perjuicio grave de difícil o imposible reparación [verificar] |
| **Resolución** | La Sala Tercera resuelve la solicitud de suspensión mediante decisión motivada [verificar] |
| **Momento** | Se solicita con la demanda o en el curso del proceso [verificar] |

---

## Procedimiento ante la Sala Tercera

1. **Presentación de la demanda** — con poder a abogado idóneo, copia autenticada del acto acusado y constancia del agotamiento de la vía gubernativa [verificar]
2. **Admisión** — examen de los requisitos formales por el magistrado sustanciador [verificar]
3. **Traslado a la Procuraduría de la Administración** — emite concepto [verificar]
4. **Pruebas** — solicitud, admisión y práctica de pruebas [verificar]
5. **Alegatos** — de las partes [verificar]
6. **Fallo** — sentencia de la Sala Tercera (instancia única) [verificar]

---

## Costas

| Regla | Detalle |
|---|---|
| **Condena en costas** | La Sala puede condenar en costas a la parte vencida conforme a las reglas del Código Judicial |
| **Liquidación** | Se liquidan según las tarifas y reglas procesales aplicables [verificar] |

---

## Formato de salida

```markdown
# Viabilidad de demanda contencioso-administrativa (Sala Tercera CSJ)

**Acto impugnado:** [descripción]
**Administración demandada:** [nombre]
**Fecha de notificación:** [fecha]
**Plazo para demandar:** [fecha límite — CRÍTICO]

---

## Presupuestos procesales

| Presupuesto | Estado | Observaciones |
|---|---|---|
| Actividad impugnable | [Sí/No] | [tipo de acto] |
| Agotamiento vía gubernativa | [Sí/No] | [vía seguida] |
| Tipo de demanda | [Plena jurisdicción / Nulidad] | [fundamento] |
| Legitimación | [Sí/Dudosa/No] | [fundamento] |
| Plazo | [Dentro/Fuera/No aplica si nulidad] | [fecha límite] |
| Órgano competente | Sala Tercera de la CSJ | [base competencial] |

---

## Viabilidad de la demanda

**Valoración:** [Alta / Media / Baja / Inviable]

[Análisis de fondo: fortalezas y debilidades de la posición]

---

## Suspensión provisional

**¿Procede solicitar suspensión?** [Sí/No]
**Fundamento:** [apariencia de buen derecho + perjuicio grave de difícil reparación]

---

## Estrategia procesal

| Aspecto | Recomendación |
|---|---|
| Tipo de demanda | [Plena jurisdicción / Nulidad] |
| Suspensión provisional | [Solicitar / No solicitar] |
| Prueba clave | [qué prueba practicar] |
| Riesgo de costas | [valoración] |

---

## Costes estimados

| Concepto | Estimación |
|---|---|
| Honorarios de abogado | [rango según complejidad, en B/. / USD] |
| Peritaje | [si necesario] |
| Gastos de autenticación y copias | [estimación] |
```

---

## Legislación de referencia

- Código Judicial de Panamá — jurisdicción contencioso-administrativa y atribuciones de la Sala Tercera de la CSJ
- Ley 38 de 2000 — Procedimiento Administrativo General y agotamiento de la vía gubernativa; intervención de la Procuraduría de la Administración
- Constitución Política de la República de Panamá — control de legalidad de los actos administrativos por la CSJ

---

## Lo que este skill NO hace

- No redacta la demanda contencioso-administrativa — analiza la viabilidad y estrategia.
- No sustituye al abogado idóneo habilitado para actuar ante la Sala Tercera de la CSJ.
- No tramita la presentación de la demanda — prepara el análisis para decisión.
