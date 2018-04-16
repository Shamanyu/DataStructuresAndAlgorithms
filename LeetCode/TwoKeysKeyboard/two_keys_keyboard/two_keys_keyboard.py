class TwoKeysKeyboard(object):

    def twoKeysKeyboard(self, n):

        def factors(n):
            d = 2
            while d*d <= n:
                while n % d == 0:
                    n /= d
                    yield d
                d += 1
            if n > 1:
                yield n

        return sum(factors(n))


from nose.tools import assert_equals, assert_raises

class TestTwoKeysKeyboard(object):

  def testTwoKeysKeyboard(self):
    twoKeysKeyboard = TwoKeysKeyboard()

    assert_equals(twoKeysKeyboard.twoKeysKeyboard(3), 3)

    print ("All test cases passed!")


def main():
  testTwoKeysKeyboard = TestTwoKeysKeyboard()
  testTwoKeysKeyboard.testTwoKeysKeyboard()

if __name__ == '__main__':
  main()
