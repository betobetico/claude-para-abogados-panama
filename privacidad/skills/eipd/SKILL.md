---
name: eipd
description: >
  Generador de Evaluación de Impacto en Protección de Datos (EIPD) — genera
  una EIPD en el formato house configurado. Evalúa si es obligatoria según la
  Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021, estructura el análisis de
  riesgos y propone medidas de mitigación. Usar cuando se plantee un nuevo
  tratamiento de datos, un cambio sustancial en uno existente, o el usuario diga
  "necesito una EIPD", "evaluación de impacto" o "¿hay que hacer EIPD?".
argument-hint: "[describir el tratamiento o adjuntar la ficha del RAT]"
---

# /eipd

1. Cargar `~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md` → formato house de EIPD, proceso, criterios.
2. Determinar si la EIPD es obligatoria (si hay duda, usar `/privacidad:triaje` primero).
3. Recopilar información del tratamiento (preguntar lo que falte).
4. Generar la EIPD en el formato configurado.
5. Evaluar si procede consulta a la ANTAI por riesgo residual alto (Ley 81 de 2019).

```
/privacidad:eipd
Queremos implementar un sistema de reconocimiento facial para control de acceso
en las oficinas.
```

---

## Propósito

La EIPD es obligatoria cuando un tratamiento entraña alto riesgo para los derechos del titular. Es el documento más completo del programa de responsabilidad demostrada en protección de datos y debe realizarse **antes** de iniciar el tratamiento. Este skill genera la EIPD completa siguiendo la Ley 81 de 2019 y su Decreto Ejecutivo 285 de 2021.

---

## Cuándo es obligatoria la EIPD

### Supuestos de alto riesgo (Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021)

- Evaluación sistemática y exhaustiva de aspectos personales basada en tratamiento automatizado, incluida la **elaboración de perfiles**, con efectos jurídicos o significativos
- Tratamiento a **gran escala** de datos sensibles
- **Observación sistemática** a gran escala de una zona de acceso público

### Tratamientos de alto riesgo a considerar

Como criterio orientativo, suelen requerir una evaluación de impacto, entre otros:
- Perfilado (evaluación o predicción de aspectos personales)
- Toma de decisiones automatizadas con efectos jurídicos
- Observación, geolocalización o control del titular de forma sistemática
- Tratamiento de datos sensibles o de naturaleza muy personal
- Tratamiento de datos a gran escala
- Asociación o combinación de conjuntos de datos
- Datos de sujetos vulnerables (menores, empleados, pacientes)
- Uso innovador de tecnologías
- Transferencias internacionales a países sin nivel adecuado de protección
- Tratamientos que impidan ejercer derechos o acceder a un servicio/contrato

**Regla de los dos criterios:** Si el tratamiento cumple dos o más de estos criterios de alto riesgo, generalmente conviene realizar la evaluación de impacto. (Criterio internacional orientativo, no vinculante en Panamá.) [verificar]

---

## Estructura de la EIPD (Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021)

### 1. Descripción sistemática del tratamiento

| Campo | Contenido |
|---|---|
| **Actividad de tratamiento** | [nombre del tratamiento] |
| **Responsable** | [identificación] |
| **Encargados** | [lista de encargados involucrados] |
| **Finalidad** | [propósito específico y concreto] |
| **Base de licitud** | [Ley 81 de 2019 — cuál y por qué] |
| **Categorías de datos** | [qué datos se tratan] |
| **Categorías de titulares** | [a quién afecta] |
| **Fuentes de datos** | [cómo se recogen] |
| **Flujo de datos** | [dónde se almacenan, quién accede, transferencias] |
| **Plazo de conservación** | [criterios o plazos concretos] |
| **Tecnología utilizada** | [sistemas, algoritmos, proveedores] |

### 2. Necesidad y proporcionalidad

