class FirstMissingPositive(object):

  def firstMissingPositive(self, nums):

    # Partition array in place around 0
    leftPointer = 0
    rightPointer = len(nums) - 1
    pivot = 0
    while (rightPointer >= leftPointer):
        if nums[rightPointer] > pivot and nums[leftPointer] <= pivot:
            nums[rightPointer], nums[leftPointer] = nums[leftPointer], nums[rightPointer]
            leftPointer += 1
            rightPointer -= 1
        elif nums[rightPointer] <= pivot and nums[leftPointer] > pivot:
            leftPointer += 1
            rightPointer -= 1
        elif nums[rightPointer] > pivot:
            leftPointer += 1
        elif nums[leftPointer] <= pivot:
            rightPointer -= 1

    partitionPosition = rightPointer+1

    # Use array to maintain elements present
    for counter in range(0, partitionPosition):
        position = abs(nums[counter])-1
        if position < len(nums):
            if nums[position] >= 0:
                nums[position] *= -1

    # Find first smallest positive number that doesn't exist
    for counter in range(0, partitionPosition):
        if nums[counter] > 0:
            return counter+1

    return partitionPosition+1

from nose.tools import assert_equals, assert_raises

class TestFirstMissingPositive(object):

  def testFirstMissingPositive(self):
    firstMissingPositive = FirstMissingPositive()

    assert_equals(firstMissingPositive.firstMissingPositive([1, 2, 0]), 3)

    assert_equals(firstMissingPositive.firstMissingPositive([3, 4, -1, 1]), 2)

    assert_equals(firstMissingPositive.firstMissingPositive([7, 8, 9, 11, 12]), 1)

    assert_equals(firstMissingPositive.firstMissingPositive([1, 1]), 2)

    print ("All test cases passed!")


def main():
  testFirstMissingPositive = TestFirstMissingPositive()
  testFirstMissingPositive.testFirstMissingPositive()

if __name__ == '__main__':
  main()
