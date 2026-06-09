---
name: indemnizacion-laboral
description: "Calcula la indemnización por despido y la prima de antigüedad según tipo de terminación, antigüedad y salario con desglose legal"
argument-hint: "<fecha-inicio> <fecha-despido> <salario-bruto-diario> <tipo-despido>"
---

## Propósito

Esta skill calcula las prestaciones por terminación del contrato de trabajo en Panamá —indemnización por despido injustificado y prima de antigüedad— según el tipo de terminación, aplicando las reglas del Código de Trabajo de Panamá. Genera un desglose detallado con base legal. Todos los importes se expresan en USD / balboas (B/.).

## Instrucciones

### Paso 1 — Recopilar datos

Solicitar al usuario:

1. **Fecha de inicio** de la relación de trabajo.
2. **Fecha de terminación** (efectos).
3. **Salario** del trabajador (mensual o diario); identificar si incluye conceptos promediables (comisiones, sobretiempo habitual) [verificar].
4. **Tipo de terminación**:
   - Despido injustificado.
   - Despido justificado (causa disciplinaria o económica).
   - Renuncia / mutuo acuerdo.
   - Vencimiento de contrato por tiempo definido o por obra.

### Paso 2 — Determinar régimen aplicable

**Prima de antigüedad:**
- En contratos por tiempo indefinido, el trabajador tiene derecho a una prima de antigüedad equivalente a una semana de salario por cada año de servicio, desde el inicio de la relación [verificar]. Procede cualquiera que sea la causa de terminación [verificar].

**Indemnización por despido injustificado:**
- Se calcula según la escala del Código de Trabajo en función de la antigüedad (semanas/días de salario por año de servicio), con tramos para los primeros años y un factor adicional por cada año subsiguiente [verificar]. Confirmar la escala vigente del artículo aplicable del Código de Trabajo.

**Despido justificado:**
- No genera indemnización por despido injustificado, pero sí la prima de antigüedad y las prestaciones proporcionales (vacaciones y décimo tercer mes) [verificar].

**Renuncia / mutuo acuerdo:**
- Prima de antigüedad y prestaciones proporcionales según el caso [verificar].

**Vencimiento de contrato por tiempo definido o por obra:**
- Prestaciones proporcionales; verificar si procede indemnización por terminación anticipada injustificada [verificar].

### Paso 3 — Calcular

1. Computar antigüedad total en años y fracción.
2. Determinar el salario base de cálculo (promedio de los últimos períodos cuando haya conceptos variables) [verificar].
3. Calcular la prima de antigüedad (una semana de salario por año de servicio) [verificar].
4. Calcular la indemnización por despido injustificado aplicando la escala vigente del Código de Trabajo.
5. Sumar prestaciones proporcionales pendientes (vacaciones, décimo tercer mes) si procede.

### Paso 4 — Generar desglose

## Formato de salida

```markdown
## Cálculo de prestaciones por terminación

### Datos de partida

| Concepto | Valor |
|----------|-------|
| Fecha de inicio | [fecha] |
| Fecha de terminación | [fecha] |
| Antigüedad total | [X años, Y meses, Z días] |
| Salario base de cálculo | [importe] B/. |
| Tipo de terminación | [tipo] |

### Cálculo

#### Prima de antigüedad

- Antigüedad computable: [X años]
- Fórmula: una semana de salario × [años de servicio] [verificar]
- Resultado: [importe] B/.

#### Indemnización por despido injustificado (si aplica)

- Antigüedad computable: [X años]
- Escala del Código de Trabajo aplicada: [detalle de tramos] [verificar]
- Resultado: [importe] B/.

#### Prestaciones proporcionales pendientes

- Vacaciones proporcionales: [importe] B/. [verificar]
- Décimo tercer mes proporcional: [importe] B/. [verificar]

#### Total

- **Total de prestaciones: [importe] B/.**

### Base legal

[Artículos aplicados del Código de Trabajo: prima de antigüedad, indemnización por despido injustificado, vacaciones y décimo tercer mes — todos marcados [verificar] hasta confirmar artículo y escala vigentes]

### Advertencias

[Factores que pueden alterar el cálculo: conceptos salariales variables, descuentos, saldos pendientes, etc.]
```

## Referencias normativas

- **Código de Trabajo de Panamá** — Prima de antigüedad [verificar].
- **Código de Trabajo de Panamá** — Indemnización por despido injustificado y escala aplicable [verificar].
- **Código de Trabajo de Panamá** — Vacaciones (30 días por cada 11 meses de trabajo continuo) [verificar].
- **Régimen del décimo tercer mes** — Decreto de Gabinete sobre el XIII mes [verificar].

## Guardrails

- **NO** determina si el despido es justificado o injustificado — calcula según el escenario indicado.
- **NO** calcula retenciones de ISR (Impuesto sobre la Renta) sobre las prestaciones — señalar que ciertas prestaciones pueden tener tratamiento fiscal especial [verificar].
- **NO** calcula cuotas obrero-patronales de la CSS sobre las prestaciones.
- **NO** sustituye la liquidación final completa — se centra en indemnización y prima de antigüedad.
- **AVISAR** si el salario proporcionado no contempla conceptos variables promediables.
- **AVISAR** si la escala de indemnización o la fórmula de la prima de antigüedad deben confirmarse contra el texto vigente del Código de Trabajo.
- **ESCALAR** si el caso involucra trabajadores con fuero (maternidad, sindical) o reintegro con salarios caídos.
