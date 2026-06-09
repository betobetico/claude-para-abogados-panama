---
name: entrevista-inicial
description: >
  Ejecuta la entrevista inicial del módulo de recetas de agentes — aprende qué
  agentes programados quieres activar, con qué frecuencia, a quién notificar y
  qué fuentes de datos configurar. Escribe el perfil en CLAUDE.md. Úsalo en la
  primera ejecución o cuando el usuario diga "configurar agentes", "onboarding",
  o quiera repetir la entrevista.
argument-hint: "[--redo para repetir] [--check-integrations para re-verificar integraciones]"
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/recetas-agentes/CLAUDE.md` — si está completo y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista (corto — 3 partes).
3. Escribir `~/.claude/plugins/config/claude-para-abogados/recetas-agentes/CLAUDE.md`. Mostrar resumen.

```
/recetas-agentes:entrevista-inicial
```

---

# Entrevista Inicial: Recetas de Agentes

## Propósito

Configurar los agentes programados — tareas automáticas que se ejecutan periódicamente para vigilar cambios normativos, vencimientos, actualizaciones de expedientes y otras tareas recurrentes. Entrevista corta: tres partes, cinco minutos.

Los agentes no hacen trabajo legal — vigilan, recopilan y notifican. El trabajo legal lo haces tú (o los otros módulos) cuando un agente detecta algo relevante.

## Comprobación de estado

Leer `~/.claude/plugins/config/claude-para-abogados/recetas-agentes/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** → ofrecer retomar.
- **Contiene marcadores `[PENDIENTE]`** → ofrecer empezar de cero o retomar.
- **Poblado** → ya configurado; saltar salvo `--redo`.

## Comprobar el perfil de empresa compartido

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`. Si existe, leerlo y confirmar. Si no, hacer las preguntas de empresa básicas.

## Antes de empezar

> **`recetas-agentes` gestiona agentes programados que vigilan cambios, vencimientos y novedades de forma automática.** No hacen trabajo legal — detectan y notifican para que tú actúes.
>
> **5 minutos** para elegir qué agentes activar, con qué frecuencia y a quién notificar.

## Ritmo de la entrevista

- **2-3 preguntas por turno.** Entrevista corta.
- **Pausa y reanudación:** "Di 'pausa' y guardaré tu progreso."

## La entrevista

### Apertura

> Los agentes programados son como un pasante que revisa las fuentes cada mañana y te avisa si hay algo que necesita tu atención. Vamos a decidir qué quieres vigilar y cómo quieres que te avise.

### Parte 0: Quién usa esto

> ¿Quién va a recibir las notificaciones de los agentes?
>
> 1. **Abogado individual** — las notifico a mí directamente.
> 2. **Equipo legal** — las notifico al equipo (Slack, email, etc.).
> 3. **Responsable de cumplimiento** — las notifico según el área afectada.

Esto determina el canal y la granularidad de las notificaciones.

### Parte 1: Agentes programados activos

> "Estos son los agentes disponibles. ¿Cuáles quieres activar?"

Presentar la lista de agentes disponibles. Para cada uno, describir en una línea qué hace:

| Agente | Descripción | ¿Activar? |
|---|---|---|
| **Vigilancia normativa** | Revisa la Gaceta Oficial de Panamá y fuentes regulatorias buscando cambios que afecten a tus áreas | [Sí/No] |
| **Vencimientos de contratos** | Avisa antes de que venzan plazos de renovación, preaviso o resolución | [Sí/No] |
| **Seguimiento de expedientes** | Monitoriza el estado de expedientes en juzgados y organismos | [Sí/No] |
| **Cambios en jurisprudencia** | Detecta sentencias relevantes para tus áreas de práctica | [Sí/No] |
| **Auditoría de cumplimiento** | Revisión periódica de checklist de cumplimiento | [Sí/No] |
| **Vencimiento de plazos procesales** | Alerta de plazos próximos a vencer | [Sí/No] |

- "¿Alguno que no esté en la lista y te gustaría tener? Los agentes son configurables — si hay una fuente que quieres vigilar, dime cuál."
- Si el usuario no sabe cuáles activar: "Te recomiendo empezar con vigilancia normativa y vencimientos — son los más útiles y los más fáciles de configurar. Los demás los puedes añadir después."

### Parte 2: Frecuencia y destinatarios

> "Para cada agente que has activado, necesito dos cosas: cada cuánto se ejecuta y a quién notifica."

Para cada agente activado:

- **Frecuencia:** ¿Diario (por la mañana), semanal (lunes), mensual, otro?
- **Canal de notificación:**
  - En la propia sesión de Claude (al abrir la conversación).
  - Slack (canal o DM).
  - Email (dirección).
  - Archivo en carpeta (se guarda un informe).
- **Nivel de detalle:** ¿Resumen de una línea por hallazgo, o informe detallado?
- **Umbral de relevancia:** ¿Todo lo que detecte, o solo lo que sea relevante para mis áreas? (Si hay perfil de empresa, usar las áreas de práctica como filtro.)

Si elige Slack o email: "Necesitaré que la integración correspondiente esté configurada. Vamos a verificarlo."

### Parte 3: Configuración de fuentes

> "¿De dónde quieres que los agentes extraigan información?"

- **Fuentes normativas:**
  - Gaceta Oficial de Panamá — por defecto para vigilancia normativa.
  - ANTAI, SMV, DGI, ACODECO, UAF, MITRADEL, otros reguladores — ¿cuáles son relevantes?
- **Fuentes de jurisprudencia:**
  - Órgano Judicial / Registro Judicial — por defecto.
  - Bases de datos de pago — ¿tiene acceso a alguna?
- **CLM (Contract Lifecycle Management):**
  - ¿Usáis un sistema de gestión de contratos? ¿Cuál?
  - Si no: ¿dónde están los contratos? (Carpeta, Drive, SharePoint.)
- **Feeds regulatorios:**
  - ¿Hay feeds RSS o newsletters a las que estés suscrito que quieras que el agente también vigile?
- **Expedientes judiciales:**
  - ¿Tenéis expedientes abiertos? ¿En qué sistema se consultan? (Sistema de notificaciones del Órgano Judicial, portal del Órgano Judicial.)

Si no tiene opinión sobre fuentes: "Te configuro las fuentes estándar: Gaceta Oficial de Panamá para normativa, Órgano Judicial para jurisprudencia. Las puedes ampliar después."

## Plantilla del perfil de práctica

```markdown
# Perfil: Recetas de Agentes

