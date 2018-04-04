class ArrayConsecutiveSubsequences(object):

    def arrayConsecutiveSubsequences(self, nums):
        openSubsequence = list()
        for counter, num in enumerate(nums):
            


from nose.tools import assert_equals, assert_raises

class TestArrayConsecutiveSubsequences(object):

  def testArrayConsecutiveSubsequences(self):
    arrayConsecutiveSubsequences = ArrayConsecutiveSubsequences()

    assert_equals(arrayConsecutiveSubsequences.arrayConsecutiveSubsequences([1, 2, 3, 3, 4, 5]), True)

    assert_equals(arrayConsecutiveSubsequences.arrayConsecutiveSubsequences([1, 2, 3, 3, 4, 4, 5, 5]), True)

    assert_equals(arrayConsecutiveSubsequences.arrayConsecutiveSubsequences([1, 2, 3, 4, 4, 5]), False)

    print ("All test cases passed!")


def main():
  testArrayConsecutiveSubsequences = TestArrayConsecutiveSubsequences()
  testArrayConsecutiveSubsequences.testArrayConsecutiveSubsequences()

if __name__ == '__main__':
  main()
