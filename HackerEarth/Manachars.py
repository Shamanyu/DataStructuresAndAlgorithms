# https://www.hackerearth.com/practice/algorithms/string-algorithm/manachars-algorithm/tutorial/

class Manachars(object):

  def __init__(self):
    pass

  def get_user_input(self):
    input_string = input()
    self.set_input(input_string)

  def set_input(self, input_string):
    self.input_string = list(input_string)
    self.input_string_length = len(input_string)

  # O(n^3) in time
  def brute_force_algorithm(self):
    longest_palindrome = list()
    for outer_counter in range(0, self.input_string_length):
      for inner_counter in range(0, self.input_string_length):
        string_to_check = self.input_string[outer_counter:inner_counter+1]
        if self.is_palindrome(string_to_check) and len(string_to_check) > len(longest_palindrome):
          longest_palindrome = string_to_check
    return ''.join(longest_palindrome)

  # O(n^2) in time
  def center_search_algorithm(self):
    longest_palindrome = list()
    for counter in range(0, self.input_string_length):
      left_counter = right_counter = counter
      while (left_counter >= 0 and right_counter < self.input_string_length):
        string_to_check = self.input_string[left_counter:right_counter+1]
        if self.is_palindrome(string_to_check):
          if len(string_to_check) > len(longest_palindrome):
            longest_palindrome = string_to_check
          left_counter -= 1
          right_counter += 1
        else:
          break
    return ''.join(longest_palindrome)


  def is_palindrome(self, input_string):
    reverse_string = list(reversed(input_string))
    if (input_string == reverse_string):
      return True
    return False

if __name__ == '__main__':
  manachars = Manachars()
  manachars.get_user_input()
  print (manachars.brute_force_algorithm())
  print (manachars.center_search_algorithm())