class Heap(object):

    def __init__(self, data=[]):
        self.heap = data
        self.heapify()

    # O(logn)
    def insert(self, data):
        self.heap.append(data)
        self._siftUp(len(self.heap)-1)

    # O(logn)
    def extractMax(self):
        if len(self.heap) is 0:
            raise Exception('extractMax attampted on empty heap')
        if len(self.heap) is 1:
            return self.heap.pop()
        dataToReturn = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._siftDown(0)
        return dataToReturn

    # O(n) as compared to sequential addition (O(n*logn))
    def heapify(self):
        numberOfInternalNodes = len(self.heap) // 2 + 1
        counter = numberOfInternalNodes - 1
        while (counter >= 0):
            self._siftDown(counter)
            counter -= 1

    # O(n)
    def getHeap(self):
        return self.heap

    def _siftUp(self, position):
        parentPosition = self._getParentPosition(position)
        if parentPosition is not None:
            if self.heap[position] > self.heap[parentPosition]:
                self.heap[position], self.heap[parentPosition] = \
                    self.heap[parentPosition], self.heap[position]
                self._siftUp(parentPosition)

    def _siftDown(self, position):
        greaterChildPosition = self._getGreaterChildPosition(position)
        if greaterChildPosition:
            if self.heap[position] < self.heap[greaterChildPosition]:
                self.heap[position], self.heap[greaterChildPosition] = \
                    self.heap[greaterChildPosition], self.heap[position]
                self._siftDown(greaterChildPosition)

    def _getParentPosition(self, position):
        if position is 0:
            return None
        return ((position-1) // 2)

    def _getGreaterChildPosition(self, position):
        leftChildPosition = (position*2)+1 if (position*2)+1<len(self.heap) else None
        rightChildPosition = (position*2)+2 if (position*2)+2<len(self.heap) else None
        if leftChildPosition and rightChildPosition:
            return leftChildPosition if self.heap[leftChildPosition] > self.heap[rightChildPosition] else rightChildPosition
        elif leftChildPosition:
            return leftChildPosition
        elif rightChildPosition:
            return rightChildPosition
        return None


from nose.tools import assert_equals, assert_raises

class TestHeap(object):

  def testHeap(self):

    heap = Heap()

    assert_raises(Exception, heap.extractMax)

    heap.insert(1)

    assert_equals(heap.extractMax(), 1)

    heap.insert(10)

    heap.insert(20)

    assert_equals(heap.extractMax(), 20)

    assert_equals(heap.extractMax(), 10)

    assert_raises(Exception, heap.extractMax)

    heap = Heap([100, 200, 300])

    assert_equals(heap.getHeap(), [300, 200, 100])

    heap = Heap([100, 200, 300, 400])

    assert_equals(heap.getHeap(), [400, 200, 300, 100])

    heap = Heap([100, 200, 300, 400, 500, 600, 700, 800])

    assert_equals(heap.getHeap(), [800, 500, 700, 400, 100, 600, 300, 200])

    print ("All test cases passed!")


def main():
  testHeap = TestHeap()
  testHeap.testHeap()

if __name__ == '__main__':
  main()
