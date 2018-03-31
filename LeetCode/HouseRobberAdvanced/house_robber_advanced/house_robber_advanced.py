class HouseRobberAdvanced(object):

  def rob(self, nums):
    if len(nums) == 0:
        return 0
    if len(nums) < 4:
        return max(nums)
    return max(self.houseRobberAdvanced(nums[1:]),
        self.houseRobberAdvanced(nums[:-1]))

  def houseRobberAdvanced(self, nums):
    self.maxValueTable = [None for num in nums]
    self.nums = nums
    return self._houseRobberAdvanced(len(nums)-1)

  def _houseRobberAdvanced(self, house):
    if house < 0:
        return 0
    elif house == 0:
        return self.nums[0]
    elif house == 1:
        return max(self.nums[0], self.nums[1])
    else:
        if not self.maxValueTable[house]:
            self.maxValueTable[house] = max(self.nums[house]+
                self._houseRobberAdvanced(house-2),
                self._houseRobberAdvanced(house-1))
        return self.maxValueTable[house]


from nose.tools import assert_equals, assert_raises

class TestHouseRobberAdvanced(object):

  def testHouseRobberAdvanced(self):
    houseRobberAdvanced = HouseRobberAdvanced()

    print ("All test cases passed!")


def main():
  testHouseRobberAdvanced = TestHouseRobberAdvanced()
  testHouseRobberAdvanced.testHouseRobberAdvanced()

if __name__ == '__main__':
  main()
