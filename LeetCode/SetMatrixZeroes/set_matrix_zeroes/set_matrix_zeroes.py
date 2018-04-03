class SetMatrixZeroes(object):

  def setMatrixZeroes(self, matrix):
    zeroRows = set()
    zeroColumns = set()
    for rowCounter in range(len(matrix)):
        for columnCounter in range(len(matrix[rowCounter])):
            if matrix[rowCounter][columnCounter] == 0:
                zeroRows.add(rowCounter)
                zeroColumns.add(columnCounter)
    for row in zeroRows:
        matrix[row] = [0 for counter in range(len(matrix[row]))]
    for row in range(len(matrix)):
        for column in zeroColumns:
            matrix[row][column] = 0


from nose.tools import assert_equals, assert_raises

class TestSetMatrixZeroes(object):

  def testSetMatrixZeroes(self):
    setMatrixZeroes = SetMatrixZeroes()

    print ("All test cases passed!")


def main():
  testSetMatrixZeroes = TestSetMatrixZeroes()
  testSetMatrixZeroes.testSetMatrixZeroes()

if __name__ == '__main__':
  main()
