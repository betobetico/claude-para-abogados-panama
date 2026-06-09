---
name: triaje
description: >
  Triaje de tratamiento de datos — decide si un tratamiento necesita EIPD,
  consulta a la ANTAI, o puede proceder directamente. Árbol de decisión
  basado en la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021. Usar cuando el
  usuario pregunte "¿necesito EIPD?", "¿puedo tratar estos datos?", "nuevo
  tratamiento" o "¿qué trámites necesito?".
argument-hint: "[describir el tratamiento que se quiere realizar]"
---

# /triaje

1. Cargar `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md` → criterios de EIPD, proceso, registro de actividades.
2. Recopilar información mínima del tratamiento.
3. Ejecutar el árbol de decisión.
4. Emitir decisión con justificación y siguiente paso.

```
/privacidad:triaje
Queremos usar un algoritmo de scoring para evaluar la solvencia de los
solicitantes de crédito.
```

---

## Propósito

No todo tratamiento requiere una EIPD completa, pero todo tratamiento requiere una evaluación previa de si la EIPD es necesaria. Este skill es el filtro previo: rápido, documentado y con decisión clara sobre el siguiente paso.

---

## Información mínima necesaria

Antes de decidir, necesitar al menos:

1. **¿Qué datos se tratan?** (categorías: identificativos, financieros, salud, biométricos, menores...)
2. **¿A cuántas personas afecta?** (escala: decenas, cientos, miles, millones)
3. **¿Para qué?** (finalidad concreta)
4. **¿Se usa tecnología innovadora?** (IA, biometría, geolocalización sistemática, IoT)
5. **¿Se elaboran perfiles o se toman decisiones automatizadas?**
6. **¿Hay datos de personas vulnerables?** (menores, empleados, pacientes)
7. **¿Hay transferencia internacional?**
8. **¿Hay combinación de conjuntos de datos?**

Si falta información, preguntar antes de decidir.

---

## Árbol de decisión

### Nivel 1: ¿Es un tratamiento de alto riesgo según la Ley 81 de 2019?

Si el tratamiento coincide con un supuesto de alto riesgo definido en la Ley 81 de 2019 y su Decreto Ejecutivo 285 de 2021, la EIPD es **obligatoria**. Pasar directamente a `/privacidad:eipd`. [verificar]

### Nivel 2: ¿Cumple supuestos de alto riesgo (Ley 81 de 2019)? [verificar]

- **Perfilado con efectos jurídicos/significativos** → EIPD obligatoria
- **Datos sensibles a gran escala** → EIPD obligatoria
- **Observación sistemática de zonas públicas a gran escala** → EIPD obligatoria

### Nivel 3: Regla de los dos criterios (criterio internacional orientativo, no vinculante)

Contar cuántos de los 9 criterios de alto riesgo se cumplen:

| # | Criterio | ¿Cumple? |
|---|---|---|
| 1 | Evaluación o scoring (incluido perfilado) | |
| 2 | Toma de decisiones automatizadas con efectos jurídicos o significativos | |
| 3 | Observación sistemática | |
| 4 | Datos sensibles o altamente personales | |
| 5 | Tratamiento a gran escala | |
| 6 | Asociación o combinación de conjuntos de datos | |
| 7 | Datos de personas vulnerables | |
| 8 | Uso innovador de tecnologías | |
| 9 | Tratamiento que impida ejercer derechos o usar un servicio/contrato | |

- **2 o más criterios** → EIPD recomendable (criterio internacional orientativo)
- **1 criterio** → EIPD recomendable pero no obligatoria; documentar la decisión
- **0 criterios** → Puede proceder sin EIPD; documentar el análisis

### Nivel 4: ¿Procede consulta a la ANTAI?

Si la EIPD concluye que el riesgo residual es alto tras las medidas de mitigación → puede ser exigible una **consulta a la ANTAI** conforme a la Ley 81 de 2019 [verificar].

---

## Formato de salida

```markdown
# Triaje de tratamiento

**Tratamiento:** [nombre/descripción breve]
**Fecha:** [fecha]

---

## Decisión

| Resultado | Decisión |
|---|---|
| **¿EIPD obligatoria?** | [Sí / No / Recomendable] |
| **¿Consulta a la ANTAI?** | [Pendiente de EIPD / No procede / Posiblemente exigible] |
| **¿Puede proceder?** | [Sí / Sí con condiciones / No hasta completar EIPD] |

---

## Justificación

**Supuesto de alto riesgo (Ley 81 de 2019):** [Coincide con supuesto X / No coincide] [verificar]
**Criterios de alto riesgo cumplidos:** [N] de 9 — [listar cuáles]

---

## Siguiente paso

[Una de las tres opciones:]
1. **Proceder** — documentar este triaje en el RAT y proceder con el tratamiento.
2. **Realizar EIPD** — ejecutar `/privacidad:eipd` con la información recopilada.
3. **Consulta a la ANTAI** — preparar documentación para la ANTAI conforme a la Ley 81 de 2019 [verificar].
```

---

## Legislación de referencia

- Ley 81 de 2019 — evaluación de impacto y supuestos de alto riesgo [verificar]
- Decreto Ejecutivo 285 de 2021 — reglamento de la Ley 81 de 2019 [verificar]
- Guías y resoluciones de la ANTAI sobre evaluaciones de impacto
- Referencia comparada (no vinculante en Panamá): directrices del CEPD (WP248 rev.01) sobre criterios de alto riesgo, como criterio internacional orientativo

---

## Lo que este skill NO hace

- No realiza la EIPD completa — para eso, usar `/privacidad:eipd`.
- No sustituye el criterio del encargado de protección de datos — la decisión final es suya.
- No tramita la consulta ante la ANTAI — indica cuándo puede ser necesaria.
