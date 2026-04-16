import numpy as np
import matplotlib.pyplot as plt
from .snowflake import iteration
from math import sqrt
from typing import List

def plot_snowflake(points):
  xs = [point[0] for point in points]
  ys = [point[1] for point in points]

  # Close the polygon so the last point connects back to the first.
  xs.append(points[0][0])
  ys.append(points[0][1])

  plt.figure(figsize=(8, 8))
  plt.plot(xs, ys, color="#1f77b4", linewidth=1.5)
  plt.fill(xs, ys, color="#1f77b4", alpha=0.08)
  plt.gca().set_aspect("equal", adjustable="box")
  plt.axis("off")
  plt.tight_layout()
  plt.show()


if __name__ == "__main__":
  initial = [[0, 0], [2, 0], [1, sqrt(3)]]
  desired = iteration(n=5, initial=initial)
  plot_snowflake(desired)
