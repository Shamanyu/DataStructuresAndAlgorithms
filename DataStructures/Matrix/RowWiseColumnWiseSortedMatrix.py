from Matrix import Matrix

class RowWiseColumnWiseSortedMatrix(Matrix):

  def __init__(self):
    Matrix.__init__(self)

  def find_key(self, key):
    x = 0
    y = self.number_of_columns - 1
    while (x < self.number_of_rows and y >= 0):
      if self.data[x][y] > key:
        y -= 1
      elif self.data[x][y] < key:
        x += 1
      else:
        return (x, y)

row_wise_column_wise_sorted_matrix = RowWiseColumnWiseSortedMatrix()

row_wise_column_wise_sorted_matrix.get_user_input()
row_wise_column_wise_sorted_matrix.print_matrix()
print (row_wise_column_wise_sorted_matrix.find_key(1))
print (row_wise_column_wise_sorted_matrix.find_key(11))
print (row_wise_column_wise_sorted_matrix.find_key(14))
print (row_wise_column_wise_sorted_matrix.find_key(17))
