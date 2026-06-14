<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin se almacena en una ruta independiente de versión que sobrevive a actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/privacidad/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración de esa ruta. No de este archivo.
2. Si ese archivo no existe o aún contiene marcadores [PLACEHOLDER], DETENERSE antes de hacer trabajo sustantivo. Decir: "Este plugin necesita configuración antes de generar resultados útiles. Ejecuta /privacidad:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica real." NO proceder con configuración por defecto o placeholder. Los únicos skills que funcionan sin configuración son /privacidad:entrevista-inicial y cualquier flag --verificar-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua de caché
   (~/.claude/plugins/cache/claude-para-abogados/privacidad/<versión>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa se encuentran en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md` — un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Privacidad y Protección de Datos

*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta entonces, es
una plantilla. Si ves valores `[PLACEHOLDER]` abajo, ejecuta `/privacidad:entrevista-inicial`
para ser entrevistado.*

*Una vez poblado: edita este archivo directamente. Cada skill de este plugin lo lee
antes de hacer nada. Corrige algo aquí y queda corregido en todas partes.*

---

## Quiénes somos

[Nombre de la Empresa / Despacho] es [tipo de entidad]. El equipo de privacidad y protección de datos lo forman [N] personas. [Nombre del responsable / encargado de protección de datos] es el punto final de escalado.

*(Datos de empresa proceden de perfil-empresa.md — editar allí para cambiar en todos los plugins.)*

**Lo que más duele:** [PLACEHOLDER — lo que el equipo dijo que les duele, en sus propias palabras]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna / encargado de datos interno | encargado de datos externo]

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a idóneo/a | Encargado de protección de datos | Compliance officer | No jurista con acceso a letrado | No jurista sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado/a]

---

## Rol en el tratamiento de datos

**Condición principal:** [PLACEHOLDER — Responsable del tratamiento | Encargado del tratamiento | Corresponsable]

**Detalle por actividad principal:**

| Actividad de tratamiento | Rol (R/E/CR) | Base jurídica | Categorías de datos |
|---|---|---|---|
| [PLACEHOLDER — ej., "Gestión de clientes/CRM"] | [R] | [PLACEHOLDER — ej., "Ejecución de la relación contractual (Ley 81 de 2019)"] | [PLACEHOLDER — ej., "Identificativos, contacto, financieros"] |
| [PLACEHOLDER — ej., "Gestión de empleados/RRHH"] | [R] | [PLACEHOLDER — ej., "Obligación legal + ejecución del contrato de trabajo (Ley 81 de 2019)"] | [PLACEHOLDER — ej., "Identificativos, financieros, salud (incapacidad)"] |
| [PLACEHOLDER — ej., "Prestación de servicio SaaS"] | [E] | [PLACEHOLDER — ej., "Contrato de encargado de tratamiento (Ley 81 de 2019)"] | [PLACEHOLDER] |
| [PLACEHOLDER] | | | |

---

## Encargado de Protección de Datos / Oficial de Datos

**Designación obligatoria:** [PLACEHOLDER — la designación de Oficial/Enlace de Protección de Datos es obligatoria solo para el SECTOR PÚBLICO (Decreto Ejecutivo 285 de 2021); para el sector privado es voluntaria/recomendada y atenúa la eventual sanción]

**Tipo:** [PLACEHOLDER — Interno | Externo]
**Nombre:** [PLACEHOLDER]
**Datos de contacto:** [PLACEHOLDER — email, teléfono]
**Comunicación a la ANTAI:** [PLACEHOLDER — ej., "Registrado ante la ANTAI con fecha DD/MM/AAAA" [verificar]]

**Funciones:**
- Informar y asesorar al responsable/encargado
- Supervisar el cumplimiento de la Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021
- Cooperar con la ANTAI como punto de contacto
- [PLACEHOLDER — funciones adicionales asignadas]

---

## Registro de actividades de tratamiento (RAT)

**Estado:** [PLACEHOLDER — ej., "Actualizado a fecha DD/MM/AAAA; revisión semestral"]
**Ubicación:** [PLACEHOLDER — ej., "Documento en Drive / herramienta de compliance X / Excel compartido"]
**Responsable de actualización:** [PLACEHOLDER]

**Tratamientos registrados:** [PLACEHOLDER — ej., "15 actividades de tratamiento como responsable; 8 como encargado"]

**Revisión periódica:** [PLACEHOLDER — ej., "Semestral; obligatoria ante cualquier nueva actividad de tratamiento, nuevo proveedor con acceso a datos, o cambio de base de licitud"]

---

## Bases jurídicas habituales

> En Panamá, la Ley 81 de 2019 articula el tratamiento en torno al **consentimiento del titular** como base principal, admitiendo otras causas de licitud (cumplimiento de obligación legal, ejecución de relación contractual, fuentes de acceso público, etc.). La referencia a los artículos concretos debe verificarse en la Ley 81 de 2019 y en el Decreto Ejecutivo 285 de 2021.

| Base jurídica | Referencia (Ley 81 de 2019) | Uso principal | Notas |
|---|---|---|---|
| Consentimiento del titular | Ley 81 de 2019 | [PLACEHOLDER — ej., "Marketing, comunicaciones comerciales"] | [PLACEHOLDER — ej., "Libre, informado, específico, inequívoco y revocable; conservar prueba"] |
| Ejecución de relación contractual | Ley 81 de 2019 | [PLACEHOLDER — ej., "Prestación del servicio, gestión de clientes"] | |
| Cumplimiento de obligación legal | Ley 81 de 2019 | [PLACEHOLDER — ej., "Planillas, facturación, prevención de blanqueo (Ley 23 de 2015)"] | [PLACEHOLDER — ej., "Identificar la norma concreta"] |
| Otras causas de licitud | Ley 81 de 2019 | [PLACEHOLDER — ej., "Prevención de fraude, seguridad, fuentes de acceso público"] | [PLACEHOLDER — ej., "Documentar la justificación"] |
| Protección de la vida o salud del titular | Ley 81 de 2019 | [PLACEHOLDER — ej., "Emergencias sanitarias"] | Uso excepcional |
| Interés público / función estatal | Ley 81 de 2019 | [PLACEHOLDER — ej., "Solo si entidad pública"] | |

**Datos sensibles (Ley 81 de 2019):**
- [PLACEHOLDER — ej., "Datos de salud de empleados (incapacidades) — base: cumplimiento de obligación legal; afiliación sindical de representantes — tratamiento conforme a la Ley 81 de 2019"]

---

## Transferencias internacionales

**¿Se realizan transferencias internacionales de datos (fuera de Panamá)?** [PLACEHOLDER — Sí / No]

> La Ley 81 de 2019 y el Decreto Ejecutivo 285 de 2021 regulan la transferencia y comunicación internacional de datos: requieren que el destino ofrezca un nivel de protección equivalente o superior, o que concurran condiciones habilitantes (consentimiento del titular, contrato, etc.).

**Mecanismos utilizados:**

| Destino | Proveedor/Receptor | Mecanismo | Estado |
|---|---|---|---|
| [PLACEHOLDER — ej., "EE.UU."] | [PLACEHOLDER — ej., "AWS, Google, Microsoft"] | [PLACEHOLDER — ej., "Consentimiento del titular / cláusulas contractuales conforme a la Ley 81 de 2019"] | [PLACEHOLDER — ej., "Vigente; monitorizar"] |
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER — ej., "Cláusulas contractuales de protección de datos"] | [PLACEHOLDER] |
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER — ej., "País con nivel adecuado de protección" [verificar]] | [PLACEHOLDER] |

**Evaluación de las transferencias:** [PLACEHOLDER — ej., "Documentada para transferencias a EE.UU.; revisar periódicamente"]

---

## Encargos de tratamiento — Playbook

**Posición como responsable (contratamos encargados):**

**Cláusulas mínimas exigidas (encargo de tratamiento, Ley 81 de 2019):**
- [ ] Objeto, duración, naturaleza y finalidad del tratamiento
- [ ] Tipo de datos personales y categorías de titulares
- [ ] Obligación de tratar solo siguiendo instrucciones documentadas del responsable
- [ ] Deber de confidencialidad del personal
- [ ] Medidas de seguridad técnicas y organizativas
- [ ] Régimen de subencargados (autorización previa general/específica + notificación)
- [ ] Asistencia al responsable en derechos de los titulares
- [ ] Asistencia en la evaluación de impacto
- [ ] Devolución o supresión de datos al finalizar
- [ ] Información y auditoría

**Posición ante subencargados:** [PLACEHOLDER — ej., "Autorización general con derecho de oposición en 15 días; lista accesible de subencargados; el encargado responde del subencargado"]

**Modelo house de contrato de encargado:** [PLACEHOLDER — ej., "Basado en plantilla interna conforme a la Ley 81 de 2019; adaptado por el equipo jurídico"]

**Posición como encargado (nos contratan como encargados):**
- [PLACEHOLDER — ej., "Usar nuestro modelo house; aceptar modelo del cliente con revisión previa; nunca aceptar responsabilidad ilimitada como encargado"]

---

## Derechos del titular (ARCO + portabilidad)

> Derechos del titular: acceso, rectificación, cancelación (supresión) y oposición (art. 15 de la Ley 81 de 2019); también se reconoce la portabilidad. Plazo de respuesta: **10 días hábiles** desde la presentación de la solicitud (art. 16 de la Ley 81 de 2019; Decreto Ejecutivo 285 de 2021, art. 15). El suministro de información es **gratuito** (art. 16). Nota: la Ley 81 no prevé prórroga general por complejidad ni la excepción del RGPD por "solicitudes manifiestamente infundadas o excesivas".

| Derecho | Referencia | Plazo de respuesta | Formulario | Responsable |
|---|---|---|---|---|
| Acceso | Art. 15 de la Ley 81 de 2019 | 10 días hábiles (art. 16) | [PLACEHOLDER] | [PLACEHOLDER] |
| Rectificación | Art. 15 de la Ley 81 de 2019 | 10 días hábiles (art. 16) | [PLACEHOLDER] | [PLACEHOLDER] |
| Cancelación / Supresión | Art. 15 de la Ley 81 de 2019 | 10 días hábiles (art. 16) | [PLACEHOLDER] | [PLACEHOLDER] |
| Oposición | Art. 15 de la Ley 81 de 2019 | 10 días hábiles (art. 16) | [PLACEHOLDER] | [PLACEHOLDER] |
| Portabilidad | Art. 15 de la Ley 81 de 2019 | 10 días hábiles (art. 16) | [PLACEHOLDER] | [PLACEHOLDER] |

**Canal de recepción:** [PLACEHOLDER — ej., "Email datos@empresa.com; formulario web; correo postal"]
**Verificación de identidad:** [PLACEHOLDER — ej., "Solicitar copia de cédula o pasaporte/carné de residente; verificar contra registros internos"]
**Proceso de respuesta:** [PLACEHOLDER — ej., "Encargado de datos recibe → verifica identidad (24h) → localiza datos (5 días) → prepara respuesta → firma responsable → envía al titular"]

**Excepciones a la supresión:** [PLACEHOLDER — ej., "Obligaciones legales (conservación fiscal/contable según el Código de Comercio y la legislación tributaria de la DGI; prevención de blanqueo: Ley 23 de 2015)"]

---

## Evaluación de Impacto (EIPD)

**Naturaleza (Ley 81 de 2019 y Decreto Ejecutivo 285 de 2021):** la EIPD está definida (Decreto Ejecutivo 285 de 2021, art. 1.9) pero **NO es obligatoria con carácter general** para todo tratamiento de alto riesgo (no rige el modelo del art. 35 del RGPD). En Panamá es una **buena práctica voluntaria** del responsable (art. 8 de la Ley 81 de 2019) y **solo deviene exigible si la ANTAI la ordena** en función de la gravedad del riesgo o la novedad tecnológica (art. 41 del Decreto Ejecutivo 285 de 2021). Para evaluar el riesgo se atiende a los **9 factores del art. 36 del Decreto Ejecutivo 285 de 2021**.

**Situaciones a valorar (factores de riesgo del art. 36; la ANTAI puede ordenar la EIPD, art. 41):**
- [ ] Elaboración de perfiles con efectos jurídicos o significativos
- [ ] Tratamiento a gran escala de datos sensibles
- [ ] Observación sistemática a gran escala de zonas públicas
- [PLACEHOLDER — supuestos adicionales aplicables al negocio]

**Formato house:** [PLACEHOLDER — ej., "Plantilla interna adaptada a la Ley 81 de 2019"]

**Proceso:**
1. [PLACEHOLDER — ej., "Identificar necesidad de evaluación de impacto (checklist)"]
2. [PLACEHOLDER — ej., "Describir tratamiento y evaluar necesidad/proporcionalidad"]
3. [PLACEHOLDER — ej., "Identificar y evaluar riesgos"]
4. [PLACEHOLDER — ej., "Determinar medidas para mitigar riesgos"]
5. [PLACEHOLDER — ej., "Consulta al encargado de protección de datos"]
6. [PLACEHOLDER — ej., "Aprobación interna y registro de la evaluación"] (Nota: en Panamá NO existe la "consulta previa" a la ANTAI del art. 36 del RGPD; lo que sí puede ocurrir es que la ANTAI ordene una EIPD conforme al art. 41 del Decreto Ejecutivo 285 de 2021.)

---

## Brechas de seguridad — Protocolo

**Obligación de notificación:** 72 horas desde el conocimiento del incidente (art. 37 del Decreto Ejecutivo 285 de 2021). Cuando la violación represente un **riesgo** (umbral único, no "alto riesgo"), se notifica **conjuntamente a la ANTAI y a los titulares afectados** en ese mismo plazo de 72 horas.

**Protocolo interno:**

| Fase | Plazo | Responsable | Acción |
|---|---|---|---|
| Detección | Inmediato | Cualquier empleado | Comunicar al encargado de datos / equipo de seguridad |
| Evaluación inicial | <12h | [PLACEHOLDER — Encargado de datos + IT] | Clasificar severidad, datos afectados, titulares afectados |
| Notificación a ANTAI y a titulares | 72 horas (art. 37 del Decreto Ejecutivo 285 de 2021) | [PLACEHOLDER — Encargado de datos + Comunicación] | Si hay riesgo, notificar conjuntamente a la ANTAI y a los titulares afectados |
| Documentación | Toda brecha (art. 38 del Decreto Ejecutivo 285 de 2021) | [PLACEHOLDER] | Registro interno: fecha, motivo, hechos y efectos, medidas correctivas |
| Post-mortem | <30 días | [PLACEHOLDER] | Análisis de causa raíz y medidas correctivas |

**Canal de notificación ANTAI:** [PLACEHOLDER — ej., "Portal o formulario de notificación de brechas de la ANTAI"]

**Plantilla de comunicación a titulares:** [PLACEHOLDER — ej., "Modelo house aprobado; incluir: naturaleza de la brecha, datos de contacto del encargado de datos, consecuencias probables, medidas adoptadas y recomendadas"]

---

## Política de privacidad

### Web

**Estado:** [PLACEHOLDER — ej., "Publicada en [URL]; última revisión DD/MM/AAAA"]
**Contenido mínimo (Ley 81 de 2019):**
- [ ] Identidad y datos de contacto del responsable
- [ ] Datos de contacto del encargado de protección de datos
- [ ] Fines y bases de licitud de cada tratamiento
- [ ] Destinatarios o categorías de destinatarios
- [ ] Transferencias internacionales y garantías
- [ ] Plazos de conservación o criterios
- [ ] Derechos del titular y cómo ejercerlos
- [ ] Derecho a reclamar ante la ANTAI
- [ ] Existencia de decisiones automatizadas

### Política de cookies

**Estado:** [PLACEHOLDER — ej., "Banner implementado con [herramienta]; informa del uso de cookies conforme a la Ley 81 de 2019"]
**Herramienta de gestión de consentimiento (CMP):** [PLACEHOLDER — ej., "Cookiebot / OneTrust / CookieYes / desarrollo propio"]
**Posición:** [PLACEHOLDER — ej., "Solo cookies técnicas sin consentimiento; resto requiere consentimiento previo, granular y revocable; no cookie walls"]

### Empleados

**Cláusula informativa en contrato de trabajo:** [PLACEHOLDER — ej., "Modelo house; incluye videovigilancia, geolocalización y control de dispositivos, conforme al Código de Trabajo de Panamá y a la Ley 81 de 2019"]

### Apps móviles

**Estado:** [PLACEHOLDER — ej., "Política integrada en la app; permisos solicitados con just-in-time notice"]

---

## Matriz de escalado

| Puede resolver | Sin escalar | Escala a | Vía |
|---|---|---|---|
| [Analista/asistente legal] | [PLACEHOLDER — ej., "Ejercicio de derechos rutinario, actualización del registro de actividades"] | [Encargado de datos / Abogado/a] | [método] |
| [Encargado de datos / Abogado/a] | [PLACEHOLDER — ej., "Evaluaciones de impacto, contratos de encargado, consultas de bases de licitud"] | [Responsable jurídico / Socio/a] | [método] |
| [Responsable jurídico] | [PLACEHOLDER — ej., "Brechas sin riesgo alto, actuaciones de rutina de la ANTAI"] | [Comité dirección / despacho externo] | [método] |

**Escalados automáticos:**
- [PLACEHOLDER — ej., "Toda brecha con riesgo alto, toda resolución sancionadora de la ANTAI, toda transferencia internacional nueva, tratamiento de datos biométricos"]

---

## Legislación de referencia

Las siguientes normas son la base del análisis de este plugin:

- **Ley 81 de 2019** — Sobre Protección de Datos Personales (Gaceta Oficial de Panamá)
- **Decreto Ejecutivo 285 de 2021** — que reglamenta la Ley 81 de 2019
- **Resoluciones y guías de la ANTAI** — Autoridad Nacional de Transparencia y Acceso a la Información, autoridad de control en materia de protección de datos
- **Ley 23 de 2015** — prevención del blanqueo de capitales, financiamiento del terrorismo y de la proliferación de armas de destrucción masiva — plazos de conservación (sujetos obligados ante la UAF)
- **Código de Comercio de Panamá** y legislación tributaria (DGI) — plazos de conservación contable y fiscal
- **Referencia comparada (no vinculante en Panamá):** RGPD (Reglamento UE 2016/679) y directrices del CEPD, citados únicamente como criterio internacional orientativo

---

## Postura ante juicios subjetivos

Cuando un skill de este plugin afronta un juicio subjetivo y la respuesta es incierta, el skill **prefiere el error recuperable**: marca la línea con `[revisión]` inline. Infra-marcar es una puerta de un solo sentido; sobre-marcar es una puerta de dos sentidos que un letrado cierra en 30 segundos.

---

*Para volver a ejecutar la entrevista: `/privacidad:entrevista-inicial --repetir`*
