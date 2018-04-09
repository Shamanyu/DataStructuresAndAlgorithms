# https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/pair-sums/

class PairSum(object):

	def __init__(self):
		self.set_input(0, list(), 0)

	def get_user_input(self):
		N, K = [int(number) for number in input().split()]
		input_array = [int(number) for number in input().split()]
		self.set_input(N, input_array, K)

	def set_input(self, N, input_array, K):
		self.N = N
		self.input_array = input_array
		self.K = K

	def output(self):
		output = "NO"
		complement_set = set()
		for counter in range(0, self.N):
			if self.input_array[counter] in complement_set:
				output = "YES"
				break
			else:
				complement_set.add(self.K - self.input_array[counter])
		return output

pair_sum = PairSum()

# pair_sum.set_input(5, [1, 2, 3, 4, 5], 9)
# print(pair_sum.output())

pair_sum.get_user_input()
print(pair_sum.output())