import random, unittest

import guess

class GuessTest(unittest.TestCase):
	def setUp(self):
		self.secret_number = 6
		self.guess_count = 0

	
	def test_guess_is_too_low(self):
		self.assertTrue(guess.guess_too_low(4,self.secret_number))


	def test_guess_is_too_high(self):
		self.assertTrue(guess.guess_too_high(7, self.secret_number))


if __name__ == '__main__':
	unittest.main()		