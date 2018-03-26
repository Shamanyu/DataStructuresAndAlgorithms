class ThreeSum(object):

  def get_all_triplets(self, nums):
    nums.sort()
    triplet_set = set(tuple())

    for position1 in range(0, len(nums)-2):
      position2 = position1+1
      position3 = len(nums)-1
      while (position2 < position3):
        current_sum = nums[position1] + nums[position2] + nums[position3]
        if (current_sum > 0):
          position3 -= 1
        elif (current_sum < 0):
          position2 += 1
        else:
          triplet_set.add((nums[position1], nums[position2], nums[position3]))
          position2 += 1
          position3 -= 1
    triplet_list = list(triplet_set)
    for counter in range(0, len(triplet_list)):
      triplet_list[counter] = list(triplet_list[counter])
    triplet_list.reverse()
    return triplet_list

from nose.tools import assert_equal, assert_raises

class TestThreeSum(object):

  def test_three_sum(self):
    three_sum = ThreeSum()

    assert_equal(three_sum.get_all_triplets([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]])

    print ('All test cases passed')


def main():
  test_three_sum = TestThreeSum()
  test_three_sum.test_three_sum()

if __name__ == '__main__':
  main()