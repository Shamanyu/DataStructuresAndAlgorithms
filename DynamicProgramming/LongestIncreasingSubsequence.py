# http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/

class LongestIncreasingSubsequence():

	def __init__(self):
		self.reset_stats()

	def reset_stats(self):
		self.longest_subsequence_length = 0
		self.current_element = -1

	def get_longest_subsequence_length(self, input_array):
		self.reset_stats()
		return self.get_longest_subsequence_length_worker(input_array)

	def get_longest_subsequence_length_worker(self, input_array):
		input_size = len(input_array)
		if input_size == 0:
			return self.longest_subsequence_length
		elif input_array[0] > self.current_element:
			self.current_element = input_array[0]
			self.longest_subsequence_length += 1
		return self.get_longest_subsequence_length_worker(input_array[1:])

# longest_increasing_subsequence = LongestIncreasingSubsequence()

# print(longest_increasing_subsequence.get_longest_subsequence_length([1, 2, 3, 4, 5]))
# print(longest_increasing_subsequence.get_longest_subsequence_length([10, 22, 9, 33, 21, 50, 41, 60, 80]))
# print(longest_increasing_subsequence.get_longest_subsequence_length([1, 2, 3, 4, 5]))
# print(longest_increasing_subsequence.get_longest_subsequence_length([1, 2, 3, 4, 5]))
