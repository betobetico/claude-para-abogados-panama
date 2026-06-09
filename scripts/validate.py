#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador de integridad estructural para todos los módulos de Claude para Abogados (España).

Comprueba que cada módulo tiene la estructura requerida:
  - .claude-plugin/plugin.json (JSON válido con campos obligatorios)
  - CLAUDE.md (con bloque de ruta de configuración)
  - README.md
  - skills/entrevista-inicial/SKILL.md (con frontmatter YAML válido)
  - hooks/hooks.json

Uso: python3 validate.py [--modulo NOMBRE]
  Sin argumentos valida todos los módulos.
  Con --modulo solo valida el módulo indicado.

Código de salida: 0 si todo pasa, 1 si hay fallos.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Directorio raíz del proyecto (un nivel arriba de scripts/)
RAIZ = Path(__file__).resolve().parent.parent

# Campos obligatorios en plugin.json
CAMPOS_PLUGIN_JSON = {"name", "version", "description", "author"}

# Patrón para el bloque de ruta de configuración en CLAUDE.md
PATRON_CONFIG = re.compile(
    r"~/.claude/plugins/config/claude-para-abogados/", re.IGNORECASE
)

# Patrón para frontmatter YAML al inicio de un archivo
PATRON_FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def detectar_modulos() -> list[Path]:
    """Devuelve las rutas de todos los módulos (directorios con .claude-plugin/)."""
    modulos = []
    for d in sorted(RAIZ.iterdir()):
        if d.is_dir() and (d / ".claude-plugin").is_dir():
            modulos.append(d)
    return modulos


def extraer_frontmatter(texto: str) -> dict | None:
    """Extrae campos del frontmatter YAML de un archivo Markdown.
    Devuelve None si no hay frontmatter válido.
    Usa parsing manual para evitar dependencias externas."""
    m = PATRON_FRONTMATTER.match(texto)
    if not m:
        return None
    bloque = m.group(1)
    campos = {}
    clave_actual = None
    for linea in bloque.split("\n"):
        # Líneas tipo "clave: valor" o "clave: >"
        match_kv = re.match(r"^(\w[\w-]*)\s*:\s*(.*)", linea)
        if match_kv:
            clave_actual = match_kv.group(1)
            valor = match_kv.group(2).strip()
            if valor == ">" or valor == "|":
                campos[clave_actual] = ""
            else:
                campos[clave_actual] = valor
        elif clave_actual and linea.startswith("  "):
            # Continuación de valor multilínea
            campos[clave_actual] = (campos.get(clave_actual, "") + " " + linea.strip()).strip()
    return campos


def validar_modulo(modulo: Path) -> list[str]:
    """Valida un módulo y devuelve lista de errores encontrados."""
    errores = []
    nombre = modulo.name

    # --- 1. plugin.json ---
    plugin_json = modulo / ".claude-plugin" / "plugin.json"
    if not plugin_json.exists():
        errores.append(f"Falta .claude-plugin/plugin.json")
    else:
        try:
            datos = json.loads(plugin_json.read_text(encoding="utf-8"))
            faltantes = CAMPOS_PLUGIN_JSON - set(datos.keys())
            if faltantes:
                errores.append(
                    f"plugin.json: faltan campos obligatorios: {', '.join(sorted(faltantes))}"
                )
        except json.JSONDecodeError as e:
            errores.append(f"plugin.json: JSON inválido — {e}")

    # --- 2. CLAUDE.md ---
    claude_md = modulo / "CLAUDE.md"
    if not claude_md.exists():
        errores.append("Falta CLAUDE.md")
    else:
        contenido = claude_md.read_text(encoding="utf-8")
        if not PATRON_CONFIG.search(contenido):
            errores.append(
                "CLAUDE.md: no contiene la ruta de configuración "
                "(~/.claude/plugins/config/claude-para-abogados/)"
            )

    # --- 3. README.md ---
    readme = modulo / "README.md"
    if not readme.exists():
        errores.append("Falta README.md")

    # --- 4. skills/entrevista-inicial/SKILL.md ---
    skill_md = modulo / "skills" / "entrevista-inicial" / "SKILL.md"
    if not skill_md.exists():
        errores.append("Falta skills/entrevista-inicial/SKILL.md")
    else:
        texto = skill_md.read_text(encoding="utf-8")
        fm = extraer_frontmatter(texto)
        if fm is None:
            errores.append(
                "skills/entrevista-inicial/SKILL.md: no tiene frontmatter YAML (---...---)"
            )
        else:
            if "name" not in fm:
                errores.append(
                    "skills/entrevista-inicial/SKILL.md: frontmatter sin campo 'name'"
                )
            if "description" not in fm:
                errores.append(
                    "skills/entrevista-inicial/SKILL.md: frontmatter sin campo 'description'"
                )

    # --- 5. hooks/hooks.json ---
    hooks_json = modulo / "hooks" / "hooks.json"
    if not hooks_json.exists():
        errores.append("Falta hooks/hooks.json")
    else:
        try:
            json.loads(hooks_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            errores.append(f"hooks/hooks.json: JSON inválido — {e}")

    return errores


def main() -> int:
    # Parsear argumentos
    modulo_filtro = None
    args = sys.argv[1:]
    if "--modulo" in args:
        idx = args.index("--modulo")
        if idx + 1 < len(args):
            modulo_filtro = args[idx + 1]
        else:
            print("Error: --modulo requiere un nombre de módulo", file=sys.stderr)
            return 2

    modulos = detectar_modulos()
    if not modulos:
        print("ERROR: No se encontraron módulos con .claude-plugin/", file=sys.stderr)
        return 2

    if modulo_filtro:
        modulos = [m for m in modulos if m.name == modulo_filtro]
        if not modulos:
            print(f"ERROR: Módulo '{modulo_filtro}' no encontrado", file=sys.stderr)
            return 2

    # Contadores
    total = len(modulos)
    pasaron = 0
    fallaron = 0

    print(f"{'='*60}")
    print(f"  Validación estructural — {total} módulos")
    print(f"{'='*60}\n")

    for modulo in modulos:
        errores = validar_modulo(modulo)
        if errores:
            fallaron += 1
            print(f"  FAIL  {modulo.name}")
            for err in errores:
                print(f"        ✗ {err}")
        else:
            pasaron += 1
            print(f"  PASS  {modulo.name}")

    # Resumen
    print(f"\n{'='*60}")
    print(f"  Resultado: {pasaron} PASS / {fallaron} FAIL de {total} módulos")
    print(f"{'='*60}")

    return 1 if fallaron > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
