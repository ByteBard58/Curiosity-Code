import time


'''
OMR Checker
This script is used to check the OMR sheet of a student. 
In this version, the list of answers are stored in the script itself. 
You can add your own list of answers by adding it to the script.
You can also add multiple question answer sets and then select the set you want to practice with.

NOTE: There is another version of this utility named "OMR_checker_v2.py" in the same sub-directory. In that 
version, you have to input the answers through CLI and then start answering them.
'''






















# Solutions
gt_1 = ['D', 'D', 'C', 'B', 'D', 'B', 'B', 'C', 'C', 'C', 'A', 'D', 'D', 'D', 'A', 'A', 'A', 'D']
gt_2 = ['D', 'C', 'B', 'A', 'A', 'A', 'C', 'C', 'D', 'C']
gt_3 = ['D', 'A', 'A', 'C', 'B', 'C', 'C', 'A', 'C', 'B', 'C', 'B', 'B', 'C', 'A']
gt_4 = ['D', 'B', 'B', 'D', 'C', 'D', 'C', 'B', 'C', 'A', 'A', 'C', 'B', 'C', 'A']
gt_5 = ['B', 'A', 'B', 'B', 'D', 'C', 'D', 'C', 'A', 'C']
gt_6 = ['B', 'B', 'B', 'C', 'A', 'B', 'C', 'B', 'A', 'B']
gt_7 = ['B', 'A', 'A', 'A', 'C', 'D', 'B', 'A', 'C', 'C']


while True:
  qnb = input(">>> Which set would you like to practice with? Input  within 1-7:")
  if qnb not in[str(i) for i in range(1,8)]:
    print("INPUT WITHIN 1-7 !!!")
    continue
  elif qnb == "1":
    gt = gt_1
  elif qnb == "2":
    gt = gt_2
  elif qnb == "3":
    gt = gt_3
  elif qnb == "4":
    gt = gt_4
  elif qnb == "5":
    gt = gt_5
  elif qnb == "6":
    gt = gt_6
  elif qnb == "7":
    gt = gt_7
  break



points = 0
neat = []
print("Choose from A,B,C and D. Input 0(zero) to skip.")
start = time.time()
for num,i in enumerate(gt):
  while True:
    user = input(f">>> Input your answer for Question No.{num + 1}: ")
    if user in ["A","B","C","D","0"]:
      break
    print("Please input A,B,C,D (in capital form) or 0(Zero)")

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

