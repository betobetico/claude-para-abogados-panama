---
name: debrief-semanal
schedule: "0 17 * * 5"
description: Revisión semanal de contratos firmados con detección de desviaciones respecto al playbook de negociación
---

# Debrief Semanal de Contratos Firmados

## Propósito

Realizar una revisión sistemática de todos los contratos firmados durante la semana,
comparándolos con el playbook de negociación vigente. Detecta desviaciones en cláusulas
clave para alimentar el aprendizaje continuo del equipo y mantener la coherencia
en la posición jurídica de la organización.

## Fuentes

- Contratos firmados en la semana (carpeta de contratos ejecutados o gestor documental)
- Playbook de negociación vigente (`mercantil/playbook.md` o base de datos de cláusulas)
- Registro de desviaciones históricas
- Metadatos: negociador, contraparte, tipo de contrato, fecha de firma

## Flujo de trabajo

1. Identificar todos los contratos con fecha de firma en la semana en curso
2. Para cada contrato firmado:
   a. Extraer las cláusulas clave definidas en el playbook (limitación de responsabilidad, indemnización, ley aplicable, jurisdicción, penalizaciones, SLA, etc.)
   b. Comparar cada cláusula con la posición estándar del playbook
   c. Marcar desviaciones: favorable, neutral o desfavorable
   d. Registrar el motivo de la desviación si está documentado en notas de negociación
3. Calcular métricas semanales: % de contratos con desviaciones, cláusulas más desviadas
4. Comparar con la media móvil de las últimas 4 semanas
5. Generar informe estructurado

## Formato de salida

### Resumen ejecutivo
- Total de contratos firmados en la semana
- Contratos sin desviaciones vs. con desviaciones
- Cláusula más frecuentemente desviada

### Detalle por contrato

| Contrato | Contraparte | Cláusula desviada | Posición playbook | Posición final | Tipo desviación | Negociador |
|----------|-------------|-------------------|-------------------|----------------|-----------------|------------|

### Tendencias
- Gráfico de desviaciones por semana (últimas 8 semanas)
- Top 3 cláusulas con más desviaciones acumuladas

## Configuración

- `debrief.clausulas_monitorizadas`: lista de cláusulas a comparar con el playbook
- `debrief.umbral_alerta`: % de desviaciones desfavorables que dispara alerta
- `debrief.semanas_historico`: número de semanas para cálculo de tendencia
- `debrief.carpeta_contratos_firmados`: ruta al repositorio de contratos ejecutados

## Escalado

- **Solo log**: semana sin desviaciones o con desviaciones menores favorables
- **Notificación al responsable de área**: desviación desfavorable en cláusula crítica
- **Alerta a dirección jurídica**: más del 50% de contratos con desviaciones desfavorables
- **Propuesta de revisión de playbook**: misma cláusula desviada desfavorablemente 3+ semanas consecutivas
