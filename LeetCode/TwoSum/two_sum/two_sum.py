class TwoSum(object):

  def find_indices(self, nums, target):
    potential_target_map = dict()
    for counter, num in enumerate(nums):
      if num in potential_target_map:
        return [potential_target_map[num], counter]
      potential_target_map[target-num] = counter
    raise ValueError


from nose.tools import assert_equal, assert_raises

class TestTwoSum(object):

  def test_two_sum(self):
    two_sum = TwoSum()
    assert_equal(two_sum.find_indices([2, 7, 11, 15], 9), [0, 1])

    two_sum = TwoSum()
    assert_raises(ValueError, two_sum.find_indices, [2, 7, 11, 15], 14)

    print("Success: TwoSum passed all the test cases")

def main():
  test_two_sum = TestTwoSum()
  test_two_sum.test_two_sum()

if __name__ == '__main__':
  main()