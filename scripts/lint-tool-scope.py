#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linter de SKILL.md para Claude para Abogados (España).

Comprueba cada SKILL.md en busca de problemas comunes:
  1. Referencias a herramientas/funciones que no existen en el plugin
  2. Ruta de configuración correcta (~/.claude/plugins/config/claude-para-abogados/)
  3. Placeholders en inglés que no deberían estar en SKILL.md
  4. Descripción del frontmatter en español (heurística: caracteres con acento)

Uso: python3 lint-tool-scope.py [--modulo NOMBRE]
  Sin argumentos analiza todos los módulos.

Código de salida: 0 si no hay problemas, 1 si los hay.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

# Directorio raíz del proyecto
RAIZ = Path(__file__).resolve().parent.parent

# Ruta esperada de configuración
RUTA_CONFIG_ESPERADA = "~/.claude/plugins/config/claude-para-abogados/"

# Patrones de placeholders en inglés (no deberían estar en SKILL.md)
PLACEHOLDERS_EN = [
    re.compile(r"\[Your Company Name\]", re.IGNORECASE),
    re.compile(r"\[PLACEHOLDER\]", re.IGNORECASE),
    re.compile(r"\[YOUR[_ ].*?\]", re.IGNORECASE),
    re.compile(r"\[INSERT[_ ].*?\]", re.IGNORECASE),
    re.compile(r"\[COMPANY[_ ]NAME\]", re.IGNORECASE),
    re.compile(r"\[CLIENT[_ ]NAME\]", re.IGNORECASE),
    re.compile(r"\[FIRM[_ ]NAME\]", re.IGNORECASE),
]

# Heurística para detectar español: caracteres acentuados O palabras comunes en español
PATRON_ESPANOL = re.compile(r"[áéíóúñ¿¡]", re.IGNORECASE)
PALABRAS_ESPANOL = re.compile(
    r"\b(del|las|los|una|para|como|con|por|que|sobre|desde|hasta|entre|"
    r"genera|ejecuta|analiza|revisa|gestiona|configura|comprueba|extrae|"
    r"obligaciones|cumplimiento|sociedad|contrato|documento|empresa|"
    r"inicial|calendario|estado|datos|entidad|usuario|derecho|legal)\b",
    re.IGNORECASE,
)

# Patrón para frontmatter YAML
PATRON_FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)

# Patrones que parecen referencias a herramientas/funciones MCP
PATRON_HERRAMIENTA = re.compile(
    r"(?:mcp_toolset|mcp_server|tool_call|function_call|"
    r"slack_send_message|slack_\w+|"
    r"google_drive_\w+|notion_\w+|"
    r"send_email|create_issue|"
    r"execute_code|run_command|shell_exec)"
)


def extraer_frontmatter(texto: str) -> dict | None:
    """Extrae campos del frontmatter YAML sin dependencias externas."""
    m = PATRON_FRONTMATTER.match(texto)
    if not m:
        return None
    bloque = m.group(1)
    campos = {}
    clave_actual = None
    for linea in bloque.split("\n"):
        match_kv = re.match(r"^(\w[\w-]*)\s*:\s*(.*)", linea)
        if match_kv:
            clave_actual = match_kv.group(1)
            valor = match_kv.group(2).strip()
            if valor in (">", "|"):
                campos[clave_actual] = ""
            else:
                campos[clave_actual] = valor
        elif clave_actual and linea.startswith("  "):
            campos[clave_actual] = (campos.get(clave_actual, "") + " " + linea.strip()).strip()
    return campos


def detectar_modulos() -> list[Path]:
    """Devuelve los directorios que son módulos (tienen .claude-plugin/)."""
    return sorted(
        d for d in RAIZ.iterdir()
        if d.is_dir() and (d / ".claude-plugin").is_dir()
    )


def encontrar_skills(modulo: Path) -> list[Path]:
    """Devuelve todos los archivos SKILL.md dentro de un módulo."""
    skills_dir = modulo / "skills"
    if not skills_dir.is_dir():
        return []
    return sorted(skills_dir.rglob("SKILL.md"))


