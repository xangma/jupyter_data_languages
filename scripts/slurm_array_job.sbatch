#!/bin/bash
#SBATCH --job-name=astro-array
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --time=00:20:00
#SBATCH --array=0-5
#SBATCH --output=logs/%x-%A_%a.out
#SBATCH --error=logs/%x-%A_%a.err
#SBATCH --export=ALL

set -euo pipefail

LOG_DIR=${LOG_DIR:-logs}
mkdir -p "$LOG_DIR"
exec > >(tee -a "$LOG_DIR/${SLURM_JOB_NAME}-${SLURM_ARRAY_JOB_ID:-$SLURM_JOB_ID}-${SLURM_ARRAY_TASK_ID}.stdout")
exec 2> >(tee -a "$LOG_DIR/${SLURM_JOB_NAME}-${SLURM_ARRAY_JOB_ID:-$SLURM_JOB_ID}-${SLURM_ARRAY_TASK_ID}.stderr" >&2)

module purge 2>/dev/null || true
module load anaconda/2023 2>/dev/null || true
if command -v conda >/dev/null 2>&1; then
    source "$(conda info --base)/etc/profile.d/conda.sh"
    conda activate base >/dev/null 2>&1 || true
fi

GRID_FILE=${GRID_FILE:-config/param_grid.txt}
if [[ ! -f "$GRID_FILE" ]]; then
    echo "Grid file $GRID_FILE not found. Run scripts/run_param_sweep.py first." >&2
    exit 2
fi

COMMAND=$(sed -n "$((SLURM_ARRAY_TASK_ID + 1))p" "$GRID_FILE")
if [[ -z "${COMMAND}" ]]; then
    line_count=$(wc -l < "$GRID_FILE")
    echo "No command found for task $SLURM_ARRAY_TASK_ID (grid file has ${line_count} lines)." >&2
    exit 3
fi

echo "Launching: $COMMAND"
eval "$COMMAND"
