number_of_rows, number_of_columns = list(map(int, input().split()))

input_matrix = [[0 for y in range(number_of_columns)] for x in range(number_of_rows)]

input_numbers = list(map(int, input().split()))

counter = 0
for x in range(number_of_rows):
	for y in range(number_of_columns):
		input_matrix[x][y] = input_numbers[counter]
		counter = counter + 1

print (input_matrix)
