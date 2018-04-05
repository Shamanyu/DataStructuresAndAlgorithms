class RemoveElement(object):

    def removeElement(self, nums, val):
        start, end = 0, len(nums)-1
        while end >= start:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end-1
            else:
                start += 1
        return start


from nose.tools import assert_equals, assert_raises

class TestRemoveElement(object):

  def testRemoveElement(self):
    removeElement = RemoveElement()

    assert_equals(removeElement.removeElement([3, 2, 2, 3], 3), 2)

    print ("All test cases passed!")


def main():
  testRemoveElement = TestRemoveElement()
  testRemoveElement.testRemoveElement()

if __name__ == '__main__':
  main()
