# http://www.geeksforgeeks.org/dynamic-programming-set-5-edit-distance/

from LongestCommonSubsequence import LongestCommonSubsequence

class EditDistance():

	def __init__(self):
		self.reset_stats('', '')

	def reset_stats(self, string1, string2):
		self.string1 = string1
		self.string2 = string2

	def get_edit_distance(self, string1, string2):
		self.reset_stats(string1, string2)
		return self.get_edit_distance_worker(string1, string2)

	def get_edit_distance_worker(self, string1, string2):
		longest_common_subsequence = LongestCommonSubsequence()
		return max(len(string1), len(string2)) - longest_common_subsequence.get_longest_common_subsequence_length(string1, string2)

edit_distance = EditDistance()

print (edit_distance.get_edit_distance('geek', 'gesek'))
# print (edit_distance.get_edit_distance('cat', 'cut'))
# print (edit_distance.get_edit_distance('sunday', 'saturday'))
# print (edit_distance.get_edit_distance('abc', 'abd'))
# print (edit_distance.get_edit_distance('abc', 'abd'))
# print (edit_distance.get_edit_distance('abc', 'abd'))
# print (edit_distance.get_edit_distance('abc', 'abd'))
# print (edit_distance.get_edit_distance('abc', 'abd'))
