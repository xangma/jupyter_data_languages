"""Regenerate the small, entirely synthetic catalogue; no network access."""
from pathlib import Path
import numpy as np
from astropy import units as u
from astropy.table import QTable

root = Path(__file__).resolve().parents[1]
rng = np.random.default_rng(20261109)
n = 400
distance = rng.uniform(20, 200, n)
sigma = rng.uniform(150, 900, n)
velocity = 70 * distance + 300 + rng.normal(0, sigma)
magnitude = rng.normal(-19.3, 0.8, n) + 5 * np.log10(distance * 1e6) - 5
velocity[[5, 40, 130]] = np.nan
sigma[20] = 0
magnitude[25] = np.nan
table = QTable({"object_id": np.arange(n), "distance": distance * u.Mpc,
    "velocity": velocity * u.km / u.s, "velocity_error": sigma * u.km / u.s,
    "apparent_magnitude": magnitude})
table.meta.update(synthetic=True, seed=20261109, slope=70.0, intercept=300.0,
    description="Invented low-redshift galaxy-like data; exact distance inputs; independent Gaussian velocity noise; no cosmology measurement.")
(root / "data").mkdir(exist_ok=True)
table.write(root / "data/mock_galaxies.ecsv", overwrite=True)
print("Wrote 400 synthetic rows")
