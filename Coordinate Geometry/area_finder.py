'''
area_finder.py

This program finds the area of a polygon using the Shoelace formula.
Input is a numpy array of shape (n,2) where n is the number of vertices.
Output is the area of the polygon.

Pass the desried input to `area_sc` function as an argument and print it, it will provide the
area. A demo is provided.

'''

import numpy as np 

def area_sc(target) -> np.float64:
  x = target[:,0]
  y = target[:,1]

  main_s = abs(np.dot(x,np.roll(y,-1)) - np.dot(y,np.roll(x,-1)))
  return 0.5 * main_s

# demo


vertex_coords = []
n_poly = int(input(">>> How many vertexes does you polygon have? (Input an Integer) "))
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
    vertex_list = [x_,y_]
    vertex_coords.append(vertex_list)
    break

print("\nYour provided coordinates are: ")
print(vertex_coords)
print(f"Area = {area_sc(np.array(vertex_coords))} square units")