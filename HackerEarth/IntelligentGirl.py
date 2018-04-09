# https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/intelligent-girl-1/

class IntelligentGirl(object):

	def __init__(self):
		self.set_input(list())

	def get_user_input(self):
		input_string = [int(number) for number in list(input())]
		self.set_input(input_string)

	def set_input(self, input_string):
		self.input_string = input_string
		self.input_length = len(self.input_string)
		self.output_array = [0 for counter in range(0, self.input_length)]

	def get_output(self):
		for counter in range(self.input_length-1, -1, -1):
			if self.input_string[counter]%2 == 0:
				if counter < self.input_length-1:
					self.output_array[counter] = self.output_array[counter+1] + 1
				else:
					self.output_array[counter] = 1
			else:
				if counter < self.input_length-1:
					self.output_array[counter] = self.output_array[counter+1]
		return self.output_array

intelligent_girl = IntelligentGirl()

intelligent_girl.get_user_input()
output_array = intelligent_girl.get_output()
for output in output_array:
	print(output, end=' ')