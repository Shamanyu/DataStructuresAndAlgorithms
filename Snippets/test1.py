input_set = ['a', 'b', 'c']
k = 2

def print_strings(input_set, k):
    output_array = list()
    print "Received", input_set, k
    if k>=1 and len(input_set) >= k:
        for current_string in print_strings(input_set[1:], k-1):
            print "Adding", input_set[0], current_string
            output_array.append(input_set[0]+current_string)
        for current_string in print_strings(input_set[1:], k):
            print "Addign again", current_array
            output_array.append(current_string)         
    else:
        output_array = [] 
    return output_array
   
output_array = print_strings(input_set, k)
print "output array is", output_array
counter=0
for element in output_array:
    if length(element) == k:
        counter += 1
        print element, counter
