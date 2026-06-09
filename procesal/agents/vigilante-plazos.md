---
name: vigilante-plazos
schedule: "0 8 * * *"
description: Monitorea diariamente los términos procesales de asuntos abiertos, alertando con semáforo sobre vencimientos en los próximos 7 días
---

# Vigilante de Términos Procesales

## Propósito

Control diario de todos los términos procesales activos en los asuntos judiciales
y arbitrales en curso. Los términos procesales son improrrogables y su incumplimiento
puede suponer la pérdida de derechos, por lo que este agente constituye una red
de seguridad crítica para el departamento jurídico.

## Fuentes

- Registro de asuntos judiciales abiertos (jurisdicción, proceso, tribunal)
- Calendario de términos procesales por asunto
- Notificaciones judiciales recibidas (sistema de notificaciones del Órgano Judicial)
- Código Judicial de Panamá: términos legales [verificar]
- Código de Trabajo de Panamá y Ley 38 de 2000 (procesos laboral y administrativo) [verificar]
- Calendario de días hábiles/inhábiles del Órgano Judicial (días feriados y de duelo nacional)

## Flujo de trabajo

1. Cargar todos los asuntos con términos activos
2. Verificar el calendario de días hábiles (excluir fines de semana y días feriados
   o de duelo nacional declarados)
3. Para cada término activo:
   a. Calcular días hábiles restantes hasta vencimiento
   b. Clasificar por semáforo:
      - 🔴 Rojo: vence hoy o mañana (1-2 días hábiles)
      - 🟠 Ámbar: vence en 3-5 días hábiles
      - 🟢 Verde: vence en 6-7 días hábiles
   c. Verificar si hay escritos en preparación para ese término
   d. Identificar al abogado responsable
4. Ordenar por urgencia (días hábiles restantes ascendente)
5. Verificar si hay notificaciones pendientes de lectura en el sistema del Órgano Judicial
6. Generar informe diario

## Formato de salida

### Términos próximos (7 días hábiles)

| Asunto | Proceso | Tribunal | Término | Vencimiento | Días hábiles | Semáforo | Abogado | Estado escrito |
|--------|---------|----------|---------|-------------|--------------|----------|---------|----------------|

### Notificaciones pendientes
- Notificaciones sin leer en el sistema del Órgano Judicial: X

### Resumen diario
- Términos que vencen hoy: X
- Términos en zona roja: X
- Términos en zona ámbar: X
- Total términos activos en 7 días: X

## Configuración

- `terminos.dias_horizonte`: días hábiles a mostrar (defecto: 7)
- `terminos.distritos_judiciales`: lista de distritos con sus calendarios de feriados
- `terminos.hora_envio`: hora de envío del informe diario (defecto: 08:00)
- `terminos.notificaciones_check`: verificar notificaciones pendientes (defecto: true)

## Escalado

- **Solo log**: todos los términos en verde, sin notificaciones pendientes
- **Notificación al abogado**: término en zona ámbar sin escrito en preparación
- **Alerta urgente al abogado y responsable procesal**: término en zona roja
- **Escalado a dirección jurídica**: término que vence hoy sin escrito preparado
- **Alerta crítica**: notificación del Órgano Judicial sin leer con más de 24 horas
