---
name: procedimiento
description: >
  Triaje de procedimiento tributario — analiza la situación procesal
  tributaria del usuario e identifica el tipo de procedimiento, plazos,
  opciones y estrategia. Cubre: requerimiento de información, fiscalización
  /auditoría, liquidación adicional, sancionador, recurso de reconsideración,
  apelación ante el Tribunal Administrativo Tributario (TAT) y demanda
  contencioso-administrativa ante la Sala Tercera de la CSJ. Usar cuando el
  usuario diga "me ha llegado una notificación de la DGI", "fiscalización",
  "requerimiento", "multa tributaria", "recurso ante el TAT".
argument-hint: "[describir la situación o pegar la notificación]"
---

# /procedimiento

1. Cargar `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md` → tipo de entidad, historial de procedimientos, asesores.
2. Identificar el tipo de procedimiento.
3. Analizar la situación procesal (plazos, fase, opciones).
4. Generar informe con opciones y estrategia.

```
/fiscal:procedimiento
Hemos recibido una notificación de inicio de fiscalización de la DGI
respecto del ITBMS del período 2024.
```

---

## Propósito

Recibir una notificación de la DGI genera incertidumbre. ¿Qué tipo de procedimiento es? ¿Cuánto tiempo tienen? ¿Qué opciones tengo? ¿Debo recurrir o aceptar? Este skill triaja la situación, identifica plazos y opciones, y propone una estrategia procesal bajo el régimen del Código Fiscal y la Ley 38 de 2000 [verificar].

---

## Tipos de procedimiento tributario

### 1. Requerimiento de información

| Aspecto | Detalle |
|---|---|
| **Qué es** | La DGI solicita documentación o aclaraciones sobre declaraciones presentadas |
| **Plazo de respuesta** | El indicado en el requerimiento [verificar] |
| **Resultado** | Archivo, inicio de fiscalización o resolución de alcance |
| **Recomendación** | Atender en plazo; conservar acuse de recibo |

### 2. Fiscalización / auditoría tributaria

| Aspecto | Detalle |
|---|---|
| **Qué es** | Verificación e investigación de la situación fiscal del contribuyente con acceso a la documentación contable |
| **Inicio** | Notificación de inicio de fiscalización [verificar] |
| **Plazo máximo** | [verificar — plazo de duración del procedimiento conforme al Código Fiscal] |
| **Resultado** | Resolución de alcance (liquidación adicional) o cierre sin ajustes |
| **Recurso** | Reconsideración y apelación ante el TAT [verificar] |

### 3. Resolución de alcance / liquidación adicional

| Aspecto | Detalle |
|---|---|
| **Qué es** | Acto que determina un impuesto adicional, recargos, intereses y/o multa |
| **Notificación** | Personal o por edicto conforme a la Ley 38 de 2000 [verificar] |
| **Recurso** | Reconsideración (ante la DGI) y apelación (ante el TAT) [verificar] |

### 4. Procedimiento sancionador

| Aspecto | Detalle |
|---|---|
| **Qué es** | Imposición de multas por morosidad, omisión, defraudación fiscal u otras infracciones del Código Fiscal [verificar] |
| **Clasificación** | Falta administrativa / defraudación fiscal (puede tener consecuencias penales) [verificar] |
| **Recurso** | Reconsideración y apelación ante el TAT [verificar] |

### 5. Recurso de reconsideración (vía gubernativa)

| Aspecto | Detalle |
|---|---|
| **Órgano** | La propia DGI |
| **Plazo de interposición** | [verificar — 15 días hábiles desde la notificación] |
| **Efecto** | Suspende la ejecución según las reglas aplicables [verificar] |

### 6. Recurso de apelación — Tribunal Administrativo Tributario (TAT)

