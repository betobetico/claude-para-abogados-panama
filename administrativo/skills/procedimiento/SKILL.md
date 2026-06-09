---
name: procedimiento
description: >
  Procedimiento administrativo — guía a través del procedimiento administrativo
  general de la Ley 38 de 2000. Cubre plazos, silencio administrativo y
  recursos administrativos (reconsideración y apelación) con árbol de decisión
  para agotar la vía gubernativa. Usar cuando el usuario diga "me han
  notificado una resolución", "recurso administrativo", "silencio", "plazo
  para recurrir", "procedimiento administrativo".
argument-hint: "[describir la situación administrativa o pegar la notificación]"
---

# /procedimiento

1. Cargar `~/.claude/plugins/config/claude-para-abogados/administrativo/CLAUDE.md` → sector, tipo de administración, historial.
2. Identificar la fase del procedimiento y el tipo de acto.
3. Analizar plazos, opciones de recurso y silencio.
4. Generar informe con árbol de decisión.

```
/administrativo:procedimiento
Hemos solicitado una licencia de actividad hace 4 meses y no hemos recibido
respuesta. ¿Qué podemos hacer?
```

---

## Propósito

El procedimiento administrativo general (Ley 38 de 2000) rige la relación del ciudadano y las empresas con la Administración Pública panameña. Los plazos son estrictos, el silencio administrativo tiene efectos jurídicos concretos y elegir mal el recurso puede cerrar vías. Este skill guía cada paso del procedimiento y ayuda a agotar correctamente la vía gubernativa antes de acudir a la Sala Tercera de lo Contencioso-Administrativo de la CSJ.

---

## Fases del procedimiento administrativo

### 1. Iniciación (Ley 38 de 2000)

| Tipo | Características |
|---|---|
| **De oficio** | Por iniciativa del funcionario competente, denuncia o solicitud de otra entidad [verificar] |
| **A petición del interesado** | Petición conforme al derecho de petición (art. 41 de la Constitución); corrección/subsanación en el plazo señalado si está incompleta [verificar] |

### 2. Instrucción (Ley 38 de 2000)

Alegaciones, práctica de pruebas, informes y derecho a ser oído del interesado, con vista del expediente [verificar].

### 3. Resolución (Ley 38 de 2000)

**Plazo máximo para resolver y notificar:** El que establezca la norma reguladora del procedimiento. En su defecto, el plazo general de la Ley 38 de 2000 [verificar].

**Obligación de decidir** — la Administración está obligada a resolver expresamente y a notificar la decisión en los procedimientos (principio de obligatoriedad) [verificar].

---

## Silencio administrativo (Ley 38 de 2000)

A diferencia de España, en Panamá la **regla general es el silencio administrativo NEGATIVO**: transcurrido el plazo para resolver sin decisión expresa, la petición o recurso se entiende DENEGADO, lo que habilita al interesado para acudir a la siguiente vía (recurso o jurisdicción contenciosa) [verificar].

| Regla | Efecto |
|---|---|
| **Regla general** | **Silencio negativo** — la petición se entiende denegada por el solo transcurso del plazo [verificar] |
| **Excepciones (silencio positivo)** | Solo cuando una norma especial lo disponga expresamente para un procedimiento concreto [verificar] |

> El silencio negativo no exime a la Administración de su deber de resolver expresamente; opera como una ficción que permite al interesado impugnar.

---

## Recursos administrativos — vía gubernativa (Ley 38 de 2000)

### Árbol de decisión

```
¿Contra qué acto se recurre?
│
├── Acto del funcionario que lo dictó (cabe revisión por él mismo)
│   └── RECURSO DE RECONSIDERACIÓN (Ley 38 de 2000) [verificar]
│       ├── Plazo: 5 días hábiles desde la notificación [verificar]
│       ├── Ante: el mismo funcionario que dictó el acto
│       └── Si se desestima y hay superior → cabe apelación
│
├── Acto recurrible ante el superior jerárquico
│   └── RECURSO DE APELACIÓN (Ley 38 de 2000) [verificar]
│       ├── Plazo: 5 días hábiles desde la notificación [verificar]
│       ├── Ante: el superior jerárquico del funcionario que dictó el acto
│       └── Su resolución AGOTA la vía gubernativa
│
└── Vía gubernativa agotada
    └── DEMANDA CONTENCIOSO-ADMINISTRATIVA ante la Sala Tercera de la CSJ
        └── Plazo: el señalado en el Código Judicial [verificar]
```

