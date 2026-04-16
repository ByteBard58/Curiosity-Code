import numpy as np
from math import sqrt
from typing import List

"""
[x] Create Function that will: 
 1. Interpolate the segment into 1/3rd and 2/3rd,
 2. Rotate it by 60 degrees
[ ] Get the interation code ready
"""

def manipulate_vector(A:np.ndarray[float],B:np.ndarray[float]) -> List[np.ndarray]:
  """
  A : [x_1,y_1]
  B : [x_2,y_2]
  """
  p_x:np.float64 = (2*A[0]+B[0]) /3
  p_y:np.float64 = (2*A[1]+B[1]) /3

  P = np.array([p_x,p_y])

  q_x:np.float64 = (A[0] + 2*B[0]) /3
  q_y:np.float64 = (A[1] + 2*B[1]) /3

  Q = np.array([q_x,q_y])

  PQ:np.ndarray = Q - P

  cos = np.cos(np.pi/3)
  sin = np.sin(np.pi/3)
  v_x = PQ[0]
  v_y = PQ[1]

  rotated_point_x = v_x * cos - v_y * sin
  rotated_point_y = v_x * sin + v_y * cos
  rotated_point = np.array([rotated_point_x,rotated_point_y])
  tip = P + rotated_point

  # Return 4 segments
  return [A, P , tip, Q, B]

def iteration(n:int,initial:List[List[float]]):
  if n > 5 :
    raise ValueError("Bruh are you for serious? RAM will start crying.") 
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


if __name__ == "__main__":
  pass

# def iteration(n:int,initial:List[List[float]]):
#   if n > 5 :
#     raise ValueError("Bruh are you for serious? RAM will start crying.") 
#   result = initial
#   k_result = []

