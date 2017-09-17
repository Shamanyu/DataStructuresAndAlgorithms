import collections

position_input = [10, 20, 50]
length_input = [15, 10, 5]
total_grazed_length = 0
cow_dict = {}

for counter in range (0, len(position_input)):
    cow_dict[position_input[counter]] = length_input[counter]

sorted_cow_dict = collections.OrderedDict(sorted(cow_dict.items()))

position_input = []
length_input = []

for key in sorted_cow_dict:
    position_input.insert(0, key)
    length_input.insert(0, sorted_cow_dict(key))

for counter2 in range(1, len(position_input)):
    if length_input[counter2-1] > (position_input[counter2-1]-position_input[counter2]+length_input[counter2]):
        length_input[counter2] = length_input[counter2-1] - (position_input[counter2-1]-position_input[counter2])

for counter in range (1, len(position_input)):
    total_grazed_length += min(position_input[counter]-position_input[counter-1], length_input[counter-1]+length_input[counter])

total_grazed_length += length_input[0]+length_input[len(length_input)-1]

print total_grazed_length
