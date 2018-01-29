class Solution(object):

    # Time complexity: O(n)
    # Space complexity: O(n)
    def fizz_buzz(self, num):
        if num is None:
            raise TypeError
        elif num is 0:
            raise ValueError
        else:
            output_list = list()
            for counter in range(1, num+1):
                if (counter % 3 == 0 and counter % 5 == 0):
                    output_list.append('FizzBuzz')
                elif (counter % 3 == 0):
                    output_list.append('Fizz')
                elif (counter % 5 == 0):
                    output_list.append('Buzz')
                else:
                    output_list.append(str(counter))
            return output_list


# %load test_fizz_buzz.py
from nose.tools import assert_equal, assert_raises

class TestFizzBuzz(object):

    def test_fizz_buzz(self):
        solution = Solution()
        assert_raises(TypeError, solution.fizz_buzz, None)
        assert_raises(ValueError, solution.fizz_buzz, 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        assert_equal(solution.fizz_buzz(15), expected)
        print('Success: test_fizz_buzz')


def main():
    test = TestFizzBuzz()
    test.test_fizz_buzz()


if __name__ == '__main__':
    main()
