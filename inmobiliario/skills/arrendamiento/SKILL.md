---
name: arrendamiento
description: >
  Revisor de arrendamiento — revisa un contrato de arrendamiento contra el
  régimen de arrendamientos panameño. Distingue entre arrendamiento de vivienda
  (régimen tutelado) y arrendamiento comercial/uso distinto. Comprueba duración,
  canon, actualización, depósito de garantía, mejoras y resolución. Marca
  cláusulas contrarias a la ley. Usar cuando el usuario diga "revisa este
  alquiler", "contrato de arrendamiento", "¿es legal esta cláusula del alquiler?",
  "arrendamiento".
argument-hint: "[archivo | enlace | pegar texto del contrato]"
---

# /arrendamiento

1. Cargar `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md` → tipo de práctica, posición habitual (arrendador/arrendatario).
2. Obtener el contrato.
3. Determinar tipo: arrendamiento de vivienda (régimen tutelado) vs arrendamiento comercial / uso distinto.
4. Revisar cláusula por cláusula contra la legislación de arrendamientos panameña.
5. Marcar cláusulas nulas o de riesgo.

```
/inmobiliario:arrendamiento
[pegar el contrato de alquiler de vivienda]
```

---

## Propósito

En Panamá los arrendamientos de vivienda están sujetos a un régimen tutelado regulado por la legislación de arrendamientos [verificar], que fija reglas imperativas de protección al arrendatario; las cláusulas contrarias se tienen por no puestas. Los arrendamientos comerciales o de uso distinto a vivienda se rigen principalmente por la autonomía de la voluntad y el Código Civil de Panamá. Distinguir correctamente el tipo de arrendamiento es el paso más importante.

> **Nota de verificación:** El marco de arrendamientos panameño ha tenido diversas normas y reformas, y existen umbrales de canon que determinan si un contrato queda bajo el régimen tutelado o queda excluido. Verificar la norma y los umbrales vigentes antes de citar artículos concretos. [verificar]

---

## Paso 1: ¿Vivienda (régimen tutelado) o uso distinto?

| Criterio | Vivienda (régimen tutelado) | Uso distinto / comercial |
|---|---|---|
| **Destino** | Satisfacer necesidad de vivienda del arrendatario | Local comercial, oficina, depósito, temporada, estacionamiento independiente |
| **Régimen** | Imperativo (protección al arrendatario) — irrenunciabilidad de derechos [verificar] | Dispositivo — autonomía de la voluntad (Código Civil de Panamá) |
| **Norma aplicable** | Legislación de arrendamientos [verificar] + supletoriamente Código Civil de Panamá | Voluntad de las partes → Código Civil de Panamá |

**Arrendamientos de temporada / amueblados de corto plazo:** suelen quedar fuera del régimen tutelado de vivienda. Verificar que realmente es temporal y no un uso fraudulento para eludir la protección del arrendatario. [verificar]

---

## Revisión de arrendamiento de VIVIENDA (régimen tutelado)

### Duración y prórroga

| Aspecto | Norma | Verificar |
|---|---|---|
| **Duración mínima / prórroga** | Régimen de arrendamientos panameño [verificar] | ¿El contrato respeta la protección del arrendatario frente al desalojo? |
| **Renovación** | Según pacto y ley aplicable [verificar] | ¿Se respetan los plazos de preaviso? |
| **Desistimiento del arrendatario** | Según pacto y ley aplicable [verificar] | ¿Se ha pactado indemnización? |

### Canon de arrendamiento

| Aspecto | Norma | Verificar |
|---|---|---|
| **Canon inicial** | Libre fijación, salvo límites del régimen tutelado [verificar] | ¿Aplica algún tope o control de canon? |
| **Actualización** | Solo si se pacta, dentro de los límites legales [verificar] | ¿El criterio pactado es conforme? |
| **Moneda** | Balboas (B/.) / dólares estadounidenses (USD) | ¿El canon está expresado en B/. o USD? |
| **Gastos e impuestos** | Repercutibles al arrendatario solo si se pacta | ¿Se ha pactado expresamente? |

### Depósito de garantía

| Aspecto | Norma |
|---|---|
| **Depósito de garantía** | Habitualmente equivalente a uno o varios cánones mensuales, según la ley aplicable [verificar] |
| **Custodia del depósito** | En Panamá el depósito de los arrendamientos sujetos al régimen tutelado se consigna ante la autoridad competente en materia de vivienda (MIVIOT) [verificar] |
| **Devolución** | Al término del contrato, descontando daños o cánones pendientes |

