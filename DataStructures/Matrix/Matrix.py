class Matrix(object):

  def __init__(self):
    self.set_input(0, 0, list(list()))

  def get_user_input(self):
    number_of_rows = int(input())
    number_of_columns = int(input())
    data = [[0 for column in range(0, number_of_columns)] for row in range(0, number_of_rows)]
    for row in range(0, number_of_rows):
      data[row] = [int(number) for number in input().split()]
    self.set_input(number_of_rows, number_of_columns, data)

  def set_input(self, number_of_rows, number_of_columns, data):
    self.number_of_rows = number_of_rows
    self.number_of_columns = number_of_columns
    self.data = data

  def print_matrix(self):
    for row in range(0, self.number_of_rows):
      for column in range(0, self.number_of_columns):
        print (self.data[row][column], end=' ')
      print ('')