> En muchos casos, reconsideración y apelación pueden interponerse de forma conjunta o subsidiaria. Verificar siempre el régimen recursivo de la entidad y norma sectorial [verificar].

### ¿Cuándo se agota la vía gubernativa?

- Cuando se resuelve el recurso de apelación.
- Cuando contra el acto no procede apelación (por carecer de superior jerárquico la autoridad que lo dictó) [verificar].
- Cuando opera el silencio administrativo negativo respecto del recurso interpuesto [verificar].

El agotamiento de la vía gubernativa es presupuesto para acudir a la Sala Tercera de lo Contencioso-Administrativo de la CSJ [verificar].

---

## Plazos clave

| Concepto | Plazo | Base legal |
|---|---|---|
| Resolución del derecho de petición | 30 días [verificar] | Constitución (art. 41) / Ley 38 de 2000 |
| Corrección/subsanación de la petición | Plazo señalado por la entidad [verificar] | Ley 38 de 2000 |
| Recurso de reconsideración | 5 días hábiles desde la notificación [verificar] | Ley 38 de 2000 |
| Recurso de apelación | 5 días hábiles desde la notificación [verificar] | Ley 38 de 2000 |
| Demanda contencioso-administrativa | Plazo del Código Judicial (referido frecuentemente como 2 meses desde notificación/ejecutoria) [verificar] | Código Judicial |

---

## Notificaciones (Ley 38 de 2000)

- La notificación personal del acto es la regla general; cuando no es posible, se acude a notificación por edicto o por otros medios previstos en la Ley 38 de 2000 [verificar].
- Los plazos para recurrir corren a partir de la notificación válida del acto [verificar].
- Verificar siempre la fecha de notificación efectiva, pues de ella depende el cómputo del plazo de impugnación.

---

## Formato de salida

```markdown
# Procedimiento administrativo

**Tipo de acto:** [resolución / silencio / requerimiento / notificación]
**Administración actuante:** [Gobierno Central / entidad autónoma o semiautónoma / municipio]
**Fecha de notificación/silencio:** [fecha]
**Plazo para actuar:** [fecha límite — CRÍTICO]

---

## Situación procesal

[Resumen: en qué fase estamos, qué ha pasado, qué opciones hay]

---

## Plazos

| Concepto | Plazo | Fecha límite | Estado |
|---|---|---|---|
| [Ej., Recurso de reconsideración] | 5 días hábiles [verificar] | [fecha] | Pendiente |

---

## Opciones de recurso

| Opción | Plazo | Ante quién | Ventajas | Inconvenientes |
|---|---|---|---|---|
| Reconsideración | 5 días hábiles [verificar] | Mismo funcionario | Rápido; permite corregir el acto | Revisa quien dictó el acto |
| Apelación | 5 días hábiles [verificar] | Superior jerárquico | Agota la vía gubernativa | Resuelve la propia Administración |
| Contencioso (Sala Tercera CSJ) | Plazo del Código Judicial [verificar] | Sala Tercera de la CSJ | Control judicial independiente | Más lento; instancia única |

---

## Recomendación

[Análisis razonado de la mejor opción]

---

## Silencio administrativo

**¿Ha transcurrido el plazo para resolver?** [Sí/No]
**Efecto del silencio:** [Positivo / Negativo — con base legal]
```

---

## Legislación de referencia

- Ley 38 de 2000 — Procedimiento Administrativo General y Procuraduría de la Administración
- Código Judicial de Panamá — jurisdicción contencioso-administrativa (Sala Tercera de la CSJ)
- Constitución Política de la República de Panamá — derecho de petición (art. 41) y control de legalidad de los actos administrativos

---

## Lo que este skill NO hace

- No redacta el recurso administrativo — identifica la vía y la estrategia.
- No presenta escritos ante la Administración — genera el análisis para decisión.
- No cubre procedimientos sectoriales con regulación propia (tributario ante la DGI, contratación pública, migratorio) — remite al skill correspondiente.
