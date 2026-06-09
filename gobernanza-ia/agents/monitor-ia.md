---
name: monitor-ia
schedule: "0 9 * * 1"
description: Monitoriza semanalmente los desarrollos en gobernanza de inteligencia artificial relevantes para Panamá, incluyendo iniciativas locales, normativa conexa (protección de datos) y marcos internacionales de referencia
---

# Monitor de Gobernanza de IA

## Propósito

Realizar un seguimiento semanal de los avances en gobernanza de inteligencia
artificial relevantes para Panamá. Panamá no cuenta con una ley de IA vinculante,
por lo que el monitor rastrea iniciativas y anteproyectos locales [verificar],
la normativa panameña conexa (protección de datos personales, supervisada por la
ANTAI), y los marcos internacionales de referencia (OCDE, UNESCO, NIST AI RMF,
ISO/IEC 42001), para mantener actualizado el registro interno de sistemas de IA.

## Fuentes

- Gaceta Oficial de Panamá: leyes, decretos y resoluciones en materia de IA, datos o tecnología
- Asamblea Nacional de Panamá: anteproyectos y proyectos de ley sobre IA [verificar]
- ANTAI (Autoridad Nacional de Transparencia y Acceso a la Información): guías y resoluciones en protección de datos e IA
- AIG (Autoridad Nacional para la Innovación Gubernamental): estrategias y lineamientos de IA en el sector público [verificar]
- OCDE: principios y recomendaciones sobre IA (referencia comparada)
- UNESCO: Recomendación sobre la ética de la IA (referencia comparada)
- NIST AI Risk Management Framework e ISO/IEC 42001 (estándares de referencia)
- Reglamento Europeo de IA: solo como referencia comparada internacional, no como derecho aplicable en Panamá

## Flujo de trabajo

1. Rastrear fuentes configuradas en busca de novedades en gobernanza de IA
2. Para cada novedad detectada:
   a. Clasificar por tipo: iniciativa local, normativa conexa, guía, estándar técnico, marco internacional
   b. Evaluar relevancia para el registro interno de sistemas de IA
   c. Identificar si afecta a sistemas clasificados como de alto riesgo según el marco interno
   d. Determinar si modifica obligaciones de gobernanza o de protección de datos existentes
   e. Vincular con sistemas de IA registrados internamente
3. Revisar el estado de las iniciativas locales panameñas en materia de IA [verificar]:
   a. Anteproyectos en trámite vs. normas aprobadas
   b. Plazos o consultas públicas aplicables
4. Verificar si hay actualizaciones en la normativa conexa de protección de datos (ANTAI)
5. Generar informe semanal con impacto en el registro interno

## Formato de salida

### Novedades de gobernanza de la semana

| Novedad | Fuente | Tipo | Fecha | Sistemas afectados | Impacto | Acción requerida |
|---------|--------|------|-------|-------------------|---------|------------------|

### Estado de iniciativas locales de IA en Panamá

| Iniciativa | Fecha | Estado | Implicación |
|------|-------|--------|-------------|

- Estados: ✅ Aprobada | ⏳ En trámite | ⚠️ En consulta | 🔴 Archivada

### Impacto en registro interno
- Sistemas de alto riesgo afectados: X
- Obligaciones nuevas o modificadas: X
- Actualizaciones de gobernanza requeridas: X

## Configuración

- `ia.fuentes`: portales y APIs a rastrear
- `ia.sistemas_registrados`: referencia al registro interno de sistemas de IA
- `ia.categorias_riesgo`: mapeo de sistemas internos a categorías del marco de referencia
- `ia.alertar_iniciativas_locales`: monitorizar anteproyectos y consultas públicas locales (defecto: true)
- `ia.incluir_soft_law`: incluir guías y recomendaciones no vinculantes (defecto: true)

## Escalado

- **Solo log**: semana sin novedades relevantes o solo soft law informativo
- **Notificación al equipo de gobernanza IA**: novedad que requiere actualización del registro
- **Alerta al responsable de gobernanza**: nuevo requisito (legal conexo o de marco interno) para sistemas de alto riesgo
- **Escalado a dirección**: práctica de IA interna potencialmente afectada por nueva iniciativa o restricción legal
