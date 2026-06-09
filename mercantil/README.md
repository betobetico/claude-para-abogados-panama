# Mercantil — Contratos mercantiles

Este módulo asiste en la revisión, gestión y seguimiento de contratos mercantiles bajo ley panameña: compraventas, distribución, agencia, suministro, franquicia y cualquier acuerdo entre empresas. Permite detectar cláusulas problemáticas, controlar vencimientos, preparar adendas de forma estructurada y escalar resúmenes ejecutivos a socios o clientes. Funciona tanto para el lado de ventas (la empresa como proveedor) como para el lado de compras (la empresa como cliente), adaptando el análisis de riesgos según la posición contractual.

## Skills disponibles

| Skill | Comando | Descripción |
|-------|---------|-------------|
| Revisión de contrato | `/revision` | Analiza un contrato mercantil e identifica riesgos, cláusulas abusivas y omisiones relevantes |
| Historial de adendas | `/historial-adendas` | Genera un cuadro cronológico de todas las modificaciones contractuales |
| Escalado | `/escalado` | Prepara un resumen ejecutivo del contrato para escalar a socio o cliente |
| Renovaciones | `/renovaciones` | Controla fechas de vencimiento y condiciones de renovación tácita o expresa |

## Primeros pasos

1. Ejecuta la entrevista inicial del proyecto para configurar tu perfil y preferencias.
2. Prueba `/revision` con un contrato de distribución o suministro para ver el análisis de riesgos.
3. Usa `/renovaciones` para crear un calendario de vencimientos de tu cartera contractual.
4. Configura `/escalado` para generar resúmenes adaptados al interlocutor (socio, cliente, dirección).

## Casos de uso típicos

- Revisión de un contrato SaaS recibido de un proveedor tecnológico.
- Análisis de cláusulas de limitación de responsabilidad e indemnización en un acuerdo de distribución.
- Control de renovaciones tácitas para evitar compromisos plurianuales no deseados.
- Preparación de un cuadro comparativo de adendas para una negociación en curso.

## Legislación de referencia

- **Código Civil de Panamá** (Libro IV — obligaciones y contratos) [verificar]
- **Código de Comercio de Panamá** (Ley 2 de 1916 — contratos mercantiles, compraventa mercantil, comisión, depósito)
- **Ley 51 de 2008** sobre documentos y firmas electrónicas y prestación de servicios de almacenamiento tecnológico de documentos [verificar] (contratación electrónica)
- **Ley 45 de 2007** de protección al consumidor y defensa de la competencia [verificar] (control de cláusulas abusivas, ACODECO)

## Lo que este plugin no hace

- **No proporciona asesoramiento fiscal** sobre la tributación de contratos (ITBMS, retenciones, precios de transferencia).
- **No gestiona litigio contractual**: no redacta demandas, contestaciones ni recursos derivados de incumplimientos.
- **No ejecuta firmas electrónicas**: no firma ni envía contratos a través de plataformas de firma digital.
- **No sustituye el criterio profesional** del abogado: las sugerencias deben ser revisadas por un abogado idóneo.

## Navegación

- [Volver al README principal](../README.md)
