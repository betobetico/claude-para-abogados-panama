---
name: checklist-cierre-ma
description: "Rastrea condiciones precedentes, consentimientos y documentos pendientes para el cierre de una operación M&A"
argument-hint: "<ruta-al-SPA-o-listado-de-CPs>"
---

## Propósito

Esta skill gestiona la checklist de cierre (closing checklist) de una operación de M&A. Rastrea el estado de cada condición precedente, consentimiento de terceros y documento pendiente de entrega. Diseñada para mantener visibilidad sobre el progreso hacia el cierre de la operación.

## Instrucciones

### Paso 1 — Extraer condiciones del SPA

1. Leer el contrato de compraventa (SPA) o el listado de condiciones precedentes proporcionado.
2. Identificar todas las condiciones de cierre:
   - **Condiciones precedentes (CPs)**: autorizaciones, consentimientos, certificados.
   - **Documentos de cierre**: escrituras públicas, poderes, certificados, cartas.
   - **Consentimientos de terceros**: cambio de control, renuncia de accionistas, autorización regulatoria.
   - **Acciones previas al cierre**: reorganizaciones, distribuciones, cancelaciones.

### Paso 2 — Asignar responsable y plazo

Para cada elemento:

1. **Responsable**: quién debe completarlo (comprador, vendedor, target, asesores, notario, Registro Público).
2. **Plazo**: fecha límite o condición temporal (ej. "antes del cierre", "5 días tras firma").
3. **Dependencias**: si un elemento depende de otro previo.

### Paso 3 — Clasificar estado

- **Pendiente**: no iniciado.
- **En curso**: trabajo en progreso, con detalle de próximo paso.
- **Completado**: entregado y conforme.
- **Bloqueado**: depende de un elemento que no avanza — indicar cuál.
- **Renunciado**: la parte beneficiaria ha renunciado a la condición (waiver).

### Paso 4 — Generar checklist

## Formato de salida

```markdown
## Checklist de cierre — [Nombre de la operación]

**Fecha de firma del SPA:** [fecha]
**Fecha prevista de cierre (longstop):** [fecha]
**Días hasta longstop:** [n]
**Estado general:** [n]/[total] completados

### Resumen de progreso

| Estado | Número | Porcentaje |
|--------|--------|------------|
| Completado | [n] | [%] |
| En curso | [n] | [%] |
| Pendiente | [n] | [%] |
| Bloqueado | [n] | [%] |

### Condiciones precedentes

| # | Condición | Responsable | Plazo | Estado | Notas |
|---|-----------|-------------|-------|--------|-------|
| CP-1 | [descripción] | [parte] | [fecha] | [estado] | [detalle] |

### Consentimientos de terceros

| # | Consentimiento | Tercero | Responsable | Estado | Notas |
|---|----------------|---------|-------------|--------|-------|
| C-1 | [descripción] | [nombre] | [parte] | [estado] | [detalle] |

### Documentos de cierre

| # | Documento | Responsable | Estado | Notas |
|---|-----------|-------------|--------|-------|
| D-1 | [descripción] | [parte] | [estado] | [detalle] |

### Elementos bloqueados

| Elemento | Bloqueado por | Acción requerida | Responsable |
|----------|---------------|------------------|-------------|
| [ref]    | [ref]         | [acción]         | [parte]     |

### Próximos pasos

[Lista priorizada de acciones para avanzar hacia el cierre]
```

## Referencias normativas

- **Ley 32 de 1927**: sociedades anónimas — fusiones y operaciones societarias.
- **Ley 25 de 1995**: fundaciones de interés privado, cuando intervengan en la estructura.
- **Código de Comercio de Panamá**: escritura pública y formalidades de constitución y reforma.
- **Código Civil de Panamá** [verificar]: compraventa — aplicable supletoriamente.
- **Ley 45 de 2007**: protección al consumidor y defensa de la competencia — control de concentraciones (ACODECO) si aplica [verificar].
- **Registro Público de Panamá**: inscripción de la transmisión de acciones / cuotas de participación.

## Guardrails

- **NO** ejecuta ninguna acción de cierre — solo rastrea el estado.
- **NO** contacta a terceros ni envía solicitudes de consentimiento.
- **NO** redacta documentos de cierre — para eso usar la skill de acuerdo-social u otras específicas.
- **NO** valora si las condiciones precedentes se han cumplido sustantivamente — solo el estado formal.
- **ESCALAR** si quedan menos de 15 días para el longstop con elementos bloqueados.
- **ESCALAR** si una condición precedente regulatoria (ACODECO, autorizaciones sectoriales) está pendiente.
- **AVISAR** si no se proporciona fecha de longstop o fecha de firma.
