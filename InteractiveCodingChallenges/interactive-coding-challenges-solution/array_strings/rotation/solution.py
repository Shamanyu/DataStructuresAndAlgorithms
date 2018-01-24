# Time complexity: O(n)
# Space complexity: O(n)
class Rotation(object):

    # Special case for Knuth-Morris-Pratt algorithm
    # Time complexity of KMP algorithm: O(n+k) = O(2n+n) = O(n)
    # Space complexity of KMP algorithm: O(n)
    def is_substring(self, s1, s2):
        return s2 in s1

    def is_rotation(self, s1, s2):
        if (s1 is None or s2 is None or len(s1) != len(s2)):
            return False
        return self.is_substring(s1+s1, s2)


# %load test_rotation.py
from nose.tools import assert_equal
class TestRotation(object):

    def test_rotation(self):
        rotation = Rotation()
        assert_equal(rotation.is_rotation('o', 'oo'), False)
        assert_equal(rotation.is_rotation(None, 'foo'), False)
        assert_equal(rotation.is_rotation('', 'foo'), False)
        assert_equal(rotation.is_rotation('', ''), True)
        assert_equal(rotation.is_rotation('foobarbaz', 'barbazfoo'), True)
        print('Success: test_rotation')


def main():
    test = TestRotation()
    test.test_rotation()


if __name__ == '__main__':
    main()
