class InsertionSort(object):

	def __init__(self):
		self.set_input(list())

	def get_user_input(self):
		input_array = [int(number) for number in input().split()]
		self.set_input(input_array)

	def set_input(self, input_array):
		self.input_array = input_array
		self.input_size = len(input_array)

	def insertion_sort(self):
		for outer_loop_counter in range(0, self.input_size):
			for inner_loop_counter in range(0, self.input_size-1):
				while(self.input_array[inner_loop_counter] > self.input_array[inner_loop_counter+1]):
					self.input_array[inner_loop_counter] += self.input_array[inner_loop_counter+1]
					self.input_array[inner_loop_counter+1] = self.input_array[inner_loop_counter] - self.input_array[inner_loop_counter+1]
					self.input_array[inner_loop_counter] -= self.input_array[inner_loop_counter+1]
		return self.input_array

	def print_output(self):
		output_array = self.insertion_sort()
		for output in output_array:
			print (output, end=' ')
		print ('')

insertion_sort = InsertionSort()

insertion_sort.set_input([1, 2, 3, 4])
insertion_sort.print_output()

insertion_sort.set_input([1, 2])
insertion_sort.print_output()

insertion_sort.set_input([4, 3, 2, 1])
insertion_sort.print_output()

insertion_sort.set_input([1])
insertion_sort.print_output()

insertion_sort.set_input([])
insertion_sort.print_output()

insertion_sort.set_input([10, 10, 4, 10, 9, 1, 2, 5, 6, 100, -100, 10])
insertion_sort.print_output()