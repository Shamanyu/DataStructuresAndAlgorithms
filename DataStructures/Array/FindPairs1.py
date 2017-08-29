#!/usr/bin/python3.4

array1 = list(map(int, input().split()))

array2 = list(map(int, input().split()))

required_sum = int(input())

for number1 in array1:
  for number2 in array2:
    if number1+number2 == required_sum:
      print (number1, number2)
