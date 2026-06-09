---
name: revision
description: >
  Revisor de declaraciones tributarias — revisión de coherencia de
  declaraciones fiscales panameñas. Cruza ITBMS causado vs soportado,
  retenciones practicadas vs declaradas, renta gravable del ISR, segregación
  de renta de fuente panameña vs extranjera y otros parámetros. Marca
  discrepancias. Usar cuando el usuario diga "revisa esta declaración",
  "coherencia fiscal", "cuadre de formularios", "revisar 430" o adjunte datos.
argument-hint: "[formulario y datos, o describir la declaración a revisar]"
---

# /revision

1. Cargar `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md` → tipo de entidad, régimen, criterios.
2. Obtener los datos de la declaración.
3. Ejecutar las comprobaciones de coherencia.
4. Verificar la correcta segregación de renta de fuente panameña vs extranjera (territorialidad).
5. Marcar discrepancias.
6. Generar informe de revisión.

```
/fiscal:revision
Formulario 430 de julio 2026: ITBMS causado 4.500 B/., ITBMS soportado
deducible 5.200 B/., saldo a favor 700 B/.
```

---

## Propósito

Una declaración tributaria incoherente internamente o con otras declaraciones del mismo período es una señal roja para la DGI. Este skill ejecuta las comprobaciones cruzadas habituales que un buen contador o asesor fiscal realiza antes de presentar: ¿cuadran los números entre formularios? ¿se ha segregado bien la renta extranjera no gravada? ¿hay discrepancias que la DGI detectará automáticamente?

---

## Comprobaciones por formulario

### Formulario 430 (ITBMS) [verificar]

| Comprobación | Cruce | Discrepancia típica |
|---|---|---|
| ITBMS causado vs registro de facturación | Base × 7% (o tasa especial) = impuesto causado | Error en tasa aplicada o base |
| ITBMS soportado deducible vs facturas de compra | Solo deducible si vincula a operaciones gravadas y cumple requisitos [verificar] | Crédito no deducible incluido |
| Operaciones exentas / no gravadas | ¿Se han declarado correctamente? | Operaciones mal clasificadas |
| Retenciones de ITBMS soportadas | ¿Se aplican como crédito? | Retención no acreditada |
| Coherencia con servicios de fuente extranjera | Servicios prestados o consumidos fuera de Panamá — fuera del ámbito del ITBMS [verificar] | Inclusión indebida de operación no territorial |

### Planilla 03 / retenciones del ISR sobre salarios [verificar]

| Comprobación | Cruce | Discrepancia típica |
|---|---|---|
| Retenciones practicadas vs declaradas | Planilla salarial → retención del ISR | Retención mal calculada o no declarada |
| Coherencia planilla CSS ↔ planilla ISR | Salarios reportados coinciden | Trabajador no incluido |
| Décimo tercer mes | Tratamiento correcto de la partida | Cálculo o exención mal aplicados [verificar] |

### Formulario 1 (Impuesto sobre la Renta) [verificar]

| Comprobación | Cruce | Discrepancia típica |
|---|---|---|
| Resultado contable → Renta gravable | Conciliación fiscal con ajustes correctamente aplicados | Ajuste omitido o duplicado |
| Segregación territorial | Renta de fuente panameña (gravada) vs extranjera (no gravada) y costos/gastos prorrateados | Renta extranjera gravada por error o gastos mal prorrateados |
| Tarifa del ISR | ¿Se aplica la tarifa correcta? (25% personas jurídicas / tarifa progresiva personas naturales) [verificar] | Tarifa incorrecta |
| CAIR | Si ingresos gravables > 1.500.000 B/.: ¿se comparó con el cálculo alternativo? [verificar] | CAIR omitido |
| Estimada del período siguiente | ¿Coherente con la renta del período? | Estimada mal calculada |
| Arrastre de pérdidas | ¿Dentro de los límites legales? [verificar] | Aplicación excesiva |

### Retención sobre dividendos [verificar]

| Comprobación | Cruce | Discrepancia típica |
|---|---|---|
| Tasa de retención | 10% acciones nominativas / 5% al portador o de zona libre [verificar] | Tasa incorrecta |
| Impuesto complementario | ¿Se calculó sobre las utilidades no distribuidas? [verificar] | Complementario omitido |

---

## Comprobaciones cruzadas entre formularios

| Cruce | Qué verificar |
|---|---|
| 430 ↔ Formulario 1 | Ingresos declarados en ITBMS coherentes con ingresos gravables del ISR (depurando exentos y fuente extranjera) |
| Planilla 03 ↔ Formulario 1 | Retenciones practicadas como gasto vs retenciones declaradas |
| Planilla CSS ↔ Planilla 03 | Masa salarial reportada coincide entre ambas administraciones |
| Dividendos ↔ utilidades del ejercicio | Retención y complementario coherentes con las utilidades distribuibles |

---

## Formato de salida

```markdown
# Revisión de declaración: Formulario [número] — [período]

**Entidad:** [nombre]
**Período:** [mes/año]
**Fecha de revisión:** [fecha]

---

## Resultado de la revisión

| Estado | Descripción |
|---|---|
| **Discrepancias encontradas** | [N] |
| **De las cuales críticas** | [N] |

---

## Detalle de comprobaciones

| # | Comprobación | Resultado | Discrepancia | Impacto | Acción |
|---|---|---|---|---|---|
| 1 | [Ej., ITBMS causado vs registro] | [Cuadra / Discrepancia] | [Diferencia de 120 B/.] | [Potencial requerimiento DGI] | [Revisar factura X] |
| 2 | ... | ... | ... | ... | ... |

---

## Discrepancias críticas (resolver antes de presentar)

[Lista detallada con origen de la discrepancia y solución propuesta]

---

## Observaciones

[Notas adicionales: cambios normativos que afectan al período, criterios interpretativos aplicados, segregación territorial]
```

---

## Legislación de referencia

- **Código Fiscal de Panamá** — régimen del ISR, ITBMS, retenciones y obligaciones formales [verificar]
- **Decreto Ejecutivo 170 de 1993** — reglamentación del ISR, prorrateo de gastos y territorialidad [verificar]
- **Ley 8 de 2010** — ITBMS y reforma tributaria [verificar]
- Normativa de precios de transferencia (informe 930) [verificar]

---

## Lo que este skill NO hace

- No presenta declaraciones ante la DGI — revisa la coherencia antes de presentar.
- No calcula la cuota a pagar desde cero — verifica la coherencia de los datos facilitados.
- No sustituye al contador público autorizado ni al asesor fiscal — identifica discrepancias para que el profesional decida.
