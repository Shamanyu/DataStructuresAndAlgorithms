# https://www.hackerearth.com/zh/practice/algorithms/searching/linear-search/practice-problems/algorithm/monk-takes-a-walk/

class MonkTakesAWalk(object):

	def __init__(self):
		self.set_input(0, [])

	def get_user_input(self):
		number_of_test_cases = int(input())
		test_cases = list()
		for test_case_number in range(0, number_of_test_cases):
			user_input = input()
			test_cases.append(user_input)
		self.set_input(number_of_test_cases, test_cases)

	def set_input(self, number_of_test_cases, test_cases):
		self.number_of_test_cases = number_of_test_cases
		self.test_cases = test_cases
		self.trees_to_attend_to = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}

	def get_output(self):
		output = list()
		for test_case in self.test_cases:
			number_of_trees_to_attend_to = 0
			for tree in test_case:
				if tree in self.trees_to_attend_to:
					number_of_trees_to_attend_to += 1
			output.append(number_of_trees_to_attend_to)
		return output

monk_takes_a_walk = MonkTakesAWalk()

monk_takes_a_walk.get_user_input()
for output in monk_takes_a_walk.get_output():
	print(output)

