import unittest

import camelcase

class CamelTest(unittest.TestCase):
	def test_capitalize_word(self):
		self.assertEqual("Word", camelcase.capitalize_word("word"))


	def test_append_word(self):
		test_list = []
		camelcase.append_word(test_list,"word")
		self.assertTrue(1, len(test_list))


	def test_join_words(self):
		unjoined_list = ["word word"]
		joined_list = camelcase.join_words(unjoined_list)
		self.assertIsNot(unjoined_list,joined_list)	



if __name__ == '__main__':
	unittest.main()			