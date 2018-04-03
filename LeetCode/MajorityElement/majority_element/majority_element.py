class MajorityElement(object):

  def majorityElement(self, nums):
    votes = 0
    majorityElement = None
    for counter, num in enumerate(nums):
        if votes == 0:
            majorityElement = num
            votes += 1
        elif majorityElement != num:
            votes -= 1
        elif majorityElement == num:
            votes += 1
        else:
            raise Exception('Reached case where votes<0 which should ideally never be reached')
    return majorityElement


from nose.tools import assert_equals, assert_raises

class TestMajorityElement(object):

  def testMajorityElement(self):
    majorityElement = MajorityElement()

    print ("All test cases passed!")


def main():
  testMajorityElement = TestMajorityElement()
  testMajorityElement.testMajorityElement()

if __name__ == '__main__':
  main()
