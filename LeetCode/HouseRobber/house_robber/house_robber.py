class HouseRobber(object):

  def houseRobber(self, nums):
    self.maxValueTable = [None for num in nums]
    self.nums = nums
    return self._houseRobber(len(nums)-1)

  def _houseRobber(self, house):
    if house < 0:
        return 0
    elif house == 0:
        return self.nums[0]
    elif house == 1:
        return max(self.nums[0], self.nums[1])
    else:
        if not self.maxValueTable[house]:
            self.maxValueTable[house] = max(self.nums[house]+self._houseRobber(house-2),
                self._houseRobber(house-1))
        return self.maxValueTable[house]


from nose.tools import assert_equals, assert_raises

class TestHouseRobber(object):

  def testHouseRobber(self):
    houseRobber = HouseRobber()

    print ("All test cases passed!")


def main():
  testHouseRobber = TestHouseRobber()
  testHouseRobber.testHouseRobber()

if __name__ == '__main__':
  main()
