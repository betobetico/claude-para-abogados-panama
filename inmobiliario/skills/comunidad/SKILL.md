---
name: comunidad
description: >
  Propiedad horizontal — revisa reglamento de copropiedad, actas de asamblea y
  cuotas extraordinarias de propiedades horizontales bajo la Ley 284 de 2022.
  Comprueba quórums y mayorías de asamblea, impugnación de acuerdos y obligaciones
  de propietarios. Usar cuando el usuario diga "propiedad horizontal", "asamblea
  de propietarios", "cuota extraordinaria", "impugnar acuerdo", "Ley 31",
  "PH" o adjunte actas/reglamento de copropiedad.
argument-hint: "[adjuntar acta/reglamento o describir la situación]"
---

# /comunidad

1. Cargar `~/.claude/plugins/config/claude-para-abogados/inmobiliario/CLAUDE.md` → tipo de práctica, posición habitual.
2. Obtener el documento (acta, reglamento de copropiedad, convocatoria) o descripción.
3. Analizar contra la Ley 284 de 2022.
4. Generar informe con hallazgos.

```
/inmobiliario:comunidad
La PH aprobó una cuota extraordinaria de 50.000 USD para instalar ascensor.
Votaron a favor el 60% de los coeficientes. ¿Es válido el acuerdo?
```

---

## Propósito

La Ley 284 de 2022 regula el régimen de propiedad horizontal en Panamá: constitución, reglamento de copropiedad, asamblea de propietarios, administración, cuotas y resolución de conflictos. Los conflictos en propiedades horizontales son frecuentes y muchos acuerdos se impugnan por defectos formales (convocatoria, quórum) o sustantivos (contenido contrario a la ley o al reglamento). Este skill revisa la validez de acuerdos, analiza el reglamento de copropiedad y evalúa la viabilidad de impugnaciones.

> **Nota de verificación:** Los quórums, mayorías y plazos exactos de la Ley 284 de 2022 deben verificarse en el texto vigente de la ley y su reglamentación antes de citar artículos concretos. [verificar]

---

## Quórums y mayorías de adopción de acuerdos (Ley 284 de 2022)

> Las mayorías concretas (simple, calificada, unanimidad) y los coeficientes exigidos según la materia se establecen en la Ley 284 de 2022 y en el reglamento de copropiedad de cada PH. Verificar el texto vigente. [verificar]

### Unanimidad

Habitualmente exigida para [verificar]:
- Modificación del reglamento de copropiedad o del título constitutivo de la PH
- Cambio de destino de bienes comunes
- Constitución de servidumbres o derechos reales sobre bienes comunes

### Mayorías calificadas

| Acuerdo | Quórum / mayoría | Base legal |
|---|---|---|
| **Obras o mejoras sobre bienes comunes no exigibles por ley** | Mayoría calificada de coeficientes [verificar] | Ley 284 de 2022 |
| **Obras de accesibilidad / supresión de barreras** | Según la ley aplicable [verificar] | Ley 284 de 2022 |
| **Modificación de cuotas o coeficientes** | Mayoría calificada / unanimidad [verificar] | Ley 284 de 2022 |

### Mayoría simple

Para los asuntos ordinarios de administración no reservados a mayoría calificada o unanimidad: mayoría de propietarios que representen la mayoría de los coeficientes de participación presentes/representados, conforme al reglamento y a la ley. [verificar]

### Obras de conservación obligatorias

Las obras necesarias para la conservación, seguridad y habitabilidad del edificio son obligatorias y corresponden a la PH conforme a la Ley 284 de 2022, aun sin necesidad de aprobación discrecional de la asamblea cuando son urgentes. [verificar]

---

## Impugnación de acuerdos de asamblea

### Causas de impugnación

| Causa |
|---|
| Acuerdos contrarios a la Ley 284 de 2022 o a su reglamentación |
| Acuerdos contrarios al reglamento de copropiedad |
| Acuerdos gravemente lesivos para la PH en beneficio de uno o varios propietarios |
| Acuerdos que causen grave perjuicio a un propietario sin obligación de soportarlo / abuso de derecho |

### Legitimación

