import random
# generate a random number between 1 and 100
number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# loop until the user guesses the correct number
while True:
    guess = int(input("Guess the number: "))

    # check if the guess is too high or too low
    if guess < number:
        print("Too low, try again!")
    elif guess > number:
        print("Too high, try again!")
    else:
        # the guess is correct, end the game
        print("Congratulations, you guessed the number!")
        break
