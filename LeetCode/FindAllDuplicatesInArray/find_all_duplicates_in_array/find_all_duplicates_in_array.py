class FindAllDuplicatesInArray(object):

    def findAllDuplicatesInArray(self, nums):
        duplicateElementsList = list()
        for counter in range(len(nums)):
            if nums[abs(nums[counter])-1] < 0:
                duplicateElementsList.append(abs(nums[counter]))
            else:
                nums[abs(nums[counter])-1] *= -1
        return duplicateElementsList


from nose.tools import assert_equals, assert_raises

class TestFindAllDuplicatesInArray(object):

  def testFindAllDuplicatesInArray(self):
    findAllDuplicatesInArray = FindAllDuplicatesInArray()

    assert_equals(findAllDuplicatesInArray.findAllDuplicatesInArray([4, 3, 2, 7, 8, 2, 3, 1]), [2, 3])

    assert_equals(findAllDuplicatesInArray.findAllDuplicatesInArray([2, 2]), [2])

    print ("All test cases passed!")


def main():
  testFindAllDuplicatesInArray = TestFindAllDuplicatesInArray()
  testFindAllDuplicatesInArray.testFindAllDuplicatesInArray()

if __name__ == '__main__':
  main()
