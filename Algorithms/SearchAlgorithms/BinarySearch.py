import math

class BinarySearch(object):

	def __init__(self):
		self.set_input(list(), None)

	def get_user_input(self):
		input_array = [int(number) for number in input().split()]
		key = int(input())

	def set_input(self, input_array, key):
		self.input_array = input_array
		self.input_size = len(input_array)
		self.key = key

	def find_key(self):
		counter = math.floor(self.input_size/2)
		low = 0
		high = self.input_size-1
		while(counter >= low and counter <= high and low <= high):
			if self.input_array[counter] == self.key:
				return counter+1
			elif self.input_array[counter] < self.key:
				low = counter+1
				counter = math.floor((low+high)/2)
			else:
				high = counter-1
				counter = math.floor((low+high)/2)
		return -1

binary_search = BinarySearch()

binary_search.set_input([1], 1)
print (binary_search.find_key())

binary_search.set_input([2], 1)
print (binary_search.find_key())

binary_search.set_input([0], 1)
print (binary_search.find_key())

binary_search.set_input([1, 2, 3, 4], 1)
print (binary_search.find_key())

binary_search.set_input([], 1)
print (binary_search.find_key())

binary_search.set_input([1, 2, 3, 4], 2)
print (binary_search.find_key())

binary_search.set_input([1, 2, 3, 4, 5], 10)
print (binary_search.find_key())