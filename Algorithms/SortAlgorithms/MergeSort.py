import math

class MergeSort(object):

	def __init__(self):
		self.set_input(list())

	def get_user_input(self):
		input_array = [int(number) for number in input().split()]
		self.set_input(input_array)

	def set_input(self, input_array):
		self.input_array = input_array
		self.input_size = len(input_array)

	def merge_sort(self):
		self.merge_sort_helper(0, self.input_size-1)
		return self.input_array

	def merge_sort_helper(self, begin, end):
		if begin < end:
			mid = math.floor((end-begin)/2)+begin
			self.merge_sort_helper(begin, mid)
			self.merge_sort_helper(mid+1, end)
			self.merge(begin, mid, mid+1, end)

	def merge(self, left_array_begin, left_array_end, right_array_begin, right_array_end):
		output_array = self.input_array[left_array_begin:right_array_end+1]
		left_array_counter = left_array_begin
		right_array_counter = right_array_begin
		counter = left_array_begin
		while (left_array_counter<=left_array_end and right_array_counter<=right_array_end):
			if output_array[left_array_counter-left_array_begin] < output_array[right_array_counter-left_array_begin]:
				self.input_array[counter] = output_array[left_array_counter-left_array_begin]
				left_array_counter += 1
				counter += 1
			else:
				self.input_array[counter] = output_array[right_array_counter-left_array_begin]
				right_array_counter += 1
				counter += 1
		while (left_array_counter<=left_array_end):
			self.input_array[counter] = output_array[left_array_counter-left_array_begin]
			left_array_counter += 1
			counter += 1
		while (right_array_counter<=right_array_end):
			self.input_array[counter] = output_array[right_array_counter-left_array_begin]
			right_array_counter += 1
			counter += 1

	def print_output(self):
		output_array = self.merge_sort()
		for output in output_array:
			print (output, end=' ')
		print ('')

merge_sort = MergeSort()

merge_sort.set_input([1, 2, 3, 4])
merge_sort.print_output()

merge_sort.set_input([1, 2])
merge_sort.print_output()

merge_sort.set_input([40, 30])
merge_sort.print_output()

merge_sort.set_input([4, 3, 2, 1])
merge_sort.print_output()

merge_sort.set_input([1])
merge_sort.print_output()

merge_sort.set_input([])
merge_sort.print_output()

merge_sort.set_input([10, 10, 4, 10, 9, 1, 2, 5, 6, 100, -100, 10])
merge_sort.print_output()