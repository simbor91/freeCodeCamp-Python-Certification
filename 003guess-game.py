# 02 Loops and Sequences
# Lesson

import random

secret_number = random.randint(1,5)
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Try again!')

print('You got it! The number is ' + str(secret_number))