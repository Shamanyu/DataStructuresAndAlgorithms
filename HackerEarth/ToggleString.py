input_string = input('')

input_list = list(input_string)

for counter in range(0, len(input_list)):
	if input_list[counter].isupper():
		input_list[counter] = input_list[counter].lower()
	elif input_list[counter].islower():
		input_list[counter] = input_list[counter].upper()

output_string = "".join(input_list)

print (output_string)
