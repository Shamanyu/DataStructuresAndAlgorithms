# http://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/

class MinCostPath():

	def __init__(self):
		self.set_costs([])

	def set_costs(self, cost_table):
		self.cost_table = cost_table
		self.m = len(cost_table)
		if self.m > 0:
			self.n = len(cost_table[0])
		else:
			self.n = 0
		self.min_cost_table = [[0 for column in range(0, self.n)] for row in range(0, self.m)]
		if self.m and self.n:
			self.min_cost_table[0][0] = self.cost_table[0][0]

	def get_min_cost(self, row, column):
		# import pdb; pdb.set_trace()
		if row > self.m or column > self.n:
			return "Node does not exist"
		elif row < 0 or column < 0:
			return float('inf')
		elif self.min_cost_table[row][column]:
			return self.min_cost_table[row][column]
		else:
			self.min_cost_table[row][column] = min(self.get_min_cost(row-1, column), 
				self.get_min_cost(row, column-1), 
				self.get_min_cost(row-1, column-1)) + self.cost_table[row][column]
			return self.min_cost_table[row][column]

min_cost_path = MinCostPath()

min_cost_path.set_costs([[1, 2, 3], [4, 8, 2], [1, 5, 3]])
print (min_cost_path.get_min_cost(4, 5))
print (min_cost_path.get_min_cost(2, 2))
print (min_cost_path.get_min_cost(0, 0))
print (min_cost_path.get_min_cost(0, 1))
print (min_cost_path.get_min_cost(1, 0))
print (min_cost_path.get_min_cost(1, 1))
print (min_cost_path.get_min_cost(1, 2))
