class Queue(object):

  def __init__(self):
    self.elements = list()
    self.front = None
    self.back = None

  def push(self, element):
    self.elements.append(element)

  def pop(self):
    try:
      return self.elements.pop(0)
    except IndexError as e:
      return e

  def top(self):
    try:
      return self.elements[0]
    except IndexError:
      return None

  def size(self):
    return len(self.elements)

  def is_empty(self):
    return self.size() == 0

  def rotate(self, number_of_operations):
    for counter in range(0, number_of_operations):
      element = self.pop()
      self.push(element)

  def print_queue(self):
    print (self.elements)

# queue = Queue()
# queue.push(1)
# queue.push(2)
# queue.push(3)
# queue.push(4)
# queue.rotate(5)
# queue.print_queue()

# queue = Queue()
# queue.push(1)
# print (queue.top())
# queue.push(2)
# print (queue.top())
# queue.push(3)
# print (queue.top())
# queue.push(4)
# print (queue.top())
# print (queue.pop())
# print (queue.pop())
# print (queue.pop())
# print (queue.pop())
# print (queue.pop())
# print (queue.top())
# queue.push(5)
# queue.push(6)
# print (queue.pop())
# print (queue.top())
# print (queue.pop())
# print (queue.top())
# queue.push(7)
# print (queue.size())
# queue.push(8)
# print (queue.size())
# queue.push(9)
# print (queue.size())
# print (queue.is_empty())
# queue.pop()
# print (queue.is_empty())
# queue.pop()
# print (queue.is_empty())
# queue.pop()
# print (queue.is_empty())
