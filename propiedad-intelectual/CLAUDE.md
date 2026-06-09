<!--
UBICACIÓN DE LA CONFIGURACIÓN

La configuración específica del usuario para este plugin se almacena en una ruta independiente de versión que sobrevive a actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/propiedad-intelectual/CLAUDE.md

Reglas para cada skill, comando y agente de este plugin:
1. LEER la configuración de esa ruta. No de este archivo.
2. Si ese archivo no existe o aún contiene marcadores [PLACEHOLDER], DETENERSE antes de hacer trabajo sustantivo. Decir: "Este plugin necesita configuración antes de generar resultados útiles. Ejecuta /propiedad-intelectual:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica real." NO proceder con configuración por defecto o placeholder. Los únicos skills que funcionan sin configuración son /propiedad-intelectual:entrevista-inicial y cualquier flag --verificar-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua de caché
   (~/.claude/plugins/cache/claude-para-abogados/propiedad-intelectual/<versión>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la
   estructura que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa se encuentran en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md` — un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Propiedad Intelectual e Industrial

*Este archivo lo escribe la entrevista inicial en la primera ejecución. Hasta entonces, es
una plantilla. Si ves valores `[PLACEHOLDER]` abajo, ejecuta `/propiedad-intelectual:entrevista-inicial`
para ser entrevistado.*

*Una vez poblado: edita este archivo directamente. Cada skill de este plugin lo lee
antes de hacer nada. Corrige algo aquí y queda corregido en todas partes.*

---

## Quiénes somos

[Nombre de la Empresa / Despacho] es [tipo de entidad]. El equipo de PI lo forman [N] personas. [Nombre del responsable] es el punto final de escalado. Gestionamos un portfolio de [N] registros activos.

*(Datos de empresa proceden de perfil-empresa.md — editar allí para cambiar en todos los plugins.)*

**Lo que más duele:** [PLACEHOLDER — lo que el equipo dijo que les duele, en sus propias palabras]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Agente o abogado de la propiedad industrial]

---

## Quién usa esto

**Rol:** [PLACEHOLDER — Abogado/a idóneo/a | Agente de la propiedad industrial | No jurista con acceso a letrado | No jurista sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado/a]

---

## Portfolio de registros

### Marcas

| Marca | Territorio | N.º registro | Clase(s) Niza | Vencimiento | Estado |
|---|---|---|---|---|---|
| [PLACEHOLDER] | [DIGERPI/OMPI] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [vigente/pendiente] |

**Alerta de renovación:** [PLACEHOLDER — ej., "6 meses antes del vencimiento"]

### Patentes y modelos de utilidad

| Título | Territorio | N.º solicitud/concesión | Vencimiento | Estado |
|---|---|---|---|---|
| [PLACEHOLDER] | [DIGERPI/PCT] | [PLACEHOLDER] | [PLACEHOLDER] | [vigente/pendiente] |

**Pago de anualidades:** [PLACEHOLDER — ej., "Recordatorio 3 meses antes; gestor externo: [nombre]"]

### Diseños industriales

| Diseño | Territorio | N.º registro | Vencimiento | Estado |
|---|---|---|---|---|
| [PLACEHOLDER] | [DIGERPI] | [PLACEHOLDER] | [PLACEHOLDER] | [vigente/pendiente] |

### Nombres de dominio

| Dominio | Registrador | Vencimiento | Renovación automática |
|---|---|---|---|
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [sí/no] |

---

## Postura de enforcement

**Estrategia general:** [PLACEHOLDER — ej., "Defensa activa de marcas core; vigilancia de nuevas solicitudes en la DIGERPI; acción contra infracciones evidentes"]

**Prioridades de enforcement:**
1. [PLACEHOLDER — ej., "Marcas denominativas principales"]
2. [PLACEHOLDER — ej., "Nombres de dominio confusamente similares"]
3. [PLACEHOLDER — ej., "Uso no autorizado en marketplaces"]

**Presupuesto anual de enforcement:** [PLACEHOLDER]

**Servicio de vigilancia:** [PLACEHOLDER — ej., "CompuMark / Corsearch / vigilancia interna mensual"]

---

## Marcas — Procedimientos por oficina

### DIGERPI (Dirección General del Registro de la Propiedad Industrial)

**Búsqueda previa:** [PLACEHOLDER — ej., "Siempre búsqueda fonética y gráfica en la base de datos de la DIGERPI antes de solicitar"]
**Tasa de solicitud vigente:** [PLACEHOLDER — verificar tarifa oficial de la DIGERPI]
**Plazo de oposición:** [PLACEHOLDER — plazo de oposición desde la publicación, conforme a la Ley 35 de 1996] [verificar]
**Duración del registro:** 10 años renovables [verificar]
**Posición ante oposiciones recibidas:** [PLACEHOLDER — ej., "Contestar siempre; escalar a responsable si oposición de marca notoria"]

### OMPI (Organización Mundial de la Propiedad Intelectual)

**Sistema de Madrid — uso:** [PLACEHOLDER — ej., "Para extensión a otros países; marca base en la DIGERPI"]
**Territorios designados habitualmente:** [PLACEHOLDER — ej., "EE.UU., México, Colombia, China"]

---

## Patentes — Procedimientos

### DIGERPI

**Tipos de protección:** Patente de invención (20 años) / Modelo de utilidad [verificar]
**Informe sobre el estado de la técnica / examen:** [PLACEHOLDER — ej., "Política sobre examen de fondo y tiempos de tramitación ante la DIGERPI"]
**Política de mantenimiento:** [PLACEHOLDER — ej., "Evaluar anualmente la utilidad comercial; abandonar patentes sin explotación tras 5 años"]

### Vía PCT (Tratado de Cooperación en materia de Patentes)

**Uso habitual:** [PLACEHOLDER — ej., "Para invenciones con mercado internacional amplio; entrada en fase nacional en Panamá vía DIGERPI"]
**Agente de patentes:** [PLACEHOLDER]

---

## Derechos de autor (Ley 64 de 2012)

**Obras protegidas principales:** [PLACEHOLDER — ej., "Software, bases de datos, contenido web, materiales de formación, diseños gráficos"]

**Software:**
- Protección: Derecho de autor (Ley 64 de 2012); el software se protege como obra, no por patente [verificar]
- Titularidad: [PLACEHOLDER — ej., "La empresa como titular de los derechos patrimoniales si la obra es creada por empleados en el ejercicio de sus funciones"] [verificar]
- Registro: [PLACEHOLDER — ej., "Registro ante la Dirección Nacional de Derecho de Autor (DIGERPI) para acreditación de autoría y fecha"] [verificar]

**Bases de datos:**
- Protección de las compilaciones y bases de datos originales bajo la Ley 64 de 2012 [verificar]
- Alcance de la protección: [PLACEHOLDER — ej., "Protección de la estructura/selección original; verificar régimen aplicable"] [verificar]

**Cesión de derechos por empleados:**
- Bajo la Ley 64 de 2012, los derechos patrimoniales sobre obras creadas en virtud de relación laboral corresponden, salvo pacto en contrario, al empleador [verificar]
- [PLACEHOLDER — cláusula house adicional en contratos de trabajo]

---

## Secretos empresariales / industriales

**Información clasificada como secreto empresarial:** [PLACEHOLDER — ej., "Algoritmos, bases de clientes, estrategias comerciales, know-how técnico"]

**Medidas razonables de protección adoptadas (régimen de secretos industriales de la Ley 35 de 1996):** [verificar]
- [PLACEHOLDER — ej., "NDAs con empleados y terceros"]
- [PLACEHOLDER — ej., "Control de acceso por niveles"]
- [PLACEHOLDER — ej., "Marcado de documentos como confidenciales"]
- [PLACEHOLDER — ej., "Políticas de seguridad de la información"]

**Protocolo ante obtención/revelación ilícita:**
1. [PLACEHOLDER — ej., "Identificar la fuente de la filtración"]
2. [PLACEHOLDER — ej., "Solicitud de medidas cautelares urgentes ante la jurisdicción competente"] [verificar]
3. [PLACEHOLDER — ej., "Requerimiento extrajudicial al infractor"]
4. [PLACEHOLDER — ej., "Acción judicial por competencia desleal (Ley 45 de 2007)"] [verificar]

---

## Open source — Política de uso

**Posición general:** [PLACEHOLDER — ej., "Uso permitido con aprobación previa; restricción de licencias copyleft en componentes distribuidos"]

**Licencias aceptables sin aprobación:** [PLACEHOLDER — ej., "MIT, BSD-2, BSD-3, Apache 2.0, ISC"]

**Licencias que requieren aprobación:** [PLACEHOLDER — ej., "LGPL, MPL 2.0, CDDL"]

**Licencias prohibidas:** [PLACEHOLDER — ej., "GPL v2/v3, AGPL, SSPL en cualquier componente que se distribuya o se ofrezca como servicio"]

**Proceso de aprobación:** [PLACEHOLDER — ej., "Solicitud a equipo legal con nombre del componente, licencia, uso previsto; respuesta en 48h"]

**Herramienta de escaneo:** [PLACEHOLDER — ej., "FOSSA / Snyk / escaneo manual"]

---

## Cláusulas de PI en contratos

### Cesión vs. licencia

**Posición house (como cedente/licenciante):** [PLACEHOLDER — ej., "Preferir licencia limitada; cesión solo si se paga precio separado por la PI"]

**Posición house (como cesionario/licenciatario):** [PLACEHOLDER — ej., "Exigir cesión plena para desarrollos a medida; licencia amplia para productos estándar"]

### Obra por encargo

**Posición house:** [PLACEHOLDER — ej., "Contrato escrito de cesión (Ley 64 de 2012); especificar modalidades de explotación, ámbito territorial y temporal, remuneración si aplica"] [verificar]

### Empleados (Ley 64 de 2012 / Ley 35 de 1996)

**Cláusula house en contratos de trabajo:** [PLACEHOLDER — ej., "Referencia expresa al régimen de obras creadas en relación laboral de la Ley 64 de 2012 para derecho de autor y al régimen de invenciones laborales de la Ley 35 de 1996"] [verificar]

---

## Requerimientos extrajudiciales

**Formato:** [PLACEHOLDER — ej., "Carta de requerimiento con acuse de recibo y certificación de contenido vía notaría o correo certificado"]

**Estructura house del requerimiento:**
1. Identificación del requirente y sus derechos
2. Descripción de la infracción con pruebas
3. Fundamento jurídico (norma infringida)
4. Petición concreta (cesar, retirar, indemnizar)
5. Plazo para cumplimiento (habitualmente [PLACEHOLDER — ej., "15 días hábiles"])
6. Advertencia de acciones judiciales

**Aprobación necesaria:** [PLACEHOLDER — ej., "Todo requerimiento extrajudicial requiere aprobación del responsable de PI"]

---

## Matriz de escalado

| Puede resolver | Sin escalar | Escala a | Vía |
|---|---|---|---|
| [Junior/paralegal] | [PLACEHOLDER — ej., "Renovaciones rutinarias, vigilancia de marcas"] | [Abogado/a de PI] | [método] |
| [Abogado/a de PI] | [PLACEHOLDER — ej., "Oposiciones, registros nuevos, consultas de licencias"] | [Socio/a responsable] | [método] |
| [Socio/a responsable] | [PLACEHOLDER — ej., "Litigios de PI, enforcement contra terceros, acuerdos de licencia >USD X"] | [Comité / despacho externo] | [método] |

**Escalados automáticos:**
- [PLACEHOLDER — ej., "Toda demanda recibida, toda medida cautelar, negociación de patentes esenciales, licencias FRAND"]

---

## Estilo house

**Formato de informes de PI:** [PLACEHOLDER]
**Citas normativas:** [PLACEHOLDER — ej., "Ley 35 de 1996 para marcas y patentes, Ley 64 de 2012 para derecho de autor"] [verificar]
**Idioma:** [PLACEHOLDER — ej., "Español para registros DIGERPI; inglés/español para OMPI"]

---

## Legislación de referencia

Las siguientes normas son la base del análisis de este plugin:

- **Ley de Propiedad Industrial** — Ley 35 de 1996 (marcas, patentes, modelos de utilidad, diseños industriales y secretos industriales) [verificar]
- **Ley de Derecho de Autor y Derechos Conexos** — Ley 64 de 2012 [verificar]
- **Ley de protección al consumidor y defensa de la competencia** — Ley 45 de 2007 — en lo relativo a actos de imitación, confusión y aprovechamiento de reputación ajena [verificar]
- **Protocolo de Madrid** (marcas internacionales) [verificar]
- **Tratado de Cooperación en materia de Patentes (PCT)** (solicitudes internacionales de patente)
- **Convenio de Berna** y **Convenio de París** (referencias internacionales aplicables en Panamá) [verificar]

*Referencias comparadas (no vinculantes en Panamá): normativa de marcas, diseños y patentes de la Unión Europea, citada solo con fines ilustrativos.*

---

## Postura ante juicios subjetivos

Cuando un skill de este plugin afronta un juicio subjetivo y la respuesta es incierta, el skill **prefiere el error recuperable**: marca la línea con `[revisión]` inline. Infra-marcar es una puerta de un solo sentido; sobre-marcar es una puerta de dos sentidos que un letrado cierra en 30 segundos.

---

*Para volver a ejecutar la entrevista: `/propiedad-intelectual:entrevista-inicial --repetir`*
