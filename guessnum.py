import random
random=random.randint(1,100)
num=int(input("Guess the number 1-100: "))
while num!=random:
  if num>random:
    num=int(input("Lower: "))
  elif num<random:
    num=int(input("Higher: "))
if num==random:
  print("Correct")