import time





























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

