import math

class MinHeap(object):

  def __init__(self):
    self.set_input(list())

  def get_user_input(self):
    data = [int(number) for number in input().split()]
    self.set_input(data)

  def set_input(self, data):
    self.data = data
    self.heap_size = len(data)

  def get_left_child_position(self, position):
    if position >= 0:
      left_child_position = position*2+1
      if left_child_position < self.heap_size:
        return left_child_position
    return None

  def get_right_child_position(self, position):
    if position >= 0:
      right_child_position = position*2+2
      if right_child_position < self.heap_size:
        return right_child_position
    return None

  def get_parent_position(self, position):
    parent_position = math.floor((position-1)/2)
    if parent_position >= 0:
      return parent_position
    return None

  def min_heapify(self, position):
    left_child_position = self.get_left_child_position(position)
    right_child_position = self.get_right_child_position(position)
    smallest = position
    if (left_child_position and left_child_position < self.heap_size and 
      self.data[left_child_position] < self.data[smallest]):
      smallest = left_child_position
    if (right_child_position and right_child_position < self.heap_size and
      self.data[right_child_position] < self.data[smallest]):
      smallest = right_child_position
    if (smallest != position):
      self.swap(position, smallest)
      self.min_heapify(smallest)

  def extract_min(self):
    if self.heap_size <= 0:
      return None
    elif self.heap_size == 1:
      self.heap_size -= 1
      return self.data.pop(0)
    else:
      root = self.data[0]
      self.swap(0, -1)
      self.data.pop()
      self.heap_size -= 1
      self.min_heapify(0)
      return root

  def decrease_key(self, position, new_value):
    self.data[position] = new_value
    while (position != 0):
      parent_position = self.get_parent_position(position)
      if parent_position != None and self.data[parent_position] > self.data[position]:
        self.swap(position, parent_position)
      position = parent_position

  def delete_key(self, position):
    self.decrease_key(position, float('-inf'))
    self.extract_min()

  def insert(self, key):
    self.data.append(key)
    position = self.heap_size
    self.heap_size += 1
    while (position):
      parent_position = self.get_parent_position(position)
      if parent_position != None and self.data[position] < self.data[parent_position]:
        self.swap(position, parent_position)
      position = parent_position

  def swap(self, position1, position2):
    if position1 != position2:
      self.data[position1], self.data[position2] = self.data[position2], self.data[position1]

  def get_min(self):
    try:
      return self.data[0]
    except:
      None

  def print_min_heap(self):
    print (self.data)

# min_heap = MinHeap()
# min_heap.get_user_input()
# min_heap.print_min_heap()

# # print (min_heap.get_left_child_position(0))
# # print (min_heap.get_left_child_position(-1))
# # print (min_heap.get_left_child_position(9))
# # print (min_heap.get_left_child_position(10))

# # min_heap.decrease_key(9, -1)
# # min_heap.print_min_heap()
# # min_heap.delete_key(2)
# # min_heap.print_min_heap()

# # print (min_heap.get_min())

# min_heap.insert(-100)
# # min_heap.insert(100)

# min_heap.print_min_heap()