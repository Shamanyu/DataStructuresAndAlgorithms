n = int(raw_input("Enter size of array: "))
unique_rows = set()
unique_columns = set()
input_array = [[0 for x in range(n)] for x in range(n)]
for counter1 in range(n):
	for counter2 in range(n):
		input_array[counter1][counter2] = int(raw_input("\nEnter element: "))
		if input_array[counter1][counter2] == 0:
			unique_rows.update([counter1])
			unique_columns.update([counter2])
for row in unique_rows:
	for counter in range(n):
		input_array[row][counter] = 0
for counter in range(n):
	for column in unique_columns:
		input_array[counter][column] = 0
print input_array
