# http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/

class MatrixChainMultiplication():

	def __init__(self):
		self.set_matrice_dimensions([])

	def set_matrice_dimensions(self, matrice_dimensions):
		self.matrice_dimensions = matrice_dimensions
		self.number_of_matrix = len(matrice_dimensions) - 1
		self.minimum_multiplications = [[0 for column in range(0, self.number_of_matrix+1)] 
			for row in range(0, self.number_of_matrix+1)]

	def get_minimum_multiplications(self):
		# import pdb; pdb.set_trace()
		for chain_length in range(2, self.number_of_matrix+1):
			for first_matrix_in_chain in range(1, self.number_of_matrix-chain_length+2):
				last_matrix_in_chain = first_matrix_in_chain + chain_length - 1
				self.minimum_multiplications[first_matrix_in_chain][last_matrix_in_chain] = \
					float('inf')
				for counter in range(first_matrix_in_chain, last_matrix_in_chain):
					cost = self.minimum_multiplications[first_matrix_in_chain][counter] + \
						self.minimum_multiplications[counter+1][last_matrix_in_chain] + \
						self.matrice_dimensions[first_matrix_in_chain-1] * \
						self.matrice_dimensions[counter] * \
						self.matrice_dimensions[last_matrix_in_chain]
					if (cost < self.minimum_multiplications[first_matrix_in_chain]
						[last_matrix_in_chain]):
						self.minimum_multiplications[first_matrix_in_chain][last_matrix_in_chain] = \
							cost
		return self.minimum_multiplications[1][self.number_of_matrix]

matrix_chain_multiplication = MatrixChainMultiplication()

matrix_chain_multiplication.set_matrice_dimensions([40, 20, 30, 10, 30])
print (matrix_chain_multiplication.get_minimum_multiplications())

matrix_chain_multiplication.set_matrice_dimensions([10, 20, 30, 40, 30])
print (matrix_chain_multiplication.get_minimum_multiplications())

matrix_chain_multiplication.set_matrice_dimensions([10, 20, 30])
print (matrix_chain_multiplication.get_minimum_multiplications())