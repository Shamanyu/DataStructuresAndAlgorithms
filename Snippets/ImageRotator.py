n = int(raw_input("Enter the size of array:\n"))
image = [[0 for x in range(n)] for x in range(n)]
for counter1 in range(n):
	for counter2 in range(n):
		image[counter2][n-1-counter1] = raw_input("\nEnter character: ")
print image
