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

## Pendiente (mejoras futuras)

- [ ] **Verificar manualmente cada cita marcada `[verificar]`** contra la fuente oficial
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
