---
name: entrevista-inicial
description: >
  Ejecuta la entrevista inicial del hub constructor — aprende qué registros de
  skills comunitarios quieres vigilar, tus preferencias de instalación y tus
  criterios de calidad mínimos. Escribe el perfil en CLAUDE.md. Úsalo en la
  primera ejecución o cuando el usuario diga "configurar hub", "onboarding", o
  quiera repetir la entrevista.
argument-hint: "[--redo para repetir] [--check-integrations para re-verificar integraciones]"
---

# /entrevista-inicial

1. Comprobar `~/.claude/plugins/config/claude-para-abogados/hub-constructor/CLAUDE.md` — si está completo y no hay `--redo`, confirmar antes de sobrescribir.
2. Ejecutar el flujo de entrevista (corto — 3 partes).
3. Escribir `~/.claude/plugins/config/claude-para-abogados/hub-constructor/CLAUDE.md`. Mostrar resumen.

```
/hub-constructor:entrevista-inicial
```

---

# Entrevista Inicial: Hub Constructor

## Propósito

Configurar el hub de skills comunitarios — qué registros vigilar, cómo instalar skills nuevos y qué nivel de calidad exigir. Entrevista corta: tres partes, cinco minutos.

## Comprobación de estado

Leer `~/.claude/plugins/config/claude-para-abogados/hub-constructor/CLAUDE.md`:
- **No existe** → iniciar la entrevista.
- **Contiene `<!-- CONFIGURACIÓN PAUSADA EN: -->`** → ofrecer retomar.
- **Contiene marcadores `[PENDIENTE]`** → ofrecer empezar de cero o retomar.
- **Poblado** → ya configurado; saltar salvo `--redo`.

## Comprobar el perfil de empresa compartido

Buscar `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`. Si existe, leerlo y confirmar. Si no, hacer las preguntas de empresa básicas.

## Antes de empezar

> **`hub-constructor` gestiona la instalación, actualización y control de calidad de skills comunitarios para tu entorno legal.** ¿Buscas un módulo de práctica jurídica? Los otros módulos son los que hacen el trabajo legal — este los descubre e instala.
>
> **5 minutos** para configurar registros, preferencias de instalación y criterios de calidad.

## Ritmo de la entrevista

- **2-3 preguntas por turno.** Entrevista corta — no hay documentos semilla.
- **Pausa y reanudación:** "Di 'pausa' y guardaré tu progreso."

## La entrevista

### Apertura

> Voy a configurar cómo descubres, instalas y actualizas skills comunitarios. Tres preguntas rápidas.

### Parte 0: Quién usa esto

> ¿Quién va a gestionar los skills comunitarios?
>
> 1. **Abogado / profesional jurídico** — gestiono mi propio entorno.
> 2. **Responsable de tecnología legal** — gestiono el entorno para un equipo o despacho.
> 3. **Desarrollador de skills** — creo skills y quiero probarlos y publicarlos.

Esto cambia el enfoque:
- **Abogado:** interfaz simple, recomendaciones basadas en práctica, instalación asistida.
- **Responsable tech:** control de versiones, allowlist estricta, despliegue a equipos.
- **Desarrollador:** acceso a QA, testing, publicación en registros.

### Parte 1: Registros de skills comunitarios

> "¿Qué registros de skills quieres vigilar? Un registro es un repositorio donde la comunidad publica skills legales."
>
> Por defecto vigilo el registro principal del ecosistema. ¿Quieres añadir otros?

- **Registros actuales:** ¿Ya tienes registros configurados? Pega URLs o di "solo el principal".
- **Áreas de interés:** ¿Qué tipo de skills te interesan más? (Esto filtra las recomendaciones.)
  - Todos los que haya.
  - Solo los de mi área de práctica (indicar cuál).
  - Solo los verificados/auditados.
- **Frecuencia de comprobación:** ¿Cada cuánto quieres que busque novedades? (Diario, semanal, manual.)

### Parte 2: Preferencias de instalación

> "Cuando encuentre un skill nuevo que encaje con tu perfil, ¿qué hago?"
>
> 1. **Auto-instalar** — lo instalo directamente si pasa los criterios de calidad.
> 2. **Pedir confirmación** — te aviso con un resumen y espero tu OK antes de instalar.
> 3. **Solo notificar** — te aviso de que existe pero no hago nada hasta que tú lo pidas.

