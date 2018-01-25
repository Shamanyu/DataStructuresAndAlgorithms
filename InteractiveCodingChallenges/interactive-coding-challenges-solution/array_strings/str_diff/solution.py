from collections import defaultdict

class Solution(object):

    # Time complexity: O(m+n)
    # Space complexity: O(n)
    def find_diff(self, s, t):
        if s is None or t is None:
            raise TypeError('str1 or str2 cannot be None')
        char_map = defaultdict(int)
        for char in s:
            char_map[char] += 1
        for char in t:
            char_map[char] -= 1
        for key in char_map:
            if char_map[key] is -1:
                return char
        return None

    # Time complexity: O(m+n)
    # Space complexity: O(1)
    def find_diff_xor(self, str1, str2):
        if str1 is None or str2 is None:
            raise TypeError('str1 or str2 cannot be None')
        result = 0
        for char in str1:
            result ^= ord(char)
        for char in str2:
            result ^= ord(char)
        return chr(result)


# %load test_str_diff.py
from nose.tools import assert_equal, assert_raises

class TestFindDiff(object):

    def test_find_diff(self):
        solution = Solution()
        assert_raises(TypeError, solution.find_diff, None, None)
        assert_equal(solution.find_diff('abcd', 'abcde'), 'e')
        assert_equal(solution.find_diff('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff')

    def test_find_diff_xor(self):
        solution = Solution()
        assert_raises(TypeError, solution.find_diff_xor, None, None)
        assert_equal(solution.find_diff_xor('abcd', 'abcde'), 'e')
        assert_equal(solution.find_diff_xor('aaabbcdd', 'abdbacade'), 'e')
        print('Success: test_find_diff_xor')


def main():
    test = TestFindDiff()
    test.test_find_diff()
    test.test_find_diff_xor()

if __name__ == '__main__':
    main()
