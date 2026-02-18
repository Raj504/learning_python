import random
from re import A

random.randint(1, 100)
jackot = random.randint(1, 100)

guess = int(input("chal guess kar"))
counter = 1
while guess != jackot:
    if guess <jackot:
        print("guess higher")
    else:
        print("guess lower")
    
    guess = int(input("chal guess kar"))
    counter+=1


print("sahi jawab")
print("you took", counter, "attempts")