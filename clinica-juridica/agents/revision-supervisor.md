---
name: revision-supervisor
schedule: "0 8 * * 1-5"
description: Agrega diariamente durante el período lectivo los trabajos de estudiantes pendientes de revisión por parte de los supervisores
---

# Cola de Revisión del Supervisor

## Propósito

Centralizar y priorizar los trabajos de los estudiantes del consultorio jurídico
que están pendientes de revisión por sus supervisores académicos. Ejecuta
diariamente durante el período lectivo, asegurando que ningún trabajo quede
sin supervisión y que los plazos de entrega a clientes pro bono se respeten.

## Fuentes

- Repositorio de trabajos del consultorio jurídico (carpeta compartida o plataforma)
- Registro de asignaciones: estudiante, asunto, supervisor, fecha de entrega
- Estado de revisión de cada trabajo (pendiente, en revisión, devuelto, aprobado)
- Calendario académico: período lectivo, festivos, períodos de exámenes
- Registro de asuntos activos del consultorio: cliente, plazo, urgencia
- Historial de revisiones por supervisor (carga de trabajo)

## Flujo de trabajo

1. Verificar si la fecha actual está dentro del período lectivo configurado
2. Si no es período lectivo, registrar en log y no generar informe
3. Cargar todos los trabajos con estado "pendiente de revisión" o "devuelto para corrección"
4. Para cada trabajo pendiente:
   a. Identificar al estudiante autor y al supervisor asignado
   b. Calcular días desde la entrega del trabajo
   c. Verificar si el asunto tiene plazo de entrega al cliente
   d. Evaluar urgencia: días desde entrega + proximidad del plazo del asunto
   e. Comprobar si el supervisor ha tenido actividad de revisión reciente
5. Agrupar trabajos por supervisor
6. Ordenar dentro de cada grupo por urgencia (descendente)
7. Calcular métricas de carga por supervisor
8. Generar informe diario con cola de revisión priorizada

## Formato de salida

### Cola de revisión por supervisor

Para cada supervisor:

**[Nombre del supervisor]** — Trabajos pendientes: X | Carga vs. media: alta/normal/baja

| Estudiante | Asunto | Tipo de trabajo | Fecha entrega | Días en cola | Plazo cliente | Urgencia |
|------------|--------|-----------------|---------------|--------------|---------------|----------|

- Urgencia: 🔴 Crítica (plazo cliente ≤7 días) | 🟠 Alta (>5 días en cola) | 🟢 Normal

### Trabajos devueltos para corrección

| Estudiante | Asunto | Fecha devolución | Motivo | Días desde devolución |
|------------|--------|------------------|--------|-----------------------|

### Resumen diario
- Trabajos pendientes de revisión: X
- Trabajos devueltos pendientes de corrección: X
- Tiempo medio en cola: X días
- Supervisores con carga alta: X
- Plazos de cliente en riesgo: X

## Configuración

- `clinica.periodo_lectivo_inicio`: fecha de inicio del período lectivo
- `clinica.periodo_lectivo_fin`: fecha de fin del período lectivo
- `clinica.repositorio_trabajos`: ruta al repositorio de trabajos
- `clinica.dias_alerta_cola`: días en cola que disparan alerta (defecto: 5)
- `clinica.umbral_carga_alta`: número de trabajos pendientes que define carga alta (defecto: 5)
- `clinica.coordinador`: persona a notificar para escalados

## Escalado

- **Solo log**: todos los trabajos con menos de 3 días en cola, sin plazos en riesgo
- **Notificación al supervisor**: trabajo con más de 5 días en cola
- **Alerta al coordinador**: plazo de cliente en riesgo por trabajo sin revisar
- **Escalado al director del consultorio**: supervisor sin actividad de revisión en más de 10 días
