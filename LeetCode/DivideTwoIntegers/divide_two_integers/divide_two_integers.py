class DivideTwoIntegers(object):

    # O(dividend)
    def divide_two_integers(self, dividend, divisor):
        if dividend > 2147483647 or dividend < -2147483648 or (dividend == -2147483648 and divisor == -1):
            return 2147483647
        quotient = 0
        sign = 1 if ((dividend >= 0 and divisor >= 0) or (dividend < 0 and divisor < 0)) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while (dividend >= divisor):
            dividend = dividend - divisor
            quotient += 1
        return quotient*sign

    # O(log(dividend))
    def divide_two_integers(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


from nose.tools import assert_equal, assert_raises

class TestDivideTwoIntegers(object):

    def test_divide_two_integers(self):
        divide_two_integers = DivideTwoIntegers()

        assert_equal(divide_two_integers.divide_two_integers(0, 1), 0)

        assert_equal(divide_two_integers.divide_two_integers(2147483647, 1), 2147483647)

        print ('All test cases passed')


def main():
    test_divide_two_integers = TestDivideTwoIntegers()
    test_divide_two_integers.test_divide_two_integers()

if __name__ == '__main__':
    main()
