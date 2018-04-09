test_cases=int(raw_input(""))
for test_case in range(test_cases):
	sides=int(raw_input(""))
	if sides==1:
		print 1
	else:
		print 6*pow(sides, 2)-12*sides+8
