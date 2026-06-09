---
name: tracker-comentarios
schedule: "0 9 * * 1"
description: Rastrea períodos abiertos de consultas públicas previas e información pública relevantes para la organización
---

# Tracker de Consultas Públicas

## Propósito

Monitorizar los procesos de participación pública y consulta abiertos por las
administraciones y supervisores panameños que sean relevantes para los sectores de
actividad de la organización. Permite al equipo jurídico y al oficial de cumplimiento
identificar oportunidades de participación en la elaboración normativa mediante consultas
públicas, períodos de comentarios sobre proyectos de acuerdo y audiencias.

## Fuentes

- Gaceta Oficial de Panamá (proyectos de ley y normas en consulta)
- Asamblea Nacional de Panamá (proyectos de ley en trámite) [verificar]
- Períodos de comentarios sobre proyectos de acuerdo de la SBP y de la SMV
- Guías y consultas de la UAF
- Portales de ANTAI, ACODECO y otros reguladores sectoriales
- Registro histórico de consultas participadas

## Flujo de trabajo

1. Rastrear los portales configurados en busca de consultas públicas abiertas
2. Para cada consulta detectada:
   a. Extraer metadatos: título, órgano promotor, fecha apertura, fecha cierre, enlace
   b. Clasificar por materia y sector
   c. Aplicar filtros de relevancia (sector de actividad, materias de interés)
   d. Calcular días restantes para presentar comentarios
   e. Evaluar prioridad: impacto potencial en la organización
3. Verificar si la consulta ya fue identificada en ejecuciones anteriores
4. Para consultas nuevas, generar ficha de oportunidad de participación
5. Actualizar el estado de consultas previamente identificadas
6. Alertar sobre consultas con plazo próximo a vencer

## Formato de salida

### Consultas públicas abiertas

| Consulta | Órgano promotor | Materia | Fecha apertura | Fecha cierre | Días restantes | Prioridad | Estado |
|----------|-----------------|---------|----------------|--------------|----------------|-----------|--------|

- Estados: 🆕 Nueva | ⏳ En plazo | ✍️ En preparación | ✅ Presentada | ❌ Descartada

### Consultas con plazo próximo (≤14 días)

| Consulta | Cierre | Días restantes | Responsable | Borrador preparado |
|----------|--------|----------------|-------------|-------------------|

### Resumen semanal
- Consultas nuevas detectadas: X
- Consultas abiertas totales: X
- Consultas con plazo ≤14 días: X
- Comentarios presentados este mes: X

## Configuración

- `consultas.portales`: lista de portales a rastrear
- `consultas.sectores_interes`: sectores de actividad relevantes
- `consultas.materias_interes`: materias jurídicas de interés
- `consultas.alerta_plazo_dias`: días de antelación para alerta (defecto: 14)
- `consultas.responsable_defecto`: persona a asignar si no hay responsable

## Escalado

- **Solo log**: semana sin consultas nuevas relevantes
- **Notificación al equipo regulatorio**: consulta nueva de prioridad media
- **Alerta con solicitud de decisión**: consulta de alta prioridad que requiere decisión de participar
- **Escalado urgente**: consulta relevante con menos de 7 días de plazo detectada por primera vez
