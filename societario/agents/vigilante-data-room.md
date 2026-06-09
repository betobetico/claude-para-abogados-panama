---
name: vigilante-data-room
schedule: "0 8 * * *"
description: Monitoriza el data room virtual durante operaciones de M&A activas, detectando nuevos documentos y evaluando su impacto en el checklist de cierre
---

# Vigilante del Data Room Virtual

## Propósito

Durante operaciones de M&A activas, monitorizar el VDR (Virtual Data Room) para detectar
nuevos documentos subidos por la contraparte o por equipos internos. Evalúa cada nuevo
documento contra el checklist de cierre vigente, identificando qué ítems cubre
y qué gaps quedan abiertos. Acelera la due diligence y evita que documentos
pasen desapercibidos.

## Fuentes

- Virtual Data Room de la operación activa (API del proveedor o carpeta sincronizada)
- Checklist de cierre de la operación (`societario/operaciones/{id}/checklist.md`)
- Índice de documentos ya revisados
- Registro de la operación: partes, plazos, condiciones precedentes
- Configuración de operaciones activas

## Flujo de trabajo

1. Verificar si hay operaciones de M&A marcadas como activas en la configuración
2. Para cada operación activa:
   a. Conectar al VDR o carpeta sincronizada
   b. Comparar el índice actual de documentos con el de la última ejecución
   c. Identificar documentos nuevos o modificados desde la última revisión
   d. Para cada documento nuevo:
      - Extraer metadatos (nombre, carpeta, fecha, subido por)
      - Clasificar por categoría (financiero, legal, laboral, fiscal, regulatorio)
      - Mapear contra ítems del checklist de cierre
      - Evaluar impacto: cubre ítem pendiente, contradice documento previo, o es adicional
   e. Actualizar el estado del checklist con los nuevos documentos
3. Generar resumen de cambios y estado actualizado del checklist

## Formato de salida

### Nuevos documentos detectados

| Documento | Carpeta VDR | Categoría | Fecha subida | Subido por | Ítem checklist relacionado |
|-----------|-------------|-----------|--------------|------------|---------------------------|

### Estado del checklist de cierre

| Ítem | Estado | Documento(s) | Observaciones |
|------|--------|--------------|---------------|

- Estados: ✅ Completo | ⏳ Parcial | ❌ Pendiente | ⚠️ Requiere revisión

### Resumen
- Documentos nuevos: X
- Ítems del checklist completados: X/Y
- Ítems con discrepancias: X
- Estimación de completitud de la due diligence: X%

## Configuración

- `data_room.operaciones_activas`: lista de IDs de operaciones en curso
- `data_room.proveedor`: tipo de VDR (Datasite, Intralinks, carpeta local)
- `data_room.frecuencia_activa`: cron para días laborables durante operación activa
- `data_room.categorias`: mapeo de carpetas VDR a categorías del checklist
- `data_room.excluir_extensiones`: tipos de archivo a ignorar

## Escalado

- **Solo log**: documentos nuevos que cubren ítems ya esperados sin discrepancias
- **Notificación al equipo de deal**: documento que cubre condición precedente clave
- **Alerta al responsable de la operación**: documento que contradice información previa
- **Escalado urgente a socios**: documento que revela contingencia no identificada previamente
