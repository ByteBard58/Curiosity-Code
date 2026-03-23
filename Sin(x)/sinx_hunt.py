"""
sinx_hunt.py

This script calculates the Taylor series expansion for sin(x) and visualizes 
both the convergence of the series approximation and the absolute error 
at each iteration.
"""

import time
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial

## MATH PART

def taylor_sine(x:np.float64, n:np.ndarray) -> tuple[np.float64, np.ndarray]:
  term = ((-1)**n * x**(2*n+1)) / (factorial(2*n+1))
  return np.sum(term), np.cumsum(term)
nukes = np.arange(0, 25)
t1 = time.time()
result, term_s = taylor_sine(5, nukes)
errors = np.abs(np.sin(5) - term_s)
t2 = time.time()
minute, second = np.divmod(t2-t1, 60)
print(f"Time Taken: {minute} Minutes {second:.3f} Seconds")

## PLOTTING PART
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Subplot 1: Convergence of the series
ax1.plot(nukes, term_s, color="orange", marker=".", label="Approximated Value of sin(5)")
ax1.axhline(np.sin(5), label=f"True sin(5) = {np.sin(5):.12f}", color="blue", linestyle="--")
ax1.set_title("Convergence of sin(x) using Taylor's series", fontdict={"fontsize": 14})
ax1.set_ylabel("Value of sin(5)", fontdict={"fontsize": 12})
ax1.grid(True, alpha=0.3)
ax1.legend()

# Subplot 2: Error Convergence
ax2.plot(nukes, errors, color="#FF4B2B", marker="o", markersize=4, label="Absolute Error")
ax2.set_title("Error Convergence", fontdict={"fontsize": 14})
ax2.set_xlabel("Number of parameters (n)", fontdict={"fontsize": 12})
ax2.set_ylabel("Error |sin(5) - terms|", fontdict={"fontsize": 12})
ax2.set_yscale("log")
ax2.grid(True, which="both", linestyle="--", alpha=0.5)
ax2.legend()

plt.tight_layout()
plt.savefig("Sin(x)/sinx_hunt.png")
plt.close()