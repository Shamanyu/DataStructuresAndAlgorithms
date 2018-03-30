class FourSum(object):

  # Time complexity: O(n^3)
  def fourSum(self, nums, target):
    result = list()
    nums.sort()
    position1 = 0
    while (position1 < len(nums)-3):
        position2 = position1+1
        while (position2 < len(nums)-2):
            position3 = position2+1
            position4 = len(nums)-1
            while (position4 > position3):
                currentSum = nums[position1]+nums[position2]+nums[position3]+nums[position4]
                if currentSum == target:
                    result.append([nums[position1], nums[position2], nums[position3], nums[position4]])
                    currentPosition3 = position3
                    while (position3 < len(nums) and nums[currentPosition3] == nums[position3]):
                        position3 += 1
                    currentPosition4 = position4
                    while (position4 >= 0 and nums[currentPosition4] == nums[position4]):
                        position4 -= 1
                elif currentSum < target:
                    currentPosition3 = position3
                    while (position3 < len(nums) and nums[currentPosition3] == nums[position3]):
                        position3 += 1
                else:
                    currentPosition4 = position4
                    while (position4 >= 0 and nums[currentPosition4] == nums[position4]):
                        position4 -= 1
            currentPosition2 = position2
            while (position2 < len(nums) and nums[currentPosition2] == nums[position2]):
                position2 += 1
        currentPosition1 = position1
        while (position1 < len(nums) and nums[currentPosition1] == nums[position1]):
            position1 += 1
    return result


from nose.tools import assert_equals, assert_raises

class TestFourSum(object):

  def testFourSum(self):
    fourSum = FourSum()

    assert_equals(sorted(fourSum.fourSum([1, 0, -1, 0, -2, 2], 0)), sorted([[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]))

    assert_equals(sorted(fourSum.fourSum([0, 0, 0, 0], 0)), sorted([[0, 0, 0, 0]]))

    assert_equals(sorted(fourSum.fourSum([-1, -5, -5, -3, 2, 5, 0, 4], -7)), sorted([[-5, -5, -1, 4], [-5, -3, -1, 2]]))

    print ("All test cases passed!")


def main():
  testFourSum = TestFourSum()
  testFourSum.testFourSum()

if __name__ == '__main__':
  main()
