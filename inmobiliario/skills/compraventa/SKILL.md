---
name: compraventa
description: >
  Compraventa inmobiliaria — revisa un contrato de compraventa de inmueble bajo
  derecho panameño. Comprueba arras, gravámenes inscritos (certificado del
  Registro Público), condiciones suspensivas, escritura pública y fiscalidad
  (ITBI, ganancia de capital). Usar cuando el usuario diga "compraventa de
  apartamento", "revisar arras", "contrato de compraventa", "certificado del
  Registro Público", "fiscalidad de la compra" o adjunte un contrato.
argument-hint: "[archivo | enlace | pegar texto del contrato o describir la operación]"
---

# /compraventa

1. Cargar `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md` → tipo de práctica, posición habitual.
2. Obtener el contrato o la descripción de la operación.
3. Analizar la estructura de la operación (arras, condiciones, escritura).
4. Verificar gravámenes inscritos si se facilita certificado del Registro Público.
5. Determinar régimen fiscal.
6. Generar informe de revisión.

```
/inmobiliario:compraventa
Vamos a comprar un local comercial de segunda mano por 300.000 USD.
El vendedor es una sociedad anónima. Revisar la fiscalidad y el contrato de arras.
```

---

## Propósito

La compraventa inmobiliaria en Panamá combina derecho civil (Código Civil de Panamá), inscripción registral (Registro Público de Panamá), administración de tierras y catastro (ANATI), normativa fiscal (ITBI, ganancia de capital, ITBMS cuando aplica) y práctica notarial. Un error en cualquiera de estos ámbitos puede tener consecuencias graves: gravámenes ocultos, fiscalidad incorrecta, pérdida de arras o imposibilidad de inscripción. Este skill revisa cada aspecto de la operación.

---

## Estructura de la operación

### 1. Arras / contrato de promesa de compraventa

| Tipo de arras | Base legal | Efecto |
|---|---|---|
| **Penitenciales / de desistimiento** | Código Civil de Panamá [verificar] | Permiten desistir: comprador pierde las arras; vendedor devuelve el doble (si se pacta) |
| **Confirmatorias** | Código Civil de Panamá [verificar] | Señal de cumplimiento; no permiten desistir — incumplimiento → resolver + daños |
| **Penales** | Pacto expreso (cláusula penal) | Penalización por incumplimiento que no sustituye la obligación de cumplir (salvo pacto) |

**Clave:** si el contrato no especifica el tipo, debe interpretarse conforme al Código Civil de Panamá y la intención de las partes; es esencial que el tipo quede expresamente pactado. En Panamá es habitual instrumentar la operación mediante un **contrato de promesa de compraventa**. [verificar]

**Verificar en el contrato de promesa / arras:**
- [ ] Tipo de arras expresamente indicado
- [ ] Importe y forma de pago (en B/. o USD)
- [ ] Plazo para otorgar la escritura pública
- [ ] Condiciones suspensivas (si las hay)
- [ ] Descripción del inmueble coincidente con el Registro Público (finca, tomo/rollo, documento/folio o folio real)
- [ ] Manifestación de gravámenes y limitaciones
- [ ] Situación posesoria (libre de ocupantes o no)
- [ ] Reparto de gastos (escritura, impuestos, registro, ganancia de capital)

### 2. Gravámenes inscritos (certificado del Registro Público)

Si se facilita certificado del Registro Público, verificar:

| Aspecto | Verificar |
|---|---|
| **Titularidad** | ¿El vendedor es el titular registral? ¿Cotitularidad? Si es sociedad anónima, ¿quién la representa? |
| **Descripción** | ¿Coincide con la realidad (superficie, linderos, uso)? Concordancia con el catastro de ANATI |
| **Gravámenes** | Hipotecas, anticresis, embargos, secuestros, servidumbres, arrendamientos inscritos |
| **Afectaciones / limitaciones** | Patrimonio familiar, prohibiciones de enajenar, fideicomisos, afectaciones urbanísticas |
| **Régimen de propiedad horizontal** | Si procede: coeficiente de participación, anexos (estacionamiento, depósito) bajo la Ley 284 de 2022 |

**Gravámenes que deben cancelarse antes o en el acto de escritura:**
- Hipotecas → cancelación o subrogación
- Embargos / secuestros → levantamiento o pago
- Anotaciones / medidas cautelares → verificar vigencia [verificar]

### 3. Condiciones suspensivas habituales

- Obtención de financiación hipotecaria por el comprador
- Cancelación de gravámenes por el vendedor
- Obtención del permiso de ocupación (obra nueva)
- Paz y salvo de impuesto de inmueble y de cuotas de propiedad horizontal
- Concordancia de la finca con el catastro de ANATI

### 4. Escritura pública e inscripción

| Paso | Verificar |
|---|---|
| **Escritura pública** | Otorgada ante notario; necesaria para la inscripción en el Registro Público y la oponibilidad frente a terceros |
| **Inscripción en el Registro Público** | La transferencia de inmuebles se perfecciona frente a terceros con la inscripción; principio de prioridad registral [verificar] |
| **Medios de pago** | Identificación de los medios de pago conforme a normativa de prevención de blanqueo (Ley 23 de 2015 y sujetos obligados ante la UAF) — transferencia, cheque de gerencia [verificar] |
| **Retención por ganancia de capital** | En Panamá el comprador retiene un porcentaje del precio en concepto de adelanto de la ganancia de capital del vendedor y lo entera ante la DGI [verificar] |

