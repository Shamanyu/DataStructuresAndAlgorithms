import math

class SqrtX(object):

  def sqrtX(self, X):
    low = 1
    high = X
    while (high-low > 0.000001):
        mid = (high+low)/2
        if mid > X/mid:
            high = mid
        else:
            low = mid
    return math.floor(high)


from nose.tools import assert_equals, assert_raises

class TestSqrtX(object):

  def testSqrtX(self):
    sqrtX = SqrtX()

    assert_equals(sqrtX.sqrtX(4), 2)

    assert_equals(sqrtX.sqrtX(8), 2)

    print ("All test cases passed!")


def main():
  testSqrtX = TestSqrtX()
  testSqrtX.testSqrtX()

if __name__ == '__main__':
  main()
