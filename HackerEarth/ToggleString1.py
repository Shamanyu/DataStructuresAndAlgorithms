input_string = input('')

input_list = list(input_string)

output_list = [input_list[counter].upper() if input_list[counter].islower() else input_list[counter].lower() for counter in range(0, len(input_list))]

output_string = "".join(output_list)

print (output_string)
