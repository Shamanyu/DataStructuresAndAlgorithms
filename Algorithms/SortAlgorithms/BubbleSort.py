class BubbleSort(object):

	def __init__(self):
		self.set_input(list())

	def get_user_input(self):
		input_array = [int(number) for number in input().split()]

	def set_input(self, input_array):
		self.input_array = input_array
		self.input_size = len(input_array)

	def bubble_sort(self):
		output_array = self.input_array
		for outer_loop_counter in range(0, self.input_size):
			for inner_loop_counter in range(0, self.input_size-outer_loop_counter-1):
				if output_array[inner_loop_counter] > output_array[inner_loop_counter+1]:
					output_array[inner_loop_counter] += output_array[inner_loop_counter+1]
					output_array[inner_loop_counter+1] = output_array[inner_loop_counter] - output_array[inner_loop_counter+1]
					output_array[inner_loop_counter] -= output_array[inner_loop_counter+1]
		return output_array

	def print_output(self):
		output_array = self.bubble_sort()
		for output in output_array:
			print (output, end=' ')
		print ('')

bubble_sort = BubbleSort()

bubble_sort.set_input([1, 2, 3, 4])
bubble_sort.print_output()

bubble_sort.set_input([1, 2])
bubble_sort.print_output()

bubble_sort.set_input([4, 3, 2, 1])
bubble_sort.print_output()

bubble_sort.set_input([1])
bubble_sort.print_output()

bubble_sort.set_input([])
bubble_sort.print_output()

bubble_sort.set_input([10, 10, 4, 10, 9, 1, 2, 5, 6, 100, -100, 10])
bubble_sort.print_output()