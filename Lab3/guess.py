import random



def get_guess():
	return int(input("Guess a number between 0 and 9: "))


def display_result(guess, secret_number):
	if guess_too_low(guess,secret_number):
		print("Guess higher")
	elif guess_too_high(guess, secret_number):
		print("Guess lower")	
	else:
		print("You got it!")
		
		

def guess_too_low(guess, secret_number):
	if guess < secret_number:
		return True


def guess_too_high(guess,secret_number):
	if guess > secret_number:
		return True				


def main():
	secret_number = random.randint(0,9)
	guess_count = 0
	player_guess = None
	while secret_number != player_guess:
		player_guess = get_guess()
		guess_count += 1
		display_result(player_guess, secret_number)

	print("It took you {} guesses".format(guess_count))	


if __name__ == '__main__':
	main()
