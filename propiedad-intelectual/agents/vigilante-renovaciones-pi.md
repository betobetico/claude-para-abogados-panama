---
name: vigilante-renovaciones-pi
schedule: "0 9 1 * *"
description: Monitoriza el portfolio de propiedad intelectual e industrial para detectar plazos de renovación próximos en marcas, patentes y otros registros
---

# Vigilante de Renovaciones de PI

## Propósito

Controlar mensualmente los plazos de renovación y mantenimiento del portfolio de
propiedad intelectual e industrial de la organización. Incluye marcas (renovación
cada 10 años, art. 109 de la Ley 35 de 1996), patentes (tasas de mantenimiento por
quinquenios, art. 207), modelos de utilidad, diseños industriales,
nombres de dominio y derechos de autor registrados. Evita la pérdida de derechos
por falta de renovación oportuna.

## Fuentes

- Registro de portfolio de PI de la entidad:
  - Marcas nacionales (DIGERPI); internacionales por registro nacional en cada país (Panamá NO es parte del Protocolo de Madrid)
  - Patentes nacionales (DIGERPI) e internacionales (PCT)
  - Modelos de utilidad, diseños industriales
  - Nombres de dominio (.pa, .com, gTLDs)
  - Registros de derecho de autor (Dirección Nacional de Derecho de Autor — DNDA, Ministerio de Cultura)
- Tablas de tasas oficiales vigentes (DIGERPI, OMPI)
- Historial de renovaciones anteriores
- Agentes o abogados de propiedad industrial asignados

## Flujo de trabajo

1. Cargar el portfolio completo de registros de PI activos
2. Para cada registro:
   a. Calcular la fecha de próxima renovación o pago de tasa de mantenimiento:
      - Marcas: 10 años contados desde la fecha de presentación de la solicitud; renovación en la ventana de 1 año antes del vencimiento (arts. 109 y 110 de la Ley 35 de 1996)
      - Patentes nacionales: tasas de mantenimiento por quinquenios (cada 5 años), no anualidades (art. 207 de la Ley 35 de 1996); caducidad de pleno derecho tras 6 meses de gracia con recargo
      - Patentes vía PCT: tasas de mantenimiento por quinquenios ante DIGERPI tras la fase nacional (art. 207 de la Ley 35 de 1996)
      - Modelos de utilidad: 10 años improrrogables (art. 26 de la Ley 35 de 1996)
      - Diseños industriales: 10 años, prorrogable una vez por 5 años (máx. 15 años) (arts. 79-80 de la Ley 35 de 1996)
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
