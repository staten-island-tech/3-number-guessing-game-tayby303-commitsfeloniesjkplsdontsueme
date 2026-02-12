import random
random=int(random.randint(1,100))
num=int(input("Guess the number 1-100: "))
while num!=random:
  if num>random:
    num=int(input("Lower: "))
  else:
    num=int(input("Higher: "))
if num==random:
  print("Correct")