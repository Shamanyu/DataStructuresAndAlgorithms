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