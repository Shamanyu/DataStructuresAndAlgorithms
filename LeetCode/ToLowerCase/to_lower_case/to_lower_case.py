class ToLowerCase(object):

    def to_lower_case(self, str):
        return str.lower()


from nose.tools import assert_equals, assert_raises


class TestToLowerCase(object):

    def test_to_lower_case(self):
        to_lower_case_instance = ToLowerCase()

        # Capitalised string to lower case string test
        assert_equals(to_lower_case_instance.to_lower_case("Hello"), "hello")

        # Upper case string to lower case string test
        assert_equals(to_lower_case_instance.to_lower_case("HELLO"), "hello")

        # Lower case string to lower case string test
        assert_equals(to_lower_case_instance.to_lower_case("hello"), "hello")

        # Special characters string to lower case string test
        assert_equals(to_lower_case_instance.to_lower_case("%$cweq%F"), "%$cweq%f")

        print("All test cases passed!")


def main():
    test_to_lower_case_instance = TestToLowerCase()
    test_to_lower_case_instance.test_to_lower_case()


if __name__ == '__main__':
    main()
