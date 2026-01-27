from scipy.constants import golden
import numpy as np
import time
import matplotlib.pyplot as plt

# True value of phi
phi_main: float = golden

# Function to generate the fibonacchi series and calculate the golden ratio
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
  print(f"Time Taken(Fibonacchi Series) {(end-strt):.5f} Second")
  
  return elements,golden_ratio,golden_ratio_x

elms,gold,gold_x = fibon(1000)

# Function to generate continued fraction of phi and generate the golden ratio
def cont_frac(n):
  element:list[float] = []
  element_x:list[int] = [0]
  
  strt: float = time.time()
  for i in range(n):
    if i == 0:
      x = 1+(1/1)
      element.append(x)
      continue
    x = sum(element[-1:])
    outp = 1+(1/x)
    element.append(outp)
    element_x.append(i)
  end: float = time.time()
  print(f"Time Taken(Continued Fraction) {(end-strt):.5f} Second")
  
  return element,element_x

gold_cont,gold_cont_x = cont_frac(1000)

# Function to generate the golden ratio from Square root iteration
def sqrt_iter(n):
  elements:list[float] = []
  elements_x:list[int] = [0]

  strt: float = time.time()
  for i in range(n):
    if i == 0:
      x = np.sqrt(1+np.sqrt(1))
      elements.append(x)
      continue
    x = sum(elements[-1:])
    output = np.sqrt(1+x)
    elements.append(output)
    elements_x.append(i)
  end: float = time.time()
  print(f"Time Taken(Square Root Iteration) {(end-strt):.5f} Second")

  return elements,elements_x

sqrt_elm,sqrt_elm_x = sqrt_iter(1000)

# Plotting the graph
plt.figure(figsize=(9,6))

plt.plot(gold_x,gold, color="orange",
            marker="s",markersize=3, label="Fibonacchi Series")
plt.plot(gold_cont_x,gold_cont, color="green",
            marker="o",markersize=3, label="Continued Fraction")
plt.plot(sqrt_elm_x,sqrt_elm, color="red",
            marker="^",markersize=3, label="Square Root Iteration")
plt.axhline(y=phi_main, color="blue", linestyle="--", linewidth=2,
            label=f"True φ = {phi_main:.12f}")

plt.title("Golden Ratio from Fibonacchi series")
plt.xlabel("Number of elements in the series")
plt.ylabel("Golden Ratio")
plt.xscale("log")
plt.legend()
plt.grid()
plt.show()
