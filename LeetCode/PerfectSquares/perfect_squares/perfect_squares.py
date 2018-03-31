import math

class PerfectSquares(object):

  def getAllPossiblePerfectSquares(self, num):
    sqrtNum = math.floor(math.sqrt(num))
    return ([number*number for number in range(1, sqrtNum+1)][::-1])

  def perfectSquares(self, num):
    self.possiblePerfectSquares = self.getAllPossiblePerfectSquares(num)
    self.minPerfectSquaresNeededTable = dict()
    return self._perfectSquares(num)

  def _perfectSquares(self, num):
    if num == 0:
        return 0
    if num not in self.minPerfectSquaresNeededTable:
        minCombinations = float('inf')
        for perfectSquare in self.possiblePerfectSquares:
            complement = num - perfectSquare
            if complement < 0:
                continue
            combinations = 1 + self._perfectSquares(complement)
            if combinations < minCombinations:
                minCombinations = combinations
        self.minPerfectSquaresNeededTable[num] = minCombinations
    return self.minPerfectSquaresNeededTable[num]


from nose.tools import assert_equals, assert_raises

class TestPerfectSquares(object):

  def testPerfectSquares(self):
    perfectSquares = PerfectSquares()

    assert_equals(perfectSquares.perfectSquares(4), 1)

    assert_equals(perfectSquares.perfectSquares(8), 2)

    assert_equals(perfectSquares.perfectSquares(12), 3)

    assert_equals(perfectSquares.perfectSquares(13), 2)

    print ("All test cases passed!")


def main():
  testPerfectSquares = TestPerfectSquares()
  testPerfectSquares.testPerfectSquares()

if __name__ == '__main__':
  main()
