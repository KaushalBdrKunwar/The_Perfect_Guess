import random

n = random.randint(1,100)
a = -1
guesses = 0

while(n!=a):
    a = int(input("Guess the Number: "))
    if(a > n):
        print("Lower number Please")
        guesses += 1

    elif(a<n):
       print("Higher number Please")
       guesses += 1
    

print(f"You have gussed the number {n} at this {guesses} gusses.")
    
    