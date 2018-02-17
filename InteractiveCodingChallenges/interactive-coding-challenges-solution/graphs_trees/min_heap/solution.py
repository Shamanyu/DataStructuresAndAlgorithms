class MinHeap(object):

    def __init__(self):
        self.data_array = list()

    def __len__(self):
        return len(self.data_array)

    def extract_min(self):
        if not self.data_array:
            return None
        if len(self.data_array) == 1:
            return self.data_array.pop(0)
        minimum = self.data_array[0]
        self.data_array[0] = self.data_array.pop(-1)
        self._bubble_down(index=0)
        return minimum

    def peek_min(self):
        return self.data_array[0] if self.data_array else None

    def insert(self, key):
        if key is None:
            raise TypeError('Key cannot be None')
        self.data_array.append(key)
        self._bubble_up(index=len(self.data_array) - 1)

    def _bubble_up(self, index):
        if index == 0:
            return 
        index_parent = (index - 1) // 2
        if self.data_array[index] < self.data_array[index_parent]:
            self.data_array[index], self.data_array[index_parent] = \
              self.data_array[index_parent], self.data_array[index]
            self._bubble_up(index_parent)

    def _bubble_down(self, index):
        min_child_index = self._find_smaller_child(index)
        if min_child_index == -1:
            return
        if self.data_array[index] > self.data_array[min_child_index]:
            self.data_array[index], self.data_array[min_child_index] = \
              self.data_array[min_child_index], self.data_array[index]
            self._bubble_down(min_child_index)

    def _find_smaller_child(self, index):
          left_child_index = index*2+1
          right_child_index = index*2+2
          if right_child_index >= len(self.data_array):
              if left_child_index >= len(self.data_array):
                  return -1
              else:
                  return left_child_index
          else:
              if self.data_array[left_child_index] < self.data_array[right_child_index]:
                  return left_child_index
              else:
                  return right_child_index



# %load test_min_heap.py
from nose.tools import assert_equal

class TestMinHeap(object):

    def test_min_heap(self):
        heap = MinHeap()
        assert_equal(heap.peek_min(), None)
        assert_equal(heap.extract_min(), None)
        heap.insert(20)
        assert_equal(heap.peek_min(), 20)
        heap.insert(5)
        assert_equal(heap.peek_min(), 5)
        heap.insert(15)
        heap.insert(22)
        heap.insert(40)
        heap.insert(5)
        assert_equal(heap.peek_min(), 5)
        heap.insert(3)
        assert_equal(heap.peek_min(), 3)
        assert_equal(heap.extract_min(), 3)
        assert_equal(heap.peek_min(), 5)
        print('Success: test_min_heap')

        
def main():
    test = TestMinHeap()
    test.test_min_heap()

    
if __name__ == '__main__':
    main()