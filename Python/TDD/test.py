"""
PRD
1) Two space/comma separated numbers should return the sum of the two numbers.
2) Non-valid inputs raise TypeError.
"""


class Adder(object):

    def _parse(self, data):
        try:
            number1, number2 = data.split()
        except:
            number1, number2 = data.split(",")
        return number1, number2

    def add_numbers(self, data):
        number1, number2 = self._parse(data)
        number = int(number1) + int(number2)
        return number


from nose.tools import assert_equals, assert_raises


class TestAdder(object):

    def test_add_two_positive_integers_in_expected_format(self, adder_class):

        assert_equals(adder_class.add_numbers('11 1'), 12)

    def test_add_two_negative_integers_in_expected_format(self, adder_class):

        assert_equals(adder_class.add_numbers('-11 -1'), -12)

    def test_add_positive_integer_with_negative_integer_in_expected_format(self, adder_class):

        assert_equals(adder_class.add_numbers('11 -1'), 10)

    def test_add_unexpected_format_integer_data(self, adder_class):

        assert_raises(AttributeError, adder_class.add_numbers, 2)

    def test_add_unexpected_format_comma_separated_input(self, adder_class):

        assert_equals(adder_class.add_numbers('-11,-1'), -12)

    def test_add_unexpected_format_dot_separated_input(self, adder_class):

        assert_raises(ValueError, adder_class.add_numbers, '11.1')

    def test_add_unexpected_format_characters(self, adder_class):

        assert_raises(ValueError, adder_class.add_numbers, 'a b')

    def test_add_unexpected_format_multiple_space_separated_input(self, adder_class):

        assert_raises(ValueError, adder_class.add_numbers, '11 12 13')

    def test_add_unexpected_format_integer_with_character(self, adder_class):

        assert_raises(ValueError, adder_class.add_numbers, '1 a')

    def test_add_unexpected_format_character_with_integer(self, adder_class):

        assert_raises(ValueError, adder_class.add_numbers, 'a 1')

    def test_add_unexpected_format_space_and_comma_separation(self, adder_class):

        assert_raises(ValueError, adder_class.add_numbers, '2, 1')

    def test_add_expected_format_two_space_separation(self, adder_class):

        assert_equals(adder_class.add_numbers('-11  -1'), -12)

    def test_add_unexpected_format_two_comma_separation(self, adder_class):

        assert_raises(ValueError, adder_class.add_numbers, '2,,1')

def main():
    test_adder = TestAdder()

    test_adder.test_add_two_positive_integers_in_expected_format(Adder())
    test_adder.test_add_two_negative_integers_in_expected_format(Adder())
    test_adder.test_add_positive_integer_with_negative_integer_in_expected_format(Adder())
    test_adder.test_add_unexpected_format_integer_data(Adder())
    test_adder.test_add_unexpected_format_comma_separated_input(Adder())
    test_adder.test_add_unexpected_format_dot_separated_input(Adder())
    test_adder.test_add_unexpected_format_characters(Adder())
    test_adder.test_add_unexpected_format_multiple_space_separated_input(Adder())
    test_adder.test_add_unexpected_format_integer_with_character(Adder())
    test_adder.test_add_unexpected_format_character_with_integer(Adder())
    test_adder.test_add_unexpected_format_space_and_comma_separation(Adder())
    test_adder.test_add_expected_format_two_space_separation(Adder())
    test_adder.test_add_unexpected_format_two_comma_separation(Adder())

    print ("All test cases passed!")


if __name__ == '__main__':
    main()
