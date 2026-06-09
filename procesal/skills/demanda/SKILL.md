---
name: borrador-demanda
description: "Redacta secciones de una demanda civil en formato del despacho siguiendo la estructura del Código Judicial de Panamá"
argument-hint: "<sección> <datos-del-caso>"
---

## Propósito

Esta skill redacta secciones individuales de una demanda civil siguiendo la estructura exigida por el Código Judicial de Panamá y el formato del despacho. Genera borradores que requieren revisión obligatoria por el abogado firmante (idóneo). No redacta demandas completas de una vez — trabaja sección por sección.

## Instrucciones

### Paso 1 — Identificar sección a redactar

1. **Encabezamiento**: tribunal, partes y representación judicial (apoderado).
2. **Hechos**: narración ordenada y numerada de los hechos relevantes.
3. **Fundamentos de derecho**: normas aplicables con subsunción.
4. **Petición (parte petitoria)**: pretensiones concretas y cuantificadas.
5. **Peticiones accesorias**: medidas cautelares, prueba anticipada, cuantía.

### Paso 2 — Recopilar información necesaria

**Para hechos:**
- Cronología de hechos (usar skill cronología si está disponible).
- Documentos de soporte para cada hecho.
- Relación causal entre hechos.

**Para fundamentos de derecho:**
- Norma sustantiva aplicable.
- Jurisdicción y competencia (Código Judicial de Panamá) [verificar].
- Legitimación activa y pasiva.
- Tipo de proceso (ordinario / sumario / oral, según cuantía y materia) [verificar].
- Jurisprudencia de apoyo de la Corte Suprema de Justicia (si disponible).

**Para petitum:**
- Pretensiones principales y subsidiarias.
- Cuantificación de daños si aplica.
- Intereses y costas.

### Paso 3 — Redactar sección

Seguir el formato del despacho (si existe en config) o el formato estándar.

**Hechos:**
- Numerados correlativamente.
- Un hecho relevante por párrafo.
- Con referencia al documento probatorio ("doc. nº X").
- Lenguaje fáctico — sin valoraciones jurídicas.

**Fundamentos de derecho:**
- Numerados correlativamente.
- Estructura: norma → interpretación → aplicación al caso.
- Cita literal del precepto cuando sea relevante.
- Jurisprudencia con referencia completa (Sala de la Corte Suprema de Justicia, fecha, número de registro judicial).

**Petición (parte petitoria):**
- Pretensiones numeradas, claras y concretas.
- Alternativas o subsidiarias claramente separadas.
- Pronunciamiento sobre costas e intereses.

## Formato de salida

```markdown
## BORRADOR — Sección de demanda

**Estado:** BORRADOR — Requiere revisión del abogado firmante (idóneo)
**Asunto:** [nombre]
**Sección:** [hechos / fundamentos / petición / encabezamiento / peticiones accesorias]

---

[Contenido de la sección redactada según el formato correspondiente]

---

### Notas internas (no incluir en el escrito final)

- **Documentos referenciados:** [lista de docs citados]
- **Puntos que requieren confirmación del abogado:** [lista]
- **Jurisprudencia citada:** [verificar vigencia]
- **Cuantía del proceso:** [cálculo orientativo]
```

## Referencias normativas

- **Código Judicial de Panamá**: requisitos de la demanda [verificar].
- **Código Judicial de Panamá**: preclusión de la alegación de hechos y fundamentos jurídicos [verificar].
- **Código Judicial de Panamá**: determinación del tipo de proceso (ordinario / sumario / oral) [verificar].
- **Código Judicial de Panamá**: jurisdicción y competencia [verificar].
- **Código Judicial de Panamá**: comparecencia, poder y representación judicial (apoderado) [verificar].
- **Código Judicial de Panamá**: condena con reserva de liquidación [verificar].
- **Código Judicial de Panamá**: imposición de costas [verificar].

## Guardrails

- **NO** genera demandas completas listas para presentar — solo secciones borrador.
- **NO** firma ni presenta escritos — todo es borrador para revisión.
- **NO** garantiza la viabilidad de la pretensión ni la estrategia procesal.
- **NO** sustituye al apoderado judicial en la representación procesal.
- **ESCALAR** si la pretensión puede estar prescrita o caducada.
- **ESCALAR** si hay dudas sobre la jurisdicción o competencia (arbitraje, fuero imperativo).
- **AVISAR** que la jurisprudencia citada debe verificarse en fuentes actualizadas (Órgano Judicial / Registro Judicial).
- **AVISAR** siempre al inicio: "Este documento es un BORRADOR y no constituye un escrito procesal válido hasta su revisión y firma por abogado idóneo."
