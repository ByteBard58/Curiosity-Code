"""
snowflake.py

This script generates the points of a Koch Snowflake 
  and visualizes it using Matplotlib.
The algorithm starts with an equilateral triangle and 
  iteratively adds new points to create the 
  characteristic zigzag pattern of the snowflake. 
  The final image is saved as "snowflake.png" in the "Koch Snowflake" directory.
"""


import numpy as np
from math import sqrt
from typing import List
import matplotlib.pyplot as plt

def manipulate_vector(A:np.ndarray[float],B:np.ndarray[float]) -> List[np.ndarray]:
  """
  Runs the math.

  `A` : [x_1,y_1]
  `B` : [x_2,y_2]
  """
  # Interpolation
  p_x:np.float64 = (2*A[0]+B[0]) /3
  p_y:np.float64 = (2*A[1]+B[1]) /3

  P = np.array([p_x,p_y])

  q_x:np.float64 = (A[0] + 2*B[0]) /3
  q_y:np.float64 = (A[1] + 2*B[1]) /3

  Q = np.array([q_x,q_y])

  PQ:np.ndarray = Q - P

  # Rotation
  cos = np.cos(- np.pi/3)
  sin = np.sin(- np.pi/3)
  v_x = PQ[0]
  v_y = PQ[1]

  rotated_point_x = v_x * cos - v_y * sin
  rotated_point_y = v_x * sin + v_y * cos
  rotated_point = np.array([rotated_point_x,rotated_point_y])
  tip = P + rotated_point

  # Return 4 segments
  return [A, P , tip, Q, B]

def iteration(n:int,initial:List[List[float]]):
  """
  The acutal algorithm.

  `n` : Number of iterations.
  `initial` : Initial points of the equilateral triangle.
  """

  result = initial
  k_result = []

  for i in range(n):
    print(f"Running {i}th iteration")
    for index in range(len(result)):
      if index == len(result) -1 :
        a,b,c,d,e = manipulate_vector(result[index],result[0])
        k_result.extend([a,b,c,d])
      else:
        a,b,c,d,e = manipulate_vector(result[index],result[index+1])
        k_result.extend([a,b,c,d])
    result = k_result
    print(f"{i}th iteration complete ! Saved points = {len(result)}")

  return result

def plot_snowflake(points):
  """
  Visualizes the snowflake

  """
  xs = [point[0] for point in points]
  ys = [point[1] for point in points]

  # Close the polygon so the last point connects back to the first.
  xs.append(points[0][0])
  ys.append(points[0][1])

  plt.figure(figsize=(8, 8))
  plt.style.use("dark_background")
  plt.plot(xs, ys, color="#36F4EB", linewidth=1.5)
  plt.fill(xs, ys, color="#36F4EB", alpha=1)
  plt.gca().set_aspect("equal", adjustable="box")
  plt.axis("off")
  plt.tight_layout()
  plt.savefig("Koch Snowflake/snowflake.png",dpi=1500)
  plt.close()


if __name__ == "__main__":
  initial = [[0, 0], [2, 0], [1, sqrt(3)]]
  desired = iteration(n=6, initial=initial)
  plot_snowflake(desired)
