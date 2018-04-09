# https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/exploring-ruins/

class ExploringRuins(object):

	def __init__(self):
		self.set_input('')

	def get_user_input(self):
		word = input('')
		self.set_input(word)

	def set_input(self, word):
		self.word = list(word)
		self.word_length = len(word)
		self.probable_word = self.word

	def get_word(self):
		for counter in range(0, self.word_length):
			if (self.probable_word[counter] == '?'):
				if (counter == 0 and counter+1 < self.word_length):
					if (self.probable_word[counter+1] != 'a'):
						self.set(counter, 'a')
					else:
						self.set(counter, 'b')
				elif (counter-1 >= 0 and counter == self.word_length-1):
					if (self.probable_word[counter-1] != 'a'):
						self.set(counter, 'a')
					else:
						self.set(counter, 'b')
				elif (counter-1 >= 0 and counter+1):
					if (self.probable_word[counter-1] != 'a' and self.probable_word[counter+1] != 'a'):
						self.set(counter, 'a')
					else:
						self.set(counter, 'b')
				else:
					self.set(counter, 'a')
		return "".join(self.probable_word)

	def set(self, position, value):
		self.probable_word[position] = value

exploring_ruins = ExploringRuins()

exploring_ruins.get_user_input()
print(exploring_ruins.get_word()) 