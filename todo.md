# Claude para Abogados (Panamá) — Tareas

## Fase 1 — Adaptación desde la versión española ✅

- [x] Partir de la estructura de `claude-para-abogados` (20 módulos, 100 skills, 17 agentes)
- [x] Reescribir README.md principal a Panamá (doble atribución)
- [x] Reescribir QUICKSTART.md (marketplace `claude-para-abogados-panama`)
- [x] Reescribir CONNECTORS.md (fuentes panameñas)
- [x] Adaptar CONTRIBUTING.md
- [x] Reescribir prompt.md con el contexto del proyecto panameño

## Fase 2 — Adaptación jurídica de los módulos ✅

- [x] Reescribir referencias normativas españolas → panameñas en los 20 plugins
- [x] plugin.json: descripción y autor "Claude para Abogados (Panamá)"
- [x] CLAUDE.md (perfiles de práctica) reenfocados a Panamá
- [x] SKILL.md y agentes con normativa panameña
- [x] Marcar con `[verificar]` las citas concretas dudosas
- [x] Conectores `.mcp.json` apuntando a fuentes panameñas

## Fase 3 — Sabor panameño ✅

- [x] Societario: sociedades anónimas (Ley 32 de 1927) y fundaciones de interés privado (Ley 25 de 1995)
- [x] Fiscal: principio de territorialidad, ISR, ITBMS, DGI
- [x] Regulatorio: antiblanqueo (Ley 23 de 2015), UAF, sujetos obligados
- [x] Startups: incentivos SEM, Ciudad del Saber, zonas económicas especiales

## Fase 4 — Verificación de citas ✅

- [x] Verificar la **identidad** de las ~45 normas de base con fuentes oficiales → [VERIFICACION.md](VERIFICACION.md)
- [x] Resolver ~513 marcadores `[verificar]` de identidad de ley confirmada
- [x] Corregir normas subrogadas: Ley 31 de 2010 → **Ley 284 de 2022** (PH); Ley 7 de 2014 → **Ley 61 de 2015** (DIP)
- [x] Documentar matices: arbitraje (Ley 131 de 2013), reglamento antiblanqueo (D.E. 35 de 2022)

## Fase 5 — Verificación a fondo por módulo (en curso)

- [x] **administrativo** — verificado artículo por artículo (123 → 53): Ley 38 de 2000 (arts. 41, 156-157, 166-172, 200), Ley 135 de 1943 (arts. 42-A, 42-B, 43-A, 43-B, 73), art. 97 Código Judicial, Texto Único Ley 22 de 2006 (arts. 93, 123, 125). Ver [VERIFICACION.md](VERIFICACION.md) §4.
- [x] **societario** — verificado artículo por artículo (50 → 8): Ley 25 de 1995 (arts. 2, 4, 5, 9, 14, 17), Ley 32 de 1927 (arts. 2, 13), Código Fiscal (arts. 318-A, 710), art. 71 Código de Comercio, Ley 129 de 2020 (beneficiario final), Ley 47 de 2013 (acciones al portador). Corregidos 2 errores de fondo. Ver [VERIFICACION.md](VERIFICACION.md) §4.
- [x] **fiscal** — verificado artículo por artículo (123 → 63): ISR (arts. 694, 698-A, 699, 700, 710, 733, 733-A), ITBMS (art. 1057-V), procedimiento (art. 1238-A, Ley 8 de 2010, Ley 76 de 2019, Ley 70 de 2019), precios de transferencia (arts. 762-A y ss.). Corregido el error de dividendos al portador (20%). Agente `calendario-aeat` → `calendario-dgi`. Ver [VERIFICACION.md](VERIFICACION.md) §4.
- [x] **laboral** — verificado artículo por artículo (111 → 34): Código de Trabajo (arts. 30-31, 54, 74, 77, 78, 106-107, 213, 218, 220, 224, 225, 383), Decreto de Gabinete 221 de 1971 (XIII mes), Ley 51 de 2005 (CSS), Decreto Ley 4 de 1997 (aprendizaje). Insertada la escala del art. 225; corregidos 2 errores de fondo (art. 213 acápites, no competencia postcontractual). Ver [VERIFICACION.md](VERIFICACION.md) §4.
- [x] **procesal** — verificado artículo por artículo (119 → 55): Código Judicial (arts. 507, 509, 511, 512, 626, 665, 1152, 1154, 1173), Código de Trabajo (arts. 915, 925-927), Código Procesal Penal (Ley 63 de 2008), Ley 135 de 1943 (arts. 42-A/42-B). **Hallazgo estructural: nuevo Código Procesal Civil (Ley 402 de 2023) vigente desde 11-oct-2025** — aviso añadido. Ver [VERIFICACION.md](VERIFICACION.md) §4.
- [x] **inmobiliario** — verificado artículo por artículo (100 → 40): Ley 93 de 1973 (art. 13, arrendamientos/MIVIOT), Código Fiscal (art. 701-g ITBI, art. 701 ganancia de capital, art. 1057-V), Código Civil (arras art. 1224, inscripción arts. 1753-1762), Ley 284 de 2022 (mayorías, art. 46 Fondo para Imprevistos), Ley 23 de 2015. Corregidos 2 errores de fondo (arras art. 1224, propietarios ausentes). Ver [VERIFICACION.md](VERIFICACION.md) §4.

