---
name: acceso
description: >
  Preparación para el ejercicio de la abogacía en Panamá (idoneidad ante la Corte Suprema
  de Justicia) mediante práctica integral de conocimientos. Formato: test multiopción +
  caso práctico. Materias: civil, penal, administrativo, laboral, comercial, procesal,
  ética profesional. Se adapta a las áreas débiles del estudiante. Usar cuando el usuario
  dice "idoneidad", "ejercicio de la abogacía", "preparo la abogacía", "test de repaso
  general", o está consolidando conocimientos para la práctica profesional.
argument-hint: "[materia específica o 'simulacro completo'] [área débil si la conoce]"
---

# /acceso

1. Leer `~/.claude/plugins/config/claude-para-abogados/estudiante-derecho/CLAUDE.md` — perfil del estudiante.
2. Determinar la materia o modalidad de práctica.
3. Generar el ejercicio adaptado.

---

## Propósito

Preparar al estudiante para el ejercicio de la abogacía en Panamá con práctica realista de conocimientos: preguntas tipo test y casos prácticos que consolidan las materias clave de la práctica profesional. Se adapta a las áreas débiles del estudiante para maximizar la eficiencia del estudio.

> **Nota sobre la idoneidad en Panamá:** el certificado de idoneidad para ejercer la abogacía lo expide la Corte Suprema de Justicia conforme a la legislación que regula la profesión [verificar]. Los requisitos y el formato de cualquier evaluación los fija la CSJ; este skill es una herramienta de repaso integral, no una réplica de un examen oficial concreto. Verificar siempre los requisitos vigentes con la CSJ.

## Estructura de la práctica de repaso

*Estructura propuesta por este skill para el repaso integral — no es un formato oficial.*

| Parte | Formato | Contenido | Duración sugerida |
|---|---|---|---|
| Test | Preguntas multiopción (4 opciones, 1 correcta) | Todas las materias | configurable |
| Caso práctico | Supuesto con preguntas tipo test y desarrollo | 1 área del derecho | configurable |

### Baremo (propuesto para el repaso)

- Respuesta correcta: +1 punto.
- Respuesta incorrecta: -0,33 puntos (para entrenar la gestión del riesgo).
- En blanco: 0 puntos.
- Umbral de referencia: 50% de la puntuación máxima.

## Distribución por materias (orientativa)

| Materia | N.o aprox. de preguntas | Peso |
|---|---|---|
| Civil y comercial | ~25-30 | Alto |
| Penal | ~15-20 | Medio-alto |
| Administrativo (Ley 38 de 2000) | ~15-20 | Medio-alto |
| Laboral y seguridad social (Código de Trabajo / CSS) | ~10-15 | Medio |
| Procesal (Código Judicial) | ~10-15 | Medio |
| Ética y ejercicio profesional | ~5-10 | Bajo-medio |
| Caso práctico | ~10-15 preguntas sobre el caso | Alto |

## Modalidades de práctica

### 1. Test por materia

- El estudiante elige una materia.
- Se generan 10-25 preguntas tipo test de esa materia.
- Nivel de repaso profesional (no nivel de concurso judicial — es más asequible).
- Tras responder: explicación detallada de cada opción.

### 2. Simulacro completo

- 50-100 preguntas de todas las materias (proporcional al examen real).
- Caso práctico incluido.
- Cronometrado si el estudiante quiere.
- Resultado con análisis por materia.

### 3. Refuerzo de áreas débiles

- Si el perfil del estudiante indica áreas débiles, generar preguntas concentradas en esas áreas.
- Dificultad progresiva: empezar con preguntas más asequibles, subir gradualmente.

### 4. Caso práctico

- Supuesto de hechos realista (extensión similar al examen).
- Preguntas tipo test sobre el caso + preguntas de desarrollo corto.
- Materia: civil, penal, administrativo o laboral (según convocatoria).

## Formato de salida (ejemplo: test por materia)

```markdown
## Repaso para el ejercicio de la abogacía — Test: [Materia]

**N.o de preguntas:** [N]
**Tiempo sugerido:** [minutos]
**Baremo:** correcta +1 / incorrecta -0,33 / blanco 0

---

**1.** [Enunciado]

a) [Opción A]
b) [Opción B]
c) [Opción C]
d) [Opción D]

[Repetir]

---

## Soluciones y explicaciones

**1.** Correcta: [letra]
[Explicación de por qué es correcta y por qué las demás no]

[Repetir]

### Resultado

| Materia | Correctas | Incorrectas | Blanco | Puntos |
|---|---|---|---|---|
| [materia] | [N] | [N] | [N] | [puntuación] |

### Análisis

**Fortalezas:** [temas donde acierta]
**Debilidades:** [temas donde falla]
**Recomendación:** [qué repasar]

---

**Qué hacer a continuación:**
1. **Repasar errores** — profundizo en las preguntas falladas con explicaciones.
2. **Refuerzo** — test centrado en tus áreas débiles.
3. **Caso práctico** — practico el caso práctico de [materia].
4. **Simulacro completo** — test de todas las materias.
5. **Otra cosa** — dime qué necesitas.
```

## Guardarraíles

- **Nivel de repaso profesional, no de concurso judicial.** El repaso para la práctica es más asequible que un concurso de la carrera judicial. No generar preguntas de nivel de concurso.
- **Baremo realista.** Aplicar la penalización de -0,33 — el estudiante debe aprender a gestionar las respuestas en blanco.
- **No inventar artículos.** Mejor "el Código Civil de Panamá regula esto en el Título de obligaciones" que inventar un número de artículo que no existe.
- **Adaptar a las áreas débiles.** Si el perfil del estudiante indica que falla en laboral, concentrar esfuerzo ahí.
- **La ética profesional no es relleno.** Muchos estudiantes la ignoran y pierden puntos fáciles. Incluir siempre preguntas de ética profesional.
- **El caso práctico es decisivo.** El razonamiento aplicado se entrena con casos. Dedicar práctica específica.
- **Verificar los requisitos vigentes.** Los requisitos y el formato de la idoneidad los fija la CSJ y pueden cambiar. Advertir al estudiante que confirme los requisitos vigentes ante la Corte Suprema de Justicia [verificar].
