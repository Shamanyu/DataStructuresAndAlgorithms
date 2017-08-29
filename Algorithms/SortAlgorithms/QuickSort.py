# import random

class QuickSort(object):

	def __init__(self):
		self.set_input(list())

	def get_user_input(self):
		input_array = [int(number) for number in input().split()]
		self.set_input(input_array)

	def set_input(self, input_array):
		self.input_array = input_array
		self.input_size = len(input_array)

	def quick_sort(self):
		self.quick_sort_helper(0, self.input_size-1)
		return self.input_array

	def quick_sort_helper(self, begin, end):
		if begin < end:
			pi = self.partition(begin, end)
			self.quick_sort_helper(begin, pi-1)
			self.quick_sort_helper(pi+1, end)

	def partition(self, begin, end):
		# import pdb; pdb.set_trace()
		pivot = self.input_array[end]
		counter1 = begin-1
		for counter2 in range(begin, end):
			if (self.input_array[counter2] <= pivot):
				counter1 += 1
				self.swap(counter1, counter2)
		self.swap(counter1+1, end)
		return counter1+1

	def swap(self, position1, position2):
		if position1 != position2:
			self.input_array[position1] += self.input_array[position2]
			self.input_array[position2] = self.input_array[position1] - self.input_array[position2]
			self.input_array[position1] -= self.input_array[position2]

	def print_output(self):
		output_array = self.quick_sort()
		for output in output_array:
			print (output, end=' ')
		print ('')

quick_sort = QuickSort()

quick_sort.set_input([1, 2, 3, 4])
quick_sort.print_output()

quick_sort.set_input([2, 1])
quick_sort.print_output()

quick_sort.set_input([40, 30])
quick_sort.print_output()

quick_sort.set_input([3, 2, 1])
quick_sort.print_output()

quick_sort.set_input([4, 3, 2, 1])
quick_sort.print_output()

quick_sort.set_input([1])
quick_sort.print_output()

quick_sort.set_input([])
quick_sort.print_output()

quick_sort.set_input([10, 10, 4, 10, 9, 1, 2, 5, 6, 100, -100, 10])
quick_sort.print_output()