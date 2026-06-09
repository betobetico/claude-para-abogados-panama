#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# =============================================================================
# Estadísticas del proyecto Claude para Abogados (Panamá)
#
# Cuenta módulos, skills, agentes, archivos y líneas de contenido.
# Muestra la tabla formateada por consola.
#
# Uso: bash contar-estadisticas.sh
# =============================================================================

set -euo pipefail

# Directorio raíz del proyecto (un nivel arriba de scripts/)
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"

# Colores para la salida
NEGRITA="\033[1m"
RESET="\033[0m"
VERDE="\033[32m"
AZUL="\033[34m"

# -------------------------------------------------------------------
# Detectar módulos (subdirectorios con .claude-plugin/)
# Se excluye el directorio raíz aunque tenga .claude-plugin propio
# -------------------------------------------------------------------
MODULOS=()
for subdir in "$RAIZ"/*/; do
    nombre="$(basename "$subdir")"
    if [ -d "$subdir/.claude-plugin" ]; then
        MODULOS+=("$nombre")
    fi
done
# Ordenar alfabéticamente
IFS=$'\n' MODULOS=($(sort <<< "${MODULOS[*]}")); unset IFS

TOTAL_MODULOS=${#MODULOS[@]}

if [ "$TOTAL_MODULOS" -eq 0 ]; then
    echo "ERROR: No se encontraron módulos con .claude-plugin/" >&2
    exit 1
fi

# -------------------------------------------------------------------
# Contar totales
# -------------------------------------------------------------------
TOTAL_SKILLS=0
TOTAL_AGENTES=0
TOTAL_ARCHIVOS=0
TOTAL_LINEAS=0

# Para encontrar el SKILL.md más grande y más pequeño
MAX_SKILL_LINEAS=0
MAX_SKILL_NOMBRE=""
MIN_SKILL_LINEAS=999999
MIN_SKILL_NOMBRE=""

# Cabecera de la tabla de módulos
printf "\n"
printf "${NEGRITA}%s${RESET}\n" "=============================================================="
printf "${NEGRITA}  Estadísticas — Claude para Abogados (Panamá)${RESET}\n"
printf "${NEGRITA}%s${RESET}\n" "=============================================================="
printf "\n"
printf "${NEGRITA}%-28s %7s %7s %7s %8s${RESET}\n" "Módulo" "Skills" "Agentes" "Archivos" "Líneas"
printf "%-28s %7s %7s %7s %8s\n" "----------------------------" "-------" "-------" "--------" "--------"

for mod in "${MODULOS[@]}"; do
    mod_dir="$RAIZ/$mod"

    # Contar skills (subdirectorios dentro de skills/)
    n_skills=0
    if [ -d "$mod_dir/skills" ]; then
        n_skills=$(find "$mod_dir/skills" -maxdepth 1 -mindepth 1 -type d | wc -l | tr -d ' ')
    fi
    TOTAL_SKILLS=$((TOTAL_SKILLS + n_skills))

    # Contar agentes (archivos .yaml/.yml en agents/)
    n_agentes=0
    if [ -d "$mod_dir/agents" ]; then
        n_agentes=$(find "$mod_dir/agents" -type f \( -name "*.yaml" -o -name "*.yml" \) | wc -l | tr -d ' ')
    fi
    TOTAL_AGENTES=$((TOTAL_AGENTES + n_agentes))

    # Contar archivos totales del módulo (excluyendo .git y __pycache__)
    n_archivos=$(find "$mod_dir" -type f ! -path '*/__pycache__/*' ! -path '*/.git/*' | wc -l | tr -d ' ')
    TOTAL_ARCHIVOS=$((TOTAL_ARCHIVOS + n_archivos))

    # Contar líneas de contenido (solo .md, .json, .yaml, .yml, .py, .sh)
    n_lineas=0
    while IFS= read -r archivo; do
        lineas_archivo=$(wc -l < "$archivo" | tr -d ' ')
        n_lineas=$((n_lineas + lineas_archivo))
    done < <(find "$mod_dir" -type f \( -name "*.md" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" -o -name "*.py" -o -name "*.sh" \) ! -path '*/__pycache__/*')
    TOTAL_LINEAS=$((TOTAL_LINEAS + n_lineas))

    # Buscar SKILL.md más grande y más pequeño
    while IFS= read -r skill_file; do
        sl=$(wc -l < "$skill_file" | tr -d ' ')
        skill_rel="$mod/$(echo "$skill_file" | sed "s|$mod_dir/||")"
        if [ "$sl" -gt "$MAX_SKILL_LINEAS" ]; then
            MAX_SKILL_LINEAS=$sl
            MAX_SKILL_NOMBRE="$skill_rel"
        fi
        if [ "$sl" -lt "$MIN_SKILL_LINEAS" ]; then
            MIN_SKILL_LINEAS=$sl
            MIN_SKILL_NOMBRE="$skill_rel"
        fi
    done < <(find "$mod_dir/skills" -name "SKILL.md" -type f 2>/dev/null)

    # Imprimir fila de la tabla
    printf "%-28s %7d %7d %7d %8d\n" "$mod" "$n_skills" "$n_agentes" "$n_archivos" "$n_lineas"
done

# -------------------------------------------------------------------
# Totales
# -------------------------------------------------------------------
printf "%-28s %7s %7s %7s %8s\n" "----------------------------" "-------" "-------" "--------" "--------"
printf "${NEGRITA}%-28s %7d %7d %7d %8d${RESET}\n" "TOTAL" "$TOTAL_SKILLS" "$TOTAL_AGENTES" "$TOTAL_ARCHIVOS" "$TOTAL_LINEAS"

# -------------------------------------------------------------------
# Resumen adicional
# -------------------------------------------------------------------
printf "\n"
printf "${NEGRITA}%s${RESET}\n" "--------------------------------------------------------------"
printf "${AZUL}  Resumen general${RESET}\n"
printf "${NEGRITA}%s${RESET}\n" "--------------------------------------------------------------"
printf "  Módulos totales:        %d\n" "$TOTAL_MODULOS"
printf "  Skills totales:         %d\n" "$TOTAL_SKILLS"
printf "  Agentes totales:        %d\n" "$TOTAL_AGENTES"
printf "  Archivos totales:       %d\n" "$TOTAL_ARCHIVOS"
printf "  Líneas de contenido:    %d\n" "$TOTAL_LINEAS"

if [ "$MAX_SKILL_LINEAS" -gt 0 ]; then
    printf "\n"
    printf "${VERDE}  SKILL.md más grande:${RESET}    %s (%d líneas)\n" "$MAX_SKILL_NOMBRE" "$MAX_SKILL_LINEAS"
fi
if [ "$MIN_SKILL_LINEAS" -lt 999999 ]; then
    printf "${VERDE}  SKILL.md más pequeño:${RESET}   %s (%d líneas)\n" "$MIN_SKILL_NOMBRE" "$MIN_SKILL_LINEAS"
fi
printf "${NEGRITA}%s${RESET}\n\n" "--------------------------------------------------------------"
