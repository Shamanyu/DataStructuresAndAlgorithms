from collections import defaultdict

class TopKFrequentElements(object):

  def topKFrequentElements(self, nums, k):
    numDict = defaultdict(int)
    for num in nums:
        numDict[num] += 1
    topKElements = list()
    count = 0
    for num in sorted(numDict, key=numDict.get, reverse=True):
        if count < k:
            topKElements.append(num)
            count += 1
        else:
            break
    return topKElements


from nose.tools import assert_equals, assert_raises

class TestTopKFrequentElements(object):

  def testTopKFrequentElements(self):
    topKFrequentElements = TopKFrequentElements()

    assert_equals(topKFrequentElements.topKFrequentElements([1, 1, 1, 2, 2, 3], 2), [1, 2])

    print ("All test cases passed!")


def main():
  testTopKFrequentElements = TestTopKFrequentElements()
  testTopKFrequentElements.testTopKFrequentElements()

if __name__ == '__main__':
  main()
