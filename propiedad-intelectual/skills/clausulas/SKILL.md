---
name: revisor-clausulas-pi
description: "Revisa cláusulas de propiedad intelectual e industrial en contratos verificando cesión, alcance y conformidad legal"
argument-hint: "<ruta-al-contrato>"
---

## Propósito

Esta skill revisa las cláusulas de propiedad intelectual e industrial contenidas en un contrato. Verifica la estructura de cesión/licencia, exclusividad, territorio, duración y conformidad con la legislación panameña de PI (Ley 64 de 2012 y Ley 35 de 1996), prestando especial atención a la obra por encargo y la PI generada en relación laboral.

## Instrucciones

### Paso 1 — Identificar cláusulas de PI

Localizar en el contrato:

1. Cláusula de titularidad / propiedad de los resultados.
2. Cesión de derechos de explotación.
3. Licencia de uso (si no hay cesión).
4. Obra por encargo / work made for hire.
5. PI preexistente (background IP).
6. PI desarrollada conjuntamente.
7. Derecho moral del autor.
8. Garantías de no infracción.
9. Invenciones y patentes (en contratos laborales o de I+D).

### Paso 2 — Analizar cada cláusula

Para cada cláusula de PI verificar:

| Aspecto | Verificación |
|---------|-------------|
| **Cesión vs. licencia** | ¿Se cede la titularidad o se licencia el uso? |
| **Exclusividad** | ¿Es exclusiva o no exclusiva? |
| **Territorio** | ¿Limitación geográfica? (Panamá, regional, mundial) |
| **Duración** | ¿Temporal o por toda la vigencia de los derechos? |
| **Modalidades** | ¿Qué derechos se ceden? (reproducción, distribución, comunicación pública, transformación) |
| **Sublicencia** | ¿Se permite sublicenciar? |
| **Contraprestación** | ¿Se establece precio o se incluye en el precio del contrato? |
| **Reversión** | ¿Qué ocurre con la PI al terminar el contrato? |

### Paso 3 — Verificar conformidad legal

**Software (Ley 64 de 2012):**
- El software se protege como obra por el derecho de autor (no por patente); su duración patrimonial es de 70 años desde la primera publicación.
- Si es empleado: los derechos patrimoniales sobre la obra creada en cumplimiento de la relación laboral corresponden, salvo pacto en contrario, al empleador (los derechos morales permanecen en el autor).
- Si es contratista independiente/encargo: se rige por el contrato — conviene cláusula expresa de cesión.

**Obras no software:**
- La transmisión de los derechos patrimoniales debe constar por escrito y se limita a las modalidades expresamente cedidas en el contrato (Ley 64 de 2012).
- Los derechos morales del autor son perpetuos, inalienables, irrenunciables e inembargables (Ley 64 de 2012).

**Invenciones laborales (Código de Trabajo, arts. 193-196; la Ley 35 de 1996, art. 9, remite al Código de Trabajo):**
- Las invenciones de empresa y de servicio pertenecen al empleador; el trabajador inventor conserva el derecho moral a ser reconocido como autor.
- Las invenciones libres del trabajador le pertenecen.
- Compensación especial al trabajador inventor de invención de servicio cuando los beneficios sean desproporcionados, no inferior al 10% de las utilidades netas (art. 196 del Código de Trabajo).

### Paso 4 — Generar informe

## Formato de salida

```markdown
## Revisión de cláusulas de PI

**Contrato:** [nombre]
**Tipo de contrato:** [prestación de servicios / laboral / licencia / colaboración / I+D]
**Fecha de revisión:** [fecha]

### Tabla de análisis

| Cláusula | Tipo | Exclusividad | Territorio | Duración | Modalidades | Conforme | Observaciones |
|----------|------|-------------|------------|----------|-------------|----------|---------------|
| [ref] | Cesión/Licencia | Sí/No | [territorio] | [duración] | [lista] | [SÍ/NO] | [detalle] |

### Problemas detectados

| # | Cláusula | Problema | Base legal | Severidad | Recomendación |
|---|----------|----------|------------|-----------|---------------|
| 1 | [ref] | [descripción] | [Ley 64 de 2012 / Ley 35 de 1996 / Código de Trabajo arts. 193-196] | [nivel] | [acción] |

### PI preexistente

[Análisis de si se delimita correctamente la PI preexistente y la generada]

### Derechos morales

[Verificar que no se incluyen renuncias a derechos morales — nulas por ley]

### Recomendaciones

[Acciones concretas para corregir o mejorar las cláusulas]
```

## Referencias normativas

- **Ley 64 de 2012**: Ley de Derecho de Autor y Derechos Conexos de Panamá.
- **Ley 64 de 2012**: derechos morales del autor — perpetuos, inalienables, irrenunciables e inembargables.
- **Ley 64 de 2012**: transmisión de derechos patrimoniales — por escrito y limitada a las modalidades de explotación expresamente cedidas.
- **Ley 64 de 2012**: protección del software como obra (no por patente; 70 años desde la primera publicación) y titularidad de obras creadas en relación laboral (patrimoniales al empleador salvo pacto en contrario; morales del autor).
- **Código de Trabajo, arts. 193-196**: invenciones laborales y de servicio (la Ley 35 de 1996, art. 9, remite al Código de Trabajo); compensación al inventor no inferior al 10% de las utilidades netas (art. 196).
- **Código Civil de Panamá**: teoría general de las obligaciones y los contratos.

## Guardrails

- **NO** redacta cláusulas de PI alternativas — solo identifica problemas y recomienda.
- **NO** determina la titularidad de derechos de PI en caso de disputa.
- **NO** valora la adecuación comercial de la cesión/licencia.
- **ESCALAR** si el contrato contiene renuncia a derechos morales (nula por imperativo de la Ley 64 de 2012).
- **ESCALAR** si la cesión de PI en un contrato laboral no respeta el régimen de invenciones laborales del Código de Trabajo, arts. 193-196 (al que remite la Ley 35 de 1996, art. 9).
- **AVISAR** si el contrato no distingue entre PI preexistente y PI generada.
- **AVISAR** si no se establece qué ocurre con la PI a la terminación del contrato.
