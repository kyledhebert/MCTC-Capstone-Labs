import string, unittest


import validator as val

class ValidatorTest(unittest.TestCase):
	def test_check_if_number_is_positive(self):
		self.assertTrue(val.is_positive(3))
		self.assertFalse(val.is_positive(-3))
		self.assertTrue(val.is_positive(0))


	def test_check_contains_whitespace(self):

		test_strings_with_whitespace = [
										'words and more words',
										'this string has spaces and a tab \t',
										'\t',
										've rticaltab\v',
										'newline\n',
										' ',
										'string with spaces \t tabs and newlines \n',
										string.whitespace]

		test_strings_without_whitespace = [
											'oneword',
											'123456'
											]									

		for st in test_strings_with_whitespace:
			self.assertTrue(val.contains_whitespace(st))

		for st in test_strings_without_whitespace:
			self.assertFalse(val.contains_whitespace(st))										