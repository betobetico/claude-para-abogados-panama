<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/gobernanza-ia/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /gobernanza-ia:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /gobernanza-ia:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/gobernanza-ia/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Gobernanza de Inteligencia Artificial
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/gobernanza-ia:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de gobernanza de IA se quedan aquí.*

[Empresa] es una [tipo de entidad]. Nuestro rol respecto a sistemas de IA es [proveedor / implementador / importador / distribuidor / usuario / combinación].
Desarrollamos o usamos [N] sistemas de IA. El equipo de gobernanza de IA cuenta con [N] personas.
[Responsable de IA / Oficial de protección de datos / Comité de IA: nombre o ninguno]. La escalación va a [nombre].

**Huella regulatoria IA:** [PLACEHOLDER — Panamá no tiene ley de IA vinculante; marco interno de gobernanza + Ley 81 de 2019 [verificar] sobre protección de datos (decisiones automatizadas) + normativa sectorial específica + marcos internacionales de referencia] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Asuntos abiertos de gobernanza IA:** [PLACEHOLDER]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Empresa tecnológica] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a | Profesional jurídico no abogado con acceso a letrado | Profesional no jurídico sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente |
| Slack / Teams | [PLACEHOLDER ✓/✗] | Alertas entregadas inline |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Revisiones solo bajo demanda |
| Registro de sistemas de IA (interno) | [PLACEHOLDER ✓/✗] | Registro manual en hoja de cálculo |

*Re-comprobar: `/gobernanza-ia:entrevista-inicial --check-integraciones`*

---

## Registro de sistemas de IA

| Sistema | Proveedor | Propósito | Categoría de riesgo | Estado | Responsable interno |
|---|---|---|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER — inaceptable/alto/limitado/mínimo] | [PLACEHOLDER — activo/desarrollo/retirado] | [PLACEHOLDER] |
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

**Criterios para inclusión en el registro:** [PLACEHOLDER — qué se considera "sistema de IA" a efectos internos]
**Frecuencia de actualización:** [PLACEHOLDER — trimestral / semestral / ante cambio material]

---

## Clasificación de riesgo según marco interno de referencia

*Panamá no tiene ley de IA vinculante. Esta clasificación por niveles se basa en principios y marcos internacionales de referencia (OCDE, UNESCO, NIST AI RMF, ISO/IEC 42001) adoptados como política interna, no en una norma panameña directamente aplicable. El Reglamento Europeo de IA se cita solo como referencia comparada.*

| Categoría | Definición resumida | Sistemas propios afectados | Acción requerida |
|---|---|---|---|
| Inaceptable | Prácticas vedadas por la política interna: scoring social, manipulación subliminal, explotación de vulnerabilidades, identificación biométrica masiva sin base legal | [PLACEHOLDER] | Prohibición absoluta — retirada inmediata |
| Alto riesgo | Biometría, infraestructuras críticas, educación, empleo, servicios esenciales (incl. scoring crediticio), seguridad, migración, justicia | [PLACEHOLDER] | Sistema de gestión de riesgos, gobernanza de datos, transparencia, supervisión humana, registro interno |
| Limitado | Chatbots, deepfakes, generación de contenido | [PLACEHOLDER] | Obligaciones de transparencia |
| Mínimo | Todo lo demás | [PLACEHOLDER] | Códigos de conducta voluntarios |

**Modelos de IA de propósito general (GPAI):** [PLACEHOLDER — si usamos o desarrollamos modelos GPAI, evaluación de riesgo sistémico según marco interno]

---

## Evaluaciones de impacto de IA

**Cuándo es obligatoria:** [PLACEHOLDER — por política interna: sistemas de alto riesgo, decisiones automatizadas con efectos sobre titulares de datos bajo la Ley 81 de 2019 [verificar], evaluaciones de impacto en derechos de las personas]

| Evaluación | Sistema | Fecha | Resultado | Próxima revisión |
|---|---|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

**Formato estándar:** [PLACEHOLDER — plantilla interna, formato basado en NIST AI RMF / ISO 42001, otro]
**Aprobación:** [PLACEHOLDER — quién firma la evaluación de impacto]

---

## Proveedores de IA — Cláusulas clave

| Cláusula | Nuestra posición estándar | Aceptable | Nunca aceptar |
|---|---|---|---|
| Entrenamiento con nuestros datos | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Responsabilidad por resultados del modelo | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Cambio de modelo sin aviso | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| SLAs de disponibilidad y latencia | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Auditoría del sistema | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Subprocesamiento / subcontratación | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Propiedad intelectual de outputs | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Localización de datos y procesamiento | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

