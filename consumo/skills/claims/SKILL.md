---
name: claims
description: >
  Checker de claims de marketing — analiza afirmaciones publicitarias de un
  producto o servicio e identifica cuáles necesitan sustanciación, cuáles son
  potencialmente engañosas y cuáles deben eliminarse. Cubre publicidad engañosa,
  comparativa, influencers y prácticas comerciales
  desleales bajo la Ley 45 de 2007. Usar cuando el usuario diga "revisa estos
  claims", "¿podemos decir esto?", "copy del producto" o "publicidad".
argument-hint: "[pegar los claims o adjuntar material publicitario]"
---

# /claims

1. Cargar `~/.claude/plugins/config/claude-para-abogados/consumo/CLAUDE.md` → sector, tolerancia al riesgo, historial de claims.
2. Obtener el material publicitario o los claims.
3. Analizar claim por claim.
4. Generar tabla con clasificación y acción requerida.

```
/consumo:claims
"Nuestro producto es el más vendido de Panamá"
"Ingredientes 100% naturales"
"Resultados garantizados en 30 días"
```

---

## Propósito

Los claims publicitarios son la primera línea de riesgo de consumo. Un claim sin sustanciación es publicidad engañosa bajo la Ley 45 de 2007 [verificar]. Un claim comparativo sin cumplir los requisitos es publicidad ilícita. Un influencer sin etiquetar la publicidad incurre en publicidad encubierta. Este skill revisa cada afirmación y clasifica el riesgo. La autoridad de aplicación es la ACODECO.

---

## Tipos de claims y marco legal

### Publicidad engañosa (Ley 45 de 2007) [verificar]

Es engañosa la publicidad que contenga información falsa o que, siendo veraz, por su contenido o presentación induzca o pueda inducir a error a los consumidores. Se evalúa:
- Existencia, naturaleza y características del producto
- Precio o modo de cálculo
- Servicio posventa y garantía
- Necesidad de servicio o pieza
- Naturaleza, cualificación y derechos del proveedor

### Publicidad comparativa (Ley 45 de 2007) [verificar]

Lícita solo si:
- No es engañosa
- Compara bienes o servicios que satisfacen las mismas necesidades
- Compara objetivamente características esenciales, pertinentes, verificables y representativas
- No desacredita ni denigra al competidor
- No se aprovecha indebidamente de la reputación del competidor
- No presenta el bien como imitación o réplica

### Prácticas comerciales con consumidores

- **Prácticas engañosas por acción** — información falsa o que induce a error [verificar]
- **Prácticas engañosas por omisión** — ocultar información sustancial [verificar]
- **Prácticas abusivas o agresivas** — coacción, acoso, influencia indebida [verificar]

### Influencers y publicidad encubierta

- Toda publicidad debe ser identificable como tal (Ley 45 de 2007) [verificar]
- El influencer debe etiquetar el contenido patrocinado de forma clara y visible
- Buenas prácticas de identificación de publicidad en redes sociales

---

## Análisis claim por claim

Para cada claim, evaluar:

| Campo | Pregunta |
|---|---|
| **Literalidad** | ¿Qué dice exactamente el claim? |
| **Tipo** | ¿Es objetivo (verificable) o subjetivo (opinión)? |
| **Sustanciación** | ¿Tiene respaldo documental/científico? |
| **Veracidad** | ¿Es verdad? ¿Puede demostrarse? |
| **Impresión global** | ¿Qué entiende el consumidor medio? |
| **Superlativos** | ¿Usa "el mejor", "el más", "el único"? → Necesita prueba |
| **Comparación** | ¿Compara con competidores? → Requisitos de publicidad comparativa (Ley 45 de 2007) [verificar] |
| **Salud/medio ambiente** | ¿Alega beneficios de salud o sostenibilidad? → Normativa sectorial |

---

## Clasificación de claims

| Clasificación | Significado | Acción |
|---|---|---|
| **CONFORME** | Claim veraz, sustanciado y lícito | Mantener |
| **MODIFICAR** | Necesita ajuste de redacción para evitar inducir a error | Reformular |
| **SUSTANCIAR** | Claim plausible pero sin documentación de respaldo | Aportar prueba o retirar |
| **RETIRAR** | Claim falso, no sustanciable o contrario a norma | Eliminar |

---

## Formato de salida

```markdown
# Revisión de claims: [Producto/Campaña]

**Fecha:** [fecha]
**Material revisado:** [descripción del material]
**Sector:** [alimentación / cosmética / tecnología / servicios / etc.]

---

## Resumen

**Claims revisados:** [N]
**Conformes:** [N] | **Modificar:** [N] | **Sustanciar:** [N] | **Retirar:** [N]

---

## Tabla de claims

| # | Claim | Tipo | Clasificación | Base legal | Acción requerida |
|---|---|---|---|---|---|
| 1 | "El más vendido de Panamá" | Superlativo objetivo | SUSTANCIAR | Ley 45 de 2007 [verificar] | Aportar datos de ventas o reformular a "uno de los más vendidos" |
| 2 | "100% natural" | Objetivo | SUSTANCIAR | Ley 45 de 2007 + normativa sanitaria si alimentación [verificar] | Verificar que todos los ingredientes son naturales; definir "natural" |
| 3 | "Resultados garantizados" | Promesa de resultado | RETIRAR | Ley 45 de 2007 [verificar] | Promesa absoluta de resultado es engañosa si no se puede garantizar |

---

## Recomendaciones generales

[Observaciones transversales sobre el material publicitario]
```

---

## Claims de especial atención

| Tipo de claim | Normativa específica | Requisito |
|---|---|---|
| Alegaciones nutricionales/salud | Normativa sanitaria y de alimentos de Panamá [verificar] | Solo alegaciones autorizadas; base científica |
| Claims medioambientales (greenwashing) | Ley 45 de 2007 [verificar] | Sustanciación específica; sin genéricos ("ecológico", "verde") |
| "Gratis" / "gratuito" | Ley 45 de 2007 [verificar] | Solo si realmente no hay coste para el consumidor |
| Testimonios | Ley 45 de 2007 [verificar] | Deben ser reales y representativos |
| Precios tachados / descuentos | Ley 45 de 2007 [verificar] | El precio anterior anunciado debe ser real y haber estado vigente |

---

## Legislación de referencia

- Ley 45 de 2007 — protección al consumidor y defensa de la competencia (publicidad engañosa, comparativa y prácticas comerciales) [verificar]
- ACODECO — Autoridad de Protección al Consumidor y Defensa de la Competencia
- Normativa sanitaria y de alimentos de Panamá — alegaciones nutricionales y de salud [verificar]
- Referencia comparada internacional (no vinculante): buenas prácticas internacionales contra el greenwashing y sobre precios de referencia

---

## Lo que este skill NO hace

- No valida claims sectoriales regulados (dispositivos médicos, medicamentos, productos financieros) — marca cuándo se necesita especialista.
- No diseña la campaña publicitaria — revisa el material existente.
- No sustituye el criterio de la ACODECO — recomienda cuándo elevar la consulta.
