class PowerOfThree(object):

  def powerOfThree(self, num):
    if num <= 0:
        return False
    return 1162261467%num == 0


from nose.tools import assert_equals, assert_raises

class TestPowerOfThree(object):

  def testPowerOfThree(self):
    powerOfThree = PowerOfThree()

    assert_equals(powerOfThree.powerOfThree(0), False)

    assert_equals(powerOfThree.powerOfThree(1), True)

    assert_equals(powerOfThree.powerOfThree(3), True)

    assert_equals(powerOfThree.powerOfThree(6), False)

    assert_equals(powerOfThree.powerOfThree(81), True)

    print ("All test cases passed!")


def main():
  testPowerOfThree = TestPowerOfThree()
  testPowerOfThree.testPowerOfThree()

if __name__ == '__main__':
  main()
