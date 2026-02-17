'''
Pi Hunt

In this script, I have tried to test the two very popular approaches of finding the value of pi, 
defined by two of the best mathematicians of all time, Leibniz and Ramanujon. After running the calculation,
I have used matplotlib to visualize the convergence. 
'''


import numpy as np
from scipy.special import factorial as sp_fact
import time
import matplotlib.pyplot as plt

print("Welcome to pi_hunt")
print("This script will calculate and test convergence of the value of pi using two different formulas, Leibniz and Ramanujon.")
print("\n")

print("Before we jump right in, choose whether you want to run the Leibniz Formula calculation or not.")
print("NOTE: The Leibniz Formula calculation will take a while. It also requires extensive computational power. So, run that code at your own risk.")

while True:
  choice = input(">>> Do you want to run the Leibniz Formula calculation? (y/n): ")
  if choice == "y" or choice == "n":
    break
  else:
    print("Invalid input. Please try again.")
    continue

up_lim = [100_000,1_000_000,10_000_000,100_000_000,500_000_000]
if choice == "y":
  print(">>> Running Leibniz Formula as per user's request")
  ## Leibniz Formula
  prime_results = []
  errors_l = []

  t1 = time.time()
  for i in up_lim:
    k = np.arange(i,dtype=np.float64)

    terms = (((-1)**k) / (2*k +1))
    result = 4 * np.sum(terms)
    error = np.pi - result
    print(f"For {i} parameters, 𝛑 = {result}, error = {error}")

    prime_results.append(result)
    errors_l.append(error)
  t2 = time.time()
  print(">>> Leibniz formula has run successfully !!")
  minutes, seconds = np.divmod((t2-t1),60)
  print(f">>> Time Elapsed (Leibniz Formula) = {minutes} Minutes {seconds:.2f} Seconds")

if choice == "n":
  print(">>> Skipping Leibniz Formula calculation and using pre-computed values")
  # Pre-computed values
  prime_results = [np.float64(3.1415826535897926), 
  np.float64(3.141591653589791), np.float64(3.1415925535897937), 
  np.float64(3.1415926435897927), np.float64(3.1415926515897934)]
  errors_l = [np.float64(1.0000000000509601e-05), 
  np.float64(1.0000000019161348e-06), np.float64(9.99999993922529e-08), 
  np.float64(1.00000003833145e-08), np.float64(1.999999721391532e-09)]


## Ramanujon formula
def fact(x):
  factorial = sp_fact(x)
  return factorial

up_lim_1 = [1,5,10,20,30,40,50]
prime_results_rm = []
errors_rm = []

t1_1 = time.time()
print(">>> Starting Ramanujon Formula")
for i in up_lim_1:
  k = np.arange(i,dtype=np.float64)

  terms = (fact(4*k) * (1103+26390*k)) / (((fact(k))**4) * (396.0 ** (4*k)))
  x = np.sum(terms)
  result = (9801 / ((2*np.sqrt(2)) * x)) 
  error = np.pi - result
  print(f"For {i} parameters, 𝛑 = {result}, error = {error}")

  prime_results_rm.append(result)
  errors_rm.append(error)
t2_1 = time.time()

print(">>> Ramanujon formula has run successfully !!")
minutes_1, seconds_1 = np.divmod((t2_1-t1_1),60)
print(f">>> Time Elapsed (Ramanujon Formula) = {minutes_1} Minutes {seconds_1:.3f} Seconds")


## Plotting
## Convergence Plotting
fig, ax = plt.subplots(2,1, figsize=(10,8))

ax[0].plot(up_lim, prime_results, 
  color="orange",marker="s",markersize=6, 
  label="Approximated Value (Leibniz Formula)"
)
ax[0].plot(up_lim_1, prime_results_rm, 
  color="red",marker="v",markersize=6, 
  label="Approximated Value (Ramanujon Formula)"
)

ax[0].set_xscale("log")

ax[0].axhline(y=np.pi, color="blue", linestyle="--", linewidth=2,
            label=f"True π = {np.pi:.12f}")

ax[0].set_title("Convergence")
ax[0].set_xlabel("Number of Parameters",fontdict={"fontsize":13})
ax[0].set_ylabel("Approximated Value of Pi",fontdict={"fontsize":13})

ax[0].set_ylim(np.pi-(1e-5),np.pi+(1e-5))

ax[0].grid()
ax[0].legend()

## Error plotting
ax[1].plot(up_lim, errors_l, 
  color="orange",marker="s",markersize=6, 
  label="Approximation Error (Leibniz Formula)"
)
ax[1].plot(up_lim_1, prime_results_rm, 
  color="red",marker="v",markersize=6, 
  label="Approximation Error (Ramanujon Formula)"
)

ax[1].set_title("Error")
ax[1].set_xlabel("Number of Parameters",fontdict={"fontsize":13})
ax[1].set_ylabel("Approximation Error",fontdict={"fontsize":13})

ax[1].legend()

fig.suptitle("Pi Hunt",fontdict={"fontsize": 15})
plt.tight_layout()
plt.grid()
plt.show()