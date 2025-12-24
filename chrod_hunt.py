import numpy as np

def chord_length(arc:float , radius:float) -> float:
  theta = arc * (360 / (2*np.pi*radius))
  theta = np.deg2rad(theta)
  result = np.sqrt((2*(radius**2)) - (2 * (radius**2) * np.cos(theta)))
  return result,theta

def main():
  try:
    arc = float(input(">>> Length of Arc: "))
    radius = float(input(">>> Length of Radius: "))
  except ValueError:
    raise ValueError("Expected float for length of arc and radius, got something else instead")
  
  circum = 2 * np.pi * radius
  if arc > circum:
    raise ValueError("Arc must be less than circumference of the circle")
  result,angle = chord_length(arc,radius)
  print(f">>> Length of Chord = {result} Unit, Angle with center = {angle} Radian")


if __name__ == "__main__":
  main()