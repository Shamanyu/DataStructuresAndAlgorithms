#  http://www.geeksforgeeks.org/dynamic-programming-set-1/
# Fibonacci numbers

class Fibonacci():

	def __init__(self):
		self.fibonacci_table = list()
		self.fibonacci_table.append(0)
		self.fibonacci_table.append(0)
		self.fibonacci_table.append(1)

	def get_nth(self, n):
		if len(self.fibonacci_table) > n:
			return self.fibonacci_table[n]
		else:
			self.fibonacci_table.append(self.get_nth(n-1) + self.get_nth(n-2))
			return self.fibonacci_table[n]

# fibonacci_table = Fibonacci()

# print (fibonacci_table.get_nth(1))
# print (fibonacci_table.get_nth(2))
# print (fibonacci_table.get_nth(3))
# print (fibonacci_table.get_nth(4))
# print (fibonacci_table.get_nth(5))
# print (fibonacci_table.get_nth(6))
