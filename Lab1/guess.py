#!/usr/bin/env python3

import random

secret_number = random.randint(0,9)
guess_count = 0

while True:
	guess = int(input("Guess a number between 0 and 9: "))
	if secret_number == guess:
		guess_count += 1
		print("You got it!")
		print("It took you {} guesses".format(guess_count))
		break
	elif guess < secret_number:
		guess_count += 1
		print("Guess higher")
	elif guess > secret_number:
		guess_count += 1
		print("Guess lower")	
		
