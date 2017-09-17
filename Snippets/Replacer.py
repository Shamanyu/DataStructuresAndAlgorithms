input_string = raw_input("Enter the string: ")
input_list = list(input_string)
for character in range(len(input_list)):
	if input_list[character] == ' ':
		input_list[character] = '%20'
print ''.join(input_list)
