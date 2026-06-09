---
name: monitor-politica
schedule: "0 9 1 * *"
description: Revisa mensualmente EIPDs, contratos de encargado y resultados de triaje para detectar desalineaciones con las políticas de privacidad vigentes
---

# Monitor de Políticas de Privacidad

## Propósito

Detectar desalineaciones entre las políticas de privacidad vigentes y la realidad
operativa de los tratamientos de datos personales. Compara las EIPDs realizadas,
los contratos de encargado de tratamiento revisados y los resultados del triaje
de nuevos tratamientos con las políticas documentadas, identificando drift y
gaps que requieren actualización.

## Fuentes

- Registro de Actividades de Tratamiento (RAT) actualizado
- EIPDs (Evaluaciones de Impacto en Protección de Datos) realizadas
- Contratos de encargado de tratamiento vigentes (Ley 81 de 2019)
- Resultados del triaje de nuevos tratamientos
- Políticas de privacidad publicadas (web, empleados, clientes)
- Cláusulas informativas en uso (formularios, contratos)
- Ley 81 de 2019, Decreto Ejecutivo 285 de 2021 y guías de la ANTAI

## Flujo de trabajo

1. Cargar el RAT actualizado con todos los tratamientos activos
2. Comparar tratamientos del RAT con los descritos en las políticas de privacidad:
   a. Identificar tratamientos en el RAT no reflejados en las políticas
   b. Identificar tratamientos en las políticas que ya no existen en el RAT
   c. Verificar coherencia de bases de licitud, finalidades y plazos de conservación
3. Revisar EIPDs realizadas en el período:
   a. Verificar que los tratamientos de alto riesgo tienen EIPD vigente
   b. Comprobar que las medidas recomendadas en EIPDs se han implementado
4. Analizar resultados de triaje de nuevos tratamientos:
   a. Nuevos tratamientos aprobados sin actualización de política
   b. Tratamientos rechazados pero operativos
5. Verificar contratos de encargado:
   a. Encargados sin contrato vigente
   b. Contratos que no reflejan los tratamientos actuales
6. Generar informe de desalineaciones con propuestas de corrección

## Formato de salida

### Desalineaciones detectadas

| Tipo | Descripción | Política afectada | Impacto | Acción correctiva | Prioridad |
|------|-------------|-------------------|---------|--------------------|-----------| 

### Estado de EIPDs

| Tratamiento | EIPD requerida | EIPD realizada | Fecha | Medidas implementadas |
|-------------|----------------|----------------|-------|----------------------|

### Resumen
- Tratamientos activos: X
- Desalineaciones detectadas: X
- EIPDs pendientes: X
- Contratos de encargado por actualizar: X

## Configuración

- `politica.rat_fuente`: ubicación del Registro de Actividades de Tratamiento
- `politica.politicas_publicadas`: rutas a las políticas vigentes
- `politica.umbral_antiguedad_eipd`: meses tras los cuales una EIPD requiere revisión (defecto: 24)
- `politica.verificar_encargados`: incluir revisión de contratos de encargado (defecto: true)

## Escalado

- **Solo log**: sin desalineaciones o solo discrepancias menores de redacción
- **Notificación al encargado de protección de datos**: desalineación que requiere actualización de política
- **Alerta urgente**: tratamiento de alto riesgo sin EIPD o encargado sin contrato
- **Escalado a dirección**: gap que puede constituir infracción de la Ley 81 de 2019 sancionable por la ANTAI
