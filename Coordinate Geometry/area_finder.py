'''
area_finder.py

This program finds the area of a polygon using the Shoelace formula.
Input is a numpy array of shape (n,2) where n is the number of vertices.
Output is the area of the polygon.

Pass the desried input to `area_sc` function as an argument and print it, it will provide the
area. A demo is provided.

'''

import numpy as np 

def order_vertices(target:np.ndarray) -> np.ndarray:
  x = target[:,0]
  y = target[:,1]

  centroid_x = np.mean(x)
  centroid_y = np.mean(y)

  target_l = target.tolist()
  target_new = []
  for i in target_l:
    x_lo = i[0]
    y_lo = i[1]
    theta = np.atan2(y_lo-centroid_y, x_lo-centroid_x)

    i.append(theta)
    target_new.append(i)
  
  target_new = np.array(target_new)
  return target_new[target_new[:,2].argsort()]

def area_sc(target:np.ndarray, assume_unordered:bool = False) -> np.float64:
  if assume_unordered:
    target = order_vertices(target)
  x: np.ndarray = target[:,0]
  y: np.ndarray = target[:,1]

  main_s: np.float64 = abs(np.dot(x,np.roll(y,-1)) - np.dot(y,np.roll(x,-1)))
  return 0.5 * main_s

# demo

def main():
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

if __name__ == "__main__":
  main()
