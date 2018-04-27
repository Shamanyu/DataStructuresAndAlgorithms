from collections import defaultdict

class DistributeCandies(object):

    def distributeCandies(self, candies):
        candyDict = defaultdict(int)
        uniqueCandies = 0
        for candy in candies:
            if candyDict[candy] == 0:
                uniqueCandies += 1
            candyDict[candy] += 1
        return min(uniqueCandies, len(candies)/2)


from nose.tools import assert_equals, assert_raises

class TestDistributeCandies(object):

  def testDistributeCandies(self):
    distributeCandies = DistributeCandies()

    assert_equals(distributeCandies.distributeCandies([1,1,2,2,3,3]), 3)

    assert_equals(distributeCandies.distributeCandies([1,1,2,3]), 2)

    print ("All test cases passed!")


def main():
  testDistributeCandies = TestDistributeCandies()
  testDistributeCandies.testDistributeCandies()

if __name__ == '__main__':
  main()
