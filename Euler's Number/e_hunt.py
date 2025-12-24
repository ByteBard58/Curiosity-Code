import numpy as np
import matplotlib.pyplot as plt
import time

trials = 10**6

nums = np.arange(0,trials,1)

t1 = time.time()
result = (1+ (1/nums))**nums
t2 = time.time()
minutes, seconds = np.divmod((t2-t1),60)
print(f">>> Time Elapsed = {minutes} Minutes {seconds:.2f} Seconds")

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# Subplot 1: Value of Euler's Number
ax1.plot(nums, result, color="orange", label="Value of Euler's Number")
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
ax2.plot(nums, error, color="red", label="Error")
ax2.set_ylabel("Error", fontdict={"fontsize": 13})
ax2.set_xlabel("Parameter", fontdict={"fontsize": 13})
ax2.set_xscale("log")
ax2.set_title("Calculation Error", fontdict={"fontsize": 16})
ax2.legend()
ax2.grid()

plt.tight_layout()
plt.show()