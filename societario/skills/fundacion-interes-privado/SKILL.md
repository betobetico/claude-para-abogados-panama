---
name: fundacion-interes-privado
description: "Asiste en la constitución, estructura y cumplimiento de fundaciones de interés privado conforme a la Ley 25 de 1995"
argument-hint: "<accion: constituir | revisar | cumplimiento> [datos-de-la-fundacion]"
---

## Propósito

Esta skill asiste en el ciclo de vida de las fundaciones de interés privado panameñas (Ley 25 de 1995): constitución (acta fundacional / carta fundacional), definición de órganos (fundador, consejo de fundación, protector), beneficiarios, patrimonio y reglamentos, así como en el seguimiento de las obligaciones de mantenimiento. Es la figura típica de planificación patrimonial y sucesoria en Panamá, sin accionistas y con fines no lucrativos.

## Instrucciones

### Paso 1 — Identificar la acción

Determinar qué se solicita:

1. **Constituir**: preparar el borrador del acta fundacional y los elementos necesarios.
2. **Revisar**: analizar un acta fundacional o reglamento existente y detectar incidencias.
3. **Cumplimiento**: verificar el estado de las obligaciones de mantenimiento de la fundación.

### Paso 2 — Recopilar datos necesarios

Solicitar al usuario los datos según la acción:

- **Fundador**: nombre, cédula / pasaporte; puede ser persona natural o jurídica.
- **Nombre de la fundación**: debe incluir la palabra "Fundación" y no ser igual al de otra existente [verificar].
- **Patrimonio inicial**: mínimo de USD 10.000 (B/. 10.000) [verificar].
- **Domicilio** y **agente residente** (abogado o firma de abogados en Panamá) [verificar].
- **Consejo de fundación**: miembros (mínimo 3 personas naturales, o 1 persona jurídica) [verificar].
- **Beneficiarios**: identificación o forma de determinarlos (a menudo en reglamento privado).
- **Protector** (opcional): facultades de supervisión.
- **Objeto / fines**: no lucrativos; pueden incluir manutención y educación de beneficiarios.

### Paso 3 — Verificar requisitos legales

Comprobar conforme a la Ley 25 de 1995:

- **Patrimonio mínimo** afectado a los fines de la fundación [verificar].
- **Acta fundacional** otorgada en escritura pública e inscrita en el Registro Público [verificar].
- **Órganos**: consejo de fundación válidamente designado.
- **Reglamento**: documento privado que regula beneficiarios y distribución (no necesariamente inscrito).
- **Agente residente** vigente.
- **Beneficiario final**: cumplimiento de la normativa de transparencia y de la Ley 23 de 2015 (si la fundación es sujeto obligado o si interviene su agente residente).

### Paso 4 — Generar el documento o informe

Según la acción, redactar el borrador del acta fundacional, el informe de revisión o el calendario de cumplimiento.

## Formato de salida

```markdown
## Fundación de interés privado — [Acción]

**Fundación:** [nombre completo]
**Fundador:** [nombre]
**Patrimonio inicial:** [importe en USD / B/.]
**Agente residente:** [nombre]
**Fecha:** [fecha]

---

### Estructura

| Elemento | Detalle | Estado / Referencia |
|----------|---------|---------------------|
| Consejo de fundación | [miembros] | Ley 25 de 1995 |
| Protector | [nombre / no designado] | [opcional] |
| Beneficiarios | [identificación / reglamento] | [privado] |
| Reglamento | [sí / no] | [privado] |

### Obligaciones de mantenimiento

| Obligación | Plazo | Estado | Base legal |
|------------|-------|--------|------------|
| Tasa única anual | Anual [verificar] | [estado] | Registro Público [verificar] |
| Agente residente | Continuo | [estado] | Ley 25 de 1995 |
| Libros / registros contables | Permanente | [estado] | Ley 25 de 1995 |
| Beneficiario final | Según normativa vigente | [estado] | Ley 23 de 2015 / transparencia [verificar] |

### Incidencias / Acciones recomendadas

[Lista de incidencias detectadas o acciones pendientes]
```

## Referencias normativas

- **Ley 25 de 1995**: sobre fundaciones de interés privado — constitución, órganos, patrimonio, beneficiarios.
- **Código Civil de Panamá** [verificar]: en lo relativo a personalidad jurídica, obligaciones y sucesiones.
- **Código de Comercio de Panamá**: libros y registros contables [verificar].
- **Ley 23 de 2015**: prevención de blanqueo de capitales — sujetos obligados, UAF y beneficiario final.
- **Normativa de transparencia y beneficiario final** [verificar]: registro de beneficiarios finales.

## Guardrails

- **NO** constituye ni inscribe la fundación ante el Registro Público — solo prepara borradores.
- **NO** asesora sobre la fiscalidad internacional del fundador o de los beneficiarios — escalar a fiscalista.
- **NO** certifica la validez del acta fundacional — requiere revisión del abogado idóneo y del notario.
- **NO** sustituye el reglamento privado, que debe redactarse según la voluntad del fundador.
- **ESCALAR** si la estructura busca eludir normas imperativas de sucesiones o de acreedores.
- **ESCALAR** si hay indicios de uso para blanqueo de capitales o evasión fiscal (Ley 23 de 2015).
- **AVISAR** si faltan datos esenciales (fundador, patrimonio, consejo de fundación o agente residente).
