import numpy as np
import time

def fibon(n) -> np.ndarray:
  if n == 0 or n == 1:
    raise ValueError(f"Fibonacchi series requires at lease 2 elements, {n} was set")
  if not isinstance(n,(int,np.integer)):
    raise TypeError(f"Expected integer for the `n` argument, got {type(n).__name__} instead")

  strt = time.time()
  elements = []
  for i in range(n):
    if i == 0 or i == 1:
      elements.append(i)
      continue
    prv = sum(elements[-2:])
    elements.append(prv)
  end = time.time()
  print(f"Time Taken {(end-strt):.5f} Second")
  
  return elements


fibon(np.int64(10000))

# Standard = 0.00620 Second

