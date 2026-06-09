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
- Si es empleado: los derechos patrimoniales sobre la obra creada en cumplimiento de la relación laboral corresponden al empleador, salvo pacto en contrario [verificar].
- Si es contratista independiente/encargo: se rige por el contrato — conviene cláusula expresa de cesión.

**Obras no software:**
- La transmisión de los derechos patrimoniales se limita a las modalidades expresamente cedidas en el contrato (Ley 64 de 2012) [verificar].
- Los derechos morales del autor son irrenunciables e inalienables (Ley 64 de 2012) [verificar].

**Invenciones laborales (Ley 35 de 1996):**
- Las invenciones del trabajador realizadas en el marco de su actividad contratada de investigación pertenecen al empleador [verificar].
- Las invenciones libres del trabajador le pertenecen [verificar].
- Eventual compensación económica al trabajador inventor según la ley y el contrato [verificar].

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
| 1 | [ref] | [descripción] | [Ley 64 de 2012 / Ley 35 de 1996] | [nivel] | [acción] |

### PI preexistente

[Análisis de si se delimita correctamente la PI preexistente y la generada]

### Derechos morales

[Verificar que no se incluyen renuncias a derechos morales — nulas por ley]

### Recomendaciones

[Acciones concretas para corregir o mejorar las cláusulas]
```

## Referencias normativas

- **Ley 64 de 2012**: Ley de Derecho de Autor y Derechos Conexos de Panamá.
- **Ley 64 de 2012**: derechos morales del autor — irrenunciables e inalienables [verificar].
- **Ley 64 de 2012**: transmisión de derechos patrimoniales — formalidades y limitación a las modalidades cedidas [verificar].
- **Ley 64 de 2012**: protección y titularidad de los programas de ordenador y obras creadas en relación laboral [verificar].
- **Ley 35 de 1996**: invenciones laborales y de servicio [verificar].
- **Código Civil de Panamá**: teoría general de las obligaciones y los contratos [verificar].

## Guardrails

- **NO** redacta cláusulas de PI alternativas — solo identifica problemas y recomienda.
- **NO** determina la titularidad de derechos de PI en caso de disputa.
- **NO** valora la adecuación comercial de la cesión/licencia.
- **ESCALAR** si el contrato contiene renuncia a derechos morales (nula por imperativo de la Ley 64 de 2012) [verificar].
- **ESCALAR** si la cesión de PI en un contrato laboral no respeta el régimen de invenciones laborales de la Ley 35 de 1996 [verificar].
- **AVISAR** si el contrato no distingue entre PI preexistente y PI generada.
- **AVISAR** si no se establece qué ocurre con la PI a la terminación del contrato.
