from Queue import Queue

class Dequeue(Queue):

  def __init__(self):
    Queue.__init__(self)

  def enqueue_front(self, element):
    self.elements.insert(0, element)

  def dequeue_front(self):
    return self.pop()

  def get_front(self):
    return self.top()

  def enqueue_back(self, element):
    self.push(element)

  def dequeue_back(self):
    try:
      return self.elements.pop()
    except IndexError as e:
      return e

  def get_back(self):
    try:
      return self.elements[-1]
    except IndexError:
      return None

  def print(self):
    print (self.elements)

# dequeue = Dequeue()

# dequeue.enqueue_front(1)
# dequeue.enqueue_front(2)
# dequeue.enqueue_back(3)
# dequeue.enqueue_back(4)
# dequeue.print()
# print (dequeue.get_front())
# print (dequeue.dequeue_front())
# dequeue.print()
# print (dequeue.get_back())
# print (dequeue.dequeue_back())
# dequeue.print()
# print (dequeue.get_front())
# print (dequeue.dequeue_front())
# dequeue.print()
# print (dequeue.get_back())
# print (dequeue.dequeue_back())
# dequeue.print()
# print (dequeue.get_front())
# print (dequeue.dequeue_front())
# dequeue.print()
# print (dequeue.get_back())
# print (dequeue.dequeue_back())
# dequeue.print()
# print (dequeue.get_front())
# print (dequeue.dequeue_front())
# print (dequeue.get_back())
# print (dequeue.dequeue_back())
# dequeue.print()
# print (dequeue.get_front())
# print (dequeue.dequeue_front())
# print (dequeue.get_back())
# print (dequeue.dequeue_back())
# dequeue.print()