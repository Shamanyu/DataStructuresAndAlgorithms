class ThreeSumClosest(object):

  def threeSumClosest(self, nums, target):
    closestToTarget = float('inf')
    nums.sort()
    for position1 in range(0, len(nums)-2):
        position2 = position1+1
        position3 = len(nums)-1
        while position2 < position3:
            currentSum = nums[position1] + nums[position2] + nums[position3]
            if abs(target - closestToTarget) > abs(target - currentSum):
                closestToTarget = currentSum
            if currentSum > target:
                position3 -= 1
            elif currentSum < target:
                position2 += 1
            else:
                return target
    return closestToTarget


from nose.tools import assert_equals, assert_raises

class TestThreeSumClosest(object):

  def testThreeSumClosest(self):
    threeSumClosest = ThreeSumClosest()

    assert_equals(threeSumClosest.threeSumClosest([-1, 2, 1, 4], 1), 2)

    print ("All test cases passed!")


def main():
  testThreeSumClosest = TestThreeSumClosest()
  testThreeSumClosest.testThreeSumClosest()

if __name__ == '__main__':
  main()
