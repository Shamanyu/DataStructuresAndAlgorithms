class ReverseInteger(object):

  # Time complexity: O(n)
  # Space complexity: O(n) 
  def reverse_integer(self, num):
    if abs(num) <= 2147483647:
      result = self.get_sign(num)*int(''.join(reversed(str(abs(num)))))
      if abs(result) <= 2147483647:
        return result
      else:
        return 0
    else:
      return 0

  # Time complexity: O(1)
  # Space complexity: O(1)
  def get_sign(self, num):
    return 1 if num >= 0 else -1


from nose.tools import assert_equal, assert_raises

class TestReverseInteger(object):

  def test_reverse_integer(self):
    reverse_integer = ReverseInteger()

    assert_equal(reverse_integer.reverse_integer(123), 321)

    assert_equal(reverse_integer.reverse_integer(9870), 789)

    assert_equal(reverse_integer.reverse_integer(-123), -321)

    print('All test cases passed')


def main():
  test_reverse_integer = TestReverseInteger()
  test_reverse_integer.test_reverse_integer()

if __name__ == '__main__':
  main()