---

## Fiscalidad de la compraventa

### Impuestos principales en Panamá

| Concepto | Impuesto | Notas |
|---|---|---|
| **Transferencia de inmueble** | **ITBI** — Impuesto de Transferencia de Bienes Inmuebles | Tarifa del 2% sobre el mayor entre el valor catastral actualizado y el valor de venta [verificar]; a cargo del vendedor |
| **Ganancia de capital** | Impuesto sobre la ganancia de capital | Tarifa del 10% sobre la ganancia; con retención anticipada del 3% del valor de venta a enterar por el comprador [verificar] |
| **ITBMS** | Impuesto de Transferencia de Bienes Muebles y Servicios | No grava la transferencia de inmuebles como tal; verificar su incidencia en operaciones de promotor o servicios asociados [verificar] |

**Principio de territorialidad:** la fiscalidad panameña grava la renta de fuente panameña; la ganancia por la venta de inmuebles situados en Panamá es de fuente panameña. [verificar]

### Otros impuestos y obligaciones

| Concepto | Sujeto pasivo | Notas |
|---|---|---|
| **Impuesto de inmueble** | Titular del inmueble | Anual; verificar exoneraciones (p. ej. patrimonio familiar tributario / vivienda principal) y que esté al día (paz y salvo) [verificar] |
| **Paz y salvo nacional (DGI)** | Vendedor | Suele exigirse para inscribir la transferencia [verificar] |
| **Cuotas de propiedad horizontal** | Vendedor (al corriente) | Certificación de no adeudo de la administración (Ley 284 de 2022) |

---

## Formato de salida

```markdown
# Revisión de compraventa inmobiliaria

**Inmueble:** [dirección, finca / folio real, corregimiento]
**Vendedor:** [persona natural / sociedad anónima]
**Comprador:** [persona natural / jurídica]
**Precio:** [importe en B/. o USD]
**Fecha de la operación:** [fecha prevista]

---

## Estructura de la operación

| Fase | Estado | Observaciones |
|---|---|---|
| Promesa de compraventa / arras | [Firmado / Pendiente] | [tipo de arras, importe] |
| Due diligence registral | [Realizado / Pendiente] | [certificado del Registro Público obtenido/pendiente] |
| Escritura pública | [Pendiente] | [notaría, fecha prevista] |
| Inscripción en el Registro Público | [Pendiente] | |

---

## Gravámenes inscritos

| Gravamen | Tipo | Estado | Acción |
|---|---|---|---|
| [Ej., Hipoteca Banco X] | Gravamen | Vigente | Cancelar en escritura |
| [Ej., Embargo] | Medida cautelar | Vigente | Levantar antes de escritura |

---

## Fiscalidad

| Concepto | Régimen | Tarifa | Importe estimado | Sujeto pasivo |
|---|---|---|---|---|
| ITBI | Transferencia de inmueble | 2% [verificar] | [importe] | [vendedor] |
| Ganancia de capital | Retención anticipada | 3% del valor / 10% sobre ganancia [verificar] | [importe] | [vendedor / retiene comprador] |
| Impuesto de inmueble | Paz y salvo | — | [al día] | [vendedor] |

---

## Hallazgos del contrato

| # | Cláusula | Observación | Riesgo | Recomendación |
|---|---|---|---|---|
| 1 | [Ej., Tipo de arras no especificado] | Ambigüedad sobre desistimiento | Alto | Especificar expresamente |
| 2 | [Ej., Sin retención por ganancia de capital] | Riesgo fiscal para el comprador | Medio | Incluir cláusula de retención |
| ... | ... | ... | ... | ... |

---

## Checklist pre-escritura

- [ ] Certificado del Registro Público actualizado (próximo a la fecha de escritura)
- [ ] Paz y salvo de impuesto de inmueble
- [ ] Paz y salvo nacional (DGI) del vendedor [verificar]
- [ ] Certificación de no adeudo de cuotas de propiedad horizontal (Ley 284 de 2022)
- [ ] Permiso de ocupación (obra nueva) si aplica
- [ ] Medios de pago preparados (transferencia / cheque de gerencia) y cumplimiento de prevención de blanqueo (Ley 23 de 2015)
```

---

## Legislación de referencia

- Código Civil de Panamá — compraventa, arras, derechos reales, hipoteca [verificar]
- Registro Público de Panamá — inscripción de la propiedad y gravámenes
- ANATI — catastro y administración de tierras
- Régimen del ITBI (Impuesto de Transferencia de Bienes Inmuebles) [verificar]
- Régimen de la ganancia de capital y retención anticipada (DGI) [verificar]
- Ley 284 de 2022 — propiedad horizontal (certificación de no adeudo)
- Ley 23 de 2015 — prevención de blanqueo de capitales (sujetos obligados, UAF)

---

## Lo que este skill NO hace

- No realiza la due diligence de uso de suelo / urbanística completa (permisos, planeamiento, situación urbanística) — marca cuándo es necesaria.
- No tramita la inscripción en el Registro Público — indica los pasos.
- No calcula impuestos con precisión definitiva — indica el régimen aplicable y remite al cálculo específico ante la DGI.
