---
name: revision-contratacion
description: "Revisa contratos de trabajo verificando cláusulas obligatorias y adecuación al tipo contractual"
argument-hint: "<ruta-al-contrato-de-trabajo>"
---

## Propósito

Esta skill revisa un contrato de trabajo individual, verifica que contiene todas las cláusulas obligatorias según el Código de Trabajo de Panamá y la normativa aplicable, y comprueba que el tipo contractual elegido se ajusta a la situación descrita.

## Instrucciones

### Paso 1 — Identificar tipo de contrato

1. **Por tiempo indefinido**: contrato por defecto bajo el Código de Trabajo [verificar].
2. **Por tiempo definido**: con plazo determinado, sujeto a los límites del Código de Trabajo [verificar].
3. **Por obra determinada**: vinculado a la ejecución de una obra o servicio específico [verificar].
4. **Contrato de aprendizaje / formación**: regulado por el Código de Trabajo y normativa del INADEH [verificar].

Recordar la regla de continuidad: la celebración sucesiva de contratos por tiempo definido o por obra que excedan los límites legales puede convertir la relación en una por tiempo indefinido [verificar].

### Paso 2 — Verificar cláusulas obligatorias

Comprobar la presencia y corrección de:

| Cláusula | Base legal | Verificación |
|----------|------------|--------------|
| Identidad de las partes (incl. cédula/RUC) | Código de Trabajo [verificar] | Datos completos |
| Fecha de inicio y duración | Código de Trabajo [verificar] | Coherente con tipo |
| Domicilio del empleador y lugar de trabajo | Código de Trabajo [verificar] | Presente |
| Cargo o clase de trabajo | Código de Trabajo [verificar] | Definido con claridad |
| Salario y forma de pago | Código de Trabajo [verificar] | ≥ salario mínimo (MITRADEL) |
| Jornada y horario | Código de Trabajo [verificar] | Dentro de la jornada máxima legal |
| Vacaciones | Código de Trabajo [verificar] | 30 días por cada 11 meses de trabajo continuo [verificar] |
| Período de prueba (si aplica) | Código de Trabajo [verificar] | Dentro de límites legales |
| Décimo tercer mes | Código de Trabajo / régimen del XIII mes [verificar] | Mención del derecho |
| Inscripción en la CSS | Ley Orgánica de la CSS [verificar] | Obligación de afiliación |

### Paso 3 — Revisar cláusulas especiales

- **No competencia postcontractual**: validez y límites bajo el Código de Trabajo y la legislación panameña; conviene compensación e interés legítimo del empleador [verificar].
- **Confidencialidad**: proporcionalidad y duración razonables.
- **Exclusividad / plena dedicación**: con contraprestación adecuada.
- **Teletrabajo**: acuerdo escrito conforme a la Ley 126 de 2020 [verificar] sobre teletrabajo.

### Paso 4 — Verificar adecuación del tipo contractual

- El contrato por tiempo definido o por obra tiene causa real y vigente.
- La duración se ajusta a los máximos legales del Código de Trabajo.
- No hay indicios de uso fraudulento de la temporalidad (sucesión de contratos que deba convertirse en indefinido) [verificar].

## Formato de salida

```markdown
## Revisión de contrato de trabajo

**Tipo contractual:** [tipo]
**Trabajador:** [nombre]
**Puesto:** [denominación]
**Convención colectiva aplicable (si existe):** [nombre de la convención]

### Verificación de cláusulas obligatorias

| Cláusula | Presente | Conforme | Observaciones |
|----------|----------|----------|---------------|
| [nombre] | [SÍ/NO] | [SÍ/NO/N/A] | [detalle] |

### Cláusulas especiales

| Cláusula | Presente | Validez | Riesgos |
|----------|----------|---------|---------|
| No competencia | [SÍ/NO] | [válida/dudosa/nula] | [detalle] |

### Adecuación del tipo contractual

[Valoración de si el tipo contractual es correcto para la situación descrita]

### Riesgos detectados

| Riesgo | Severidad | Consecuencia | Recomendación |
|--------|-----------|--------------|---------------|
| [riesgo] | [nivel] | [qué puede pasar] | [qué hacer] |
```

## Referencias normativas

- **Código de Trabajo de Panamá** — Forma, duración y modalidades del contrato de trabajo [verificar].
- **Código de Trabajo** — Período de prueba [verificar].
- **Código de Trabajo** — Contratos por tiempo definido y por obra determinada; regla de conversión a indefinido [verificar].
- **Código de Trabajo** — Jornada, vacaciones (30 días por cada 11 meses) y salario [verificar].
- **Régimen del décimo tercer mes** — Decreto de Gabinete sobre el XIII mes [verificar].
- **Ley Orgánica de la CSS** — Afiliación obligatoria del trabajador [verificar].
- **Ley 126 de 2020** — Teletrabajo [verificar].

## Guardrails

- **NO** redacta contratos de trabajo — solo revisa los existentes.
- **NO** determina la convención colectiva aplicable con certeza — sugiere la probable.
- **NO** calcula planillas ni cuotas obrero-patronales de la CSS.
- **ESCALAR** si el contrato por tiempo definido o por obra carece de causa o supera la duración máxima legal.
- **ESCALAR** si la cláusula de no competencia carece de contraprestación o de interés legítimo del empleador.
- **AVISAR** si no se identifica la convención colectiva aplicable (cuando exista) para verificar mejoras sobre el mínimo legal.
