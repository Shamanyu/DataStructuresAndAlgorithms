from nose.tools import assert_equal


roman_number_to_value_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


class RomanToInteger(object):

    @staticmethod
    def roman_to_integer(roman_number: str) -> int:
        result = 0
        while roman_number:
            if len(roman_number) > 1:
                if roman_number_to_value_map[roman_number[0]] >= roman_number_to_value_map[roman_number[1]]:
                    result += roman_number_to_value_map[roman_number[0]]
                    roman_number = roman_number[1:]
                else:
                    result += (roman_number_to_value_map[roman_number[1]] - roman_number_to_value_map[roman_number[0]])
                    roman_number = roman_number[2:]
            else:
                result += roman_number_to_value_map[roman_number[0]]
                roman_number = roman_number[1:]
        return result


class TestRomanToInteger(object):

    def test_roman_to_integer(self):
        roman_to_integer_instance = RomanToInteger()

        assert_equal(roman_to_integer_instance.roman_to_integer('III'), 3)

        assert_equal(roman_to_integer_instance.roman_to_integer('IV'), 4)

        assert_equal(roman_to_integer_instance.roman_to_integer('IX'), 9)

        assert_equal(roman_to_integer_instance.roman_to_integer('LVIII'), 58)

        assert_equal(roman_to_integer_instance.roman_to_integer('MCMXCIV'), 1994)

        print("All test cases passed!")


def main():
    test_roman_to_integer_instance = TestRomanToInteger()
    test_roman_to_integer_instance.test_roman_to_integer()


if __name__ == '__main__':
    main()