def lint_skill(skill_path: Path, modulo_nombre: str) -> list[str]:
    """Analiza un SKILL.md y devuelve lista de problemas encontrados."""
    problemas = []
    texto = skill_path.read_text(encoding="utf-8")
    ruta_relativa = f"{modulo_nombre}/skills/{skill_path.parent.name}/SKILL.md"

    # --- 1. Comprobar frontmatter ---
    fm = extraer_frontmatter(texto)
    if fm is None:
        problemas.append(f"{ruta_relativa}: sin frontmatter YAML")
    else:
        descripcion = fm.get("description", "")
        # Comprobar que la descripción está en español
        # Heurística: debe contener caracteres acentuados O palabras comunes españolas
        if descripcion and not PATRON_ESPANOL.search(descripcion) and not PALABRAS_ESPANOL.search(descripcion):
            problemas.append(
                f"{ruta_relativa}: la descripción del frontmatter no parece estar en español "
                f"(no contiene caracteres españoles ni palabras comunes): \"{descripcion[:80]}...\""
            )

    # --- 2. Comprobar ruta de configuración ---
    # Si el SKILL.md hace referencia a rutas de config, debe usar la correcta
    rutas_config = re.findall(
        r"~/\.claude/plugins/(?:config|cache)/[^\s)\"']+", texto
    )
    for ruta in rutas_config:
        if "config/claude-para-abogados/" not in ruta:
            # Permitir rutas de cache que son parte de la lógica de migración
            if "cache/claude-para-abogados/" not in ruta:
                problemas.append(
                    f"{ruta_relativa}: ruta de configuración incorrecta: {ruta}"
                )

    # Si no hay ninguna referencia a la ruta de config, es sospechoso
    # (la mayoría de skills deberían referenciarla)
    if RUTA_CONFIG_ESPERADA not in texto and "entrevista-inicial" not in str(skill_path):
        # No es obligatorio para todos los skills, pero sí recomendable
        pass

    # --- 3. Comprobar placeholders en inglés ---
    # Excepción: entrevista-inicial usa [PLACEHOLDER] legítimamente como parte
    # de la plantilla de configuración que el skill rellena
    es_entrevista = "entrevista-inicial" in str(skill_path) or "cold-start" in str(skill_path)
    for patron in PLACEHOLDERS_EN:
        matches = patron.findall(texto)
        for match in matches:
            if es_entrevista and match.upper() == "[PLACEHOLDER]":
                continue  # Legítimo en skills de configuración
            problemas.append(
                f"{ruta_relativa}: placeholder en inglés encontrado: {match}"
            )

    # --- 4. Comprobar referencias a herramientas sospechosas ---
    # Buscar en el cuerpo (después del frontmatter)
    cuerpo = texto
    m_fm = PATRON_FRONTMATTER.match(texto)
    if m_fm:
        cuerpo = texto[m_fm.end():]

    herramientas = PATRON_HERRAMIENTA.findall(cuerpo)
    for h in herramientas:
        problemas.append(
            f"{ruta_relativa}: referencia a herramienta/función posiblemente inexistente: {h}"
        )

    return problemas


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
        print("ERROR: No se encontraron módulos", file=sys.stderr)
        return 2

    if modulo_filtro:
        modulos = [m for m in modulos if m.name == modulo_filtro]
        if not modulos:
            print(f"ERROR: Módulo '{modulo_filtro}' no encontrado", file=sys.stderr)
            return 2

    total_problemas = 0
    total_skills = 0

    print(f"{'='*70}")
    print(f"  Lint de SKILL.md — {len(modulos)} módulos")
    print(f"{'='*70}\n")

    for modulo in modulos:
        skills = encontrar_skills(modulo)
        if not skills:
            print(f"  {modulo.name}: sin directorio skills/")
            continue

        problemas_modulo = []
        for skill in skills:
            total_skills += 1
            problemas_modulo.extend(lint_skill(skill, modulo.name))

        if problemas_modulo:
            total_problemas += len(problemas_modulo)
            print(f"  {modulo.name} ({len(skills)} skills) — {len(problemas_modulo)} problema(s):")
            for p in problemas_modulo:
                print(f"    ✗ {p}")
        else:
            print(f"  {modulo.name} ({len(skills)} skills) — OK")

    # Resumen
    print(f"\n{'='*70}")
    print(f"  {total_skills} SKILL.md analizados, {total_problemas} problema(s) encontrado(s)")
    print(f"{'='*70}")

    return 1 if total_problemas > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
