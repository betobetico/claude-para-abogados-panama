# Prompt original del proyecto

## Contexto

Proyecto iniciado el 8 de junio de 2026.

Parte de [claude-para-abogados](https://github.com/betobetico/claude-para-abogados) (adaptación al derecho **español**), que a su vez deriva del repositorio original [claude-for-legal](https://github.com/anthropics/claude-for-legal) de [Anthropic](https://www.anthropic.com) (enfocado al derecho estadounidense).

## Prompt inicial

> Quiero hacer una nueva versión de este repo pero para **Abogados Panameños**.
> https://github.com/betobetico/claude-para-abogados

## Objetivo

Adaptar la suite de agentes, skills y conectores legales al **derecho panameño**, manteniendo el castellano y reescribiendo todas las referencias normativas españolas (LSC, BOE, CENDOJ, AEAT, AEPD, OEPM, EUR-Lex…) por sus equivalentes panameños (Ley 32 de 1927, Gaceta Oficial, Órgano Judicial, DGI, ANTAI, DIGERPI, SMV…), y reforzando las áreas características de Panamá: sociedades anónimas y fundaciones de interés privado, régimen fiscal territorial, compliance/antiblanqueo, inmigración, zonas económicas especiales y derecho marítimo.

## Público objetivo

- Despachos de abogados panameños, pequeños y medianos
- Abogados in-house de empresas con operaciones en Panamá
- Firmas de servicios corporativos (constitución de sociedades, fundaciones)
- Startups y fundadores (módulo específico)

## Decisiones clave

- Nombre: **Claude para Abogados (Panamá)**
- Marketplace: `claude-para-abogados-panama`
- 20 módulos heredados de la versión española, reenfocados a Panamá
- Citas concretas dudosas marcadas con `[verificar]` (no hay conector activo a la Gaceta Oficial)
- Publicación: repositorio público con atribución a la adaptación española y al original de Anthropic
- Toda la documentación y skills en español

## Atribución

Cadena de crédito: **Anthropic** (`claude-for-legal`, diseño original) → **adaptación española** (`claude-para-abogados`) → **esta adaptación panameña**. El crédito de la arquitectura de plugins, los patrones de cold-start interview y el concepto de perfiles de práctica corresponde a Anthropic.
