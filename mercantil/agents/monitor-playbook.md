---
name: monitor-playbook
schedule: "0 9 1-7 * 1"
description: Analiza el registro de desviaciones y propone actualizaciones al playbook de negociación cuando detecta patrones recurrentes
---

# Monitor del Playbook de Negociación

## Propósito

Identificar patrones recurrentes en las desviaciones registradas respecto al playbook
de negociación mercantil. Cuando una posición estándar se desvía consistentemente,
el agente propone una actualización formal del playbook, evitando que las posiciones
queden desactualizadas respecto a la práctica real de negociación.

## Fuentes

- Registro de desviaciones acumulado (generado por `debrief-semanal`)
- Playbook de negociación vigente (`mercantil/playbook.md`)
- Histórico de versiones del playbook
- Informes de debrief semanal de los últimos 3 meses
- Notas de negociación con motivos de desviación

## Flujo de trabajo

1. Cargar todas las desviaciones registradas en el último mes (o trimestre, según configuración)
2. Agrupar desviaciones por cláusula y tipo (favorable / neutral / desfavorable)
3. Para cada cláusula con desviaciones recurrentes:
   a. Calcular frecuencia de desviación (% de contratos que la desvían)
   b. Identificar la posición final más habitual (moda)
   c. Analizar si la tendencia es estable o creciente
   d. Revisar los motivos documentados
4. Filtrar cláusulas que superan el umbral de recurrencia configurado
5. Para cada cláusula candidata, redactar propuesta de actualización:
   - Posición actual del playbook
   - Posición propuesta (basada en la práctica real)
   - Justificación con datos (frecuencia, tendencia, motivos)
   - Impacto estimado en futuras negociaciones
6. Priorizar propuestas por impacto y frecuencia

## Formato de salida

### Resumen de actividad
- Total de desviaciones analizadas en el período
- Cláusulas con patrón detectado

### Propuestas de actualización

Para cada propuesta:

| Campo | Contenido |
|-------|-----------|
| Cláusula | Nombre de la cláusula |
| Posición actual | Texto vigente en el playbook |
| Posición propuesta | Nueva redacción sugerida |
| Frecuencia de desviación | X% de contratos en el período |
| Tendencia | Estable / Creciente / Decreciente |
| Motivos principales | Listado de razones documentadas |
| Prioridad | Alta / Media / Baja |

## Configuración

- `monitor_playbook.umbral_recurrencia`: % mínimo de desviación para proponer cambio (defecto: 40%)
- `monitor_playbook.periodo_analisis`: meses a analizar (defecto: 3)
- `monitor_playbook.min_contratos`: mínimo de contratos para que la muestra sea significativa
- `monitor_playbook.clausulas_intocables`: cláusulas que nunca se proponen para cambio

## Escalado

- **Solo log**: no se detectan patrones que superen el umbral
- **Informe a responsable de área**: 1-2 propuestas de prioridad media
- **Reunión de revisión de playbook**: 3+ propuestas o cualquiera de prioridad alta
- **Alerta a dirección jurídica**: propuesta que afecta a cláusula de limitación de responsabilidad o indemnización
