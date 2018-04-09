def main():
  T = int(input())
  N = list(map(int, input().split()))
  for counter in range(0, len(N)):
    for inner_counter in range(0, N[counter]):
      if (inner_counter+1)%15 == 0:
        print ("FizzBuzz")
      elif (inner_counter+1)%5 == 0:
        print ("Buzz")
      elif (inner_counter+1)%3 == 0:
        print ("Fizz")
      else:
        print (inner_counter+1)
  return

if __name__ == '__main__':
  main()