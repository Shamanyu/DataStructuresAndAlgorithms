class MaximumSubarray(object):

  def maximum_subarray(self, nums):
    maximum_sum = float('-inf')
    current_sum = 0
    for num in nums:
      current_sum = max(current_sum+num, num)
      if current_sum > maximum_sum:
        maximum_sum = current_sum
    return maximum_sum


from nose.tools import assert_equal, assert_raises

class TestMaximumSubarray(object):

  def test_maximum_subarray(self):
    maximum_subarray = MaximumSubarray()

    assert_equal(maximum_subarray.maximum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    print ('All test cases passed')


def main():
  test_maximum_subarray = TestMaximumSubarray()
  test_maximum_subarray.test_maximum_subarray()

if __name__ == '__main__':
  main()