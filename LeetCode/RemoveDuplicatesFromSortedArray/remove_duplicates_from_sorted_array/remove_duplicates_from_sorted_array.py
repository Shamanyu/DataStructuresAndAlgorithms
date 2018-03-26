class RemoveDuplicatesFromSortedArray(object):

  def remove_duplicates_from_sorted_array(self, nums):
    current_position = 1

    for counter_position in range(1, len(nums)):
      if nums[counter_position] != nums[counter_position-1]:
        nums[current_position] = nums[counter_position]
        current_position += 1

    return len(nums[:current_position])


from nose.tools import assert_equal, assert_raises

class TestRemoveDuplicatesFromSortedArray(object):

  def test_remove_duplicates_from_sorted_array(self):
    remove_duplicates_from_sorted_array = RemoveDuplicatesFromSortedArray()

    assert_equal(remove_duplicates_from_sorted_array.remove_duplicates_from_sorted_array([1, 1, 2]), 2)

    print ('All test cases passed')


def main():
  test_remove_duplicates_from_sorted_array = TestRemoveDuplicatesFromSortedArray()
  test_remove_duplicates_from_sorted_array.test_remove_duplicates_from_sorted_array()

if __name__ =='__main__':
  main()