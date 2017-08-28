class SelectionSort(object):

	def __init__(self):
		self.set_input(list())

	def get_user_input(self):
		input_array = [int(number) for number in input().split()]
		self.set_input(input_array)

	def set_input(self, input_array):
		self.input_array = input_array
		self.input_size = len(input_array)

	def selection_sort(self):
		for outer_loop_counter in range(0, self.input_size):
			min_position = outer_loop_counter
			min = self.input_array[outer_loop_counter]
			flag = 0
			for inner_loop_counter in range(outer_loop_counter+1, self.input_size):
				if self.input_array[inner_loop_counter] < min:
					min_position = inner_loop_counter
					min = self.input_array[inner_loop_counter]
					flag = 1
			if flag:
				self.input_array[outer_loop_counter] += self.input_array[min_position]
				self.input_array[min_position] = self.input_array[outer_loop_counter] - self.input_array[min_position]
				self.input_array[outer_loop_counter] -= self.input_array[min_position]
		return self.input_array

	def print_output(self):
		output_array = self.selection_sort()
		for output in output_array:
			print (output, end=' ')
		print ('')

selection_sort = SelectionSort()

selection_sort.set_input([1, 2, 3, 4])
selection_sort.print_output()

selection_sort.set_input([1, 2])
selection_sort.print_output()

selection_sort.set_input([4, 3, 2, 1])
selection_sort.print_output()

selection_sort.set_input([1])
selection_sort.print_output()

selection_sort.set_input([])
selection_sort.print_output()

selection_sort.set_input([10, 10, 4, 10, 9, 1, 2, 5, 6, 100, -100, 10])
selection_sort.print_output()