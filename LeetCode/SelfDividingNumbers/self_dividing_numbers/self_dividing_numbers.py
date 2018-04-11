class SelfDividingNumbers(object):

    def selfDividingNumbers(self, left, right):
        return [number for number in range(left, right+1) if not any([digit == '0' or number % int(digit) != 0 for digit in str(number)])]


from nose.tools import assert_equals, assert_raises

class TestSelfDividingNumbers(object):

  def testSelfDividingNumbers(self):
    selfDividingNumbers = SelfDividingNumbers()

    assert_equals(selfDividingNumbers.selfDividingNumbers(1, 22), [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22])

    print ("All test cases passed!")


def main():
  testSelfDividingNumbers = TestSelfDividingNumbers()
  testSelfDividingNumbers.testSelfDividingNumbers()

if __name__ == '__main__':
  main()
