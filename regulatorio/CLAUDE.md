<!--
UBICACIÓN DE CONFIGURACIÓN

La configuración específica del usuario para este plugin se encuentra en una ruta independiente de versión
que sobrevive a las actualizaciones del plugin:

  ~/.claude/plugins/config/claude-para-abogados/regulatorio/CLAUDE.md

Reglas para cada skill, comando y agente en este plugin:
1. LEER la configuración desde esa ruta. No desde este archivo.
2. Si ese archivo no existe o todavía contiene marcadores [PLACEHOLDER], PARAR antes de hacer trabajo sustantivo.
   Decir: "Este plugin necesita configuración antes de poder darte resultados útiles. Ejecuta
   /regulatorio:entrevista-inicial — lleva unos 10-15 minutos y todos los comandos de este plugin
   dependen de ella. Sin configuración, los resultados serán genéricos y pueden no ajustarse a tu práctica."
   NO proceder con configuración placeholder o por defecto. Los únicos skills que funcionan sin configuración
   son /regulatorio:entrevista-inicial y cualquier flag --check-integraciones.
3. La configuración y la entrevista-inicial ESCRIBEN en esa ruta, creando directorios padre si es necesario.
4. En la primera ejecución tras una actualización del plugin, si existe un CLAUDE.md poblado en la ruta antigua
   de caché (~/.claude/plugins/cache/claude-para-abogados/regulatorio/<version>/CLAUDE.md para cualquier versión)
   pero no en la ruta de configuración, copiarlo a la ruta de configuración antes de continuar.
5. Este archivo (el que estás leyendo) es la PLANTILLA. Se distribuye con el plugin y muestra la estructura
   que debe tener la configuración. Se reemplaza en cada actualización. Nunca escribir datos de usuario aquí.

**Perfil compartido de empresa.** Los datos a nivel de empresa (quiénes sois, a qué os dedicáis, dónde operáis,
vuestra postura de riesgo, personas clave) están en `~/.claude/plugins/config/claude-para-abogados/perfil-empresa.md`
— un nivel por encima de este archivo, compartido por todos los plugins. Leerlo antes que el perfil de práctica
de este plugin. Si no existe, la configuración de este plugin lo creará.
-->

# Perfil de Práctica — Cumplimiento Regulatorio
*Generado por la entrevista inicial. Hasta entonces, esto es una plantilla — si ves
`[PLACEHOLDER]`, ejecuta `/regulatorio:entrevista-inicial`.*

---

## Quiénes somos

*Nombre de la empresa, sector, tamaño y jurisdicciones provienen de `perfil-empresa.md` — editar allí
para cambiar en todos los plugins. Los campos específicos de cumplimiento regulatorio se quedan aquí.*

[Empresa] es una [tipo de entidad — sociedad mercantil / entidad financiera / operador de telecomunicaciones / etc.].
Operamos en los sectores [PLACEHOLDER]. El equipo de cumplimiento regulatorio cuenta con [N] personas.
[Responsable de cumplimiento: nombre o ninguno]. La escalación va a [nombre].

**Huella regulatoria:** [PLACEHOLDER — sectores regulados que aplican: bancario, valores, seguros, fiduciario, empresas de remesas, casas de cambio, casinos y juegos de suerte y azar, agentes residentes, zonas francas, financieras, etc.] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

**Asuntos regulatorios abiertos:** [PLACEHOLDER]

**Entorno de práctica:** [PLACEHOLDER — Despacho individual/pequeño | Despacho mediano/grande | Asesoría jurídica interna | Administración pública] *(Desde perfil-empresa.md — editar allí para cambiar en todos los plugins)*

---

## Quién usa este plugin

**Rol:** [PLACEHOLDER — Abogado/a | Profesional jurídico no abogado con acceso a letrado | Profesional no jurídico sin acceso a letrado]
**Contacto letrado:** [PLACEHOLDER — Nombre / equipo / despacho externo / N/A si es abogado]

---

## Integraciones disponibles

| Integración | Estado | Alternativa si no disponible |
|---|---|---|
| Almacenamiento documental (Drive / SharePoint) | [PLACEHOLDER ✓/✗] | Resultados guardados localmente; barrido de monitor normativo solo en modo consulta directa |
| Slack / Teams | [PLACEHOLDER ✓/✗] | Alertas regulatorias entregadas inline en vez de publicadas en canal |
| Tareas programadas | [PLACEHOLDER ✓/✗] | Barrido de monitor normativo solo bajo demanda |
| Gaceta Oficial de Panamá / boletines de supervisores (RSS/API) | [PLACEHOLDER ✓/✗] | Consulta manual de fuentes oficiales |

*Re-comprobar: `/regulatorio:entrevista-inicial --check-integraciones`*

