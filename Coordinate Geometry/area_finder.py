'''
area_finder.py

This program finds the area of a polygon using the Shoelace formula.
Input is a numpy array of shape (n,2) where n is the number of vertices.
Output is the area of the polygon.

Pass the desried input to `area_sc` function as an argument and print it, it will provide the
area. A demo is provided.

'''

import numpy as np 

def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - \
           (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    points = sorted(points.tolist())
    
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return np.array(lower[:-1] + upper[:-1])

def area_sc(target) -> np.float64:
  target = convex_hull(target)
  x: np.ndarray = target[:,0]
  y: np.ndarray = target[:,1]

  main_s: np.float64 = abs(np.dot(x,np.roll(y,-1)) - np.dot(y,np.roll(x,-1)))
  return 0.5 * main_s

# demo


vertex_coords:list[list[float]] = []
n_poly:int = int(input(">>> How many vertexes does you polygon have? (Input an Integer) "))
print(">>> Input coordinates in this format: x,y")
for i in range(n_poly):
  while True:
    input_coord = input(f">>> Input the coordinate of the {i+1}th vertex: ")
    try:
      x_,y_ = input_coord.split(",")
    except ValueError:
      print(">>> Invalid input. Please provide the coordinates in this format: x,y")
      continue
    try:
      x_,y_ = float(x_),float(y_)
    except ValueError:
      print(">>> Invalid input. Please provide real numbers as coordinates and follow this format: x,y")
      continue
    vertex_list:list[float] = [x_,y_]
    vertex_coords.append(vertex_list)
    break

print("\nYour provided coordinates are: ")
print(vertex_coords)
print(f"Area = {area_sc(np.array(vertex_coords))} square units")