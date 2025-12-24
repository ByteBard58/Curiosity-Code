import time
import numpy as np

# Solutions
gt = []

points = 0
neat = []
print("Choose from A,B,C and D. Input 0(zero) to skip.")
start = time.time()
for num,i in enumerate(gt):
  user = input(f">>> Input your answer for Question No.{num + 1}: ")
  if user not in ["A","B","C","D","0"]:
    print("Please input A,B,C or D (in capital form)")
    break
  elif user == i:
    print("Correct Answer !")
    points += 1
  elif user != i:
    print("Wrong Answer !")
  elif user == "0":
    print("Question Skipped")
  else: 
    print(f"Something went wrong. Iteration Number = {num}")
    break
end = time.time()
elapsed = end - start
mins, secs = divmod(elapsed, 60)
print(f"Your Score = {points}/{len(gt)}")
print(f"Time taken: {int(mins)} min {secs:.2f} sec")

