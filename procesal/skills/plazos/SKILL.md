---
name: calculadora-plazos
description: "Calcula términos procesales en días hábiles según el Código Judicial de Panamá, considerando días feriados y de duelo nacional"
argument-hint: "<tipo-proceso> <fecha-notificación> [jurisdicción]"
---

## Propósito

Esta skill calcula términos procesales en el orden jurisdiccional civil, laboral, contencioso-administrativo y penal de Panamá. Aplica las reglas de cómputo del Código Judicial de Panamá: días hábiles, exclusión de sábados, domingos y días feriados o de duelo nacional, y reglas especiales por jurisdicción [verificar].

## Instrucciones

### Paso 1 — Recopilar datos de entrada

1. **Tipo de proceso**: ordinario, sumario, oral, ejecutivo, laboral, contencioso, penal.
2. **Fecha de notificación**: fecha en que se recibe la comunicación.
3. **Jurisdicción**: civil, laboral, contencioso-administrativo, penal.
4. **Provincia/distrito judicial**: para identificar días feriados locales o de duelo.
5. **Acción procesal**: contestación, recurso, oposición, etc.

### Paso 2 — Identificar término aplicable

**Jurisdicción civil (Código Judicial de Panamá):** [verificar]

| Acción | Término | Base legal |
|--------|---------|------------|
| Contestación demanda (proceso ordinario) | [n] días [verificar] | Código Judicial [verificar] |
| Contestación (proceso sumario/oral) | [n] días [verificar] | Código Judicial [verificar] |
| Recurso de reconsideración | [n] días [verificar] | Código Judicial [verificar] |
| Recurso de apelación (anuncio/sustentación) | [n] días [verificar] | Código Judicial [verificar] |
| Oposición en proceso ejecutivo | [n] días [verificar] | Código Judicial [verificar] |
| Recurso de casación (ante la CSJ) | [n] días [verificar] | Código Judicial [verificar] |
| Recurso de hecho | [n] días [verificar] | Código Judicial [verificar] |

**Jurisdicción laboral (Código de Trabajo de Panamá):** [verificar]

| Acción | Término | Base legal |
|--------|---------|------------|
| Recurso de apelación laboral | [n] días [verificar] | Código de Trabajo [verificar] |
| Recurso de casación laboral (ante la CSJ) | [n] días [verificar] | Código de Trabajo [verificar] |
| Conciliación previa | Según convocatoria del MITRADEL [verificar] | Código de Trabajo [verificar] |

**Jurisdicción contencioso-administrativa (Sala Tercera de la CSJ):** [verificar]

| Acción | Término | Base legal |
|--------|---------|------------|
| Demanda contencioso-administrativa de plena jurisdicción | [n] meses [verificar] | Código Judicial / Ley 135 de 1943 [verificar] |
| Demanda de nulidad | Sin término de caducidad [verificar] | Código Judicial [verificar] |

### Paso 3 — Aplicar reglas de cómputo

1. **Dies a quo**: el día de la notificación NO cuenta [verificar].
2. **Días hábiles**: se excluyen sábados, domingos y días feriados o de duelo nacional [verificar].
3. **No hay vacancia judicial general** equivalente al agosto inhábil español; los términos corren salvo declaratoria de feriado o duelo nacional. Verificar el calendario oficial del Órgano Judicial [verificar].
4. **Jurisdicción penal**: verificar el régimen de días hábiles aplicable bajo el Sistema Penal Acusatorio [verificar].
5. **Si el último día es inhábil**: se prorroga al siguiente día hábil [verificar].
6. **Hora límite de presentación**: hasta el cierre del despacho judicial del último día del término, o según el sistema de notificaciones del Órgano Judicial [verificar].

### Paso 4 — Calcular y presentar resultado

## Formato de salida

```markdown
## Cálculo de término procesal

### Datos de entrada

| Concepto | Valor |
|----------|-------|
| Proceso | [tipo] |
| Jurisdicción | [civil/laboral/contencioso/penal] |
| Acción procesal | [tipo] |
| Fecha de notificación | [fecha] |
| Término aplicable | [n] días [hábiles/calendario] |
| Base legal | [artículo del Código Judicial — verificar] |

### Cómputo

- Dies a quo (no cuenta): [fecha notificación]
- Primer día del cómputo: [fecha]
- Días inhábiles en el período: [lista de fechas con motivo]
- Feriado o duelo nacional en el período: [SÍ/NO — motivo]
- Último día del término: [fecha]
- Si cae en inhábil, prórroga a: [fecha]

### Resultado

| Fecha límite | Hora límite | Forma |
|--------------|-------------|-------|
| **[fecha]** | Hasta el cierre del despacho judicial del [fecha] [verificar] | Tribunal / sistema de notificaciones del Órgano Judicial |

### Advertencias

- [Verificar días feriados o de duelo nacional en [provincia/distrito] no incluidos en este cálculo]
- [Este cálculo es orientativo — verificar con el calendario oficial del Órgano Judicial]
```

## Referencias normativas

- **Código Judicial de Panamá**: días y horas hábiles [verificar].
- **Código Judicial de Panamá**: habilitación de días y horas [verificar].
- **Código Judicial de Panamá**: términos procesales y su carácter improrrogable [verificar].
- **Código Judicial de Panamá**: cómputo de los términos [verificar].
- **Código Judicial de Panamá**: presentación de escritos y hora límite [verificar].
- **Código de Trabajo de Panamá**: términos en la jurisdicción laboral [verificar].
- **Código Judicial / Ley 135 de 1943**: términos en lo contencioso-administrativo (Sala Tercera de la CSJ) [verificar].

## Guardrails

- **NO** garantiza la exactitud del cómputo — es orientativo y debe verificarse.
- **NO** tiene acceso al calendario oficial del Órgano Judicial ni a los días feriados o de duelo nacional declarados.
- **NO** presenta escritos ni gestiona términos en el sistema de notificaciones del Órgano Judicial.
- **AVISAR** siempre: "Este cálculo es orientativo. Verifique con el calendario oficial del Órgano Judicial."
- **AVISAR** si el término puede verse afectado por días feriados o de duelo nacional y hay duda.
- **ESCALAR** si el término vence en menos de 3 días hábiles.
- **ESCALAR** si hay duda sobre la habilidad de un día para el caso concreto.
