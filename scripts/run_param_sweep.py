#!/usr/bin/env python3
"""Generate per-run config files and (optionally) print/run sweep commands."""
from __future__ import annotations

import argparse
import itertools
from pathlib import Path
from typing import Dict, Iterable, List, Sequence

import yaml


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--config",
        default="config/sweep.yaml",
        help="YAML file describing the sweep.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only print the commands without writing any files.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Optional cap on the number of parameter combinations.",
    )
    return parser.parse_args()


def load_yaml(path: Path) -> Dict:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def combo_iter(spec: Dict[str, Sequence]) -> Iterable[Dict[str, object]]:
    keys = list(spec.keys())
    values_product = itertools.product(*(spec[key] for key in keys))
    for values in values_product:
        yield {key: value for key, value in zip(keys, values)}


def main() -> None:
    args = parse_args()
    sweep_cfg = load_yaml(Path(args.config))
    base_cfg_path = Path(sweep_cfg.get("base_config", "config/params.yaml"))
    base_cfg = load_yaml(base_cfg_path)

    sweep_space = sweep_cfg.get("sweep") or {}
    if not sweep_space:
        raise ValueError("sweep.yaml must define at least one parameter in the 'sweep' section")

    combinations = list(combo_iter(sweep_space))
    if args.limit is not None:
        combinations = combinations[: args.limit]

    configs_dir = Path(sweep_cfg.get("configs_dir", "config/generated_params"))
    grid_file = Path(sweep_cfg.get("grid_file", "config/param_grid.txt"))
    prefix = sweep_cfg.get("grid_name", "sweep")

    commands: List[str] = []
    generated_files: List[Path] = []

    for idx, overrides in enumerate(combinations):
        cfg = {**base_cfg, **overrides}
        cfg_path = configs_dir / f"{prefix}_{idx:03d}.yaml"
        commands.append(f"python scripts/run_local.py --config {cfg_path.as_posix()}")
        generated_files.append(cfg_path)
        if args.dry_run:
            continue
        cfg_path.parent.mkdir(parents=True, exist_ok=True)
        with cfg_path.open("w", encoding="utf-8") as handle:
            yaml.safe_dump(cfg, handle, sort_keys=True)

    if not commands:
        print("No parameter combinations were generated.")
        return

    for command in commands:
        print(command)

    if args.dry_run:
        print("Dry run complete; no files were written.")
        return

    grid_file.parent.mkdir(parents=True, exist_ok=True)
    grid_file.write_text("\n".join(commands) + "\n", encoding="utf-8")
    print(
        f"Wrote {len(commands)} commands to {grid_file} and {len(generated_files)} configs to {configs_dir}"
    )


if __name__ == "__main__":
    main()
