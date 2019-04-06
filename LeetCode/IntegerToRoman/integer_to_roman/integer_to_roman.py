class IntegerToRoman(object):

    def integer_to_roman(self, num):
        roman_number = list()
        while num >= 1000:
            roman_number.append('M')
            num -= 1000
        if num >= 900:
            roman_number.append('CM')
            num -= 900
        if num >= 500:
            roman_number.append('D')
            num -= 500
        if num >= 400:
            roman_number.append('CD')
            num -= 400
        while num >= 100:
            roman_number.append('C')
            num -= 100
        if num >= 90:
            roman_number.append('XC')
            num -= 90
        if num >= 50:
            roman_number.append('L')
            num -= 50
        if num >= 40:
            roman_number.append('XL')
            num -= 40
        while num >= 10:
            roman_number.append('X')
            num -= 10
        if num == 9:
            roman_number.append('IX')
            num -= 9
        if num >= 5:
            roman_number.append('V')
            num -= 5
        if num == 4:
            roman_number.append('IV')
            num -= 4
        while num >= 1:
            roman_number.append('I')
            num -= 1
        return ''.join(roman_number)



from nose.tools import assert_equals, assert_raises


class TestIntegerToRoman(object):

    def test_integer_to_roman(self):
        integer_to_roman_instance = IntegerToRoman()

        # Case 1
        assert_equals(integer_to_roman_instance.integer_to_roman(1), 'I')

        # Case 2
        assert_equals(integer_to_roman_instance.integer_to_roman(5), 'V')

        # Case 3
        assert_equals(integer_to_roman_instance.integer_to_roman(10), 'X')

        # Case 4
        assert_equals(integer_to_roman_instance.integer_to_roman(50), 'L')

        # Case 5
        assert_equals(integer_to_roman_instance.integer_to_roman(100), 'C')

        # Case 6
        assert_equals(integer_to_roman_instance.integer_to_roman(500), 'D')

        # Case 7
        assert_equals(integer_to_roman_instance.integer_to_roman(1000), 'M')

        # Case 8
        assert_equals(integer_to_roman_instance.integer_to_roman(4), 'IV')

        # Case 9
        assert_equals(integer_to_roman_instance.integer_to_roman(9), 'IX')

        # Case 10
        assert_equals(integer_to_roman_instance.integer_to_roman(40), 'XL')

        # Case 11
        assert_equals(integer_to_roman_instance.integer_to_roman(90), 'XC')

        # Case 12
        assert_equals(integer_to_roman_instance.integer_to_roman(400), 'CD')

        # Case 13
        assert_equals(integer_to_roman_instance.integer_to_roman(900), 'CM')

        # Case 14
        assert_equals(integer_to_roman_instance.integer_to_roman(58), 'LVIII')

        print("All test cases passed!")


def main():
    test_integer_to_roman_instance = TestIntegerToRoman()
    test_integer_to_roman_instance.test_integer_to_roman()


if __name__ == '__main__':
    main()
