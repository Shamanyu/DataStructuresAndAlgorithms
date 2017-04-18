# This technique shows how a nested for loop in few problems can be converted to single for loop and hence reduce the time complexity
# Given an array of 'n' integers, calculate the maximum sum of 'k' consecutive elements in the array

input_array = [int(number) for number in  input().split()]
k = int(input())
n = len(input_array)

if k > n:
	print ("Not possible")
else:
	counter = 0
	sum = 0
	while counter < k:
		sum += input_array[counter]
		counter += 1
	maximum_sum = sum
	while counter < n:
		sum = sum + input_array[counter] - input_array[counter-k]
		if sum > maximum_sum:
			maximum_sum = sum
		counter += 1
	print (maximum_sum)