"""
Number Guessing Game, upgraded

**Uses:** `random.randint()`

1. Open your Week 2 guessing game.
2. Add `import random` at the top of the file.
3. Find the line where you set the secret number.
4. Replace the fixed number with `random.randint(1, 100)`.
5. Run the game a few times and check that the secret number changes each time.
 """

import random

secret_number = random.randint(1, 100)

set guess = None

while guess != secret_number:

    guess = int(input("Guess a number between 1 and 100: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the secret number.")