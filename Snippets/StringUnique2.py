input_string = input('')

input_string = list(input_string)
input_string.sort()
input_string = ''.join(input_string)

unique = True

for counter in range(0, len(input_string)-1):
    if input_string[counter] == input_string[counter+1]:
        unique = False
        break
print (unique)
