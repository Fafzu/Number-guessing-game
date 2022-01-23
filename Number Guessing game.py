import random
randNumber = random.randint(1,100)
print(randNumber)
userGuess = None
guesses = 0

while userGuess != randNumber:
    userGuess = int(input("Enter your guess:\n"))
    guesses += 1
    if userGuess == randNumber:
        print("Congratulations! You guessed the correct number")
    else:
        if userGuess>randNumber:
            print("Unfortunately, You guesses it wrong! Enter a small number ")
        else:
            print("Unfortunately, You guesses it wrong! Enter a larger number ")
    

print(f"You guessed the number {guesses} guesses ")