class MinCostStairs(object):

  def minCostStairs(self, cost):
    cost.insert(0, 0)
    self.minCostTable = [None for stairCost in cost]
    return self._minCostStairs(cost, 0)

  def _minCostStairs(self, cost, stair):
    if len(cost) == 0:
        return 0
    if not self.minCostTable[stair]:
        self.minCostTable[stair] = cost[0] + min(self._minCostStairs(cost[1:], stair+1), self._minCostStairs(cost[2:], stair+2))
    return self.minCostTable[stair]

from nose.tools import assert_equals, assert_raises

class TestMinCostStairs(object):

  def testMinCostStairs(self):
    minCostStairs = MinCostStairs()

    assert_equals(minCostStairs.minCostStairs([10, 15, 20]), 15)

    assert_equals(minCostStairs.minCostStairs(
        [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

    print ("All test cases passed!")


def main():
  testMinCostStairs = TestMinCostStairs()
  testMinCostStairs.testMinCostStairs()

if __name__ == '__main__':
  main()
