class PalindromeNumber(object):

  # Time complexity: O(n)
  # Space complexity: O(n)
  def palindrome_number(self, num):
    return str(num) == str(num)[::-1]

from nose.tools import assert_equal, assert_raises

class TestPalindromNumber(object):

  def test_palindrome_number(self):
    palindrome_number = PalindromeNumber()

    assert_equal(palindrome_number.palindrome_number(1231), False)

    assert_equal(palindrome_number.palindrome_number(1221), True)

    assert_equal(palindrome_number.palindrome_number(101), True)

    print('All test cases passed.')

def main():
  test_palindrome_number = TestPalindromNumber()
  test_palindrome_number.test_palindrome_number()

if __name__ == '__main__':
  main()