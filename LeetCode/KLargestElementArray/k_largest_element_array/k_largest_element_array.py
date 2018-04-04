import heapq

class KLargestElementArray(object):

    def kLargestElementArray(self, nums, k):
        data = [-1*num for num in nums]
        heapq.heapify(data)
        counter = 0
        while (counter < k):
            value = heapq.heappop(data)
            counter += 1
        return -1*value


from nose.tools import assert_equals, assert_raises

class TestKLargestElementArray(object):

  def testKLargestElementArray(self):
    kLargestElementArray = KLargestElementArray()

    assert_equals(kLargestElementArray.kLargestElementArray([3, 2, 1, 5, 6, 4], 2), 5)

    print ("All test cases passed!")


def main():
  testKLargestElementArray = TestKLargestElementArray()
  testKLargestElementArray.testKLargestElementArray()

if __name__ == '__main__':
  main()
