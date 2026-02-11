import random
random=int(random.randint(1,3))
num=int(input("Guess the number 1-100: "))
if num!=random:
  while num!=random:
    if num>random:
      num=int(input("Lower: "))
    else:
      num=int(input("Higher: "))
else:
  print("Correct")