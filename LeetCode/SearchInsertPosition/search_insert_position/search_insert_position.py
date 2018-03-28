class SearchInsertPosition(object):

  def searchInsertPosition(self, nums, numToInsert):
    positionToInsert = 0
    for _, num in enumerate(nums):
      if num < numToInsert:
        positionToInsert += 1
      else:
        break
    return positionToInsert


from nose.tools import assert_equals, assert_raises

class TestSearchInsertPosition(object):

  def testSearchInsertPosition(self):
    searchInsertPosition = SearchInsertPosition()

    assert_equals(searchInsertPosition.searchInsertPosition([1, 3, 5, 6], 5), 2)

    assert_equals(searchInsertPosition.searchInsertPosition([1, 3, 5, 6], 2), 1)

    assert_equals(searchInsertPosition.searchInsertPosition([1, 3, 5, 6], 0), 0)

    print ("All test cases passed!")


def main():
  testSearchInsertPosition = TestSearchInsertPosition()
  testSearchInsertPosition.testSearchInsertPosition()

if __name__ == '__main__':
  main()
    
