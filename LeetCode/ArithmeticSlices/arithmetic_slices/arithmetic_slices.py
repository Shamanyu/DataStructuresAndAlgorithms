class ArithmeticSlices(object):

    def arithmeticSlices(self, nums):
        numberOfSlices = currentSlices = 0
        for counter in range(2, len(nums)):
            if nums[counter] - nums[counter-1] == nums[counter-1] - nums[counter-2]:
                currentSlices += 1
                numberOfSlices += currentSlices
            else:
                currentSlices = 0
        return numberOfSlices


from nose.tools import assert_equals, assert_raises

class TestArithmeticSlices(object):

  def testArithmeticSlices(self):
    arithmeticSlices = ArithmeticSlices()

    assert_equals(arithmeticSlices.arithmeticSlices([1, 2, 3, 4]), 3)

    print ("All test cases passed!")


def main():
  testArithmeticSlices = TestArithmeticSlices()
  testArithmeticSlices.testArithmeticSlices()

if __name__ == '__main__':
  main()
