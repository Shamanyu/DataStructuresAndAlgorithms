class ClimbingStairs(object):

  # Time complexity: O(2*n), optimize using dynamic programming
  def climbingStairs(self, n):
      self.climbingStairsTable = [None for counter in range(0, n+2)]
      return self._climbingStairs(n+1)

  def _climbingStairs(self, n):
    if (n <= 1):
        return n
    else:
        if self.climbingStairsTable[n]:
            return self.climbingStairsTable[n]
        else:
            self.climbingStairsTable[n] = self._climbingStairs(n-1) + self._climbingStairs(n-2)
            return self.climbingStairsTable[n]


from nose.tools import assert_equals, assert_raises

class TestClimbingStairs(object):

  def testClimbingStairs(self):
    climbingStairs = ClimbingStairs()

    assert_equals(climbingStairs.climbingStairs(2), 2)

    assert_equals(climbingStairs.climbingStairs(3), 3)

    print ("All test cases passed!")


def main():
  testClimbingStairs = TestClimbingStairs()
  testClimbingStairs.testClimbingStairs()

if __name__ == '__main__':
  main()
