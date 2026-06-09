---
name: vigilante-renovaciones
schedule: "0 9 * * 1"
description: Escanea el registro de contratos para detectar fechas de cancelación y renovación próximas en 30, 60 y 90 días
---

# Vigilante de Renovaciones Contractuales

## Propósito

Monitorizar de forma proactiva el registro de contratos mercantiles para identificar
aquellos cuyas fechas de vencimiento, cancelación o renovación automática se aproximan.
Permite al equipo jurídico actuar con antelación suficiente, evitando renovaciones
no deseadas o pérdidas de plazo para renegociar condiciones.

## Fuentes

- Registro de contratos mercantiles (base de datos o hoja de cálculo centralizada)
- Campo `fecha_fin` o `fecha_renovacion` de cada contrato
- Campo `preaviso_cancelacion` (días de antelación requeridos para resolver)
- Campo `renovacion_automatica` (booleano)
- Metadatos: contraparte, tipo de contrato, valor económico, responsable interno

## Flujo de trabajo

1. Cargar el registro completo de contratos activos
2. Calcular los días restantes hasta cada fecha relevante (vencimiento, renovación, preaviso)
3. Clasificar por urgencia:
   - **Rojo** (≤30 días): acción inmediata requerida
   - **Ámbar** (31-60 días): planificación necesaria
   - **Verde** (61-90 días): seguimiento informativo
4. Filtrar contratos sin fecha de vencimiento o con duración indefinida (excluir del informe)
5. Ordenar la tabla resultante por días restantes (ascendente)
6. Generar el informe en formato tabla con columnas estandarizadas
7. Si hay contratos en rojo, marcar el informe como urgente

## Formato de salida

Tabla con las siguientes columnas:

| Contrato | Contraparte | Tipo | Fecha límite | Días restantes | Urgencia | Responsable | Acción sugerida |
|----------|-------------|------|--------------|----------------|----------|-------------|-----------------|

- Urgencia codificada por color: 🔴 🟠 🟢
- Resumen ejecutivo al inicio con totales por nivel de urgencia
- Nota al pie con contratos de renovación automática cuyo preaviso ya venció

## Configuración

- `renovaciones.umbral_rojo`: 30 (días)
- `renovaciones.umbral_ambar`: 60 (días)
- `renovaciones.umbral_verde`: 90 (días)
- `renovaciones.excluir_tipos`: lista de tipos de contrato a ignorar
- `renovaciones.responsable_defecto`: persona a notificar si no hay responsable asignado

## Escalado

- **Alerta inmediata al responsable**: contrato en rojo con renovación automática cuyo preaviso vence esta semana
- **Notificación al equipo**: cualquier contrato que pase de ámbar a rojo desde la última ejecución
- **Solo log**: contratos en verde sin cambios respecto a la semana anterior
- **Escalado a dirección jurídica**: contrato de valor superior al umbral configurado en rojo
