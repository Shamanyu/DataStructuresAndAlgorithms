class FirstMissingPositive(object):

  def firstMissingPositive(self, nums):

    # nums.append(0)
    # n = len(nums)
    # for i in range(len(nums)): #delete those useless elements
    #     if nums[i]<0 or nums[i]>=n:
    #         nums[i]=0
    # for i in range(len(nums)): #use the index as the hash to record the frequency of each number
    #     nums[nums[i]%n]+=n
    # for i in range(1,len(nums)):
    #     if nums[i]/n==0:
    #         return i
    pass

from nose.tools import assert_equals, assert_raises

class TestFirstMissingPositive(object):

  def testFirstMissingPositive(self):
    firstMissingPositive = FirstMissingPositive()

    assert_equals(firstMissingPositive.firstMissingPositive([1, 2, 0]), 3)

    assert_equals(firstMissingPositive.firstMissingPositive([3, 4, -1, 1]), 2)

    print ("All test cases passed!")


def main():
  testFirstMissingPositive = TestFirstMissingPositive()
  testFirstMissingPositive.testFirstMissingPositive()

if __name__ == '__main__':
  main()
