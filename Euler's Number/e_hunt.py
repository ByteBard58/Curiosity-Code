import numpy as np
import matplotlib.pyplot as plt
import time
import math

trials = 1000

def factorial(n):
  return math.factorial(n)

## Euler's Formula
def euler_form(trial) -> tuple[np.ndarray, np.ndarray]:
  nums = np.arange(1,trial,1)
  t1 = time.time()
  result = (1+ (1/nums))**nums
  t2 = time.time()
  minutes, seconds = np.divmod((t2-t1),60)
  print(f">>> Time Elapsed (Euler's Formula) = {minutes} Minutes {seconds:.4f} Seconds")
  return nums, result

nums,result = euler_form(trial=trials)


## Continuous Fraction
def cont_frac(n) -> tuple[list,list]:
  t1 = time.time()
  result = []
  n_params = []
  for i in range(n):
    if i == 0:
      n_params.append(i)
      prv = 1
      result.append(prv)
      continue
    now = 1/ factorial(i)
    to_append = prv + now
    result.append(to_append)
    n_params.append(i)
    prv = to_append
  t2 = time.time()
  minutes,seconds = np.divmod((t2-t1),60)
  print(f">>> Time Elapsed (Continuous Fraction) = {minutes} Minutes {seconds:.4f} Seconds")
  return result,n_params

result_2, n_params_2 = cont_frac(n=trials)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Subplot 1: Value of Euler's Number
ax1.plot(nums, result, color="orange", label="Value of Euler's Number (Euler's Formula)")
ax1.plot(n_params_2, result_2, color="green", label="Value of Euler's Number (Continuous Fraction)")
ax1.axhline(np.e, color="blue", linestyle="--", linewidth=2, label="Actual Value of Euler's Number")
ax1.set_ylabel("Value of Euler's Number", fontdict={"fontsize": 13})
ax1.set_xlabel("Parameter", fontdict={"fontsize": 13})
ax1.set_xscale("log")
ax1.set_ylim(1.5, 3.0)
ax1.set_title("Euler Number Hunt", fontdict={"fontsize": 16})
ax1.legend()
ax1.grid()

# Subplot 2: Calculation Error

error = np.abs(result - np.e)
error_2 = np.abs(np.array(result_2) - np.e)
ax2.plot(nums, error, color="orange", label="Error (Euler's Formula)")
ax2.plot(n_params_2, error_2, color="green", label="Error (Continuous Fraction)")
ax2.set_ylabel("Error", fontdict={"fontsize": 13})
ax2.set_xlabel("Parameter", fontdict={"fontsize": 13})
ax2.set_xscale("log")
ax2.set_title("Calculation Error", fontdict={"fontsize": 16})
ax2.legend()
ax2.grid()

plt.tight_layout()
plt.show()