#!/bin/bash
#SBATCH --job-name=astro-fit
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --time=00:20:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err
#SBATCH --export=ALL

set -euo pipefail

LOG_DIR=${LOG_DIR:-logs}
mkdir -p "$LOG_DIR"
exec > >(tee -a "$LOG_DIR/${SLURM_JOB_NAME}-${SLURM_JOB_ID}.stdout")
exec 2> >(tee -a "$LOG_DIR/${SLURM_JOB_NAME}-${SLURM_JOB_ID}.stderr" >&2)

module purge 2>/dev/null || true
module load anaconda/2023 2>/dev/null || true
if command -v conda >/dev/null 2>&1; then
    source "$(conda info --base)/etc/profile.d/conda.sh"
    conda activate base >/dev/null 2>&1 || true
fi

CONFIG_PATH=${1:-config/params.yaml}
python scripts/run_local.py --config "$CONFIG_PATH"
