# Time complexity: O(n)
# Space complexity: O(n)
class UniqueChars(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        character_map = set()
        for character in string:
            if character in character_map:
                return False
            else:
                character_map.add(character)
        return True


# Time complexity: O(n)
# Space complexity: O(n)
class UniqueCharsSet(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        return len(set(string)) == len(string)


# Time complexity: O(n^2)
# Space complexity: O(1)
class UniqueCharsInPlace(object):

    def has_unique_chars(self, string):
        if string is None:
            return False
        for char in string:
            if string.count(char) > 1:
                return False
        return True


# %load test_unique_chars.py
from nose.tools import assert_equal
class TestUniqueChars(object):

    def test_unique_chars(self, func):
        assert_equal(func(None), False)
        assert_equal(func(''), True)
        assert_equal(func('foo'), False)
        assert_equal(func('bar'), True)
        assert_equal(func('Bba'), True)
        print('Success: test_unique_chars')


def main():
    test = TestUniqueChars()
    unique_chars = UniqueChars()
    test.test_unique_chars(unique_chars.has_unique_chars)
    try:
        unique_chars_set = UniqueCharsSet()
        test.test_unique_chars(unique_chars_set.has_unique_chars)
        unique_chars_in_place = UniqueCharsInPlace()
        test.test_unique_chars(unique_chars_in_place.has_unique_chars)
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()
