import random

randNumber = random.randint(1,100)
#print(randNumber)
Gusses = 0
YourGuess = None
while(YourGuess != randNumber):
    YourGuess = int(input("Enter your Guess:"))
    Gusses += 1
    if(YourGuess == randNumber):
        print("Your Guess is correct!!")
    else:
        if(YourGuess > randNumber):
            print("You Gussed it wrong! Enter a smaller number")
        else:
            print("You Gussed it wrong! Enter a larger number")


print(f"You guess the number in {Gusses} guesses")