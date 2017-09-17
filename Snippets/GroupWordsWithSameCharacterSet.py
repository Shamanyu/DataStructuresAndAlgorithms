word_list = input().split()

word_dictionary = dict()

for original_word in word_list:
	word = "".join(set(original_word))
	key = 0
	for character in word:
		key += ord(character) - ord('a')
	words_for_key = word_dictionary.get(key, [])
	words_for_key.append(original_word)
	word_dictionary[key] = words_for_key

for key in word_dictionary:
	print (word_dictionary[key])
