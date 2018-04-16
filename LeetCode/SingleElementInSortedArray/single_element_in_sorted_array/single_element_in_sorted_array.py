class SingleElementInSortedArray(object):

    def singleElementInSortedArray(self, nums):
        for counter in range(0, len(nums), 2):
            if ((counter+1 >= len(nums)) or (nums[counter] != nums[counter+1])):
                return nums[counter]
        return -1


from nose.tools import assert_equals, assert_raises

class TestSingleElementInSortedArray(object):

  def testSingleElementInSortedArray(self):
    singleElementInSortedArray = SingleElementInSortedArray()

    assert_equals(singleElementInSortedArray.singleElementInSortedArray([1, 1, 2, 3, 3, 4, 4, 8, 8]), 2)

    assert_equals(singleElementInSortedArray.singleElementInSortedArray([3, 3, 7, 7, 10, 11, 11]), 10)

    assert_equals(singleElementInSortedArray.singleElementInSortedArray([1, 1, 2]), 2)

    print ("All test cases passed!")


def main():
  testSingleElementInSortedArray = TestSingleElementInSortedArray()
  testSingleElementInSortedArray.testSingleElementInSortedArray()

if __name__ == '__main__':
  main()
