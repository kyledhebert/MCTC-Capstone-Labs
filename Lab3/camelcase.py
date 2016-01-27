def capitalize_word(word):
	return word.capitalize()
	
def append_word(output_list, word):
	output_list.append(word)	

def join_words(output_list):
	return "".join(output_list)		

def main():
	sentence = input("Enter a sentence: ").lower()
	input_list = sentence.split()
	output_list = []

	for word in input_list:
		if word == input_list[0]:
			append_word(output_list,word)
		else:
			cap_word = capitalize_word(word)
			append_word(output_list,cap_word)

	print(join_words(output_list))


if __name__ == '__main__':
	main()
					




