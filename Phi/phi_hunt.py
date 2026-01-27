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


# Function to generate continuous fraction of phi and generate the golden ratio
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
  print(f"Time Taken(Continuous Fraction) {(end-strt):.5f} Second")
  
  return element,element_x

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

elms,gold,gold_x = fibon(1000)
gold_cont,gold_cont_x = cont_frac(1000)
sqrt_elm,sqrt_elm_x = sqrt_iter(1000)

# Calculate Errors
errors_fib: list[float] = np.abs(np.array(gold) - phi_main)
errors_cont: list[float] = np.abs(np.array(gold_cont) - phi_main)
errors_sqrt: list[float] = np.abs(np.array(sqrt_elm) - phi_main)

# Plotting the graph
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Subplot 1: Convergence
ax[0].plot(gold_x, gold, color="orange",
            marker="s", markersize=3, label="Fibonacci Series")
ax[0].plot(gold_cont_x, gold_cont, color="green",
            marker="o", markersize=3, label="Continuous Fraction")
ax[0].plot(sqrt_elm_x, sqrt_elm, color="red",
            marker="^", markersize=3, label="Square Root Iteration")

ax[0].axhline(y=phi_main, color="blue", linestyle="--", linewidth=2,
            label=f"True φ = {phi_main:.12f}")

ax[0].set_title("Convergence to Golden Ratio (φ)")
ax[0].set_ylabel("Approximated Value")
ax[0].set_xscale("log")
ax[0].legend()
ax[0].grid(True)

# Subplot 2: Error Analysis
ax[1].plot(gold_x, errors_fib, color="orange",
            marker="s", markersize=3, label="Fibonacci Error")
ax[1].plot(gold_cont_x, errors_cont, color="green",
            marker="o", markersize=3, label="Continuous Fraction Error")
ax[1].plot(sqrt_elm_x, errors_sqrt, color="red",
            marker="^", markersize=3, label="Square Root Iteration Error")

ax[1].set_title("Approximation Error")
ax[1].set_xlabel("Number of Iterations")
ax[1].set_ylabel("Absolute Error (|Approx - True|)")
ax[1].set_xscale("log")
ax[1].set_yscale("log") # Log scale helps visualize the rapid convergence
ax[1].legend()
ax[1].grid(True)

plt.tight_layout()
plt.show()
