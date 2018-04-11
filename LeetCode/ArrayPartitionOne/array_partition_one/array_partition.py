class ArrayPartition(object):

    def arrayPartition(self, nums):
        nums.sort()
        for counter in range(len(nums)-1, -1, -1):
            if counter%2 == 1:
                del nums[counter]
        return sum(nums)


from nose.tools import assert_equals, assert_raises

class TestArrayPartition(object):

  def testArrayPartition(self):
    arrayPartition = ArrayPartition()

    assert_equals(arrayPartition.arrayPartition([1, 4, 3, 2]), 4)

    print ("All test cases passed!")


def main():
  testArrayPartition = TestArrayPartition()
  testArrayPartition.testArrayPartition()

if __name__ == '__main__':
  main()
