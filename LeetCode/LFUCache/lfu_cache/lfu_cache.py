from collections import OrderedDict

class LfuCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.keyFrequency = dict()
        self.frequencyDict = dict()
        self.minFrequency = 1

    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache[key]
        frequency = self.keyFrequency[key]
        newFrequency = frequency+1
        self.keyFrequency[key] = newFrequency
        del self.frequencyDict[frequency][key]
        if newFrequency in self.frequencyDict:
            self.frequencyDict[newFrequency][key] = 1
        else:
            self.frequencyDict[newFrequency] = OrderedDict()
            self.frequencyDict[newFrequency][key] = 1
        if frequency == self.minFrequency and len(self.frequencyDict[frequency]) == 0:
            self.minFrequency = newFrequency
        return value

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.cache:
            self.cache[key] = value
            self.get(key)
        else:
            if len(self.cache) == self.capacity:
                keyToExtract = self.frequencyDict[self.minFrequency].popitem(last=False)[0]
                del self.cache[keyToExtract]
                del self.keyFrequency[keyToExtract]
            self.cache[key] = value
            frequency = 1
            self.keyFrequency[key] = frequency
            if frequency in self.frequencyDict:
                self.frequencyDict[frequency][key] = 1
            else:
                self.frequencyDict[frequency] = OrderedDict()
                self.frequencyDict[frequency][key] = 1
            self.minFrequency = 1
            

from nose.tools import assert_equals, assert_raises

class TestLfuCache(object):

  def testLFUCache(self):
    cache = LfuCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    assert_equals(cache.get(1), 1)

    cache.put(3, 3)
    assert_equals(cache.get(2), -1)

    assert_equals(cache.get(3), 3)

    cache.put(4, 4);
    assert_equals(cache.get(1), -1)

    assert_equals(cache.get(3), 3)

    assert_equals(cache.get(4), 4)

    print ("All test cases passed!")


def main():
  testLFUCache = TestLfuCache()
  testLFUCache.testLFUCache()

if __name__ == '__main__':
  main()
