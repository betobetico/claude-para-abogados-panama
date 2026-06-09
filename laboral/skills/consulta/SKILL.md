---
name: consulta-laboral
description: "Responde consultas rápidas de derecho laboral con referencia a artículos del Código de Trabajo y convención colectiva"
argument-hint: "<pregunta-laboral>"
---

## Propósito

Esta skill proporciona respuestas rápidas y estructuradas a consultas de derecho laboral panameño. Siempre referencia el artículo del Código de Trabajo aplicable y, cuando es relevante, señala si la respuesta depende de la convención colectiva específica.

## Instrucciones

### Paso 1 — Analizar la consulta

1. Identificar el tema: contratación, jornada, vacaciones, licencias y permisos, salario, décimo tercer mes, prima de antigüedad, terminación, Caja de Seguro Social, riesgos profesionales, derechos colectivos, teletrabajo, no discriminación.
2. Determinar si la respuesta depende de la convención colectiva aplicable.
3. Verificar si hay normativa especial aplicable (ley o decreto específico).

### Paso 2 — Buscar la base legal

Orden de fuentes:

1. **Constitución Política de Panamá** — derechos laborales fundamentales [verificar].
2. **Código de Trabajo de Panamá** — norma principal.
3. **Leyes y decretos especiales**: régimen del décimo tercer mes [verificar], Ley 126 de 2020 (teletrabajo) [verificar], Ley Orgánica de la CSS [verificar], normativa de riesgos profesionales [verificar].
4. **Convención colectiva**: mejoras sobre los mínimos legales.
5. **Jurisprudencia de la Corte Suprema de Justicia**: cuando la interpretación no sea pacífica [verificar].

### Paso 3 — Estructurar la respuesta

1. Respuesta directa a la pregunta.
2. Base legal con artículo concreto.
3. Matices o excepciones importantes.
4. Indicación de si la convención colectiva puede mejorar la regulación legal.

### Paso 4 — Evaluar completitud

- Si la respuesta requiere conocer la convención colectiva y no está en la configuración, indicarlo expresamente.
- Si la pregunta tiene múltiples respuestas posibles según la casuística, presentar todas las opciones.

## Formato de salida

```markdown
## Consulta laboral

**Pregunta:** [pregunta del usuario]

### Respuesta

[Respuesta directa, concisa y precisa]

### Base legal

| Norma | Artículo | Contenido relevante |
|-------|----------|---------------------|
| Código de Trabajo | Art. [X] [verificar] | [extracto relevante] |
| [otra norma] | Art. [X] [verificar] | [extracto relevante] |

### Matices y excepciones

- [Matiz 1]
- [Matiz 2]

### Dependencia de la convención colectiva

[Indicar si la convención puede modificar/mejorar la regulación legal y en qué sentido]

### Referencias adicionales

- [Jurisprudencia relevante de la Corte Suprema de Justicia si la hay]
- [Criterio de MITRADEL si aplica]
```

## Temas frecuentes — Referencia rápida

| Tema | Código de Trabajo | Normativa especial |
|------|-------------------|-------------------|
| Período de prueba | Art. [X] [verificar] | Convención colectiva |
| Jornada y sobretiempo | Art. [X] [verificar] | Jornada máxima legal |
| Vacaciones | Art. [X] [verificar] | 30 días por cada 11 meses de trabajo continuo [verificar] |
| Décimo tercer mes | — | Decreto de Gabinete sobre el XIII mes [verificar] |
| Prima de antigüedad | Art. [X] [verificar] | Una semana de salario por año de servicio [verificar] |
| Licencias y permisos | Art. [X] [verificar] | Convención colectiva |
| Maternidad / fuero | Art. [X] [verificar] | Licencia de 14 semanas [verificar] |
| Riesgos profesionales | — | Régimen de riesgos profesionales de la CSS [verificar] |
| Teletrabajo | — | Ley 126 de 2020 |
| Seguridad Social | — | Ley Orgánica de la CSS [verificar] |

## Referencias normativas

- **Código de Trabajo de Panamá**: norma principal del derecho laboral.
- **Ley Orgánica de la CSS** (Ley 51 de 2005): seguridad social.
- **Régimen de riesgos profesionales** administrado por la CSS [verificar].
- **Régimen del décimo tercer mes** — Decreto de Gabinete sobre el XIII mes [verificar].
- **Ley 126 de 2020**: teletrabajo.
- **MITRADEL**: resoluciones, salario mínimo y trámites administrativos laborales.

## Guardrails

- **NO** proporciona asesoramiento jurídico vinculante — es orientación general.
- **NO** interpreta convenciones colectivas específicas salvo que estén cargadas en configuración.
- **NO** sustituye la consulta a un abogado laboralista idóneo en casos complejos.
- **AVISAR** siempre que la respuesta dependa de la convención colectiva y esta no esté disponible.
- **AVISAR** si la pregunta implica un supuesto de hecho que requiere análisis individualizado.
- **ESCALAR** si la consulta involucra derechos fundamentales (discriminación, libertad sindical, intimidad).
