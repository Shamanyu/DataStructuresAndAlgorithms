number=(gets.chomp).to_i
trailing_zeros=0
divider=5
adder=number/divider
while adder>0 do
	trailing_zeros+=adder
	divider*=5
	adder=number/divider
end
puts trailing_zeros
