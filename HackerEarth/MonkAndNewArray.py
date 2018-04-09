# https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/monk-and-new-array/

from bisect import bisect_left

class MonkAndNewArray(object):

	def __init__(self):
		self.set_input(0, 0	, list(list()))

	def get_user_input(self):
		N, M = [int(number) for number in input().split()]
		matrix = [[0 for column in range(0, M)] for row in range(0, N)]
		for row in range(0, N):
			matrix[row] = [int(number) for number in input().split()]
		self.set_input(N, M, matrix)

	def set_input(self, N, M, matrix):
		self.N = N
		self.M = M
		self.matrix = matrix

	def MinimumPossibleAbsoluteDifference(self):
		for row in range(0, self.N):
			self.matrix[row] = sorted(self.matrix[row])
		minimum_possible_absolute_difference = float('inf')
		for row in range(0, self.N-1):
			for column in range(0, self.M):
				current_element = self.matrix[row][column]
				current_element_partner_position = bisect_left(self.matrix[row+1], current_element)
				if current_element_partner_position == 0:
					current_element_partner_difference = self.matrix[row+1][current_element_partner_position]-current_element
				elif current_element_partner_position < self.M:
					current_element_partner_difference = min(current_element-self.matrix[row+1][current_element_partner_position-1], self.matrix[row+1][current_element_partner_position]-current_element) 
				elif current_element_partner_position == self.M-1:
					current_element_partner_difference = current_element-self.matrix[row+1][current_element_partner_position-1]
				minimum_possible_absolute_difference = min(minimum_possible_absolute_difference, current_element_partner_difference)
		return minimum_possible_absolute_difference

monk_and_new_array = MonkAndNewArray()

monk_and_new_array.get_user_input()
print(monk_and_new_array.MinimumPossibleAbsoluteDifference())