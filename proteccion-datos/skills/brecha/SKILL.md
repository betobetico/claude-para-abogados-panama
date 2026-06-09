---
name: brecha
description: >
  Protocolo de respuesta ante brechas de seguridad de datos personales. Guía el proceso
  desde la detección hasta la notificación a la ANTAI y la comunicación a los titulares
  si hay alto riesgo, conforme a la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021.
  Genera checklist de acciones y plantillas de notificación. Usar cuando el usuario dice
  "brecha de seguridad", "incidente de datos", "notificación ANTAI", "nos han hackeado",
  "fuga de datos", o ante cualquier incidente que afecte a datos personales.
argument-hint: "[descripción del incidente o 'protocolo preventivo']"
---

# /brecha

1. Leer `~/.claude/plugins/config/claude-para-abogados/proteccion-datos/CLAUDE.md` — perfil de práctica.
2. Evaluar el incidente según la tipología y gravedad.
3. Determinar obligaciones de notificación.
4. Generar checklist de acciones y plantillas.

---

## Propósito

Guiar la respuesta inmediata ante una brecha de seguridad de datos personales, asegurando el cumplimiento de los plazos legales para notificar a la ANTAI y la correcta evaluación del riesgo para los titulares.

## URGENCIA: El reloj corre

> **Desde que se tiene conocimiento de la brecha** hay un plazo legal para notificar a la ANTAI si existe riesgo para los derechos de los titulares [verificar el plazo exacto en la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021]. Si se supera el plazo, hay que justificar el retraso. Se entiende por "tener conocimiento" el momento en que el responsable tiene certeza razonable de que se ha producido un incidente de seguridad que afecta a datos personales.

## Paso 1: Detección y contención

| Acción | Responsable | Plazo | Estado |
|---|---|---|---|
| Confirmar que el incidente afecta a datos personales | IT + responsable de protección de datos | Inmediato | [ ] |
| Contener la brecha (aislar sistemas, revocar accesos) | IT | Inmediato | [ ] |
| Documentar: qué ha pasado, cuándo, cómo se detectó | IT + Legal | Primeras horas | [ ] |
| Preservar evidencias (logs, capturas, correos) | IT | Inmediato | [ ] |
| Activar equipo de respuesta a incidentes | Dirección | Inmediato | [ ] |

## Paso 2: Evaluación del riesgo

### Datos afectados

| Factor | Descripción | Impacto |
|---|---|---|
| Tipo de datos | Identificativos / económicos / salud / menores / judiciales | A más sensibilidad, mayor riesgo |
| Volumen | N.o de registros y de titulares afectados | A mayor volumen, mayor riesgo |
| Categorías de titulares | Empleados / clientes / menores / pacientes | Personas vulnerables = mayor riesgo |

### Naturaleza de la brecha

| Tipo | Descripción | Ejemplo |
|---|---|---|
| **Confidencialidad** | Acceso no autorizado o divulgación | Datos expuestos en internet, robo de BBDD |
| **Integridad** | Modificación no autorizada | Alteración de registros médicos |
| **Disponibilidad** | Pérdida de acceso (temporal o permanente) | Ransomware, destrucción de datos sin backup |

### Nivel de riesgo

| Nivel | Criterio | Obligación |
|---|---|---|
| **Sin riesgo** | Datos cifrados, brecha contenida sin acceso efectivo | Documentar internamente [verificar] |
| **Riesgo** | Posible impacto en los derechos del titular | Notificar a la ANTAI en el plazo legal [verificar] |
| **Alto riesgo** | Probable impacto grave: usurpación de identidad, daño reputacional, perjuicio económico significativo | Notificar a la ANTAI + comunicar a los titulares [verificar] |

## Paso 3: Notificación a la ANTAI

### Plazo: el plazo legal desde el conocimiento [verificar]

### Contenido de la notificación [verificar]

| Campo | Contenido |
|---|---|
| Naturaleza de la brecha | Tipo, categorías de datos y de titulares, n.o aproximado |
| Datos de contacto del responsable de protección de datos | Nombre, email, teléfono |
| Consecuencias probables | Descripción de los posibles efectos |
| Medidas adoptadas | Medidas de contención y mitigación |

### Canal: ANTAI

La notificación se realiza a través del canal habilitado por la ANTAI. Se puede hacer una notificación inicial y complementarla después [verificar].

## Paso 4: Comunicación a los titulares

### Solo si hay alto riesgo [verificar]

