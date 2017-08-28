class LinearSearch(object):

	def __init__(self):
		self.set_input(list(), None)

	def get_user_input(self):
		input_array = [int (number) for number in input().split()]
		key = int(input())
		self.set_input(input_array, key)

	def set_input(self, input_array, key):
		self.input_array = input_array
		self.input_size = len(input_array)
		self.key = key

	def find_key(self):
		for counter in range(0, self.input_size):
			if self.key == self.input_array[counter]:
				return counter+1
		return -1

linear_search = LinearSearch()

linear_search.get_user_input()
print(linear_search.find_key())
