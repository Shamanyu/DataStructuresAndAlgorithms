array_size = int(input(''))

rows = list()
columns = list()

input_array = [['0']*array_size]*array_size

for row_counter in range(0, array_size):
    input_array[row_counter] = input('').split(' ')
    for column_counter in range(0, array_size):
        if input_array[row_counter][column_counter] == '0':
            rows.append(row_counter)
            columns.append(column_counter)

rows = set(rows)
columns = set(columns)

for element in rows:
    input_array[element] = ['0']*array_size


for element in columns:
    for row in range(0, array_size):
        input_array[row][element] = '0'

print (input_array)
