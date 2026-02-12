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

points = np.array([
  [0,0], [3,-2], [4,5]
])

print(area_sc(points))
