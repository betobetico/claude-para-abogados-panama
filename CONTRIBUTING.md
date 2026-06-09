# Contribuir a Claude para Abogados (Panamá)

Notas para cualquiera que escriba o edite un plugin en este repositorio. Breve — los principios de diseño que más importan para la calidad del resultado, no una guía de estilo.

## Principio de diseño: SKILL.md codifica el comportamiento correcto; las guardarraíles de CLAUDE.md son la red de seguridad

Cada plugin en este repositorio tiene dos capas de instrucción:

1. **`<plugin>/skills/<skill>/SKILL.md`** — lo que este skill específico hace, paso a paso. El andamiaje estrecho y específico de la tarea.
2. **`<plugin>/CLAUDE.md`** — las guardarraíles compartidas y el perfil de práctica. Disciplina de citas, verificación de hechos jurídicos, comprobación de premisas, severidad mínima entre skills. La red de seguridad amplia a nivel de plugin.

**Si el resultado correcto de un skill depende de que una guardarraíl de CLAUDE.md atrape un error que el SKILL.md habría cometido, eso es un defecto de diseño.** El SKILL.md debería decirle al modelo qué hacer directamente; las guardarraíles deberían atrapar lo que el SKILL.md no previó. Cada vez que una guardarraíl tiene que rescatar un skill, dependemos de que se active consistentemente — y en una ejecución mala, un modelo menos capaz, un prompt más escueto, o un futuro editor que solo lea el texto del skill, el rescate no ocurre.

**Regla práctica: si un test de QA pasa solo porque una guardarraíl se activó, añade el comportamiento al SKILL.md directamente.** La guardarraíl se queda (cinturón y tirantes), pero el skill ahora lleva el conocimiento que necesita por sí solo.

Ejemplos de esta regla en la práctica:

- Una consulta sobre marca denominativa no debería pasar un triaje de infracción solo porque la guardarraíl general permite al modelo salirse del flujo de marca figurativa. El skill debería ramificar según el tipo de marca y aplicar el test de confusión correcto.
- Un término procesal que cae en sábado no debería calcularse correctamente solo porque el usuario pensó en preguntar por días hábiles. El skill de términos debería llevar la regla de días hábiles del Código Judicial [verificar] incorporada en cada respuesta.
- Un cálculo de prestaciones por despido no debería acertar la fórmula solo porque el modelo recuerda el Código de Trabajo. El skill debería tener un checklist que fuerce la prima de antigüedad, la indemnización por despido injustificado, el décimo tercer mes y el salario de referencia en cada respuesta [verificar].

## Algunas cosas concretas que se derivan

- **Pon la doctrina en el skill.** Si un skill cubre despidos, cubre los tres tipos (objetivo, disciplinario, colectivo). Si cubre plazos, cubre la regla de agosto inhábil. No un puntero a "y además piensa en" — el checklist real.
- **Adjunta etiquetas de procedencia a los números, no a los párrafos.** `[cálculo del modelo — verificar contra la cláusula]` junto a la cifra; `[verificar — consultar con laboralista antes de comunicar]` en la línea donde aparece la indemnización. Las etiquetas en la prosa circundante se pierden; las etiquetas en el dato crítico no.
- **Haz que la vía de rechazo sea un andamiaje, no una vía de escape.** Si la respuesta correcta a alguna categoría de pregunta es "no calculo esto", incorpóralo al skill como una puerta dura. La regla de no-calcular de `/clinica:plazos` es el patrón: declarada claramente, no sobreescribible, propiedad del skill.
- **Escribe la cabecera de la puerta de forma que la puerta esté activada por defecto.** Si hay una excepción, formula el título como la puerta y estrecha la excepción en un sub-punto, no al revés.

## Notas de flujo de trabajo

- **Lee el `CLAUDE.md` del plugin antes de editar cualquier skill de ese plugin.** El perfil de práctica, la tabla de integraciones, las guardarraíles compartidas y la declaración de postura de decisión moldean lo que el skill debe decir y omitir.
- **Incrementa la versión del plugin en un cambio material.** Patch para adiciones de comportamiento; minor para nuevos skills o nuevos inputs requeridos.
- **Ejecuta los validadores.** `scripts/validate.py` y `scripts/lint-tool-scope.py` comprueban las invariantes estructurales de las que depende el cargador de plugins.
- **No elimines las guardarraíles compartidas de CLAUDE.md.** La red se queda. El objetivo es un skill que no necesite la red, no un plugin sin ella.

## Idioma

- Todo el contenido orientado al usuario debe estar en **español**.
- Las referencias legislativas deben incluir el nombre completo de la ley panameña y los artículos relevantes; si no se está seguro de la cita exacta, marcarla con `[verificar]`.
- Usar siempre acentos correctos (á, é, í, ó, ú, ñ).