- **Actualizaciones:** ¿Y cuando un skill instalado tiene una versión nueva?
  - Mismo criterio que arriba.
  - Diferente (p. ej., auto-actualizar pero pedir confirmación para nuevos).
- **Rollback:** ¿Quieres que guarde la versión anterior al actualizar? (Recomendado: sí.)

Si es responsable tech o despacho: "¿Hay un proceso de aprobación antes de desplegar a los usuarios? Te puedo generar un informe de QA para cada skill antes de desplegarlo."

### Parte 3: Criterios de calidad mínimos

> "¿Qué nivel de calidad exiges a un skill antes de instalarlo?"

- **Licencia:** ¿Aceptas cualquier licencia open source, o solo algunas? (MIT, Apache 2.0, etc.)
- **Documentación:** ¿Exiges que tenga SKILL.md documentado? (Recomendado: sí.)
- **Jurisdicción:** ¿Solo skills adaptados a Panamá, o también internacionales?
- **Autor verificado:** ¿Exiges que el autor esté en una lista de confianza?
- **Tests:** ¿Exiges que el skill tenga tests automatizados?

Si no tiene opinión: "Te pongo los valores por defecto: licencia permisiva (MIT/Apache), documentación obligatoria, skills panameños e internacionales, sin exigir autor verificado ni tests. Los puedes cambiar después."

## Plantilla del perfil de práctica

```markdown
# Perfil: Hub Constructor

*Escrito por la entrevista inicial el [FECHA].*

---

## Quién usa esto

**Rol:** [Abogado / Responsable tech / Desarrollador]

---

## Integraciones disponibles

| Integración | Estado | Alternativa |
|---|---|---|
| Slack | [PENDIENTE] | Notificaciones en línea |
| Tareas programadas | [PENDIENTE] | Comprobación manual |

---

## Registros vigilados

| Registro | URL | Frecuencia | Último check |
|---|---|---|---|
| Principal | [URL] | [Diario/Semanal/Manual] | [fecha] |

**Áreas de interés:** [Todas / Específicas — lista]

---

## Preferencias de instalación

**Skills nuevos:** [Auto-instalar / Pedir confirmación / Solo notificar]
**Actualizaciones:** [Auto-actualizar / Pedir confirmación / Solo notificar]
**Rollback:** [Sí / No]

---

## Criterios de calidad

| Criterio | Valor |
|---|---|
| Licencia | [MIT, Apache 2.0 / Cualquiera / Específicas] |
| Documentación SKILL.md | [Obligatoria / Recomendada] |
| Jurisdicción | [Panamá / Internacional / Ambas] |
| Autor verificado | [Sí / No] |
| Tests automatizados | [Sí / No / Recomendado] |

---

*Re-ejecutar: `/hub-constructor:entrevista-inicial --redo`*
```

## Después de escribir

> **Configurado.** El hub vigilará [N] registros con preferencia [X] para instalaciones.
>
> **Lo que puedo hacer:**
> - **Buscar skills** — `/hub-constructor:buscador-skills`
> - **Instalar un skill** — `/hub-constructor:instalar`
> - **Verificar calidad** — `/hub-constructor:qa`
> - **Ver actualizaciones** — `/hub-constructor:actualizaciones`
>
> **Sugerencia:** Ejecuta `/hub-constructor:buscador-skills` para ver qué hay disponible para tu área.

Cerrar:

> "Tu configuración está en `~/.claude/plugins/config/claude-para-abogados/hub-constructor/CLAUDE.md`. Edítalo directamente o ejecuta `--redo`."

## Modos de fallo

- **No auto-instalar sin confirmación por defecto.** El valor por defecto es "pedir confirmación", no "auto-instalar". Un skill comunitario puede tener calidad variable.
- **No ignorar la licencia.** Un skill con licencia GPL tiene implicaciones si se usa en un producto comercial. Siempre verificar.
- **No asumir que "comunitario" significa "fiable".** Un skill comunitario puede tener errores, citas inventadas o razonamiento incorrecto. El QA es el filtro.
- **No mezclar roles.** Un desarrollador necesita herramientas de testing; un abogado necesita que funcione. No dar herramientas de desarrollo a quien quiere resultados.
