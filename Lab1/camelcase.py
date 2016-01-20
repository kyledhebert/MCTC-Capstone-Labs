
sentence = input("Enter a sentence: ").lower()


input_list = sentence.split()
output_list = []

for word in input_list:
	if word == input_list[0]:
		output_list.append(word)
	else:
		cap_word = word.capitalize()
		output_list.append(cap_word)

print("".join(output_list))			



