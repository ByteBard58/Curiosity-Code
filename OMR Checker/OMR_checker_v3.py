'''
OMR Checker v3
This script is used to check the OMR sheet of a student. 
In this version, the list of answers (Answer Set) is read from a .TXT file.
You have to input the filename of the answer key and then start answering.
'''

import time
import os

while True:
  print("The answer file options:\n1. answer_key.txt\n2. backup.txt")
  filename = int(input(">>> Input the number of the file (1 or 2): "))
  if filename in [1]:
    filename = "answer_key.txt"
    if not os.path.exists(filename):
      print("File not found. Try the other option.")
      continue
    break
  elif filename in [2]:
    filename = "backup.txt"
    if not os.path.exists(filename):
      print("File not found. Try the other option.")
      continue
    break
  else:
    print("Please input 1 or 2")


def load_answer_key(filename = filename):
    try:
        with open(filename, 'r') as f:
            content = f.read().upper()
        
        loaded_gt = [char for char in content if char in ["A", "B", "C", "D"]]
        
        if not loaded_gt:
            print("Error: No valid answers (A, B, C, D) found in the file.")
            return []
        
        print(f"Successfully loaded {len(loaded_gt)} answers from {filename}")
        return loaded_gt

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Solutions
gt = []

while True:
    gt = load_answer_key()
    if gt:
        break
    print("Please try again.")

while True:
  perm = input("Are you ready for answering? y/n: ")
  if perm in ["y","n","Y","N"]:
    break
  print('Allowed inputs are ["y","n","Y","N"]')

if perm in ["n","N"]:
  print("Waiting 5 seconds and then starting...")
  time.sleep(5)

points = 0
print("Choose from A,B,C and D. Input 0(zero) to skip.")
start = time.time()
for num,i in enumerate(gt):
  while True:
    user = input(f">>> Input your answer for Question No.{num + 1}: ")
    user = user.upper()
    if user in ["A","B","C","D","0"]:
      break
    print("Please input A,B,C,D or 0(Zero)")

  if user == i:
    print("Correct Answer !")
    points += 1
  elif user == "0":
    print("Question Skipped")
  else:
    print("Wrong Answer !")
end = time.time()
elapsed = end - start
mins, secs = divmod(elapsed, 60)
print(f"Your Score = {points}/{len(gt)}")
print(f"Time taken: {int(mins)} min {secs:.2f} sec")
