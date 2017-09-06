class Stack(object):

  def __init__(self):
    self.elements = list()

  def push(self, element):
    self.elements.append(element)

  def pop(self):
    try:
      return self.elements.pop()
    except IndexError as e:
      return e

  def get_top(self):
    try:
      return self.elements[-1]
    except IndexError:
      return None

# stack = Stack([1, 2, 3])
# stack.push(4)
# stack.push(5)
# print (stack.pop())
# print (stack.get_top())
# print (stack.pop())
# print (stack.get_top())
# print (stack.pop())
# print (stack.get_top())
# print (stack.pop())
# print (stack.get_top())
# print (stack.pop())
# print (stack.get_top())
# print (stack.pop())
# print (stack.get_top())
# stack.push(6)
# stack.push(7)
# stack.push(8)
# print (stack.pop())
# print (stack.get_top())
# print (stack.pop())
# print (stack.get_top())
# print (stack.pop())
# print (stack.get_top())
# print (stack.pop())
# print (stack.get_top())
# print (stack.pop())
# print (stack.get_top())