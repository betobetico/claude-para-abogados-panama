---
name: cumplimiento-registral
schedule: "0 9 1 * *"
description: Monitoriza las obligaciones de cumplimiento registral y societario, alertando sobre plazos próximos como tasa única anual, declaración de renta, libros sociales y renovación de cargos
---

# Vigilante de Cumplimiento Registral

## Propósito

Controlar el calendario de obligaciones registrales y societarias de todas las
entidades gestionadas, asegurando que se cumplen los plazos legales para el pago
de la tasa única anual, presentación de la declaración de renta, mantenimiento de
libros sociales y agente residente, renovación de cargos sociales y demás
obligaciones ante el Registro Público y la DGI.

## Fuentes

- Registro de entidades gestionadas (denominación, RUC, forma jurídica, folio del Registro Público)
- Calendario legal de obligaciones societarias panameñas:
  - Tasa única anual: pago anual para el mantenimiento de la sociedad [verificar]
  - Declaración jurada de renta (ISR) ante la DGI: hasta el 31 de marzo siguiente al cierre del período fiscal [verificar]
  - Mantenimiento del agente residente: continuo [verificar]
  - Libros sociales (actas y registro de acciones): actualizados conforme al Código de Comercio [verificar]
  - Declaración de beneficiario final: según la normativa de transparencia vigente [verificar]
- Registro de cargos sociales (dignatarios y directores) con fecha de nombramiento y duración prevista en el pacto social
- Histórico de cumplimiento de cada entidad

## Flujo de trabajo

1. Cargar la lista de entidades activas con sus datos registrales
2. Para cada entidad, calcular los plazos aplicables según su fecha de cierre de período fiscal
3. Verificar el estado de cada obligación:
   - ¿Se ha pagado la tasa única anual?
   - ¿Se ha presentado la declaración jurada de renta ante la DGI?
   - ¿Se mantiene el agente residente vigente?
   - ¿Están al día los libros sociales (actas y registro de acciones)?
   - ¿Hay cargos próximos a vencer o ya vencidos?
4. Calcular días restantes para cada obligación pendiente
5. Clasificar por urgencia y generar el informe mensual
6. Verificar inscripciones pendientes en el Registro Público

## Formato de salida

### Obligaciones próximas

| Entidad | RUC | Obligación | Plazo legal | Días restantes | Estado | Responsable |
|---------|-----|------------|-------------|----------------|--------|-------------|

- Estados: ✅ Cumplida | ⏳ En curso | ⚠️ Próxima | 🔴 Vencida

### Cargos sociales

| Entidad | Cargo | Titular | Fecha nombramiento | Duración | Fecha caducidad | Estado |
|---------|-------|---------|--------------------|----------|-----------------|--------|

### Resumen
- Entidades al día: X/Y
- Obligaciones pendientes urgentes: X
- Cargos por renovar en próximos 3 meses: X

## Configuración

- `cumplimiento.entidades`: lista de entidades a monitorizar
- `cumplimiento.cierre_periodo_fiscal`: fecha de cierre por entidad (defecto: 31/12)
- `cumplimiento.alerta_anticipada_dias`: días de antelación para alertar (defecto: 30)
- `cumplimiento.responsable_defecto`: persona a notificar si no hay responsable asignado

## Escalado

- **Solo log**: obligaciones cumplidas o con más de 60 días de margen
- **Notificación al responsable**: obligación a menos de 30 días sin acción iniciada
- **Alerta al equipo societario**: obligación vencida o a menos de 7 días
- **Escalado a dirección**: riesgo de suspensión de derechos corporativos, multas o disolución por incumplimiento reiterado [verificar]
