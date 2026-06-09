---
name: informe-despachos-externos
schedule: "0 10 * * 1"
description: Genera borradores semanales de emails de seguimiento para despachos externos con asuntos activos
---

# Informe de Seguimiento a Despachos Externos

## Propósito

Automatizar la generación de borradores de correo electrónico de seguimiento
dirigidos a los despachos de abogados externos que llevan asuntos en nombre
de la organización. Garantiza un seguimiento regular y homogéneo, evitando
que asuntos queden sin supervisión y manteniendo el control sobre la estrategia
procesal externalizada.

## Fuentes

- Registro de asuntos delegados a despachos externos
- Último informe de estado recibido de cada despacho (fecha y contenido)
- Calendario procesal de cada asunto externalizado
- Presupuesto y facturación por despacho/asunto
- Datos de contacto del abogado responsable en cada despacho
- Hitos recientes: audiencias, resoluciones

## Flujo de trabajo

1. Cargar la lista de asuntos activos gestionados por despachos externos
2. Para cada asunto:
   a. Verificar fecha del último informe de estado recibido
   b. Identificar próximos hitos procesales (audiencias, términos, resoluciones esperadas)
   c. Revisar si hay facturación pendiente de aprobar
   d. Evaluar si el asunto requiere seguimiento urgente o rutinario
3. Agrupar asuntos por despacho externo
4. Para cada despacho, generar un borrador de email que incluya:
   a. Saludo profesional personalizado
   b. Lista de asuntos activos con solicitud de actualización
   c. Preguntas específicas por asunto (próximos pasos, plazos, estrategia)
   d. Recordatorio de hitos próximos
   e. Solicitud de previsión de honorarios si procede
5. Marcar borradores como pendientes de revisión y envío

## Formato de salida

### Borradores generados

Para cada despacho externo:

**Para:** [Email del despacho]
**Asunto:** Seguimiento semanal — [Nombre de la entidad] — [Fecha]

Cuerpo estructurado:
1. Introducción breve
2. Tabla de asuntos con columnas: Referencia | Asunto | Último estado | Pregunta específica
3. Solicitud de respuesta antes del [fecha]
4. Cierre profesional

### Resumen de gestión

| Despacho | Asuntos activos | Último informe | Días sin actualización | Facturación pendiente |
|----------|-----------------|----------------|------------------------|-----------------------|

## Configuración

- `despachos.frecuencia_seguimiento`: días máximos sin informe antes de escalar (defecto: 14)
- `despachos.plantilla_email`: plantilla base para los borradores
- `despachos.idioma`: idioma del email (defecto: español)
- `despachos.cc_interno`: personas en copia interna de los seguimientos
- `despachos.firma`: firma del remitente para los borradores

## Escalado

- **Solo log**: todos los despachos han reportado en las últimas 2 semanas
- **Borrador con tono urgente**: despacho sin informe en más de 3 semanas
- **Alerta al responsable procesal**: despacho sin respuesta tras 2 seguimientos consecutivos
- **Escalado a dirección**: asunto externalizado sin supervisión efectiva en más de 30 días