- ¿El tratamiento es **necesario** para la finalidad declarada? ¿Hay alternativas menos intrusivas?
- ¿Los datos recogidos son **proporcionales** a la finalidad? ¿Se aplica el principio de minimización (Ley 81 de 2019)?
- ¿La base de licitud es **adecuada** y está correctamente identificada?
- ¿Se informa a los titulares (deber de información de la Ley 81 de 2019)?
- ¿Se garantizan los derechos del titular (acceso, rectificación, cancelación/supresión, oposición, portabilidad)?
- ¿Existe mecanismo de limitación de conservación?

### 3. Identificación y evaluación de riesgos

Para cada riesgo identificado:

| Riesgo | Descripción | Probabilidad | Impacto | Nivel | Derechos afectados |
|---|---|---|---|---|---|
| [Ej., Acceso no autorizado] | [Detalle] | [Alta/Media/Baja] | [Alto/Medio/Bajo] | [Valor] | [Arts. afectados] |
| [Ej., Discriminación por perfilado] | [Detalle] | | | | |
| [Ej., Pérdida de datos] | [Detalle] | | | | |

Categorías de riesgo a evaluar:
- Acceso ilegítimo a datos
- Modificación no autorizada
- Pérdida de datos
- Discriminación
- Usurpación de identidad
- Pérdida de confidencialidad
- Limitación de derechos
- Perjuicio económico o social

### 4. Medidas de mitigación

Para cada riesgo identificado, proponer medidas concretas:

| Riesgo | Medida propuesta | Tipo | Riesgo residual |
|---|---|---|---|
| [Riesgo] | [Medida técnica u organizativa] | [Técnica/Organizativa] | [Alto/Medio/Bajo] |

Medidas habituales:
- **Técnicas:** cifrado, seudonimización, control de acceso, logs de auditoría, backups
- **Organizativas:** formación, políticas internas, contratos de confidencialidad, auditorías periódicas, encargado de protección de datos designado

---

## Evaluación de riesgo residual y consulta previa

Si tras aplicar las medidas de mitigación el **riesgo residual sigue siendo alto**, puede ser exigible una **consulta a la ANTAI** antes de iniciar el tratamiento, conforme a la Ley 81 de 2019 y su reglamento [verificar].

La consulta debe incluir: responsabilidades del responsable y encargado, fines y medios del tratamiento, medidas para proteger los derechos del titular, datos de contacto del encargado de protección de datos, y la propia EIPD.

El plazo de respuesta de la ANTAI debe verificarse en la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021.

---

## Formato de salida

```markdown
# Evaluación de Impacto en Protección de Datos (EIPD)

**Tratamiento:** [nombre]
**Responsable:** [empresa]
**Fecha:** [fecha]
**Versión:** [número]
**Autor:** [nombre / equipo]
**Encargado de protección de datos consultado:** [Sí/No — fecha]

---

## 1. Descripción del tratamiento
[Tabla descriptiva completa]

## 2. Necesidad y proporcionalidad
[Análisis punto por punto]

## 3. Riesgos identificados
[Tabla de riesgos con probabilidad, impacto y nivel]

## 4. Medidas de mitigación
[Tabla de medidas con riesgo residual]

## 5. Conclusión
[Riesgo residual global: alto/medio/bajo]
[¿Procede consulta a la ANTAI? Sí/No — justificación]

## 6. Plan de acción
| Medida | Responsable | Plazo | Estado |
|---|---|---|---|
```

---

## Legislación de referencia

- Ley 81 de 2019 — evaluación de impacto en protección de datos [verificar]
- Decreto Ejecutivo 285 de 2021 — reglamento de la Ley 81 de 2019
- Guías y resoluciones de la ANTAI sobre evaluaciones de impacto
- Referencia comparada (no vinculante en Panamá): directrices del CEPD (WP248 rev.01) sobre EIPD, como criterio internacional orientativo

---

## Lo que este skill NO hace

- No sustituye el juicio del encargado de protección de datos — la EIPD requiere su valoración.
- No realiza la consulta a la ANTAI — señala cuándo puede ser necesaria.
- No evalúa medidas de seguridad técnicas en detalle — eso es responsabilidad del equipo de seguridad.
