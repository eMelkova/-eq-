import random 
n = random.randint(1,100) 
m = int(input()) 
while m!=n: 
    m = int(input()) 
else: 
    print("Поздравляю, вы угадали число",n)
