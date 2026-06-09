---
name: portfolio-pi
description: "Rastrea el estado de registros de PI, fechas de renovación y tasas de mantenimiento pendientes"
argument-hint: "[ruta-al-registro-de-activos-PI]"
---

## Propósito

Esta skill gestiona el portfolio de activos de propiedad intelectual e industrial de una empresa o cliente. Rastrea el estado de registros, fechas de renovación, tasas de mantenimiento y acciones pendientes para marcas, patentes y diseños.

## Instrucciones

### Paso 1 — Cargar inventario de activos

1. Leer el registro de activos de PI proporcionado por el usuario.
2. Clasificar cada activo por tipo:
   - **Marcas**: nacionales (DIGERPI), internacionales (OMPI/Protocolo de Madrid).
   - **Patentes**: nacionales (DIGERPI), internacionales (PCT).
   - **Modelos de utilidad**: DIGERPI.
   - **Diseños industriales**: DIGERPI.
   - **Nombres de dominio**: .pa, .com, otros.
   - **Derechos de autor**: registros en la Dirección Nacional de Derecho de Autor (DIGERPI) [verificar].

### Paso 2 — Calcular fechas clave

**Marcas:**
- Duración: 10 años desde el registro, renovable por períodos iguales (Ley 35 de 1996).
- Renovación: solicitar dentro del plazo previo al vencimiento, con eventual período de gracia con recargo [verificar].

**Patentes:**
- Duración máxima: 20 años desde la presentación de la solicitud (Ley 35 de 1996).
- Anualidades: pago periódico de tasas de mantenimiento ante la DIGERPI [verificar].

**Diseños industriales:**
- Vigencia y renovaciones según la Ley 35 de 1996.

**Modelos de utilidad:**
- Vigencia y mantenimiento según la Ley 35 de 1996.

### Paso 3 — Evaluar estado

Para cada activo:
- **Vigente**: registro activo con todas las tasas al día.
- **Próxima renovación**: vence en los próximos 90 días.
- **En gracia**: período de gracia activo (con recargo).
- **Pendiente de pago**: tasa vencida sin pago registrado.
- **En trámite**: solicitud pendiente de resolución.
- **Caducado/Extinguido**: derecho perdido.

### Paso 4 — Generar informe

## Formato de salida

```markdown
## Portfolio de propiedad intelectual e industrial

**Titular:** [nombre/empresa]
**Fecha del informe:** [fecha]
**Total de activos:** [número]

### Resumen por tipo

| Tipo | Vigentes | En trámite | Próx. renovación (90d) | Caducados |
|------|----------|------------|------------------------|-----------|
| Marcas | [n] | [n] | [n] | [n] |
| Patentes | [n] | [n] | [n] | [n] |
| Diseños | [n] | [n] | [n] | [n] |
| Otros | [n] | [n] | [n] | [n] |

### Acciones urgentes (próximos 90 días)

| Activo | Tipo | Registro | Acción | Fecha límite | Tasa estimada |
|--------|------|----------|--------|--------------|---------------|
| [nombre] | [tipo] | [nº registro] | [renovación/anualidad] | [fecha] | [USD (B/.)] |

### Inventario completo

| Activo | Tipo | Registro | Clases/Reivindicaciones | Territorio | Vigencia | Estado | Próxima acción |
|--------|------|----------|-------------------------|------------|----------|--------|----------------|
| [nombre] | [tipo] | [nº] | [detalle] | [territorio] | [hasta fecha] | [estado] | [acción y fecha] |

### Presupuesto estimado de tasas (próximos 12 meses)

| Activo | Acción | Fecha | Tasa estimada |
|--------|--------|-------|---------------|
| [nombre] | [tipo] | [fecha] | [USD (B/.)] |
| **TOTAL** | | | **[USD (B/.)]** |
```

## Referencias normativas

- **Ley 35 de 1996** (propiedad industrial): duración y renovación de marcas [verificar].
- **Ley 35 de 1996**: duración y mantenimiento de patentes y modelos de utilidad [verificar].
- **Ley 35 de 1996**: protección y vigencia de los diseños industriales [verificar].
- **Protocolo de Madrid**: gestión y renovación de marcas internacionales (OMPI).
- **Tratado de Cooperación en materia de Patentes (PCT)**: solicitudes internacionales de patente.

## Guardrails

- **NO** presenta solicitudes de renovación ni paga tasas.
- **NO** accede a bases de datos oficiales (DIGERPI, OMPI) — trabaja con datos proporcionados.
- **NO** valora la conveniencia de mantener o abandonar un activo.
- **NO** estima con precisión las tasas — proporciona rangos orientativos.
- **ESCALAR** si un activo estratégico está en período de gracia o próximo a caducar.
- **AVISAR** si faltan datos para calcular fechas de renovación (fecha de solicitud, territorio).
- **AVISAR** si se detectan activos sin responsable asignado.
