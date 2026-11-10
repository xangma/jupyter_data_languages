#!/usr/bin/env python3
"""Generate synthetic data, fit a straight line, and persist results."""
from __future__ import annotations

import argparse
import json
import logging
import shutil
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

import numpy as np
import yaml

from capture_git import get_git_hash


@dataclass
class FitResult:
    slope: float
    intercept: float
    mse: float

    def as_json(self) -> Dict[str, float]:
        return asdict(self)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        default="config/params.yaml",
        help="Path to the YAML file with run parameters.",
    )
    parser.add_argument(
        "--output-root",
        default="outputs",
        help="Directory where run artifacts are stored.",
    )
    return parser.parse_args()


def load_params(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as stream:
        params = yaml.safe_load(stream) or {}
    required = ["data_size", "slope", "intercept", "noise_sigma"]
    missing = [key for key in required if key not in params]
    if missing:
        raise ValueError(f"Missing parameters in {path}: {', '.join(missing)}")
    return params


def setup_logger(log_path: Path) -> logging.Logger:
    logger = logging.getLogger("run_local")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(formatter)
    file_handler = logging.FileHandler(log_path)
    file_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger


def generate_data(params: Dict[str, Any]) -> tuple[np.ndarray, np.ndarray]:
    rng = np.random.default_rng(params.get("seed", 0))
    x = np.linspace(0.0, 1.0, int(params["data_size"]))
    y = params["slope"] * x + params["intercept"]
    noise = rng.normal(0.0, params["noise_sigma"], size=x.shape)
    return x, y + noise


def fit_line(x: np.ndarray, y: np.ndarray) -> FitResult:
    slope, intercept = np.polyfit(x, y, deg=1)
    residuals = y - (slope * x + intercept)
    mse = float(np.mean(residuals**2))
    return FitResult(slope=float(slope), intercept=float(intercept), mse=mse)


def persist_results(run_dir: Path, params: Dict[str, Any], fit: FitResult) -> None:
    data_csv = run_dir / "data.csv"
    results_json = run_dir / "results.json"
    with data_csv.open("w", encoding="utf-8") as handle:
        handle.write("x,y\n")
        for x_val, y_val in zip(params["x_values"], params["y_values"]):
            handle.write(f"{x_val:.6f},{y_val:.6f}\n")
    payload = {
        "parameters": {k: v for k, v in params.items() if k not in {"x_values", "y_values"}},
        "fit": fit.as_json(),
    }
    results_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    args = parse_args()
    config_path = Path(args.config)
    params = load_params(config_path)
    git_hash = get_git_hash()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    run_dir = Path(args.output_root) / f"{git_hash}-{timestamp}"
    # Ensure we never overwrite an existing run directory.
    run_dir.mkdir(parents=True, exist_ok=False)

    log_path = run_dir / "run.log"
    logger = setup_logger(log_path)

    logger.info("Using config %s", config_path)
    logger.info("Git hash: %s", git_hash)

    # Keep an immutable copy of the parameters alongside the run.
    copied_config = run_dir / config_path.name
    shutil.copy2(config_path, copied_config)
    logger.info("Copied parameters to %s", copied_config)

    x, y = generate_data(params)
    params["x_values"] = x.tolist()
    params["y_values"] = y.tolist()

    fit = fit_line(x, y)
    logger.info("Fit slope=%.4f intercept=%.4f mse=%.6f", fit.slope, fit.intercept, fit.mse)

    persist_results(run_dir, params, fit)
    logger.info("Artifacts written to %s", run_dir)


if __name__ == "__main__":
    main()
