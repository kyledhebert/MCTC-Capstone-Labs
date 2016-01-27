def is_positive(number):
	if number > 0:
		return True
	return False	


def contains_whitespace(s):
	if ' ' in s:
		return True
	elif '\t' in s:
		return True

	return False			