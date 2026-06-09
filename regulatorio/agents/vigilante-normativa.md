---
name: vigilante-normativa
schedule: "0 7 * * *"
description: Rastreo diario de la Gaceta Oficial de Panamá y de los acuerdos de la SBP, la SMV y la UAF para detectar cambios normativos relevantes filtrados por sector
---

# Vigilante Normativo

## Propósito

Rastrear diariamente las publicaciones oficiales (Gaceta Oficial de Panamá y acuerdos,
circulares y guías de los supervisores configurados) para identificar cambios normativos
relevantes para la organización. Filtra por sector, materia y palabras clave, generando un
digest que permite al equipo jurídico y al oficial de cumplimiento mantenerse actualizado
sin revisar manualmente cada publicación.

## Fuentes

- Gaceta Oficial de Panamá (leyes, decretos ejecutivos, resoluciones)
- Acuerdos y circulares de la Superintendencia de Bancos de Panamá (SBP)
- Acuerdos y opiniones de la Superintendencia del Mercado de Valores (SMV)
- Guías, tipologías y avisos de la Unidad de Análisis Financiero (UAF)
- Base de datos de filtros por sector y materia
- Registro de módulos del sistema (mercantil, laboral, fiscal, etc.)
- Histórico de alertas normativas previas

## Flujo de trabajo

1. Consultar las publicaciones del día en cada fuente configurada
2. Para cada publicación:
   a. Extraer metadatos: título, rango normativo, órgano emisor, fecha, referencia
   b. Clasificar por materia: prevención de blanqueo (KYC/PEP), bancario, valores, seguros,
      mercantil, laboral, fiscal, societario, protección de datos, regulatorio, procesal,
      propiedad intelectual, etc.
   c. Aplicar filtros de relevancia por sector (palabras clave, actividad económica, materias)
   d. Evaluar nivel de impacto: alto, medio, bajo
   e. Vincular con el módulo del sistema correspondiente
3. Descartar publicaciones que no superan los filtros de relevancia
4. Para las publicaciones relevantes, generar resumen ejecutivo de cada una
5. Agrupar por módulo y ordenar por impacto
6. Generar el digest diario

## Formato de salida

### Digest normativo — [Fecha]

**Publicaciones relevantes: X** (Alto impacto: X | Medio: X | Bajo: X)

Para cada norma relevante:

| Campo | Contenido |
|-------|-----------|
| Norma | Título completo |
| Rango | Ley / Decreto Ley / Decreto Ejecutivo / Acuerdo / Resolución / Circular / Guía |
| Fuente | Gaceta Oficial / SBP / SMV / UAF / otro supervisor |
| Referencia | Número de Gaceta o de acuerdo / código de publicación |
| Módulo afectado | Mercantil / Laboral / Fiscal / etc. |
| Impacto | Alto / Medio / Bajo |
| Resumen | 2-3 líneas con los puntos clave |
| Acción sugerida | Revisar, adaptar procedimiento, informar a cliente, etc. |

### Sin novedades
Si no hay publicaciones relevantes, indicar: "Sin novedades normativas relevantes hoy."

## Configuración

- `normativa.fuentes`: lista de fuentes a rastrear (defecto: Gaceta Oficial + acuerdos SBP/SMV + guías UAF)
- `normativa.supervisores`: supervisores cuyos acuerdos y circulares incluir
- `normativa.filtros_sector`: palabras clave y actividad económica por sector
- `normativa.filtros_materia`: materias jurídicas de interés
- `normativa.excluir_rangos`: rangos normativos a excluir (ej: anuncios, nombramientos)
- `normativa.modulos`: mapeo de materias a módulos del sistema

## Escalado

- **Solo log**: día sin publicaciones relevantes o solo de impacto bajo
- **Digest estándar**: publicaciones de impacto medio (flujo normal)
- **Alerta al módulo afectado**: publicación de alto impacto para un área específica
- **Alerta general al equipo jurídico**: nueva ley o reforma significativa que afecta a varios módulos
