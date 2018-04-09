# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/maximum-occurrence-9/

class MaximumOccurence(object):

	def __init__(self):
		self.set_string("")

	def set_string(self, input_string):
		self.string = input_string
		self.occurence_count = dict()
		for character in self.string:
			if character in self.occurence_count:
				self.occurence_count[character] += 1
			else:
				self.occurence_count[character] = 1

	def get_most_frequent_character(self):
		most_frequent_character = ''
		most_frequent_character_count = -1
		for character in self.occurence_count:
			if self.occurence_count[character] > most_frequent_character_count:
				most_frequent_character = character
				most_frequent_character_count = self.occurence_count[most_frequent_character]
			elif self.occurence_count[character] == most_frequent_character_count:
				if character < most_frequent_character:
					most_frequent_character = 	character
		return most_frequent_character, most_frequent_character_count

maximum_occurence = MaximumOccurence()

# maximum_occurence.set_string('Shubham##ss#s$$$$#!!!!9')
# most_frequent_character, most_frequent_character_count = maximum_occurence.get_most_frequent_character()
# print(most_frequent_character, most_frequent_character_count)

maximum_occurence.set_string(input(''))
most_frequent_character, most_frequent_character_count = maximum_occurence.get_most_frequent_character()
print(most_frequent_character, most_frequent_character_count)