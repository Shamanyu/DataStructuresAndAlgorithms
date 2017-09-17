input_string = input('')

input_string_sorted = ''.join(sorted(list(input_string)))

unique = True

for counter in range(0, len(input_string_sorted)-1):
    if input_string_sorted[counter] == input_string_sorted[counter+1]:
        unique = False
        break
print (unique)
