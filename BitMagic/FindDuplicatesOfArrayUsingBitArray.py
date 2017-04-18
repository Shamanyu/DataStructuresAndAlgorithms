# http://www.geeksforgeeks.org/find-duplicates-of-array-using-bit-array/
''' You have an array of N numbers, where N is at most 32,000. 
The array may have duplicates entries and you do not know what N is. 
With only 4 Kilobytes of memory available, how would print all duplicates elements in the array ?'''

from bitstring import BitArray

bit_array = BitArray(4*1024*8)

output_file = open('FindDuplicatesOfArrayUsingBitArrayOutputFile.txt', 'w')
user_input = None
while user_input != -1:
	user_input = int(input()) 
	if bit_array[user_input]:
		output_file.write("%d\n" % user_input)
	else:
		bit_array[user_input] = 1