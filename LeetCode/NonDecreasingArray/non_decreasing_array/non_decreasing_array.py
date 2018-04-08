class NonDecreasingArray(object):

    def nonDecreasingArray(self, nums):
        problemIndex = None
        for counter in range(0, len(nums)-1):
            if nums[counter] > nums[counter+1]:
                if problemIndex != None:
                    return False
                problemIndex = counter
        return (problemIndex is None or problemIndex == 0 or
            problemIndex == len(nums)-2 or
            nums[problemIndex-1] <= nums[problemIndex+1] or
            nums[problemIndex] <= nums[problemIndex+2])



from nose.tools import assert_equals, assert_raises

class TestNonDecreasingArray(object):

  def testNonDecreasingArray(self):
    nonDecreasingArray = NonDecreasingArray()

    assert_equals(nonDecreasingArray.nonDecreasingArray([4, 2, 3]), True)

    assert_equals(nonDecreasingArray.nonDecreasingArray([4, 2, 1]), False)

    print ("All test cases passed!")


def main():
  testNonDecreasingArray = TestNonDecreasingArray()
  testNonDecreasingArray.testNonDecreasingArray()

if __name__ == '__main__':
  main()
