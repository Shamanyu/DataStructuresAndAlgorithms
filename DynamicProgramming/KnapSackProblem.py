# http://www.geeksforgeeks.org/dynamic-programming-set-10-0-1-knapsack-problem/

class KnapSackProblem():

	def __init__(self):
		self.set_input(list(), list(), 0)

	def set_input(self, values, weights, bag_capacity):
		if len(values) != len(weights):
			return "Error"
		self.values = values
		self.weights = weights
		self.item_count = len(values)
		self.bag_capacity = bag_capacity
		self.max_bag_value_table = [[0 for weight in range(0, bag_capacity+1)] \
			for value in range(0, self.item_count+1)]

	def get_maximum_bag_value(self):
		for counter in range(0, self.item_count+1):
			for weight in range(0, self.bag_capacity+1):
				if (counter == 0 or weight == 0):
					self.max_bag_value_table[counter][weight] = 0
				elif (self.weights[counter-1] <= weight):
					self.max_bag_value_table[counter][weight] = \
						max(self.values[counter-1] + \
						self.max_bag_value_table[counter-1][weight-self.weights[counter-1]], 
						self.max_bag_value_table[counter-1][weight])
				else:
					self.max_bag_value_table[counter][weight] = \
						self.max_bag_value_table[counter-1][weight]

		return self.max_bag_value_table[self.item_count][self.bag_capacity]

knapsack_problem = KnapSackProblem()

knapsack_problem.set_input([1, 2, 3], [1, 2, 3], 4)
print (knapsack_problem.get_maximum_bag_value())

knapsack_problem.set_input([6, 10, 20], [1, 2, 3], 5)
print (knapsack_problem.get_maximum_bag_value())

knapsack_problem.set_input([60, 100, 200], [10, 20, 30], 50)
print (knapsack_problem.get_maximum_bag_value())

knapsack_problem.set_input([60, 100, 120], [10, 20, 30], 50)
print (knapsack_problem.get_maximum_bag_value())