---
name: calendario-aeat
schedule: "0 9 1 * *"
description: Genera el calendario de obligaciones fiscales del mes con declaraciones, plazos y estado de cumplimiento
---

# Calendario de Obligaciones Fiscales DGI

## Propósito

Generar mensualmente el calendario de obligaciones tributarias de la entidad
ante la Dirección General de Ingresos (DGI) del Ministerio de Economía y
Finanzas y, en su caso, los municipios. Permite al equipo fiscal y contable
planificar con antelación la preparación y presentación de declaraciones,
evitando recargos e intereses por presentación tardía.

## Fuentes

- Calendario tributario de la DGI (publicación anual) [verificar]
- Perfil fiscal de la entidad: forma jurídica, régimen de ITBMS, obligaciones específicas
- Declaraciones y formularios tributarios aplicables a la entidad
- Registro de presentaciones anteriores (formulario, período, fecha, resultado)
- Calendario de días feriados nacionales (afecta a plazos)
- Régimen de zona especial aplicable (Ciudad del Saber, ZLC, Panamá Pacífico, SEM) si procede

## Flujo de trabajo

1. Cargar el perfil fiscal de cada entidad gestionada
2. Identificar las declaraciones tributarias a presentar en el mes en curso:
   - Declaración mensual de ITBMS (formulario 430) [verificar]
   - Planilla mensual de retenciones del ISR sobre salarios (formulario 03) [verificar]
   - Retenciones de ITBMS y de servicios profesionales
   - Declaración jurada anual del ISR (formulario 1) [verificar]
   - Estimada del ISR y CAIR (Cálculo Alternativo del Impuesto sobre la Renta) [verificar]
   - Retención sobre dividendos y complementario [verificar]
   - Tasa única de sociedades anónimas y fundaciones — coordinar con módulo societario
3. Para cada obligación:
   a. Verificar el plazo exacto de presentación (día del mes)
   b. Comprobar si hay arreglos de pago o facilidades vigentes
   c. Verificar el estado de preparación (datos disponibles, borrador, revisado)
   d. Calcular días restantes hasta el vencimiento
4. Generar el calendario mensual con todas las obligaciones

## Formato de salida

### Obligaciones fiscales — [Mes Año]

| Formulario | Concepto | Período | Plazo presentación | Días restantes | Estado | Responsable |
|--------|----------|---------|--------------------|----------------|--------|-------------|

- Estados: ✅ Presentado | 📝 En preparación | ⏳ Pendiente | 🔴 Vencido

### Arreglos de pago vigentes

| Referencia | Importe pendiente | Próximo vencimiento | Estado |
|------------|-------------------|---------------------|--------|

### Resumen del mes
- Obligaciones del mes: X
- Ya presentadas: X
- En preparación: X
- Pendientes de iniciar: X
- Importe estimado total: X USD (B/.)

## Configuración

- `fiscal.entidades`: lista de entidades con su perfil fiscal
- `fiscal.regimen_itbms`: periodicidad de ITBMS por entidad
- `fiscal.administracion`: DGI, municipio, régimen de zona especial
- `fiscal.formularios_aplicables`: lista de formularios por entidad
- `fiscal.responsable_fiscal`: persona responsable por defecto
- `fiscal.alerta_anticipacion_dias`: días de antelación para alertar (defecto: 10)

## Escalado

- **Solo log**: todas las obligaciones presentadas o con más de 15 días de margen
- **Notificación al responsable fiscal**: obligación a menos de 10 días sin borrador preparado
- **Alerta al equipo**: obligación a menos de 5 días sin datos completos
- **Escalado a dirección financiera**: riesgo de presentación tardía con recargo e intereses