| Aspecto | Detalle |
|---|---|
| **Órgano** | Tribunal Administrativo Tributario (creado por la Ley 8 de 2010) [verificar] |
| **Plazo de interposición** | [verificar — 15 días hábiles desde la notificación de la resolución de reconsideración] |
| **Resultado** | Agota la vía gubernativa [verificar] |

### 7. Demanda contencioso-administrativa

| Aspecto | Detalle |
|---|---|
| **Órgano** | Sala Tercera de lo Contencioso-Administrativo de la Corte Suprema de Justicia (CSJ) |
| **Plazo** | [verificar — 2 meses desde la notificación que agota la vía gubernativa] |
| **Base normativa** | Ley 38 de 2000; Código Judicial [verificar] |

---

## Árbol de decisión procesal

```
Notificación recibida
├── ¿Qué tipo de acto es?
│   ├── Requerimiento de información → Atender en plazo
│   ├── Inicio de fiscalización → Analizar alcance y plazo
│   ├── Resolución de alcance / liquidación adicional → ¿Recurrir?
│   │   ├── Reconsideración (ante la DGI) [verificar plazo]
│   │   └── Apelación ante el TAT [verificar plazo]
│   ├── Resolución sancionadora → ¿Aceptar y pagar o recurrir?
│   └── Resolución que agota la vía gubernativa → ¿Contencioso ante la Sala Tercera CSJ? [verificar plazo]
```

---

## Formato de salida

```markdown
# Triaje de procedimiento tributario

**Tipo de procedimiento:** [requerimiento / fiscalización / liquidación adicional / sancionador / reconsideración / apelación TAT / contencioso]
**Fecha de notificación:** [fecha]
**Plazo para actuar:** [fecha límite — CRÍTICO]
**Órgano actuante:** [DGI / TAT / Sala Tercera CSJ]

---

## Situación procesal

[Resumen: en qué fase estamos, qué ha pasado, qué viene]

---

## Plazos

| Concepto | Plazo | Fecha límite | Estado |
|---|---|---|---|
| [Ej., Recurso de reconsideración] | [15 días hábiles] [verificar] | [fecha] | [Pendiente] |
| [Ej., Apelación ante el TAT] | [15 días hábiles] [verificar] | [fecha] | [Pendiente] |

---

## Opciones

| Opción | Ventajas | Inconvenientes | Recomendación |
|---|---|---|---|
| 1. [Ej., Aceptar y pagar] | [Evita intereses adicionales] | [Renuncia a recurrir] | [Para importes bajos con poca defensa] |
| 2. [Ej., Reconsideración] | [Mantiene opciones; misma DGI] | [Plazo y posible confirmación] | [Si hay argumentos sólidos] |
| 3. [Ej., Apelación ante el TAT] | [Órgano independiente] | [Plazo largo; garantía si se solicita suspensión] | [Si liquidación > X B/.] |

---

## Estrategia recomendada

[Análisis razonado de la mejor opción según las circunstancias]

---

## Suspensión / garantía

**¿Procede solicitar la suspensión del cobro?** [Sí/No] [verificar]
**Tipo de garantía:** [fianza / depósito / otra] [verificar]
**Garantía necesaria:** [tipo y cuantía estimada]
```

---

## Legislación de referencia

- **Código Fiscal de Panamá** — procedimientos de fiscalización, sancionador y recursos [verificar]
- **Ley 8 de 2010** — creación y competencias del Tribunal Administrativo Tributario (TAT) [verificar]
- **Ley 38 de 2000** — procedimiento administrativo general (notificaciones, recursos, términos)
- **Código Judicial de Panamá** — demanda contencioso-administrativa ante la Sala Tercera de la CSJ [verificar]

---

## Lo que este skill NO hace

- No redacta el escrito de descargos o recurso — identifica la estrategia. Para redacción, indicar que se necesita el escrito.
- No presenta recurso ante ningún órgano — genera el análisis para decisión del profesional.
- No sustituye al abogado tributarista en procedimientos complejos de fiscalización — recomienda cuándo acudir a especialista.
