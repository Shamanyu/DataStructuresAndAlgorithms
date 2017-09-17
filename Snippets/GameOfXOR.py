input_array = list(map(int, input().split()))

result = 0
if (len(input_array)%2) == 0:
	pass
else:
	for counter in range(1, len(input_array), 2):
		result = result ^ input_array[counter]

print (result)