| Campo | Contenido |
|---|---|
| Lenguaje | Claro y sencillo |
| Naturaleza de la brecha | Qué ha pasado, sin tecnicismos |
| Datos de contacto del responsable de protección de datos | Para más información |
| Consecuencias probables | Qué riesgos tiene para el titular |
| Medidas adoptadas | Qué se ha hecho para solucionar y proteger |
| Recomendaciones | Qué puede hacer el titular (cambiar contraseñas, vigilar cuentas, etc.) |

### Excepciones a la comunicación [verificar]

- Los datos estaban cifrados u otra medida que los haga ininteligibles.
- Se han tomado medidas posteriores que eliminan el alto riesgo.
- Supondría un esfuerzo desproporcionado — en ese caso, comunicación pública.

## Paso 5: Documentación

Toda brecha debe documentarse, con independencia de si se notifica a la ANTAI [verificar]:

- Hechos: qué ocurrió, cuándo, cómo.
- Efectos: qué datos se vieron afectados.
- Medidas correctivas adoptadas.
- Decisión de notificar o no (y justificación si no se notifica).

## Formato de salida

```markdown
URGENTE — GESTIÓN DE BRECHA DE SEGURIDAD — ACCIÓN INMEDIATA REQUERIDA

> **Nota para el revisor**
> - **Plazo de notificación a la ANTAI:** [fecha/hora límite — plazo legal desde el conocimiento] [verificar]
> - **Nivel de riesgo estimado:** [sin riesgo / riesgo / alto riesgo]
> - **Antes de actuar:** confirmar alcance real con IT; validar evaluación de riesgo con el responsable de protección de datos; verificar si aplican obligaciones sectoriales adicionales.

## Brecha de seguridad: [Descripción breve]

### Cronología

| Fecha/hora | Evento |
|---|---|
| [fecha] | Detección del incidente |
| [fecha] | Conocimiento por el responsable |
| [fecha] | **Plazo límite notificación ANTAI** [verificar] |

### Evaluación de riesgo

[Tabla con la evaluación]

### Checklist de acciones

- [ ] Contención del incidente
- [ ] Preservación de evidencias
- [ ] Evaluación de riesgo completada
- [ ] Notificación a la ANTAI (si procede) — plazo: [fecha] [verificar]
- [ ] Comunicación a titulares (si alto riesgo)
- [ ] Documentación interna del incidente
- [ ] Análisis de causa raíz
- [ ] Medidas correctivas implementadas

### Plantilla de notificación a la ANTAI

[Plantilla con los campos exigidos, rellenados con los datos disponibles] [verificar]

### Plantilla de comunicación a titulares (si procede)

[Plantilla en lenguaje claro]

---

**Qué hacer a continuación:**
1. **Notificar a la ANTAI** — ya está la plantilla, hay que presentarla por el canal habilitado.
2. **Comunicar a titulares** — si el riesgo es alto, enviar la comunicación.
3. **Análisis forense** — coordinar con IT el análisis de causa raíz.
4. **Actualizar protocolo** — ajustar medidas de seguridad para prevenir recurrencia.
5. **Otra cosa** — dime qué necesitas.
```

## Referencias legislativas

- **Ley 81 de 2019** — deber de seguridad, notificación de incidentes y comunicación a los titulares [verificar].
- **Decreto Ejecutivo 285 de 2021** — reglamento; procedimiento y plazos de notificación de brechas [verificar].
- **Guías de la ANTAI** para la gestión y notificación de incidentes de seguridad.

## Guardarraíles

- **El plazo cuenta desde el CONOCIMIENTO, no desde el incidente.** No vale alegar desconocimiento si la brecha se debió detectar antes [verificar].
- **En caso de duda sobre si notificar, notificar.** Es mejor notificar una brecha que resulte menor que no notificar una que resulte grave.
- **No minimizar el riesgo para evitar notificar.** La ANTAI puede sancionar tanto la falta de notificación como la evaluación de riesgo negligente [verificar].
- **Obligaciones sectoriales adicionales.** Según el sector (telecomunicaciones, banca, salud), puede haber obligaciones adicionales de notificación a otros reguladores (SBP, ASEP, MINSA, etc.) [verificar].
- **No borrar evidencias.** La contención no puede destruir los logs y pruebas necesarios para el análisis forense.
- **Este skill gestiona la respuesta jurídica.** La respuesta técnica (contención, análisis forense) es competencia de IT/ciberseguridad.
