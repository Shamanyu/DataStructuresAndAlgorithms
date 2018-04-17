class MaxXor(object):

    def maxXor(self, nums):
        pass


from nose.tools import assert_equals, assert_raises

class TestMaxXor(object):

  def testMaxXor(self):
    maxXor = MaxXor()

    assert_equals(maxXor.maxXor([3, 10, 5, 25, 2, 8]), 28)

    print ("All test cases passed!")


def main():
  testMaxXor = TestMaxXor()
  testMaxXor.testMaxXor()

if __name__ == '__main__':
  main()
