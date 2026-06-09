---
name: vigilante-renovaciones-pi
schedule: "0 9 1 * *"
description: Monitoriza el portfolio de propiedad intelectual e industrial para detectar plazos de renovación próximos en marcas, patentes y otros registros
---

# Vigilante de Renovaciones de PI

## Propósito

Controlar mensualmente los plazos de renovación y mantenimiento del portfolio de
propiedad intelectual e industrial de la organización. Incluye marcas (renovación
cada 10 años) [verificar], patentes (anualidades), modelos de utilidad, diseños industriales,
nombres de dominio y derechos de autor registrados. Evita la pérdida de derechos
por falta de renovación oportuna.

## Fuentes

- Registro de portfolio de PI de la entidad:
  - Marcas nacionales (DIGERPI) e internacionales (OMPI / Protocolo de Madrid)
  - Patentes nacionales (DIGERPI) e internacionales (PCT)
  - Modelos de utilidad, diseños industriales
  - Nombres de dominio (.pa, .com, gTLDs)
  - Registros de derecho de autor (DIGERPI — Dirección Nacional de Derecho de Autor) [verificar]
- Tablas de tasas oficiales vigentes (DIGERPI, OMPI)
- Historial de renovaciones anteriores
- Agentes o abogados de propiedad industrial asignados

## Flujo de trabajo

1. Cargar el portfolio completo de registros de PI activos
2. Para cada registro:
   a. Calcular la fecha de próxima renovación o pago de anualidad:
      - Marcas: cada 10 años desde la fecha de registro/última renovación [verificar]
      - Patentes nacionales: anualidades de mantenimiento según la Ley 35 de 1996 [verificar]
      - Patentes vía PCT: anualidades ante DIGERPI tras la fase nacional [verificar]
      - Modelos de utilidad: vigencia y renovación según la Ley 35 de 1996 [verificar]
      - Diseños industriales: vigencia y renovaciones según la Ley 35 de 1996 [verificar]
      - Dominios: según período contratado (1-10 años)
   b. Calcular días restantes hasta el vencimiento
   c. Verificar si hay período de gracia disponible (habitualmente 6 meses con recargo)
   d. Estimar tasas de renovación aplicables
   e. Identificar al responsable o agente de PI asignado
3. Clasificar por urgencia:
   - 🔴 Rojo: ≤30 días (o en período de gracia)
   - 🟠 Ámbar: 31-90 días
   - 🟢 Verde: 91-180 días
4. Generar informe mensual con acciones requeridas

## Formato de salida

### Renovaciones próximas (180 días)

| Registro | Tipo | Oficina | Nº registro | Fecha renovación | Días restantes | Urgencia | Tasa estimada | Responsable |
|----------|------|---------|-------------|------------------|----------------|----------|---------------|-------------|

### En período de gracia

| Registro | Tipo | Vencimiento original | Fin período gracia | Recargo | Acción urgente |
|----------|------|----------------------|--------------------|---------|----------------|

### Resumen
- Registros activos en portfolio: X
- Renovaciones en próximos 180 días: X
- En período de gracia: X
- Coste estimado de renovaciones del trimestre: X USD (B/.)

## Configuración

- `pi.portfolio_fuente`: ubicación del registro de portfolio
- `pi.umbral_rojo_dias`: 30
- `pi.umbral_ambar_dias`: 90
- `pi.umbral_verde_dias`: 180
- `pi.incluir_dominios`: monitorizar nombres de dominio (defecto: true)
- `pi.agente_pi_defecto`: agente de PI a notificar si no hay responsable asignado
- `pi.moneda`: USD (B/.)

## Escalado

- **Solo log**: renovaciones en verde sin cambios respecto al mes anterior
- **Notificación al responsable**: renovación en zona ámbar, iniciar trámite
- **Alerta al responsable y agente de PI**: renovación en zona roja, acción inmediata
- **Escalado urgente a dirección**: registro en período de gracia sin acción iniciada
