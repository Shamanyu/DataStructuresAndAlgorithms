# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/marut-and-girls/

class MarutAndGirls(object):

	def __init__(self):
		self.set_input(0, 0, set(), set())

	def get_user_input(self):
		M = int(input())
		qualities_required = set([int(number) for number in input().split()])
		N = int(input())
		girls_qualities_lists = list()
		for girl in range(0, N):
			girls_qualities_lists.append([int(number) for number in input().split()])
		self.set_input(M, qualities_required, N, girls_qualities_lists)

	def set_input(self, M, qualities_required, N, girls_qualities_lists):
		self.M = M
		self.N = N
		self.qualities_required = qualities_required
		self.girls_qualities_lists = girls_qualities_lists

	def output(self):
		possible_matches = 0
		for girl_qualities_list in self.girls_qualities_lists:
			match_count = 0
			for quality in girl_qualities_list:
				if quality in self.qualities_required:
					match_count += 1
			if match_count == self.M:
				possible_matches += 1
		return possible_matches

marut_and_girls = MarutAndGirls()

# marut_and_girls.set_input(5, {1, 2, 3, 4, 5}, 3, [[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5], [1, 2, 3, 4]])
# print(marut_and_girls.output())

marut_and_girls.get_user_input()
print(marut_and_girls.output())