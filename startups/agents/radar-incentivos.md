---
name: radar-incentivos
schedule: "0 9 1 * *"
description: Monitoriza cambios en incentivos, regímenes especiales y opciones migratorias aplicables a startups en Panamá, incluyendo SEM, Ciudad del Saber, Panamá Pacífico y visas de inversionista
---

# Radar de Incentivos para Startups

## Propósito

Rastrear mensualmente los cambios normativos y administrativos que afectan a los
incentivos, regímenes especiales y opciones migratorias aplicables a empresas
emergentes en Panamá. Cubre el régimen SEM (Ley 41 de 2007 [verificar]), Ciudad
del Saber, Panamá Pacífico, EMMA, la Zona Libre de Colón, el tratamiento del ISR
bajo el principio de territorialidad, y las categorías migratorias para fundadores
e inversionistas.

## Fuentes

- Gaceta Oficial de Panamá: modificaciones de las leyes de regímenes especiales y normativa de desarrollo
- DGI (Dirección General de Ingresos): resoluciones y notas sobre ISR e ITBMS
- Comisión SEM / MICI: cambios en el régimen de sedes de empresas multinacionales
- Fundación Ciudad del Saber: requisitos y convocatorias de afiliación
- Agencia Panamá Pacífico: actualizaciones del régimen de la zona
- Servicio Nacional de Migración: cambios en categorías de visa (inversionista, países amigos, jubilado pensionado)
- SMV (Superintendencia del Mercado de Valores): novedades sobre ofertas de valores y exenciones
- UAF / régimen de prevención de blanqueo (Ley 23 de 2015): obligaciones que afecten a la estructura

## Flujo de trabajo

1. Rastrear fuentes configuradas en busca de novedades en incentivos y migración
2. Para cada cambio detectado:
   a. Clasificar por tipo:
      - Fiscales: ISR (principio de territorialidad), ITBMS, tarifas reducidas de regímenes especiales
      - Regímenes especiales: SEM, Ciudad del Saber, Panamá Pacífico, EMMA, Zona Libre de Colón
      - Migratorios: visa de inversionista, países amigos, jubilado pensionado, permisos de régimen especial
      - Regulatorios: SMV (ofertas de valores), beneficiario final, prevención de blanqueo
   b. Evaluar impacto: cambio favorable, desfavorable o neutral
   c. Determinar aplicabilidad según perfil de las entidades gestionadas
   d. Identificar plazos de solicitud o aplicación
3. Verificar el estado de los incentivos y licencias actualmente aplicados:
   a. Requisitos que podrían dejar de cumplirse (empleo local, sustancia económica)
   b. Plazos de vigencia de licencias y permisos
   c. Nuevos requisitos documentales
4. Generar informe mensual con novedades y acciones

## Formato de salida

### Novedades en incentivos y migración

| Régimen / Visa | Tipo | Fuente | Cambio | Impacto | Aplicable | Acción requerida |
|----------------|------|--------|--------|---------|-----------|------------------|

### Estado de regímenes y licencias aplicados

| Régimen / Licencia | Entidad | Estado | Vigencia | Requisitos pendientes |
|--------------------|---------|--------|----------|-----------------------|

### Convocatorias y plazos abiertos

| Programa / Trámite | Organismo | Fecha apertura | Fecha cierre | Requisito | Elegibilidad |
|--------------------|-----------|----------------|--------------|-----------|--------------|

### Resumen
- Cambios normativos detectados: X
- Regímenes/licencias activos monitorizados: X
- Plazos abiertos relevantes: X
- Acciones requeridas este mes: X

## Configuración

- `incentivos.entidades_emergentes`: lista de entidades con perfil startup
- `incentivos.sectores`: sectores de actividad para filtrar convocatorias
- `incentivos.regimenes`: regímenes especiales a rastrear (SEM, Ciudad del Saber, Panamá Pacífico, EMMA)
- `incentivos.incluir_migracion`: monitorizar cambios en categorías de visa para fundadores/inversionistas (defecto: true)
- `incentivos.responsable_fiscal`: persona a notificar de cambios fiscales
- `incentivos.responsable_migratorio`: persona a notificar de cambios migratorios

## Escalado

- **Solo log**: mes sin cambios relevantes ni plazos nuevos
- **Notificación al responsable fiscal**: cambio en requisitos de un régimen o incentivo actualmente aplicado
- **Notificación al responsable migratorio**: cambio en requisitos de visa de fundadores/inversionistas
- **Alerta al equipo**: nuevo plazo o convocatoria con solicitud abierta
- **Escalado a dirección**: pérdida potencial de licencia o incentivo por incumplimiento de requisitos