- [x] **propiedad-intelectual** — verificado artículo por artículo (56 → 7): Ley 35 de 1996 (arts. 20, 26, 79-80, 109-110, 167-172, 176-177, 205, 207), Ley 64 de 2012, Código de Trabajo (arts. 193-196), Ley 45 de 2007 (art. 124.5), Código Penal (art. 268). Corregidos 5 errores de fondo (Madrid, DNDA, invenciones laborales, competencia desleal, quinquenios). Ver [VERIFICACION.md](VERIFICACION.md) §4.

- [x] **privacidad** y **proteccion-datos** — verificados a fondo (privacidad 36 → 4; proteccion-datos 77 → 20): Ley 81 de 2019 (arts. 4, 6, 8, 13, 15, 16, 31-33, 44) y Decreto Ejecutivo 285 de 2021 (arts. 34-38, 41). Corregidos varios GDPR-ismos (interés legítimo, EIPD obligatoria, consulta previa, escalonado de brechas); brecha 72 horas, multas B/.1.000-10.000. Skill `aepd` → `antai`. Ver [VERIFICACION.md](VERIFICACION.md) §4.

**Verificación a fondo completada en 9 módulos** (administrativo, societario, fiscal, laboral, procesal, inmobiliario, propiedad-intelectual, privacidad, proteccion-datos).

## Pendiente (mejoras futuras)

- [ ] **Confirmar los `[verificar]` restantes** (artículos, plazos, importes) contra el texto vigente de cada ley, módulo por módulo
- [ ] Testear entrevistas iniciales con casos reales
- [ ] Testear skills principales con documentos jurídicos reales
- [ ] Desarrollar conectores MCP a fuentes panameñas
- [ ] Añadir un módulo de **derecho marítimo / registro de naves** (AMP) si hay demanda
- [ ] Añadir un módulo de **inmigración y residencias** (visa de inversionista, jubilado-pensionado)
- [x] Publicar en GitHub (público, con atribución)

### MCPs por desarrollar

| Prioridad | MCP | Fuente |
|---|---|---|
| **Alta** | Gaceta Oficial | Legislación y disposiciones |
| **Alta** | Órgano Judicial | Registro Judicial y jurisprudencia CSJ |
| **Alta** | Registro Público | Sociedades, fundaciones, inmuebles |
| **Alta** | DGI | Calendario y obligaciones tributarias |
| **Alta** | ANTAI | Resoluciones de protección de datos |
| **Media** | SMV | Mercado de valores |
| **Media** | DIGERPI | Marcas y patentes |
| **Media** | UAF | Guías y tipologías antiblanqueo |
| **Media** | MITRADEL | Trabajo y desarrollo laboral |
| **Media** | PanamaCompra | Contratación pública |
| **Baja** | ACODECO | Protección al consumidor |
| **Baja** | ANATI | Catastro |
| **Baja** | AMP | Registro de naves |

## Estadísticas del proyecto

| Concepto | Cantidad |
|---|---|
| Módulos | 20 |
| Skills totales | 100+ |
| Agentes programados | 17 |
| Documentación raíz | 8 archivos |