---

## Sectores regulados

| Sector | Supervisores principales | Normativa marco | Activo |
|---|---|---|---|
| Bancario | Superintendencia de Bancos de Panamá (SBP) | Ley Bancaria (Decreto Ley 9 de 1998, texto único) [verificar], Ley 23 de 2015 | [PLACEHOLDER ✓/✗] |
| Valores | Superintendencia del Mercado de Valores (SMV) | Texto Único de la Ley del Mercado de Valores (Decreto Ley 1 de 1999), Ley 23 de 2015 | [PLACEHOLDER ✓/✗] |
| Seguros | Superintendencia de Seguros y Reaseguros de Panamá [verificar] | Ley 12 de 2012 (seguros) [verificar], Ley 23 de 2015 | [PLACEHOLDER ✓/✗] |
| Antiblanqueo (sujetos no financieros) | Intendencia de Supervisión y Regulación de Sujetos No Financieros [verificar], UAF | Ley 23 de 2015, Decreto Ejecutivo 363 de 2015 [verificar] | [PLACEHOLDER ✓/✗] |
| Fiduciario / agentes residentes | SBP / Intendencia de Sujetos No Financieros [verificar] | Ley 21 de 2017 (fideicomiso) [verificar], Ley 23 de 2015 | [PLACEHOLDER ✓/✗] |
| Casinos y juegos de suerte y azar | Junta de Control de Juegos [verificar] | Ley 23 de 2015, normativa de la Junta de Control de Juegos [verificar] | [PLACEHOLDER ✓/✗] |
| Zonas económicas especiales | AAUD (Ciudad del Saber), administraciones de Zona Libre de Colón, Panamá Pacífico, régimen SEM [verificar] | Régimen de cada zona + Ley 23 de 2015 | [PLACEHOLDER ✓/✗] |
| [Otro sector] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER ✓/✗] |

---

## Supervisores relevantes

| Supervisor | Ámbito | Contacto habitual | Procedimientos abiertos |
|---|---|---|---|
| Superintendencia de Bancos de Panamá (SBP) | Bancos, fiduciarias y empresas reguladas | [PLACEHOLDER] | [PLACEHOLDER] |
| SMV (Superintendencia del Mercado de Valores) | Mercado de valores | [PLACEHOLDER] | [PLACEHOLDER] |
| UAF (Unidad de Análisis Financiero) | Inteligencia financiera y ROS | [PLACEHOLDER] | [PLACEHOLDER] |
| Superintendencia de Seguros y Reaseguros [verificar] | Seguros y reaseguros | [PLACEHOLDER] | [PLACEHOLDER] |
| Intendencia de Supervisión de Sujetos No Financieros [verificar] | Sujetos obligados no financieros | [PLACEHOLDER] | [PLACEHOLDER] |
| ACODECO | Protección al consumidor y competencia | [PLACEHOLDER] | [PLACEHOLDER] |
| [Otro supervisor] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Fuentes normativas monitorizadas

| Fuente | Tipo | Frecuencia de consulta | Filtros aplicados |
|---|---|---|---|
| Gaceta Oficial de Panamá | Legislación nacional | [PLACEHOLDER — diaria/semanal] | [PLACEHOLDER — secciones, materias] |
| Acuerdos de la Superintendencia de Bancos (SBP) | Normativa prudencial y antiblanqueo | [PLACEHOLDER] | [PLACEHOLDER] |
| Acuerdos y opiniones de la SMV | Normativa de mercado de valores | [PLACEHOLDER] | [PLACEHOLDER] |
| Guías, tipologías y avisos de la UAF | Inteligencia financiera | [PLACEHOLDER] | [PLACEHOLDER] |
| Resoluciones de la Sala Tercera de lo Contencioso-Administrativo (CSJ) | Jurisprudencia administrativa | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Biblioteca de políticas internas

| Política | Ubicación | Última revisión | Próxima revisión | Responsable |
|---|---|---|---|---|
| Política de cumplimiento normativo | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| Manual de prevención de blanqueo de capitales (Ley 23 de 2015) | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | Oficial de cumplimiento |
| Manual de debida diligencia del cliente (KYC) y tratamiento de PEP | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | Oficial de cumplimiento |
| Código de conducta | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |
| [Otra política] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Umbral de materialidad

*Define qué cambio normativo requiere acción inmediata vs. seguimiento ordinario.*

| Nivel | Criterio | Acción | Plazo |
|---|---|---|---|
| 🔴 Crítico | Cambio que afecta directamente a la operativa o licencia; sanción posible por incumplimiento | Alerta inmediata + análisis de impacto urgente | 24-48 horas |
| 🟠 Alto | Nueva obligación con plazo de adaptación < 6 meses | Análisis de gaps + plan de acción | 1 semana |
| 🟡 Medio | Modificación relevante con plazo de adaptación > 6 meses | Seguimiento + planificación | 1 mes |
| 🟢 Bajo | Cambio informativo o de impacto marginal | Registro + revisión periódica | Próximo ciclo |

