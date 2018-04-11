class ReverseString(object):

    def reverseString(self, stringToReverse):
        return ''.join(list(reversed(stringToReverse)))


from nose.tools import assert_equals, assert_raises

class TestReverseString(object):

  def testReverseString(self):
    reverseString = ReverseString()

    assert_equals(reverseString.reverseString('Hey'), 'yeH')

    assert_equals(reverseString.reverseString('hello'), 'olleh')

    print ("All test cases passed!")


def main():
  testReverseString = TestReverseString()
  testReverseString.testReverseString()

if __name__ == '__main__':
  main()