*Escrito por la entrevista inicial el [FECHA].*

---

## Quién usa esto

**Rol:** [Abogado individual / Equipo legal / Responsable cumplimiento]

---

## Integraciones disponibles

| Integración | Estado | Necesario para |
|---|---|---|
| Slack | [PENDIENTE] | Notificaciones en tiempo real |
| Email | [PENDIENTE] | Notificaciones por correo |
| Tareas programadas | [PENDIENTE] | Ejecución automática |
| Almacenamiento | [PENDIENTE] | Guardar informes |

---

## Agentes activos

| Agente | Frecuencia | Canal | Detalle | Umbral |
|---|---|---|---|---|
| [PENDIENTE] | | | | |

---

## Fuentes configuradas

### Normativas
| Fuente | URL/Acceso | Estado |
|---|---|---|
| Gaceta Oficial de Panamá | gacetaoficial.gob.pa [verificar] | [Activo/PENDIENTE] |

### Jurisprudencia
| Fuente | Acceso | Estado |
|---|---|---|
| Órgano Judicial / Registro Judicial | organojudicial.gob.pa [verificar] | [Activo/PENDIENTE] |

### Contratos
**Sistema CLM:** [PENDIENTE / No hay]
**Ubicación contratos:** [PENDIENTE]

### Expedientes
**Sistema:** [Sistema de notificaciones del Órgano Judicial / Portal del Órgano Judicial / PENDIENTE / No hay]

---

*Re-ejecutar: `/recetas-agentes:entrevista-inicial --redo`*
```

## Después de escribir

> **Configurado.** Tienes [N] agentes activos.
>
> **Lo que puedo hacer:**
> - **Ver el estado de los agentes** — `/recetas-agentes:estado`
> - **Ejecutar un agente ahora** — `/recetas-agentes:ejecutar [nombre]`
> - **Añadir un agente nuevo** — `/recetas-agentes:nuevo`
> - **Ver el último informe** — `/recetas-agentes:informe`
>
> **Sugerencia:** Ejecuta `/recetas-agentes:ejecutar vigilancia-normativa` para ver un primer barrido de novedades en la Gaceta Oficial de Panamá.

Cerrar:

> "Tu configuración está en `~/.claude/plugins/config/claude-para-abogados/recetas-agentes/CLAUDE.md`. Edítalo directamente o ejecuta `--redo`."

## Modos de fallo

- **No activar todos los agentes por defecto.** Cada agente consume recursos y genera notificaciones. Mejor empezar con pocos y añadir que saturar al usuario.
- **No prometer acceso a fuentes de pago.** Si el usuario no tiene acceso a una base de datos jurídica de pago, no ofrecer jurisprudencia de esas fuentes. Usar el Órgano Judicial / Registro Judicial como base.
- **No confundir vigilancia con análisis.** El agente detecta y notifica. El análisis lo hace el usuario o los otros módulos. No generar conclusiones jurídicas automáticas.
- **No ignorar falsos positivos.** Un agente de vigilancia normativa que avise de toda la Gaceta Oficial cada día es inútil. El filtro por áreas de práctica es crítico.
- **No asumir que los portales judiciales están accesibles.** No todos los usuarios tienen acceso al sistema de notificaciones del Órgano Judicial o a sus portales electrónicos. Preguntar antes de configurar.
