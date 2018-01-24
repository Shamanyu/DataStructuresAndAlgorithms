# Time complexity: O(n)
# Space complexity: O(n)
class CompressString(object):

    def calculate_partial_result(self, character, count):
        return character + (str(count) if count > 1 else '')

    def compress(self, string):
        if string is None or not string:
            return string
        result = ''
        current_character = ''
        current_count = 0
        for character in string:
            if character == current_character:
                current_count += 1
            else:
                result += self.calculate_partial_result(current_character, current_count)
                current_character = character
                current_count = 1
        result += self.calculate_partial_result(current_character, current_count)
        return result if len(result) < len(string) else string

# %load test_compress.py
from nose.tools import assert_equal
class TestCompress(object):

    def test_compress(self, func):
        assert_equal(func(None), None)
        assert_equal(func(''), '')
        assert_equal(func('AABBCC'), 'AABBCC')
        assert_equal(func('AAABCCDDDDE'), 'A3BC2D4E')
        assert_equal(func('BAAACCDDDD'), 'BA3C2D4')
        assert_equal(func('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: test_compress')


def main():
    test = TestCompress()
    compress_string = CompressString()
    test.test_compress(compress_string.compress)


if __name__ == '__main__':
    main()