### Mejoras y reparaciones

| Tipo | Régimen |
|---|---|
| **Conservación (arrendador)** | Obligación del arrendador mantener el inmueble en estado de servir al uso pactado (Código Civil de Panamá) |
| **Mejoras (arrendador)** | Régimen según pacto y ley aplicable [verificar] |
| **Obras del arrendatario** | Sin consentimiento del arrendador: en principio prohibidas; verificar excepciones [verificar] |

### Resolución / desalojo

| Causa de resolución por arrendador | Causa de resolución por arrendatario |
|---|---|
| Falta de pago del canon [verificar] | Incumplimiento de reparaciones necesarias |
| Subarriendo no consentido | Perturbación del arrendador en el uso |
| Daños dolosos u obras no consentidas | |
| Uso distinto al pactado / actividades ilícitas | |

**Nota procesal:** El desalojo en arrendamientos de vivienda sujetos al régimen tutelado puede requerir trámite ante la autoridad administrativa de vivienda antes que la vía judicial. Verificar el procedimiento aplicable. [verificar]

### Cláusulas nulas en vivienda (régimen tutelado)

**Se tienen por no puestas** las cláusulas que modifiquen en perjuicio del arrendatario las normas imperativas del régimen tutelado. Ejemplos habituales de cláusulas de riesgo:

- Renuncia anticipada del arrendatario a la protección frente al desalojo [verificar]
- Depósito de garantía superior al permitido por la ley [verificar]
- Repercusión de gastos de gestión o formalización al arrendatario cuando la ley no lo permite [verificar]
- Actualización de canon por encima del límite legal [verificar]
- Cláusulas de desalojo automático sin el debido proceso

---

## Revisión de arrendamiento de USO DISTINTO / COMERCIAL

En uso distinto, prima la autonomía de la voluntad bajo el Código Civil de Panamá. La revisión se centra en:

| Aspecto | Verificar |
|---|---|
| Duración y prórrogas | ¿Son razonables para el negocio? |
| Canon y actualización | Libre; ¿el criterio es claro y aplicable? ¿Moneda en B/. o USD? |
| Depósito de garantía | Libre pacto |
| Obras y mejoras | ¿Quién las asume? ¿Derecho de remoción al finalizar? |
| Cesión y subarriendo | ¿Se permite? Régimen según pacto y Código Civil de Panamá |
| Resolución anticipada | Causas pactadas; ¿penalización equilibrada? |
| Mejoras del local | ¿Quién paga la adecuación? ¿Reversión al arrendador? |

---

## Formato de salida

```markdown
# Revisión de arrendamiento: [Dirección del inmueble]

**Tipo:** [Vivienda (régimen tutelado) / Uso distinto - comercial]
**Arrendador:** [persona natural / jurídica]
**Fecha del contrato:** [fecha]
**Duración pactada:** [años]

---

## Resultado global

**Hallazgos:** [N] Conforme [N] Riesgo medio [N] Riesgo alto [N] Nula

---

## Detalle por cláusula

| # | Cláusula | Lo que dice el contrato | Norma aplicable | Riesgo | Observación |
|---|---|---|---|---|---|
| 1 | Duración | [Ej., 1 año sin prórroga] | Régimen de arrendamientos [verificar] | Riesgo | Verificar protección del arrendatario |
| 2 | Depósito de garantía | [Ej., 3 cánones] | Régimen de arrendamientos [verificar] | Riesgo | Verificar tope legal |
| ... | ... | ... | ... | ... | ... |

---

## Cláusulas nulas (solo vivienda)

[Lista de cláusulas contrarias al régimen tutelado con consecuencia: se tienen por no puestas]

---

## Recomendaciones

[Ajustes recomendados para que el contrato sea conforme]
```

---

## Legislación de referencia

- Legislación de arrendamientos de Panamá [verificar]
- Código Civil de Panamá (arrendamiento — disposiciones supletorias) [verificar]
- MIVIOT (Ministerio de Vivienda y Ordenamiento Territorial) — autoridad en materia de vivienda y arrendamientos [verificar]

---

## Lo que este skill NO hace

- No redacta contratos de arrendamiento desde cero — revisa los existentes.
- No determina si un canon queda dentro o fuera del régimen tutelado — indica cuándo verificarlo.
- No tramita la consignación del depósito de garantía ante la autoridad de vivienda.