- Propietarios que votaron en contra y dejaron constancia de su voto en el acta
- Propietarios ausentes que manifiesten su discrepancia dentro del plazo legal [verificar]
- Propietarios indebidamente privados de su derecho de voto

### Plazos de impugnación

| Aspecto | Plazo |
|---|---|
| Impugnación de acuerdos de asamblea | Plazo establecido en la Ley 284 de 2022 |

### Requisito: estar al corriente de pago

Para ejercer ciertos derechos (incluido a veces el voto y la impugnación), el propietario debe estar al corriente en el pago de las cuotas de la PH, o consignar lo adeudado. Verificar el alcance en la Ley 284 de 2022.

---

## Cuotas y gastos extraordinarios

| Aspecto | Norma |
|---|---|
| **Obligación de contribuir** | Según el coeficiente de participación, salvo regla distinta del reglamento de copropiedad (Ley 284 de 2022) |
| **Fondo de reserva / imprevistos** | Conforme a la Ley 284 de 2022 y al reglamento [verificar] |
| **Cuotas extraordinarias** | Aprobadas por la asamblea con la mayoría que corresponda a la materia [verificar] |
| **Morosos** | Cobro de cuotas mediante el procedimiento que establezca la Ley 284 de 2022 (vía ejecutiva / jurisdicción de PH) y posible gravamen sobre la unidad [verificar] |

---

## Revisión de actas de asamblea

### Requisitos formales del acta

- [ ] Fecha, hora y lugar de la asamblea
- [ ] Indicación de si es primera o segunda convocatoria
- [ ] Identificación del convocante / administrador
- [ ] Lista de asistentes y representados (con coeficientes)
- [ ] Orden del día
- [ ] Acuerdos adoptados con indicación de votos a favor, en contra y abstenciones
- [ ] Firma de quien preside y del secretario
- [ ] Notificación a los propietarios ausentes (en plazo) [verificar]

### Defectos habituales que invalidan acuerdos

| Defecto | Consecuencia |
|---|---|
| Convocatoria defectuosa (falta de orden del día, plazo insuficiente) | Acuerdo impugnable |
| Quórum / mayoría insuficiente | Acuerdo nulo o impugnable |
| Acuerdo sobre asunto no incluido en el orden del día | Impugnable (salvo asamblea con presencia total) |
| Acta no notificada a ausentes | Los ausentes pueden alegar indefensión |

---

## Formato de salida

```markdown
# Revisión de propiedad horizontal

**PH:** [dirección / nombre del edificio o conjunto]
**Documento revisado:** [acta / reglamento de copropiedad / convocatoria / cuota extraordinaria]
**Fecha del documento:** [fecha]

---

## Hallazgos

| # | Aspecto | Observación | Riesgo | Base legal | Recomendación |
|---|---|---|---|---|---|
| 1 | [Ej., Quórum de la cuota] | [60% de coeficientes para instalación de ascensor] | [Verificar] | Ley 284 de 2022 | [Confirmar mayoría exigida] |
| 2 | [Ej., Notificación a ausentes] | [No consta notificación] | Alto | Ley 284 de 2022 | [Notificar en plazo] |
| ... | ... | ... | ... | ... | ... |

---

## Viabilidad de impugnación (si procede)

| Aspecto | Evaluación |
|---|---|
| **Causa de impugnación** | [contraria a ley / reglamento / lesiva] |
| **Legitimación** | [¿Votó en contra? ¿Ausente? ¿Al corriente de pago?] |
| **Plazo** | [plazo de la Ley 284 de 2022 — verificar] |
| **Viabilidad** | [Alta / Media / Baja] |

---

## Recomendaciones

[Acciones concretas a tomar]
```

---

## Legislación de referencia

- Ley 284 de 2022 — Régimen de propiedad horizontal en Panamá (y su reglamentación)
- Código Civil de Panamá — copropiedad / comunidad de bienes (supletorio) [verificar]
- Código Judicial de Panamá — vía procesal para el cobro de cuotas e impugnaciones [verificar]

---

## Lo que este skill NO hace

- No redacta el reglamento de copropiedad — revisa los existentes.
- No tramita la impugnación judicial — evalúa la viabilidad y los plazos.
- No gestiona el cobro de la morosidad — indica el procedimiento aplicable bajo la Ley 284 de 2022.
