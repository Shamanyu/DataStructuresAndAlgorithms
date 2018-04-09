from collections import defaultdict

class ArithmeticSlicesTwo(object):

    def arithmeticSlicesTwo(self, nums):
        arithmeticSlices = 0
        differenceDict = [defaultdict(int) for num in nums]
        for outerCounter in range(0, len(nums)):
            for innerCounter in range(outerCounter):
                differenceDict[outerCounter][nums[outerCounter] - nums[innerCounter]] += 1
                if (nums[outerCounter] - nums[innerCounter]) in differenceDict[innerCounter]:
                    differenceDict[outerCounter][nums[outerCounter] - nums[innerCounter]] += differenceDict[innerCounter][nums[outerCounter] - nums[innerCounter]]
                    arithmeticSlices += differenceDict[innerCounter][nums[outerCounter] - nums[innerCounter]]
        return arithmeticSlices


from nose.tools import assert_equals, assert_raises

class TestArithmeticSlicesTwo(object):

  def testArithmeticSlicesTwo(self):
    arithmeticSlicesTwo = ArithmeticSlicesTwo()

    assert_equals(arithmeticSlicesTwo.arithmeticSlicesTwo([2, 4, 6, 8, 10]), 7)

    print ("All test cases passed!")


def main():
  testArithmeticSlicesTwo = TestArithmeticSlicesTwo()
  testArithmeticSlicesTwo.testArithmeticSlicesTwo()

if __name__ == '__main__':
  main()
