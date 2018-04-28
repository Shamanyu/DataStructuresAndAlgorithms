class OptimalDivision(object):

    def optimalDivision(self, nums):
        nums = list(map(str, nums))
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0]+'/'+nums[1]
        return nums[0]+'/('+'/'.join(nums[1:])+')'


from nose.tools import assert_equals, assert_raises

class TestOptimalDivision(object):

  def testOptimalDivision(self):
    optimalDivision = OptimalDivision()

    assert_equals(optimalDivision.optimalDivision([1000, 100, 10, 2]),
        '1000/(100/10/2)')

    print ("All test cases passed!")


def main():
  testOptimalDivision = TestOptimalDivision()
  testOptimalDivision.testOptimalDivision()

if __name__ == '__main__':
  main()
