import random
secret_number = random.randint(1, 10)
guess = 0
print("i am thinking of a number between 1 and 10 can you guess it!")
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        print("correct.")

