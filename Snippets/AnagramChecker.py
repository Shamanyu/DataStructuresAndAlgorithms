input_string1 = input('')
input_string2 = input('')

character_check = [0]*256

for character in input_string1:
    character_check[ord(character)] += 1

for character in input_string2:
    character_check[ord(character)] -= 1

anagram = True

for x in range(0, 256):
    if character_check[x] != 0:
        anagram = False
        break

print (anagram)
