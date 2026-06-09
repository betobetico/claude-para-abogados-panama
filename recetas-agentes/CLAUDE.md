<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin vive en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/recetas-agentes/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de generar output útil. Ejecuta
   /recetas-agentes:cold-start-interview — lleva unos 5 minutos y todos los comandos dependen de ella.
   Sin configurar, las respuestas serán genéricas."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin setup
   son /recetas-agentes:cold-start-interview y cualquier flag --check-integrations.
3. El setup y cold-start-interview ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta
   antigua de caché (~/.claude/plugins/cache/claude-para-abogados/recetas-agentes/<version>/CLAUDE.md
   para cualquier versión) pero no en la ruta de config, copiarlo a la ruta de config antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la config. Se reemplaza en cada actualización. Nunca escribir datos de
   usuario aquí.

**Perfil de empresa compartido.** Los datos a nivel de empresa (quién eres, qué haces, dónde operas,
tu postura de riesgo, personas clave) viven en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes del perfil de
práctica de este plugin. Si no existe, el setup de este plugin lo creará.
-->

# Perfil de Práctica — Recetas de Agentes Programados

*Escrito por la cold-start interview. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/recetas-agentes:cold-start-interview`.*

---

## Qué es esto

Las Recetas de Agentes son cookbooks para desplegar agentes programados que ejecutan flujos de
trabajo jurídicos recurrentes de forma autónoma. Cada agente se configura una vez y se ejecuta
según un calendario, generando informes y alertas sin intervención manual.

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a | Profesional jurídico | No jurista con acceso a abogado]
**Contacto de abogado:** [PLACEHOLDER — Nombre / despacho / N/A]

---

## Agentes disponibles

| Agente | Descripción | Estado |
|---|---|---|
| **Vigilante de renovaciones** | Monitoriza fechas de vencimiento de contratos, seguros, licencias, dominios y alerta antes del plazo | [PLACEHOLDER — activo / configurado / no usado] |
| **Vigilante de expedientes judiciales** | Consulta el estado de expedientes en el Órgano Judicial / Registro Judicial / sistema de notificaciones del Órgano Judicial y alerta ante cambios | [PLACEHOLDER] |
| **Monitor regulatorio** | Vigila la Gaceta Oficial de Panamá y boletines de reguladores en busca de normas relevantes para la práctica | [PLACEHOLDER] |
| **Radar de lanzamientos** | Detecta nuevas versiones de skills, plugins y herramientas legales relevantes | [PLACEHOLDER] |
| **Grid de due diligence** | Ejecuta checklists de due diligence recurrentes contra fuentes públicas (Registro Público de Panamá, DGI, ANTAI) | [PLACEHOLDER] |

---

## Configuración de agentes

### Vigilante de renovaciones

| Campo | Valor |
|---|---|
| Fuentes de fechas | [PLACEHOLDER — carpeta de contratos, hoja de cálculo, calendario] |
| Antelación de alerta | [PLACEHOLDER — días antes del vencimiento] |
| Destinatarios | [PLACEHOLDER — email, Slack, inline] |
| Frecuencia de revisión | [PLACEHOLDER — diaria / semanal] |

### Vigilante de expedientes judiciales

| Campo | Valor |
|---|---|
| Expedientes vigilados | [PLACEHOLDER — lista de números de expediente / proceso] |
| Fuentes | [PLACEHOLDER — sistema de notificaciones del Órgano Judicial, Registro Judicial, portal del Órgano Judicial] |
| Frecuencia | [PLACEHOLDER — diaria / semanal] |
| Alerta ante | [PLACEHOLDER — nueva resolución, señalamiento de audiencia, notificación] |

### Monitor regulatorio

| Campo | Valor |
|---|---|
| Fuentes | [PLACEHOLDER — Gaceta Oficial de Panamá, boletines de reguladores específicos (DGI, SMV, ANTAI, ACODECO)] |
| Palabras clave | [PLACEHOLDER — términos de búsqueda relevantes para la práctica] |
| Áreas de derecho | [PLACEHOLDER — las que se correspondan con los plugins activos] |
| Frecuencia | [PLACEHOLDER — diaria] |
| Formato de output | [PLACEHOLDER — resumen ejecutivo / tabla / alerta breve] |

### Radar de lanzamientos

| Campo | Valor |
|---|---|
| Registros vigilados | [PLACEHOLDER — los mismos que hub-constructor] |
| Frecuencia | [PLACEHOLDER — semanal] |
| Criterio de relevancia | [PLACEHOLDER — perfil de práctica / todos] |

### Grid de due diligence

| Campo | Valor |
|---|---|
| Checklist activo | [PLACEHOLDER — ruta al checklist de DD] |
| Fuentes públicas | [PLACEHOLDER — Registro Público de Panamá, DGI, ANATI, listas UAF/sanciones] |
| Frecuencia | [PLACEHOLDER — bajo demanda / programada] |
| Entidades vigiladas | [PLACEHOLDER] |

---

## Despliegue

**Infraestructura:** Managed Agents API

| Campo | Valor |
|---|---|
| Agentes desplegados | [PLACEHOLDER — número] |
| Endpoint de API | [PLACEHOLDER] |
| Autenticación | [PLACEHOLDER — método] |
| Región | [PLACEHOLDER] |

---

## Monitorización

| Campo | Valor |
|---|---|
| Logs | [PLACEHOLDER — ubicación de logs de ejecución] |
| Alertas de fallo | [PLACEHOLDER — destino: email, Slack, inline] |
| Última ejecución exitosa | [PLACEHOLDER — por agente] |
| Errores en últimas 24h | [PLACEHOLDER] |
| Dashboard de estado | [PLACEHOLDER — URL o ruta] |

---

## Integraciones disponibles

| Integración | Estado | Fallback si no disponible |
|---|---|---|
| Slack / Teams | [PLACEHOLDER] | Alertas entregadas por email o inline |
| Email | [PLACEHOLDER] | Alertas inline |
| Calendario | [PLACEHOLDER] | Fechas gestionadas manualmente |
| Tareas programadas | [PLACEHOLDER] | Ejecución manual bajo demanda |
| Sistema de notificaciones del Órgano Judicial / portales judiciales | [PLACEHOLDER] | Consulta manual |

*Re-comprobar: `/recetas-agentes:cold-start-interview --check-integrations`*

---

## Outputs

**Carpeta de outputs:** [PLACEHOLDER — donde se guardan informes de agentes, alertas archivadas]
**Convención de nombres:** [PLACEHOLDER — patrón: agente-fecha-tipo.md]

Este plugin genera informes operativos, no trabajo jurídico sustantivo. Los informes no llevan
cabecera de trabajo profesional. Si un informe de agente contiene hallazgos que requieren acción
jurídica, el informe lo indica y deriva al plugin correspondiente.

---

*Re-ejecutar: `/recetas-agentes:cold-start-interview --redo`*