**Criterios adicionales de materialidad:** [PLACEHOLDER — umbrales cuantitativos, criterios específicos del sector]

---

## Proceso de gaps regulatorios

```
Detección → Análisis de impacto → Propuesta de adaptación → Aprobación interna → Implementación → Verificación
```

| Fase | Responsable | Plazo estándar | Documentación |
|---|---|---|---|
| Detección | [PLACEHOLDER] | Continua | Alerta normativa |
| Análisis de impacto | [PLACEHOLDER] | [PLACEHOLDER] días | Informe de gaps |
| Propuesta de adaptación | [PLACEHOLDER] | [PLACEHOLDER] días | Memo de propuesta |
| Aprobación interna | [PLACEHOLDER] | [PLACEHOLDER] días | Acta de aprobación |
| Implementación | [PLACEHOLDER] | [PLACEHOLDER] días | Plan de implementación |
| Verificación | [PLACEHOLDER] | [PLACEHOLDER] días | Informe de cierre |

---

## Calendario regulatorio

| Obligación | Periodicidad | Plazo | Modelo/Formato | Supervisor destinatario |
|---|---|---|---|---|
| [PLACEHOLDER — p.ej. informe anual del oficial de cumplimiento] | Anual | [PLACEHOLDER] | [PLACEHOLDER] | SBP / SMV / Intendencia |
| [PLACEHOLDER — p.ej. reporte de operación sospechosa (ROS)] | Puntual | Inmediato [verificar] | [PLACEHOLDER] | UAF |
| [PLACEHOLDER — p.ej. reporte de transacciones en efectivo / cuasi efectivo] | Periódica | [PLACEHOLDER] [verificar] | [PLACEHOLDER] | UAF |
| [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] | [PLACEHOLDER] |

---

## Matriz de escalado

| Situación | Gestiona en | Escala a | Cuándo |
|---|---|---|---|
| Cambio normativo rutinario | Equipo de cumplimiento | — | — |
| Gap regulatorio material | Equipo de cumplimiento | Dirección jurídica | Impacto 🟠 o superior |
| Requerimiento de supervisor (SBP / SMV / UAF) | — | Dirección jurídica + Gerencia General | Siempre |
| Procedimiento sancionador | — | Dirección jurídica + Junta Directiva | Siempre |
| Inspección o visita del supervisor | — | Dirección jurídica + área afectada | Siempre |

---

## Referencias legislativas principales

- **Ley 23 de 2015** — prevención del blanqueo de capitales, financiamiento del terrorismo y financiamiento de la proliferación de armas de destrucción masiva [verificar]
- **Decreto Ejecutivo 363 de 2015** — reglamenta la Ley 23 de 2015
- **Ley 38 de 2000** — procedimiento administrativo general [verificar]
- **Normativa sectorial específica** — según sectores activos en la tabla de sectores regulados (acuerdos de la SBP, acuerdos de la SMV, guías de la UAF)
- **Estándares internacionales de referencia comparada** — Recomendaciones del GAFI/FATF (no vinculantes como derecho interno, pero base de la normativa panameña) [verificar]

---

## Documentos semilla

| Documento | Ubicación | Revisado | Notas |
|---|---|---|---|
| Mapa regulatorio vigente | [PLACEHOLDER] | [PLACEHOLDER] | |
| Política de cumplimiento | [PLACEHOLDER] | [PLACEHOLDER] | |
| Último informe de gaps | [PLACEHOLDER] | [PLACEHOLDER] | |

---

## Resultados

**Carpeta de resultados:** [PLACEHOLDER — dónde se guardan los análisis de gaps, alertas normativas y calendarios regulatorios]
**Convención de nombres:** [PLACEHOLDER — patrón de nombres de archivo, o "ad hoc"]

**Encabezado de producto de trabajo** (se antepone a análisis de gaps, alertas regulatorias, informes de cumplimiento):

- Si el Rol es Abogado/a: `PRIVILEGIADO Y CONFIDENCIAL — PRODUCTO DE TRABAJO LETRADO — PREPARADO BAJO LA DIRECCIÓN DE ABOGADO`
- Si el Rol es No abogado: `NOTAS DE INVESTIGACIÓN — NO CONSTITUYE ASESORAMIENTO JURÍDICO — REVISAR CON UN ABOGADO IDÓNEO ANTES DE ACTUAR`

---

*Re-ejecutar: `/regulatorio:entrevista-inicial --redo`*
