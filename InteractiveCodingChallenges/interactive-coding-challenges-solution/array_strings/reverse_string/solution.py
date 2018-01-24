# Time complexity: O(n)
# Space complexity: O(1)
import math
class ReverseString(object):

    def reverse(self, chars):
        if chars is None:
          return chars
        number_of_chars = len(chars)
        for counter in range(0, math.floor(number_of_chars/2)):
          temp = chars[counter]
          chars[counter] = chars[number_of_chars-1-counter]
          chars[number_of_chars-1-counter] = temp
        return chars

# Time complexity: O(n)
# Space complexity: O(1)
class ReverseStringOriginal(object):

    def reverse(self, chars):
        if chars:
            size = len(chars)
            for i in range(size // 2):
                chars[i], chars[size - 1 - i] = \
                    chars[size - 1 - i], chars[i]
        return chars

# Time complexity: O(n)
# Space complexity: O(n)
# Pythonic solutions
class ReverseStringAlt(object):

    def reverse_string_alt(string):
        if string:
            return string[::-1]
        return string

    def reverse_string_alt2(string):
        if string:
            return ''.join(reversed(string))
        return string

# %load test_reverse_string.py
from nose.tools import assert_equal

class TestReverse(object):

    def test_reverse(self, func):
        assert_equal(func(None), None)
        assert_equal(func(['']), [''])
        assert_equal(func(
            ['f', 'o', 'o', ' ', 'b', 'a', 'r']),
            ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse')

    def test_reverse_inplace(self, func):
        target_list = ['f', 'o', 'o', ' ', 'b', 'a', 'r']
        func(target_list)
        assert_equal(target_list, ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse_inplace')


def main():
    test = TestReverse()
    reverse_string = ReverseString()
    test.test_reverse(reverse_string.reverse)
    test.test_reverse_inplace(reverse_string.reverse)


if __name__ == '__main__':
    main()