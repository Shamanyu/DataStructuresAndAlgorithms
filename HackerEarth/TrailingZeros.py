number=int(raw_input(""))
trailing_zeros=0
divider=5
adder=number/divider
while(adder>0):
	trailing_zeros+=adder
	divider*=5
	adder=number/divider
print trailing_zeros
