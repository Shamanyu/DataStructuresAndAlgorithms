class LinkedListNode(object):

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LruCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.currentSize = 0
        self.nodeDict = dict()
        self.head = LinkedListNode()
        self.tail = LinkedListNode()
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key):
        if key in self.nodeDict:
            value = self._remove(self.nodeDict[key])
            self._add(LinkedListNode(key, value))
            return value
        return -1

    def put(self, key, value):
        if key in self.nodeDict:
            self._remove(self.nodeDict[key])
        if self.capacity == self.currentSize:
            self._remove(self.head.next)
        self._add(LinkedListNode(key, value))

    def _add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        self.nodeDict[node.key] = node
        self.currentSize += 1

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        value = node.value
        del self.nodeDict[node.key]
        self.currentSize -= 1
        return value

from nose.tools import assert_equals, assert_raises

class TestLruCache(object):

  def testLruCache(self):
    lruCache = LruCache(2)

    lruCache.put(1, 1)
    lruCache.put(2, 2)
    assert_equals(lruCache.get(1), 1)
    lruCache.put(3, 3)
    assert_equals(lruCache.get(2), -1)
    lruCache.put(4, 4)
    assert_equals(lruCache.get(1), -1)
    assert_equals(lruCache.get(3), 3)
    assert_equals(lruCache.get(4), 4)


    print ("All test cases passed!")


def main():
  testLruCache = TestLruCache()
  testLruCache.testLruCache()

if __name__ == '__main__':
  main()
