class Node():

  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.prev = None
    self.next = None

class LRUCache():

  def __init__(self, capacity):
    self.capacity = capacity
    self.dict = dict()
    self.head = Node(0, 0)
    self.tail = Node(0, 0)
    self.head.next = self.tail
    self.tail.prev = self.head

  def get(self, key):
    if key in self.dict:
      node = self.dict[key]
      self._remove(node)
      self._add(node)
      return node.value
    return -1

  def put(self, key, value):
    if key in self.dict:
      self._remove(key)
    node = Node(key, value)
    self._add(node)
    self.dict[key] = node
    if len(self.dict) > self.capacity:
      node = self.head.next
      self._remove(node)
      del self.dict[node.key]

  def _remove(self, node):
    prev = node.prev
    next = node.next
    prev.next = next
    next.prev = prev

  def _add(self, node):
    prev = self.tail.prev
    prev.next = node
    self.tail.prev = node
    node.prev = prev
    node.next = self.tail

  def print_data(self):
    current = self.head.next
    print ('Data:')
    while current != self.tail:
      print(current.key)
      current = current.next

if __name__ == '__main__':

  lru_cache = LRUCache(2)

  lru_cache.print_data()

  lru_cache.put(1, 1)
  lru_cache.put(2, 2)
  lru_cache.print_data()

  print(lru_cache.get(1))
  print(lru_cache.get(2))

  lru_cache.put(3, 3)
  lru_cache.print_data()

  lru_cache.get(2)
  lru_cache.put(4, 4)
  lru_cache.print_data()
