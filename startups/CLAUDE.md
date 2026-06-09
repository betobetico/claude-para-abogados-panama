<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin vive en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/startups/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de generar output útil. Ejecuta
   /startups:cold-start-interview — lleva unos 10 minutos y todos los comandos dependen de ella.
   Sin configurar, las respuestas serán genéricas y pueden no ajustarse a tu situación."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin setup
   son /startups:cold-start-interview y cualquier flag --check-integrations.
3. El setup y cold-start-interview ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta
   antigua de caché (~/.claude/plugins/cache/claude-para-abogados/startups/<version>/CLAUDE.md
   para cualquier versión) pero no en la ruta de config, copiarlo a la ruta de config antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la config. Se reemplaza en cada actualización. Nunca escribir datos de
   usuario aquí.

**Perfil de empresa compartido.** Los datos a nivel de empresa (quién eres, qué haces, dónde operas,
tu postura de riesgo, personas clave) viven en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes del perfil de
práctica de este plugin. Si no existe, el setup de este plugin lo creará.
-->

# Perfil de Práctica — Startups

*Escrito por la cold-start interview. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/startups:cold-start-interview`.*

---

## Quiénes somos

*El nombre de la empresa, sector, tamaño y jurisdicciones vienen de `perfil-empresa.md` — edita allí
para cambiar en todos los plugins. Los campos específicos de startups van aquí.*

[Empresa] es una startup en fase [PLACEHOLDER — ideación / pre-seed / seed / serie A / growth].
Sector: [PLACEHOLDER]. Fundadores: [PLACEHOLDER — nombres]. Domicilio social: [PLACEHOLDER — provincia].

**Entorno de práctica:** [PLACEHOLDER — Fundador sin abogado | Fundador con abogado externo | Abogado de startup | Despacho especializado en startups]
*(Desde perfil-empresa.md — edita allí para cambiar en todos los plugins)*

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a | Fundador/a con acceso a abogado | Fundador/a sin acceso a abogado]
**Contacto de abogado:** [PLACEHOLDER — Nombre / despacho / N/A si es abogado]

---

## Fase de la startup

| Campo | Valor |
|---|---|
| Fase actual | [PLACEHOLDER — Ideación / Pre-seed / Seed / Serie A / Growth] |
| Fecha de constitución | [PLACEHOLDER — o "pendiente"] |
| Empleados | [PLACEHOLDER] |
| Facturación último ejercicio | [PLACEHOLDER — o "pre-revenue"] |
| Régimen de incentivos (SEM / Ciudad del Saber / otro) | [PLACEHOLDER — Sí/No/Pendiente de licencia] |

---

## Constitución

| Campo | Valor |
|---|---|
| Forma jurídica | [PLACEHOLDER — S.A. / S. de R.L. / pendiente] |
| Capital social | [PLACEHOLDER — sin mínimo legal exigido para S.A.; capital autorizado habitual USD 10,000 [verificar]] |
| Pacto social | [PLACEHOLDER — estándar / personalizado / ruta al documento] |
| Objeto social | [PLACEHOLDER] |
| Agente residente | [PLACEHOLDER — abogado o firma idónea, obligatorio para S.A.] |
| Disponibilidad de denominación | [PLACEHOLDER — verificada en Registro Público Sí/No, fecha] |
| Notaría | [PLACEHOLDER] |
| Inscripción en el Registro Público de Panamá | [PLACEHOLDER — completada Sí/No, ficha/documento/asiento] |

*Referencia: Ley 32 de 1927 (sociedades anónimas); Ley 4 de 2009 [verificar] (S. de R.L.); Código de Comercio de Panamá.*

---

## Pacto de accionistas

| Cláusula | Incluida | Detalle |
|---|---|---|
| Vesting | [PLACEHOLDER] | [PLACEHOLDER — periodo, cliff, aceleración] |
| Good/bad leaver | [PLACEHOLDER] | [PLACEHOLDER — valoración en cada caso] |
| Arrastre (drag-along) | [PLACEHOLDER] | [PLACEHOLDER — umbrales] |
| Acompañamiento (tag-along) | [PLACEHOLDER] | |
| Anti-dilución | [PLACEHOLDER] | [PLACEHOLDER — full ratchet / weighted average] |
| Derecho de adquisición preferente | [PLACEHOLDER] | |
| Bloqueo (lock-up) | [PLACEHOLDER] | [PLACEHOLDER — periodo] |
| Deadlock | [PLACEHOLDER] | [PLACEHOLDER — mecanismo de resolución] |
| No competencia | [PLACEHOLDER] | [PLACEHOLDER — duración, ámbito] |

**Ubicación del pacto:** [PLACEHOLDER — ruta al documento]

---

## Equity e incentivos

| Mecanismo | Estado | Detalle |
|---|---|---|
| Stock options | [PLACEHOLDER] | [PLACEHOLDER — plan aprobado, beneficiarios, precio de ejercicio] |
| Phantom shares | [PLACEHOLDER] | |
| Carried interest | [PLACEHOLDER] | |

**Régimen fiscal stock options:**
- Tributación por ISR como remuneración en el momento que corresponda según la legislación panameña [verificar]
- Aplicación del principio de territorialidad: rentas de fuente panameña [verificar]
- [PLACEHOLDER — aplicabilidad a nuestra empresa: Sí/No]

*Referencia: Código Fiscal (ISR); legislación laboral y societaria panameña [verificar].*

---

## Rondas de inversión

| Ronda | Estado | Importe | Valoración | Instrumento |
|---|---|---|---|---|
| [PLACEHOLDER] | | | | [PLACEHOLDER — equity, nota convertible, SAFE] |

**Documentos tipo:**

| Documento | Ubicación | Notas |
|---|---|---|
| Term sheet modelo | [PLACEHOLDER] | |
| SHA (Shareholders Agreement) | [PLACEHOLDER] | |
| Nota convertible | [PLACEHOLDER] | |
| SAFE adaptado | [PLACEHOLDER] | |

**Cap table:** [PLACEHOLDER — ruta a la cap table actualizada o herramienta utilizada]

---

## Incentivos y regímenes especiales

| Incentivo | Aplicable | Detalle |
|---|---|---|
| Régimen SEM (Sede de Empresa Multinacional) | [PLACEHOLDER] | Ley 41 de 2007 [verificar] |
| Ciudad del Saber | [PLACEHOLDER] | Decreto Ley 6 de 1998 [verificar] |
| Zona Libre de Colón | [PLACEHOLDER] | [verificar] |
| Panamá Pacífico | [PLACEHOLDER] | Ley 41 de 2004 [verificar] |
| EMMA (manufactura multinacional) | [PLACEHOLDER] | Ley 159 de 2020 [verificar] |
| Visa de inversionista para fundadores extranjeros | [PLACEHOLDER — solicitada / obtenida / no aplica] | |

*Referencia: regímenes de incentivos y zonas económicas especiales de Panamá [verificar].*

---

## Primeras contrataciones

| Campo | Valor |
|---|---|
| Plantilla actual | [PLACEHOLDER] |
| Régimen laboral aplicable | [PLACEHOLDER — Código de Trabajo / régimen especial de zona] |
| Tipos de contrato usados | [PLACEHOLDER — indefinido, por tiempo definido, por obra determinada] |
| Practicantes/pasantes | [PLACEHOLDER — convenio con universidad, Sí/No] |
| Independientes/contratistas | [PLACEHOLDER — riesgo de relación laboral encubierta evaluado Sí/No] |
| Teletrabajo | [PLACEHOLDER — acuerdo de teletrabajo firmado, Ley 126 de 2020 [verificar]] |

*Referencia: Código de Trabajo de Panamá; Ley 126 de 2020 sobre teletrabajo [verificar].*

---

## Propiedad intelectual para startups

| Campo | Valor |
|---|---|
| Titularidad del código | [PLACEHOLDER — cesión de empleados y de contratistas conforme a la legislación de derecho de autor] |
| Contratos de cesión IP firmados | [PLACEHOLDER] |
| NDAs modelo | [PLACEHOLDER — ruta] |
| Marcas registradas | [PLACEHOLDER — DIGERPI] |
| Dominios | [PLACEHOLDER] |

*Referencia: Ley 64 de 2012 (derecho de autor); Ley 35 de 1996 (propiedad industrial).*

---

## Protección de datos para startups

**Mínimo viable de compliance:**

| Elemento | Estado |
|---|---|
| Política de privacidad publicada | [PLACEHOLDER] |
| Registro de actividades de tratamiento | [PLACEHOLDER] |
| Base jurídica identificada por tratamiento | [PLACEHOLDER] |
| Consentimiento para cookies | [PLACEHOLDER] |
| Contrato de encargado con proveedores clave | [PLACEHOLDER] |
| Cláusulas informativas en formularios | [PLACEHOLDER] |

*Referencia: Ley 81 de 2019 (protección de datos personales); Decreto Ejecutivo 285 de 2021.*

---

## Integraciones disponibles

| Integración | Estado | Fallback si no disponible |
|---|---|---|
| Almacenamiento (Drive / SharePoint) | [PLACEHOLDER] | Outputs guardados localmente |
| Slack / Teams | [PLACEHOLDER] | Notificaciones entregadas inline |
| Tareas programadas | [PLACEHOLDER] | Revisiones bajo demanda |

*Re-comprobar: `/startups:cold-start-interview --check-integrations`*

---

## Outputs

**Carpeta de outputs:** [PLACEHOLDER — donde se guardan pactos, actas, informes]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Cabecera de trabajo:**

- Si el Rol es Abogado/a: `CONFIDENCIAL — TRABAJO PROFESIONAL — PREPARADO BAJO DIRECCIÓN LETRADA`
- Si el Rol es Fundador/a o no jurista: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON ABOGADO ANTES DE ACTUAR`

---

## Legislación de referencia

| Norma | Referencia | Ámbito |
|---|---|---|
| Ley de sociedades anónimas | Ley 32 de 1927 | Sociedades anónimas (S.A.) |
| Ley de S. de R.L. | Ley 4 de 2009 [verificar] | Sociedades de responsabilidad limitada |
| Código de Comercio | Código de Comercio de Panamá | Disposiciones mercantiles generales |
| Código Fiscal | ISR — principio de territorialidad [verificar] | Incentivos y tributación |
| Régimen SEM | Ley 41 de 2007 [verificar] | Sedes de empresas multinacionales |
| Código de Trabajo | Código de Trabajo de Panamá | Relaciones laborales |
| Derecho de autor | Ley 64 de 2012 | Propiedad intelectual (cesión código) |

---

*Re-ejecutar: `/startups:cold-start-interview --redo`*