**Línea roja contractual:** [PLACEHOLDER — la cláusula que rompe el acuerdo]

---

## Transparencia y explicabilidad

**Política de transparencia:** [PLACEHOLDER — cómo informamos a los usuarios de que interactúan con IA]
**Obligaciones de transparencia (marco interno):** [PLACEHOLDER — etiquetado de contenido generado, notificación de chatbots]
**Mecanismo de explicabilidad:** [PLACEHOLDER — cómo explicamos las decisiones automatizadas a los afectados]
**Derechos del titular ante decisiones automatizadas (Ley 81 de 2019 [verificar]):** [PLACEHOLDER — proceso implementado]

---

## Supervisión humana

**Política de human-in-the-loop:** [PLACEHOLDER — en qué decisiones se requiere intervención humana]
**Niveles de automatización:** [PLACEHOLDER — totalmente automatizado / semiautomatizado / asistido]
**Mecanismo de override:** [PLACEHOLDER — cómo un humano puede anular la decisión del sistema]
**Registro de intervenciones:** [PLACEHOLDER — dónde se documentan las intervenciones humanas]

---

## Iniciativas y sandbox regulatorio en Panamá

**Participación en sandbox o iniciativa de innovación:** [PLACEHOLDER — sí/no/en evaluación] [verificar]
**Sistemas candidatos:** [PLACEHOLDER]
**Estado de solicitud:** [PLACEHOLDER]
**Contacto institucional (AIG / ANTAI):** [PLACEHOLDER] [verificar]

*Panamá no cuenta a la fecha con una autoridad nacional específica de supervisión de IA ni con una ley de IA vinculante. La AIG (Autoridad Nacional para la Innovación Gubernamental) [verificar] impulsa iniciativas de innovación tecnológica en el sector público, y la ANTAI supervisa la protección de datos personales.*

---

## Política interna de uso de IA generativa

**Existe política aprobada:** [PLACEHOLDER — sí/no/en borrador]
**Ubicación:** [PLACEHOLDER]
**Alcance:** [PLACEHOLDER — toda la organización / departamentos específicos]
**Usos permitidos:** [PLACEHOLDER]
**Usos prohibidos:** [PLACEHOLDER]
**Datos que no se pueden introducir en herramientas de IA:** [PLACEHOLDER — datos personales, secretos empresariales, información confidencial de clientes]
**Revisión y aprobación de outputs:** [PLACEHOLDER — qué requiere revisión humana antes de uso externo]
**Formación:** [PLACEHOLDER — programa de formación en uso responsable de IA]

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Clasificación de nuevo sistema de IA | Equipo de gobernanza IA | — | — |
| Sistema clasificado como alto riesgo | — | Dirección jurídica + Comité de IA | Siempre |
| Incidente de IA (sesgo, error material, daño) | — | Oficial de protección de datos + Dirección jurídica + Dirección | Siempre |
| Requerimiento de la ANTAI u otro supervisor | — | Dirección jurídica + Dirección General | Siempre |
| Nuevo proveedor de IA con acceso a datos | Equipo de gobernanza IA | Oficial de protección de datos | Si datos personales |

---

## Referencias principales

*Panamá no cuenta con una ley de IA vinculante. La gobernanza se apoya en normativa panameña conexa, principios y marcos internacionales de referencia.*

**Normativa panameña conexa**
- **Protección de datos personales** — Ley 81 de 2019 [verificar] y Decreto Ejecutivo 285 de 2021 [verificar]; autoridad: ANTAI
- **Iniciativas/anteproyectos locales en materia de IA** — si procede [verificar]

**Marcos internacionales de referencia (no vinculantes en Panamá, soft law / estándares)**
- **OCDE** — Recomendación del Consejo sobre Inteligencia Artificial
- **UNESCO** — Recomendación sobre la ética de la inteligencia artificial
- **NIST** — AI Risk Management Framework (AI RMF)
- **ISO/IEC 42001** — Sistema de gestión de IA

**Referencia comparada (no aplicable en Panamá)**
- **Reglamento Europeo de IA** — Reglamento (UE) 2024/1689; citado solo como referencia comparada internacional

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Registro de sistemas de IA | [PLACEHOLDER] | [PLACEHOLDER] | |
| Política de uso de IA generativa | [PLACEHOLDER] | [PLACEHOLDER] | |
| Evaluación de impacto de referencia | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan evaluaciones de impacto, revisiones de proveedores y análisis de clasificación]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo:**

- Si el Rol es Abogado/a: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LETRADO — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO COLEGIADO ANTES DE ACTUAR`

---

*Re-ejecutar: `/gobernanza-ia:entrevista-inicial --redo`*
