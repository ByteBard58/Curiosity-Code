"""
l2.py

Approximates ln(2) using the alternating harmonic series and visualizes
both the convergence of the partial sums and the absolute error.
"""

import time
import os

os.environ.setdefault("MPLCONFIGDIR", "/tmp/matplotlib")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


TRIALS = 10_000
TRUE_LN2 = np.log(2)


def alternating_harmonic_ln2(n: int) -> tuple[np.ndarray, np.ndarray]:
  if n < 1:
    raise ValueError("Number of terms must be at least 1")

  terms_x = np.arange(1, n + 1, dtype=np.float64)
  terms = ((-1) ** (terms_x + 1)) / terms_x
  partial_sums = np.cumsum(terms)

  return terms_x, partial_sums


t1 = time.time()
nums, approximations = alternating_harmonic_ln2(TRIALS)
errors = np.abs(approximations - TRUE_LN2)
t2 = time.time()

minutes, seconds = np.divmod(t2 - t1, 60)
print(f">>> Time Elapsed = {minutes:.0f} Minutes {seconds:.4f} Seconds")
print(f">>> ln(2) approximation after {TRIALS} terms = {approximations[-1]:.12f}")
print(f">>> Absolute error = {errors[-1]:.12e}")


fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Subplot 1: Convergence
ax1.plot(
  nums,
  approximations,
  color="orange",
  linewidth=1.4,
  label="Alternating Harmonic Series",
)
ax1.axhline(
  TRUE_LN2,
  color="blue",
  linestyle="--",
  linewidth=2,
  label=f"True ln(2) = {TRUE_LN2:.12f}",
)
ax1.set_title("Convergence to ln(2)", fontdict={"fontsize": 14})
ax1.set_ylabel("Approximated Value", fontdict={"fontsize": 12})
ax1.set_xscale("log")
ax1.grid(True, which="both", linestyle="--", alpha=0.45)
ax1.legend()

# Subplot 2: Error Analysis
ax2.plot(
  nums,
  errors,
  color="#FF4B2B",
  linewidth=1.4,
  label="Absolute Error",
)
ax2.set_title("Approximation Error", fontdict={"fontsize": 14})
ax2.set_xlabel("Number of Terms", fontdict={"fontsize": 12})
ax2.set_ylabel("Error |Approx - True|", fontdict={"fontsize": 12})
ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.grid(True, which="both", linestyle="--", alpha=0.45)
ax2.legend()

fig.suptitle("ln(2) Hunt", fontdict={"fontsize": 16})
plt.tight_layout()
plt.savefig("ln(2) Riemann Series/l2_hunt.png", dpi=200)
plt.close()
