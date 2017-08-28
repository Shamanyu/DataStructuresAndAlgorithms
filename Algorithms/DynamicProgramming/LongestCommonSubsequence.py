# http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/

class LongestCommonSubsequence():

	def __init__(self):
		self.reset_stats('', '')

	def reset_stats(self, string1, string2):
		self.longest_common_subsequence_length = 0
		self.string1 = string1
		self.string2 = string2
		self.data_matrix = [[-1 for counter1 in range(0, len(string2))] for counter2 in range(0, len(string1))]

	def get_longest_common_subsequence_length(self, string1, string2):
		self.reset_stats(string1, string2)
		return self.get_longest_common_subsequence_length_worker(string1, string2)

	def get_longest_common_subsequence_length_worker(self, string1, string2):
		# import pdb; pdb.set_trace()
		# print (self.data_matrix)
		index1 = len(string1) - 1
		index2 = len(string2) - 1
		if index1 < 0 or index2 < 0:
			return 0
		elif self.data_matrix[index1][index2] != -1:
			return self.data_matrix[index1][index2]
		else:
			if string1[index1] == string2[index2]:
				self.data_matrix[index1][index2] = max(self.get_longest_common_subsequence_length_worker(string1, string2[0:-1]), self.get_longest_common_subsequence_length_worker(string1[0:-1], string2)) + 1
			else:
				self.data_matrix[index1][index2] = max(self.get_longest_common_subsequence_length_worker(string1, string2[0:-1]), self.get_longest_common_subsequence_length_worker(string1[0:-1], string2))
			return self.data_matrix[index1][index2]

# longest_common_subsequence = LongestCommonSubsequence()

# print (longest_common_subsequence.get_longest_common_subsequence_length('ab', 'ab'))
# print (longest_common_subsequence.get_longest_common_subsequence_length('abcdfe', 'xyzabacwwwwwdef'))
