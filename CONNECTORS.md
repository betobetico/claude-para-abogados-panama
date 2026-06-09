# Añadir un conector

Los plugins funcionan mejor cuando están conectados a fuentes autorizadas. Si construyes u operas una fuente de datos jurídicos, herramienta de investigación, CLM, gestor documental, plataforma de eDiscovery o sistema de gestión de despacho, queremos tu conector MCP en la suite.

## Qué hace un buen conector jurídico MCP

- **Servidor MCP remoto sobre HTTPS** con OAuth o API key (transporte streamable HTTP o SSE)
- **Herramientas orientadas a lectura** — buscar, consultar, listar. Las herramientas de escritura (crear, enviar, presentar) necesitan un prompt de confirmación explícito en el cliente; indícalo en las descripciones de tus herramientas.
- **Procedencia en los resultados** — devuelve la fuente, fecha de consulta e identificador listo para citar. Los plugins etiquetan cada cita por fuente; tu conector debería hacerlo posible.
- **Sin contenido tipo instrucción en los resultados** — los plugins tratan el contenido recuperado como datos, no como comandos. Si tus resultados incluyen metadatos o notas del sistema, márcalos claramente para que no parezcan directivas embebidas.
- **Límites de tasa y errores que degradan gracefully** — los plugins tienen un fallback para cuando un conector no responde; un error limpio es mejor que un timeout.

## Cómo contribuir

1. Publica tu servidor MCP y documenta sus herramientas, flujo de autenticación y cobertura de datos.
2. Abre un PR añadiendo tu servidor al `.mcp.json` del plugin relevante con la URL, método de autenticación y una descripción de una línea de lo que aporta a Claude.
3. Incluye una nota sobre para qué áreas de práctica / plugins es más útil.
4. Testearemos contra los flujos del plugin y haremos merge. Los conectores que pasen las comprobaciones de calidad de recuperación y resistencia a inyección van en el `.mcp.json` por defecto; los demás se documentan en el README del plugin para que los usuarios los añadan.

## Conectores actuales

Conectores incluidos en el `.mcp.json` por defecto de cada plugin:

| Conector | Plugins |
|---|---|
| **Slack** | todos |
| **Google Drive** (`gdrive`) | todos |
| **Órgano Judicial** (jurisprudencia / Registro Judicial) | procesal, clinica-juridica, estudiante-derecho |
| **Gaceta Oficial** (legislación) | regulatorio, fiscal, administrativo, laboral |
| **ANTAI** (resoluciones protección de datos) | privacidad, proteccion-datos |
| **Registro Público** (sociedades, fundaciones, inmuebles) | societario, mercantil, concursal, inmobiliario |
| **DIGERPI** (marcas/patentes) | propiedad-intelectual |
| **SMV** (mercado de valores) | societario, startups, regulatorio |
| **UAF** (antiblanqueo) | regulatorio, societario |
| **DGI** (calendario fiscal) | fiscal, startups |

Consulta el `.mcp.json` de cada directorio de plugin para la lista completa.

## Conectores deseados

Estos harían plugins específicos significativamente más útiles. Si construyes u operas uno, consulta "Cómo contribuir" arriba.

- **Bases de datos de jurisprudencia** (vLex, LegisPan, Gaceta Oficial digital) — investigación y doctrina para todos los plugins
- **Gestores de despacho** — gestión de expedientes para `procesal`, `mercantil`, `laboral`
- **CLM y firma electrónica** (DocuSign, firma electrónica calificada panameña) — ciclo de vida de contratos para `mercantil`
- **Registro Público de Panamá** — información societaria, de fundaciones e inmobiliaria para `societario`, `mercantil`, `inmobiliario`
- **PanamaCompra** — licitaciones y contratación pública para `administrativo`
- **UAF** — guías y tipologías de prevención de blanqueo para `regulatorio`, `societario`
- **DIGERPI / OMPI** — marcas, patentes y registros internacionales para `propiedad-intelectual`
- **DGI Consultas** — doctrina y resoluciones tributarias para `fiscal`
- **AMP** — registro de naves y derecho marítimo para `societario`, `mercantil`
- **Tracker de Regulación de IA** (Global AI Regulation Tracker) — seguimiento de regulación de IA para `gobernanza-ia` y `regulatorio`

## Preguntas

Abre un issue en este repositorio.
