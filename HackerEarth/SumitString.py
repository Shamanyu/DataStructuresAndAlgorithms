# https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/sumits-string/

class SumitString(object):

  def __init__(self):
    self.set_input(0, list())

  def get_user_input(self):
    T = int(input())
    input_strings = ['' for counter in range(0, T)]
    for counter in range(0, T):
      input_strings[counter] = input()
    self.set_input(T, input_strings)

  def set_input(self, T, input_strings):
    self.T = T
    self.input_strings = input_strings

  def is_sumit_string(self):
    output = ["" for counter in range(0, self.T)]
    for test_case_counter in range(0, self.T):
      for counter in range(0, len(self.input_strings[test_case_counter])-1):
        if (ord(self.input_strings[test_case_counter][counter]) == ord(self.input_strings[test_case_counter][counter+1]) + 1 or
          ord(self.input_strings[test_case_counter][counter]) == ord(self.input_strings[test_case_counter][counter+1]) - 1):
          pass
        else:
          output[test_case_counter] = "No"
          break
        output[test_case_counter] = "Yes"
    return output

  def get_output(self):
    output_array = self.is_sumit_string()
    for output in output_array:
      print (output)

sumit_string = SumitString()

sumit_string.get_user_input()
sumit_string.get_output()