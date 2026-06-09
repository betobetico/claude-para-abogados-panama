---
name: cumplimiento-societario
description: "Genera el calendario de obligaciones societarias y rastrea su estado de cumplimiento"
argument-hint: "<tipo-sociedad> [datos-de-la-entidad]"
---

## Propósito

Esta skill genera y mantiene el calendario de obligaciones societarias legales para una entidad mercantil panameña (S.A. o S. de R.L.). Verifica el estado de cumplimiento de cada obligación y alerta sobre plazos próximos o vencidos.

## Instrucciones

### Paso 1 — Identificar la entidad

1. Determinar el tipo de sociedad: S.A. (Sociedad Anónima) o S. de R.L. (Sociedad de Responsabilidad Limitada).
2. Recopilar datos relevantes: fecha de cierre del período fiscal, fecha de constitución, junta directiva, dignatarios y sus fechas de nombramiento.
3. Cargar configuración específica desde `~/.claude/plugins/config/claude-para-abogados/societario/CLAUDE.md`.

### Paso 2 — Generar calendario de obligaciones

Obligaciones comunes a S.A. y S. de R.L.:

1. **Tasa única anual**: pago anual obligatorio para el mantenimiento de la sociedad ante el Registro Público [verificar].
2. **Declaración jurada de renta (ISR)**: presentación ante la DGI dentro del plazo legal — generalmente hasta el 31 de marzo siguiente al cierre del período fiscal [verificar].
3. **Mantenimiento del agente residente**: la sociedad debe contar en todo momento con agente residente (abogado o firma de abogados) [verificar].
4. **Libros sociales**: libro de actas y registro de acciones actualizados (Código de Comercio de Panamá) [verificar].
5. **Renovación de cargos**: según duración prevista en el pacto social.
6. **Registro de acciones / cuotas de participación**: actualización tras cada traspaso.
7. **Declaración de beneficiario final**: ante el sistema correspondiente conforme a la normativa de transparencia [verificar].

Obligaciones específicas según régimen:

8. **Estados financieros auditados**: cuando la entidad esté obligada conforme a su régimen o actividad [verificar].
9. **Reporte a la UAF**: si la entidad es sujeto obligado bajo la Ley 23 de 2015.
10. **Junta de accionistas ordinaria**: según lo previsto en el pacto social.

### Paso 3 — Verificar estado

Para cada obligación:

- **Cumplida**: documentación disponible que acredita el cumplimiento.
- **En plazo**: el plazo no ha vencido.
- **Próxima**: vence en los próximos 30 días.
- **Vencida**: el plazo ha expirado sin acreditar cumplimiento.

### Paso 4 — Generar informe

## Formato de salida

```markdown
## Calendario de cumplimiento societario

**Sociedad:** [denominación]
**Tipo:** [S.A. / S. de R.L.]
**Período fiscal:** [año]
**Fecha del informe:** [fecha]

### Estado general

- Obligaciones cumplidas: [n]/[total]
- Próximas (≤30 días): [n]
- Vencidas sin cumplir: [n]

### Calendario de obligaciones

| Obligación | Plazo legal | Fecha límite | Estado | Base legal | Notas |
|------------|-------------|--------------|--------|------------|-------|
| Tasa única anual | Anual | [fecha] [verificar] | [estado] | Registro Público | [nota] |
| Declaración de renta (ISR) | Hasta 31 marzo [verificar] | [fecha] | [estado] | Código Fiscal [verificar] | [nota] |
| Agente residente | Continuo | [fecha] | [estado] | Ley 32 de 1927 [verificar] | [nota] |

### Renovación de cargos

| Cargo | Titular | Fecha nombramiento | Duración | Vencimiento | Estado |
|-------|---------|--------------------|-----------| ------------|--------|
| [cargo] | [nombre] | [fecha] | [años] | [fecha] | [estado] |

### Alertas

[Lista de obligaciones vencidas o próximas con acción recomendada]
```

## Referencias normativas

- **Ley 32 de 1927**: sociedades anónimas — junta directiva, dignatarios y agente residente.
- **Ley 25 de 1995**: fundaciones de interés privado — obligaciones de mantenimiento.
- **Código de Comercio de Panamá**: libros sociales y obligaciones contables.
- **Código Fiscal de Panamá** [verificar]: declaración de renta (ISR) y tasa única anual.
- **Ley 23 de 2015**: prevención de blanqueo de capitales y sujetos obligados (UAF).
- **Normativa de transparencia y beneficiario final** [verificar]: registro y reporte de beneficiarios finales.

## Guardrails

- **NO** presenta ni tramita documentos ante el Registro Público ni la DGI.
- **NO** redacta los estados financieros ni el informe de gestión.
- **NO** verifica la corrección contable de las cuentas.
- **ESCALAR** si se detectan obligaciones vencidas que puedan acarrear sanciones (multas, suspensión de derechos corporativos por falta de pago de la tasa única anual, caducidad de cargos) [verificar].
- **ESCALAR** si la sociedad debería estar obligada a auditar y no consta auditor nombrado.
- **AVISAR** si faltan datos para calcular algún plazo (ej. fecha de cierre del período fiscal).
