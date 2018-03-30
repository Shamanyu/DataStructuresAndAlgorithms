class ZigZagConversion(object):

  def zigZagConversion(self, string, numberOfRows):
    if numberOfRows == 1:
        return string
    self.rows = [[] for counter in range(numberOfRows)]
    currentRow = 0
    direction = 1
    for _, character in enumerate(string):
        self.rows[currentRow].append(character)
        if currentRow == numberOfRows-1 and direction == 1:
            currentRow -= 1
            direction = -1
        elif currentRow == 0 and direction == -1:
            currentRow += 1
            direction = 1
        elif direction == 1:
            currentRow += 1
        else:
            currentRow -= 1
    return ''.join([item for sublist in self.rows for item in sublist])

from nose.tools import assert_equals, assert_raises

class TestZigZagConversion(object):

  def testZigZagConversion(self):
    zigZagConversion = ZigZagConversion()

    assert_equals(zigZagConversion.zigZagConversion("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")

    assert_equals(zigZagConversion.zigZagConversion("ABC", 1), "ABC")

    print ("All test cases passed!")


def main():
  testZigZagConversion = TestZigZagConversion()
  testZigZagConversion.testZigZagConversion()

if __name__ == '__main__':
  main()
