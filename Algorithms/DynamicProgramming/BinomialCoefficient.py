# http://www.geeksforgeeks.org/dynamic-programming-set-9-binomial-coefficient/

class BinomialCoefficient():

	def __init__(self):
		self.set_values(0, 0)

	def set_values(self, n, k):
		self.n = n
		self.k = k
		self.binomial_coefficient_table = [[0 for selections in range(0, k+1)] \
			for set in range(0, n+1)]

	def get_binomial_coefficient(self):
		return self.get_binomial_coefficient_worker(self.n, self.k)

	def get_binomial_coefficient_worker(self, n, k):
		if n < k:
			return 0
		elif k == 0 or n == k:
			return 1
		elif self.binomial_coefficient_table[n][k]:
			return self.binomial_coefficient_table[n][k]
		else:
			self.binomial_coefficient_table[n][k] = \
				self.get_binomial_coefficient_worker(n-1, k-1) + \
				self.get_binomial_coefficient_worker(n-1, k)
			return self.binomial_coefficient_table[n][k]

binomial_coefficient = BinomialCoefficient()

binomial_coefficient.set_values(4, 2)
print (binomial_coefficient.get_binomial_coefficient())

binomial_coefficient.set_values(5, 2)
print (binomial_coefficient.get_binomial_coefficient())