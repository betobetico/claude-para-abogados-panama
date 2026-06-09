---
name: auditoria-encargados
schedule: "0 9 1 1,4,7,10 *"
description: Revisión trimestral de contratos de custodio o encargado de tratamiento y calendario de auditorías a proveedores que tratan datos personales
---

# Auditoría de Custodios o Encargados de Tratamiento

## Propósito

Controlar trimestralmente el estado de los contratos de custodio o encargado de tratamiento
(Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021) y el cumplimiento del plan de
auditorías a proveedores que tratan datos personales por cuenta de la organización. Asegura
que todos los custodios o encargados tienen contrato vigente y que se cumplen las auditorías
periódicas pactadas.

## Fuentes

- Registro de custodios o encargados de tratamiento con datos contractuales
- Contratos de custodio o encargado vigentes (Ley 81 de 2019 / Decreto Ejecutivo 285 de 2021)
- Plan de auditorías a custodios o encargados (anual o según contrato)
- Informes de auditorías realizadas
- Registro de Actividades de Tratamiento (RAT): tratamientos delegados a cada custodio o encargado
- Registro de incidentes y brechas de seguridad por custodio o encargado
- Certificaciones del custodio o encargado (ISO 27001, SOC 2, etc.)

## Flujo de trabajo

1. Cargar el registro de custodios o encargados de tratamiento activos
2. Para cada custodio o encargado:
   a. Verificar existencia y vigencia del contrato de tratamiento conforme a la Ley 81 de 2019
   b. Comprobar que el contrato cubre todos los tratamientos delegados según el RAT
   c. Verificar fecha de vencimiento del contrato y necesidad de renovación
   d. Revisar el plan de auditorías:
      - Última auditoría realizada (fecha, resultado)
      - Próxima auditoría programada
      - Acciones correctivas pendientes de auditorías anteriores
   e. Comprobar vigencia de certificaciones aportadas
   f. Verificar si ha habido incidentes o brechas en el trimestre
3. Identificar custodios o encargados con contrato vencido o próximo a vencer
4. Identificar auditorías vencidas o próximas según el plan
5. Generar informe trimestral con estado y acciones requeridas

## Formato de salida

### Estado de contratos de custodio o encargado

| Custodio/Encargado | Tratamientos | Contrato vigente | Vencimiento | Días restantes | Acciones |
|--------------------|--------------|------------------|-------------|----------------|----------|

### Plan de auditorías

| Custodio/Encargado | Última auditoría | Resultado | Próxima programada | Estado | Correctivas pendientes |
|--------------------|------------------|-----------|--------------------|--------|------------------------|

### Certificaciones

| Custodio/Encargado | Certificación | Fecha emisión | Fecha caducidad | Estado |
|--------------------|---------------|---------------|-----------------|--------|

### Resumen trimestral
- Custodios o encargados activos: X
- Contratos vigentes: X / Con renovación próxima: X / Vencidos: X
- Auditorías realizadas en el trimestre: X / Pendientes: X
- Acciones correctivas abiertas: X
- Incidentes reportados: X

## Configuración

- `encargados.registro`: ubicación del registro de custodios o encargados
- `encargados.frecuencia_auditoria_defecto`: meses entre auditorías (defecto: 12)
- `encargados.alerta_renovacion_dias`: días de antelación para renovación (defecto: 60)
- `encargados.verificar_certificaciones`: comprobar vigencia de certificaciones (defecto: true)
- `encargados.responsable_contacto`: responsable de protección de datos a notificar en caso de incidencias

## Escalado

- **Solo log**: todos los contratos vigentes, auditorías al día, sin incidencias
- **Notificación al responsable de protección de datos**: contrato próximo a vencer (≤60 días) o auditoría programada próxima
- **Alerta al equipo de privacidad**: contrato vencido o auditoría vencida sin reprogramar
- **Escalado urgente**: custodio o encargado sin contrato vigente que sigue tratando datos, o brecha detectada
