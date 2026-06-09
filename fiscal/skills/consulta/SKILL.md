---
name: consulta
description: >
  Consulta tributaria rápida — responde preguntas fiscales bajo el principio
  de territorialidad panameño, con referencia al Código Fiscal y a los
  criterios y resoluciones de la DGI cuando existan. Marca cuando la respuesta
  depende de interpretación o jurisprudencia pendiente. Usar cuando el usuario
  pregunte "¿cómo tributa...?", "¿puedo deducir...?", "consulta fiscal",
  "ITBMS de...", "retención de...", "¿es renta de fuente extranjera?".
argument-hint: "[describir la cuestión tributaria]"
---

# /consulta

1. Cargar `~/.claude/plugins/config/claude-para-abogados/fiscal/CLAUDE.md` → tipo de entidad, régimen fiscal, sector, régimen de zona especial.
2. Recibir la consulta.
3. Analizar contra la normativa vigente.
4. Determinar la **fuente de la renta** (panameña vs extranjera): clave bajo el principio de territorialidad.
5. Buscar criterios o resoluciones de la DGI relevantes.
6. Emitir respuesta con citas.

```
/fiscal:consulta
¿Cómo tributa la venta de un local comercial por una sociedad a un particular?
¿ITBMS o no?
```

---

## Propósito

Las consultas tributarias del día a día necesitan respuestas rápidas, fundamentadas y con las citas correctas. Este skill responde citando siempre la norma aplicable del Código Fiscal (o ley especial) y, cuando existe, el criterio o resolución de la DGI que soporta la interpretación. Marca explícitamente cuando la respuesta depende de interpretación o hay jurisprudencia contradictoria. **Antes de nada, determina si la renta es de fuente panameña** — la renta de fuente extranjera no tributa en Panamá.

---

## Estructura de la respuesta

Toda respuesta incluye obligatoriamente:

1. **Respuesta directa** — 2-4 frases claras con la conclusión
2. **Fuente de la renta** — si aplica, indicar si es de fuente panameña (gravada) o extranjera (no gravada)
3. **Norma aplicable** — siempre citar el artículo concreto del Código Fiscal o ley especial (ISR, ITBMS, dividendos, CAIR, etc.) [verificar]
4. **Criterio DGI** — si existe una resolución, nota o criterio de la DGI que respalde la posición, citarlo con fecha y referencia
5. **Jurisprudencia** — si hay fallos relevantes del Tribunal Administrativo Tributario (TAT), la Sala Tercera de la CSJ o la Corte Suprema de Justicia
6. **Alertas** — marcar explícitamente cuando:
   - La respuesta depende de una interpretación discutible → `[interpretación — verificar]`
   - Hay jurisprudencia contradictoria → `[jurisprudencia dividida — verificar]`
   - Hay un cambio normativo reciente o pendiente → `[cambio normativo — verificar]`
   - La DGI ha cambiado de criterio → `[cambio de criterio DGI — verificar]`

---

## Áreas cubiertas

| Área | Normativa principal |
|---|---|
| ISR — principio de territorialidad | Código Fiscal; Decreto Ejecutivo 170 de 1993 [verificar] |
| ITBMS | Código Fiscal; Ley 8 de 2010 [verificar] |
| Dividendos y complementario | Código Fiscal [verificar] |
| CAIR (Cálculo Alternativo del ISR) | Código Fiscal [verificar] |
| Retenciones (salarios, no residentes, dividendos) | Código Fiscal [verificar] |
| Precios de transferencia | Código Fiscal; normativa de PT (informe 930) [verificar] |
| Regímenes de zona especial | Ley 41 de 2007 (SEM); Ley 41 de 2004 (Panamá Pacífico); normas de Ciudad del Saber y ZLC [verificar] |
| Procedimientos tributarios | Código Fiscal; Ley 38 de 2000; Ley 8 de 2010 (TAT) [verificar] |
| Tributos municipales | Régimen municipal aplicable [verificar] |

---

## Criterios y consultas de la DGI

Las resoluciones, notas y criterios de la DGI son la interpretación oficial de la Administración tributaria. Al citarlos:
- Referencia completa: tipo de acto, número y fecha
- Indicar si es criterio consolidado o ha habido cambio de criterio
- Recordar que NO son vinculantes para los tribunales (TAT, Sala Tercera de la CSJ)
- Si no existe criterio aplicable, indicarlo expresamente

---

## Formato de salida

```markdown
# Consulta tributaria

**Pregunta:** [la pregunta del usuario]
**Fecha:** [fecha]

---

## Respuesta

[2-4 frases con la conclusión clara]

---

## Fuente de la renta

[Panameña (gravada) / Extranjera (no gravada) / No aplica — solo cuando sea pertinente bajo territorialidad]

---

## Fundamento

**Normativa:**
- [Código Fiscal / ley especial] art. [X]: [contenido relevante] [verificar]
- [Norma] art. [Y]: [si hay más de una norma aplicable]

**Criterios DGI:**
- [Resolución/nota DGI] de [fecha]: [resumen de la conclusión]
- [Si no hay criterio aplicable: "No se ha localizado criterio de la DGI directamente aplicable"]

**Jurisprudencia:**
- [Si existe: fallo del TAT / Sala Tercera CSJ de [fecha], expediente [número]: resumen]
- [Si no: "Sin jurisprudencia relevante identificada"]

---

## Alertas

[Si aplica alguna de las marcas de verificación, incluirlas aquí.
Si no: "Sin alertas."]

---

## Ejemplo práctico

[Si ayuda a la comprensión: un ejemplo numérico concreto en B/. / USD]
```

---

## Legislación de referencia

- **Código Fiscal de Panamá** — régimen del ISR, ITBMS, dividendos, procedimientos [verificar]
- **Decreto Ejecutivo 170 de 1993** — reglamentación del ISR [verificar]
- **Ley 8 de 2010** — reforma tributaria, ITBMS y TAT [verificar]
- **Ley 41 de 2007 (SEM)**, **Ley 41 de 2004 (Panamá Pacífico)** y normas de Ciudad del Saber y ZLC [verificar]
- Base de criterios y resoluciones de la DGI (dgi.mef.gob.pa) [verificar]

---

## Lo que este skill NO hace

- No sustituye una consulta formal ante la DGI — es una orientación profesional.
- No cubre tributos municipales en detalle (solo remite a la normativa municipal cuando aplica).
- No calcula cuotas — para eso, usar `/fiscal:revision` o una herramienta de cálculo.
