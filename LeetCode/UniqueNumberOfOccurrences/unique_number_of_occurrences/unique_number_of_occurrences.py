from typing import List
from nose.tools import assert_equal
from collections import defaultdict


class UniqueNumberOfOccurrences(object):

    @staticmethod
    def unique_number_of_occurrences(input_array: List[int]) -> bool:
        occurrence_count_map = defaultdict(int)
        for number in input_array:
            occurrence_count_map[number] += 1
        occurrence_count_list = occurrence_count_map.values()
        return len(occurrence_count_list) == len(set(occurrence_count_list))


class TestUniqueNumberOfOccurrences(object):

    def test_unique_number_of_occurrences(self):
        unique_number_of_occurrences_instance = UniqueNumberOfOccurrences()

        assert_equal(unique_number_of_occurrences_instance.unique_number_of_occurrences([1, 2]), False)

        assert_equal(unique_number_of_occurrences_instance.unique_number_of_occurrences([1, 2, 2]), True)

        assert_equal(unique_number_of_occurrences_instance.unique_number_of_occurrences([1, 2, 2, 1, 1, 3]), True)

        print("All test cases passed!")


def main():
    test_unique_number_of_occurrences_instance = TestUniqueNumberOfOccurrences()
    test_unique_number_of_occurrences_instance.test_unique_number_of_occurrences()


if __name__ == '__main__':
    main()
