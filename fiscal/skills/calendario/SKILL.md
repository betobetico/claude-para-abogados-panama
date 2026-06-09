---
name: calendario
description: >
  Calendario fiscal — genera el calendario de obligaciones tributarias por
  tipo de entidad y obligaciones configuradas. Formularios: 430 (ITBMS), 03
  (planilla retenciones ISR), 1 (declaración jurada ISR), CAIR, retención de
  dividendos, tasa única y otros. Muestra formulario, plazo y estado. Usar
  cuando el usuario diga "calendario fiscal", "¿qué declaración toca?",
  "plazos tributarios", "obligaciones fiscales".
argument-hint: "[--trimestre X | --mes X | --anual | --todo]"
---

# /calendario

1. Cargar `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md` → tipo de entidad, régimen de ITBMS, obligaciones, régimen de zona especial.
2. Generar calendario según el período solicitado.
3. Cruzar con plazos de la DGI.
4. Marcar estado de cada obligación.

```
/fiscal:calendario --trimestre 2T-2026
```

---

## Propósito

Cumplir los plazos tributarios es una obligación de resultado. Una declaración presentada fuera de plazo genera automáticamente recargos e intereses y potenciales multas conforme al Código Fiscal. Este skill genera el calendario de obligaciones tributarias de la entidad para que nada se escape.

---

## Obligaciones por tipo de formulario

### ITBMS

| Formulario | Descripción | Periodicidad | Plazo |
|---|---|---|---|
| **430** [verificar] | Declaración-liquidación del ITBMS | Mensual | Dentro de los 15 días calendario siguientes al cierre del mes [verificar] |
| **433** [verificar] | Declaración de retenciones de ITBMS (agentes de retención) | Mensual | Dentro de los 15 días siguientes al mes [verificar] |

### Retenciones del ISR

| Formulario | Descripción | Periodicidad | Plazo |
|---|---|---|---|
| **03** [verificar] | Planilla de retenciones del ISR sobre salarios | Mensual | Dentro de los primeros días del mes siguiente [verificar] |
| **Retención a no residentes** [verificar] | Retención del ISR sobre pagos al exterior (servicios, regalías) gravados de fuente panameña | Según pago | Al momento del pago / mes siguiente [verificar] |
| **Retención sobre dividendos** [verificar] | 10% acciones nominativas / 5% al portador o de zona libre; complementario | Según distribución | [verificar] |

### Impuesto sobre la Renta (ISR)

| Formulario | Descripción | Periodicidad | Plazo |
|---|---|---|---|
| **1** [verificar] | Declaración jurada de rentas (personas jurídicas y naturales) | Anual | Hasta el 31 de marzo siguiente al cierre del período; prórroga de hasta 1 mes [verificar] |
| **Estimada / CAIR** [verificar] | Impuesto estimado del período siguiente; Cálculo Alternativo del ISR si los ingresos gravables superan 1.500.000 B/. [verificar] | Anual / cuotas | Junto con la declaración jurada [verificar] |

### Otros tributos habituales

| Formulario | Descripción | Periodicidad | Plazo |
|---|---|---|---|
| **Tasa única** [verificar] | Tasa única anual de sociedades anónimas y fundaciones de interés privado | Anual | Según fecha de inscripción en el Registro Público [verificar] |
| **Aviso de operación** [verificar] | Impuesto anual sobre el aviso de operación de empresa | Anual | [verificar] |
| **Impuesto de inmuebles** [verificar] | Sobre bienes inmuebles, tasa progresiva | Trimestral / anual | [verificar] |
| **Planilla CSS** [verificar] | Cuota obrero-patronal de la Caja de Seguro Social (incluye décimo tercer mes) | Mensual | [verificar] |

---

## Regímenes de zona especial

Si la entidad opera bajo un régimen especial, las obligaciones y exenciones varían sustancialmente:

| Régimen | Norma | Tratamiento fiscal típico |
|---|---|---|
| **SEM (Sede de Empresa Multinacional)** | Ley 41 de 2007 | Tarifa reducida del ISR sobre servicios a partes del grupo; exenciones de ITBMS en ciertos servicios al exterior [verificar] |
| **Ciudad del Saber** | Ley respectiva [verificar] | Exención de ISR e ITBMS sobre actividades autorizadas [verificar] |
| **Zona Libre de Colón** | Régimen de la ZLC [verificar] | Renta de reexportación tratada como de fuente extranjera (no gravada); operaciones internas sujetas [verificar] |
| **Panamá Pacífico** | Ley 41 de 2004 | Incentivos de ISR, ITBMS y otros para actividades elegibles [verificar] |

**Recordatorio de territorialidad:** la renta de fuente extranjera no tributa en Panamá. Verificar siempre la fuente de la renta antes de incluir una obligación.

---

## Recargos e intereses por presentación tardía

| Concepto | Tratamiento |
|---|---|
| Recargo por presentación tardía | [verificar — porcentaje sobre el impuesto causado] |
| Intereses moratorios | [verificar — sobre el saldo insoluto] |
| Multa por no presentación / morosidad | [verificar] |

> Los porcentajes y plazos exactos deben confirmarse contra el Código Fiscal y las resoluciones vigentes de la DGI. [verificar]

---

## Formato de salida

```markdown
# Calendario fiscal — [Período]

**Entidad:** [nombre]
**Tipo:** [S.A. / S. de R.L. / persona natural / régimen de zona especial]
**Régimen ITBMS:** [contribuyente ordinario / agente de retención / no obligado]
**Fecha de generación:** [fecha]

---

## Obligaciones del período

| # | Formulario | Descripción | Plazo | Estado | Notas |
|---|---|---|---|---|---|
| 1 | 430 | ITBMS mensual | 15/07/2026 | Pendiente | |
| 2 | 03 | Planilla retenciones ISR | 15/07/2026 | Pendiente | |
| 3 | 1 | Declaración jurada ISR | 31/03/2026 | Presentado | |
| ... | ... | ... | ... | ... | ... |

---

## Próximos vencimientos (7 días)

[Lista de formularios con plazo en los próximos 7 días — si los hay]

---

## Vencidos sin presentar

[Lista de formularios cuyo plazo ha pasado y no consta presentación — si los hay]
```

---

## Legislación de referencia

- **Código Fiscal de Panamá** — régimen del ISR, ITBMS y obligaciones formales [verificar]
- **Decreto Ejecutivo 170 de 1993** — reglamentación del ISR [verificar]
- **Ley 8 de 2010** — reforma tributaria e ITBMS [verificar]
- **Ley 41 de 2007 (SEM), Ley 41 de 2004 (Panamá Pacífico)** y normas de Ciudad del Saber y ZLC [verificar]
- Resoluciones de la DGI de aprobación de formularios (actualizadas periódicamente)
- Calendario tributario de la DGI (dgi.mef.gob.pa) [verificar]

---

## Lo que este skill NO hace

- No presenta los formularios ante la DGI — genera el calendario y marca los plazos.
- No calcula las cuotas a pagar — para eso, usar `/fiscal:revision`.
- No sustituye la consulta al calendario oficial de la DGI — se basa en él pero debe verificarse.
