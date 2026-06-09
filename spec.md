# Claude para Abogados (Panamá) — Especificación del Proyecto

## Objetivo

Adaptar al **derecho panameño** la suite de agentes legales [claude-para-abogados](https://github.com/betobetico/claude-para-abogados) (versión española), que deriva de [claude-for-legal](https://github.com/anthropics/claude-for-legal) de Anthropic. El resultado es un conjunto de agentes legales especializados que cubren las principales ramas del derecho en la República de Panamá.

## Público objetivo

- **Despachos de abogados** panameños, pequeños y medianos
- **Abogados in-house** de empresas con operaciones en Panamá
- **Firmas de servicios corporativos** (constitución de sociedades y fundaciones)
- **Startups** (módulo específico con enfoque práctico)

## Decisiones de diseño

- Idioma: español en todo (UI, prompts, skills, documentación)
- Nivel de profundidad inicial: ligero (playbooks básicos), iterando después
- Estructura: misma arquitectura de plugins que el repo original
- Legislación: referenciada con nombre completo y artículos; citas dudosas marcadas con `[verificar]`

---

## Módulos (20)

| # | Módulo | Legislación clave panameña |
|---|--------|----------------------------|
| 1 | **societario** | Ley 32 de 1927 (sociedades anónimas), Ley 25 de 1995 (fundaciones de interés privado), Código de Comercio, Registro Público, SMV |
| 2 | **mercantil** | Código de Comercio de Panamá, Código Civil (obligaciones y contratos) |
| 3 | **laboral** | Código de Trabajo, MITRADEL, CSS, décimo tercer mes, prima de antigüedad |
| 4 | **propiedad-intelectual** | Ley 35 de 1996 (propiedad industrial), Ley 64 de 2012 (derecho de autor), DIGERPI |
| 5 | **procesal** | Código Judicial, Órgano Judicial, CSJ |
| 6 | **privacidad** | Ley 81 de 2019, Decreto Ejecutivo 285 de 2021, ANTAI |
| 7 | **consumo** | Ley 45 de 2007 (protección al consumidor), ACODECO |
| 8 | **regulatorio** | Gaceta Oficial, antiblanqueo Ley 23 de 2015, UAF, Superintendencia de Bancos, SMV |
| 9 | **gobernanza-ia** | Marcos internacionales de referencia (sin ley de IA vinculante en Panamá) |
| 10 | **fiscal** | Código Fiscal, principio de territorialidad, ISR, ITBMS, DGI |
| 11 | **administrativo** | Ley 38 de 2000 (procedimiento administrativo), Sala Tercera de la CSJ |
| 12 | **inmobiliario** | Registro Público, Ley 31 de 2010 (propiedad horizontal), ANATI |
| 13 | **concursal** | Ley 12 de 2016 (proceso concursal de insolvencia) |
| 14 | **familia** | Código de la Familia de Panamá |
| 15 | **proteccion-datos** | Ley 81 de 2019, ANTAI (enfoque operativo) |
| 16 | **startups** | Constitución de sociedades, SMV, incentivos (SEM, Ciudad del Saber), inmigración |
| 17 | **clinica-juridica** | Acceso a la justicia, asistencia pro bono, Órgano Judicial |
| 18 | **estudiante-derecho** | Grado en Derecho, examen de idoneidad profesional |
| 19 | **hub-constructor** | Sin contenido jurídico — descubrimiento de skills |
| 20 | **recetas-agentes** | Sin contenido jurídico — cookbooks de agentes |

---

## Fases de ejecución

### Fase 1 — Adaptación desde la versión española
- Partir de los 20 módulos, 100 skills y 17 agentes de `claude-para-abogados`
- Reescribir la infraestructura común (README, QUICKSTART, CONNECTORS, CONTRIBUTING)

### Fase 2 — Adaptación jurídica
- Reescribir referencias normativas españolas → panameñas en cada plugin
- Adaptar plugin.json, CLAUDE.md, SKILL.md y agentes
- Marcar con `[verificar]` las citas concretas dudosas

### Fase 3 — Sabor panameño
- Reforzar sociedades/fundaciones, fiscalidad territorial, antiblanqueo e incentivos

### Fase 4 — Verificación y publicación
- Verificar marcadores `[verificar]`, testear, publicar en GitHub con atribución

---

## Notas

- El módulo de **privacidad** se enfoca en cumplimiento normativo y contratos de tratamiento
- El módulo de **protección de datos** se enfoca en operativa diaria: brechas, evaluaciones de impacto, registro de actividades, relación con la ANTAI
- El módulo de **startups** cruza transversalmente societario, fiscal y laboral con enfoque práctico para fundadores
- Las áreas más características de Panamá (sociedades anónimas, fundaciones de interés privado, fiscalidad territorial, antiblanqueo, zonas económicas especiales) reciben énfasis especial
