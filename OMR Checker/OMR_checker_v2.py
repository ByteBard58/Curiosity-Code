import time


# Solutions
gt = []
target = int(input(">>> How many questions are there in you question set? : "))
for i in range(target):
  while True:
    ans = input(f"Input the answer of question {i+1}: ")
    if ans in ["A","B","C","D"]:
      gt.append(ans)
      break
    print('Allowed inputs are ["A","B","C","D"]')

points = 0
neat = []
print("Choose from A,B,C and D. Input 0(zero) to skip.")
start = time.time()
for num,i in enumerate(gt):
  while True:
    user = input(f">>> Input your answer for Question No.{num + 1}: ")
    if user in ["A","B","C","D","0"]:
      break
    print("Please input A,B,C or D (in capital form)")

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

