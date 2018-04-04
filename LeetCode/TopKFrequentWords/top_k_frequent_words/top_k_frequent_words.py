from collections import defaultdict
import heapq

class TopKFrequentWords(object):

    def topKFrequentWords(self, words, k):
        wordFrequencyMap = defaultdict(int)
        for word in words:
            wordFrequencyMap[word] += 1
        wordHeap = [(-value, key) for key,value in wordFrequencyMap.items()]
        largestKElements = heapq.nsmallest(k, wordHeap)
        return [key for _, key in largestKElements]


from nose.tools import assert_equals, assert_raises

class TestTopKFrequentWords(object):

  def testTopKFrequentWords(self):
    topKFrequentWords = TopKFrequentWords()

    assert_equals(topKFrequentWords.topKFrequentWords(["i", "love", "leetcode", "i", "love", "coding"], 2), ["i", "love"])

    print ("All test cases passed!")


def main():
  testTopKFrequentWords = TestTopKFrequentWords()
  testTopKFrequentWords.testTopKFrequentWords()

if __name__ == '__main__':
  main()
