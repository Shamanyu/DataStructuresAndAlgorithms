import math

input_size = int(input(''))

input_list = [int(n) for n in input('').split()]

product = 1

for counter in range(0, input_size):
	product = (product * input_list[counter]) % (1000000000+7)

print (product)
