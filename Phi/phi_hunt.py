from scipy.constants import golden
import numpy as np
import time
import matplotlib.pyplot as plt

phi_main: float = golden

def fibon(n) -> tuple[list[int],list[float],list[int]]:
  if n == 0 or n == 1:
    raise ValueError(f"Fibonacchi series requires at lease 2 elements, {n} was set")
  if not isinstance(n,(int,np.integer)):
    raise TypeError(f"Expected integer for the `n` argument, got {type(n).__name__} instead")

  strt: float = time.time()
  elements: list[int] = []
  golden_ratio: list[float] = []
  golden_ratio_x: list[int] = []
  
  for i in range(n):
    if i == 0 or i == 1:
      elements.append(i)
      continue
    prv: int = sum(elements[-2:])
    golden_ratio.append(prv/int(elements[-1]))
    golden_ratio_x.append(i)
    elements.append(prv)
  end: float = time.time()
  print(f"Time Taken {(end-strt):.5f} Second")
  
  return elements,golden_ratio,golden_ratio_x

elms,gold,gold_x = fibon(1000)

plt.figure(figsize=(9,6))

plt.plot(gold_x,gold, color="orange",
            marker="s",markersize=6, label="Approximated Value")
plt.axhline(y=phi_main, color="blue", linestyle="--", linewidth=2,
            label=f"True φ = {phi_main:.12f}")

plt.title("Golden Ratio from Fibonacchi series")
plt.xlabel("Number of elements in the series")
plt.ylabel("Golden Ratio")
plt.xscale("log")
plt.legend()
plt.grid()
plt.show()

