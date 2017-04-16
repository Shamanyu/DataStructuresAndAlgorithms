array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
required_sum = int(input())

for number2 in array2:
  search_number = required_sum-number2
  if search_number in array1:
    print (search_number, number2)
