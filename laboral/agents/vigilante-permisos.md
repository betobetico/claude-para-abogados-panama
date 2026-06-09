---
name: vigilante-permisos
schedule: "0 9 * * 1"
description: Monitoriza permisos, licencias e incapacidades activas, alertando sobre fechas de retorno y acciones pendientes
---

# Vigilante de Permisos y Situaciones Especiales

## Propósito

Mantener un control actualizado de todos los empleados en situación especial:
incapacidad por enfermedad o riesgo profesional, licencias remuneradas o no
remuneradas, permisos, reducciones de jornada y suspensiones del contrato.
Alerta sobre fechas de retorno próximas, vencimientos de períodos máximos y
acciones administrativas pendientes para evitar incumplimientos laborales.

## Fuentes

- Registro de RRHH: empleados activos con situaciones especiales vigentes
- Certificados de incapacidad de la CSS: fecha de inicio, diagnóstico genérico, duración estimada
- Solicitudes de licencias y permisos: tipo, fecha inicio/fin, resolución
- Convención colectiva aplicable (si existe): duraciones máximas y condiciones
- Código de Trabajo de Panamá: plazos legales de referencia
- Calendario de revisiones médicas (incapacidades de larga duración)

## Flujo de trabajo

1. Cargar el registro de empleados en situación especial
2. Para cada situación activa:
   a. Verificar tipo: incapacidad por enfermedad, incapacidad por riesgo profesional,
      licencia remunerada, licencia no remunerada, fuero (maternidad/sindical), reducción
      de jornada, suspensión del contrato de trabajo
   b. Calcular días transcurridos y días hasta fecha de retorno prevista
   c. Verificar si se acerca algún hito legal:
      - Incapacidad por enfermedad: límites de subsidio de la CSS y vencimiento [verificar]
      - Licencia no remunerada: fin del período concedido, derecho de reintegro
      - Licencia de maternidad: 14 semanas (6 prenatales y 8 posnatales) — Código de Trabajo, art. 107; fuero de maternidad en el art. 106
   d. Identificar acciones administrativas pendientes (avisos a la CSS y a MITRADEL)
3. Clasificar por urgencia temporal
4. Generar informe semanal con acciones requeridas

## Formato de salida

### Empleados en situación especial

| Empleado | Departamento | Tipo situación | Fecha inicio | Fecha retorno prevista | Días restantes | Acciones pendientes |
|----------|--------------|----------------|--------------|------------------------|----------------|---------------------|

### Hitos legales próximos

| Empleado | Hito | Fecha | Implicación | Acción requerida |
|----------|------|-------|-------------|------------------|

### Resumen
- Empleados incapacitados: X (corta: X, larga: X)
- Licencias no remuneradas activas: X
- Permisos/licencias en curso: X
- Acciones pendientes esta semana: X

## Configuración

- `permisos.tipos_monitorizados`: lista de situaciones a rastrear
- `permisos.alerta_retorno_dias`: días de antelación para alerta de retorno (defecto: 7)
- `permisos.convencion_referencia`: convención colectiva aplicable (si existe)
- `permisos.responsable_rrhh`: persona a notificar de acciones pendientes

## Escalado

- **Solo log**: situaciones estables sin cambios ni hitos próximos
- **Notificación a RRHH**: retorno previsto en los próximos 7 días laborables
- **Alerta al responsable laboral**: hito legal próximo (vencimiento de subsidio de incapacidad, fin de licencia)
- **Escalado urgente**: incumplimiento de plazo de aviso a la CSS o a MITRADEL
