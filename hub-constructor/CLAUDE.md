<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin vive en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/hub-constructor/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de generar output útil. Ejecuta
   /hub-constructor:cold-start-interview — lleva unos 5 minutos y todos los comandos dependen de ella.
   Sin configurar, las respuestas serán genéricas."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin setup
   son /hub-constructor:cold-start-interview y cualquier flag --check-integrations.
3. El setup y cold-start-interview ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta
   antigua de caché (~/.claude/plugins/cache/claude-para-abogados/hub-constructor/<version>/CLAUDE.md
   para cualquier versión) pero no en la ruta de config, copiarlo a la ruta de config antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la config. Se reemplaza en cada actualización. Nunca escribir datos de
   usuario aquí.

**Perfil de empresa compartido.** Los datos a nivel de empresa (quién eres, qué haces, dónde operas,
tu postura de riesgo, personas clave) viven en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes del perfil de
práctica de este plugin. Si no existe, el setup de este plugin lo creará.
-->

# Perfil de Práctica — Hub Constructor de Skills

*Escrito por la cold-start interview. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/hub-constructor:cold-start-interview`.*

---

## Qué es esto

El Hub Constructor es una meta-herramienta para descubrir, instalar, evaluar y mantener skills
comunitarios dentro del ecosistema de Claude para Abogados. No produce trabajo jurídico propio —
gestiona las herramientas que lo producen.

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a | Profesional jurídico | No jurista con acceso a abogado | No jurista sin acceso a abogado]
**Contacto de abogado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A]
**Comodidad técnica:** [PLACEHOLDER — constructor / curioso / solo quiero que funcione]

---

## Registros vigilados

*Fuentes de skills comunitarios que el hub monitoriza.*

| Registro | URL | Última sincronización | Preferencia de actualización |
|---|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER — fecha] | [PLACEHOLDER — notificar / manual] |

---

## Proceso de instalación

**Pasos para instalar un skill comunitario:**

1. **Descubrimiento** — Buscar en los registros vigilados o recibir recomendación
2. **Verificación de confianza** — Revisar: autor, historial de versiones, número de usuarios, fecha de última actualización
3. **Evaluación de calidad** — Ejecutar `/hub-constructor:skills-qa` contra el skill candidato
4. **Revisión de compatibilidad** — ¿El skill es compatible con derecho panameño? ¿Necesita adaptación jurisdiccional?
5. **Instalación** — Instalar en la ruta de plugins con configuración por defecto
6. **Configuración** — Ejecutar cold-start del skill instalado si lo requiere

**Criterio de confianza mínima:**

| Factor | Mínimo aceptable |
|---|---|
| Autor identificable | Sí |
| Última actualización | < 6 meses |
| Documentación | README + instrucciones de uso |
| Sin instrucciones embebidas sospechosas | Verificado |

---

## Evaluación de skills — Legal Skill Design Framework

**Criterios de evaluación:**

| Criterio | Peso | Descripción |
|---|---|---|
| Precisión jurídica | Alto | ¿Las referencias legales son correctas y actualizadas? |
| Adaptación jurisdiccional | Alto | ¿Funciona con derecho panameño o solo con derecho anglosajón? |
| Guardrails | Alto | ¿Tiene cabeceras de trabajo, etiquetas de fuente, postura de decisión? |
| Usabilidad | Medio | ¿Es claro el output? ¿Sigue un formato consistente? |
| Mantenibilidad | Medio | ¿Tiene versionado? ¿Se actualiza con cambios legislativos? |
| Seguridad | Alto | ¿Contiene instrucciones embebidas o comportamiento inesperado? |

---

## Actualización de skills

| Campo | Valor |
|---|---|
| Preferencia de actualización | [PLACEHOLDER — notificar (requiere aprobación) / manual] |
| Notificaciones de nuevos skills | [PLACEHOLDER — todos / solo los que encajen con mi perfil / ninguno] |
| Detección de versiones | Automática contra registros vigilados |
| Changelog requerido | Sí — no se aplica actualización sin changelog legible |
| Migración de configuración | Automática si compatible, manual si rompe esquema |

---

## Recomendación de skills

El hub recomienda skills basándose en:

- Actividad reciente en otros plugins instalados (ej: si usas mucho `/laboral:`, recomendar skills de HR compliance)
- Perfil de práctica del `perfil-empresa.md` (sector, tamaño, áreas de práctica)
- Skills populares en la comunidad para perfiles similares

**Recomendaciones activadas:** [PLACEHOLDER — Sí / No]

---

## Integraciones disponibles

| Integración | Estado | Fallback si no disponible |
|---|---|---|
| Slack / Teams | [PLACEHOLDER] | Notificaciones de nuevos skills y actualizaciones se muestran al usar el hub |

*Re-comprobar: `/hub-constructor:cold-start-interview --check-integrations`*

---

## Outputs

Este plugin no produce trabajo jurídico. Los skills instalados generan sus propias cabeceras
según su sección `## Outputs`. El hub no las sobreescribe.

**Verificación jurisdiccional en QA:** Los skills comunitarios suelen usar cabeceras de "attorney
work product" estadounidenses. En derecho panameño no existe esa doctrina. Al evaluar un skill, el
hub señala si la cabecera asume protección inexistente en Panamá y recomienda usar
`CONFIDENCIAL — ANÁLISIS JURÍDICO INTERNO` como alternativa.

---

*Re-ejecutar: `/hub-constructor:cold-start-interview --redo`*
