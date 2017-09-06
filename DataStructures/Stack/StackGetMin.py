from Stack import Stack

class StackGetMin(object):

  def __init__(self):
    self.main_stack = Stack()
    self.min_stack = Stack()

  def push(self, element):
    self.main_stack.push(element)
    min_element = self.min_stack.get_top()
    if min_element and min_element < element:
      self.min_stack.push(min_element)
    else:
      self.min_stack.push(element)

  def pop(self):
    self.min_stack.pop()
    return self.main_stack.pop()

  def get_top(self):
    return self.main_stack.get_top()

  def get_min(self):
    return self.min_stack.get_top()

# stack_get_min = StackGetMin()

# stack_get_min.push(2)
# stack_get_min.push(1)
# stack_get_min.push(3)
# stack_get_min.push(4)
# stack_get_min.push(5)
# print (stack_get_min.get_min())
# print (stack_get_min.get_top())
# print (stack_get_min.pop())
# print (stack_get_min.get_min())
# print (stack_get_min.get_top())
# print (stack_get_min.pop())
# print (stack_get_min.get_min())
# print (stack_get_min.get_top())
# print (stack_get_min.pop())
# print (stack_get_min.get_min())
# print (stack_get_min.get_top())
# print (stack_get_min.pop())
# print (stack_get_min.get_min())
# print (stack_get_min.get_top())
# print (stack_get_min.pop())
# print (stack_get_min.get_min())
# print (stack_get_min.get_top())
# print (stack_get_min.pop())
# print (stack_get_min.get_min())
# print (stack_get_min.get_top())
# print (stack_get_min.pop())
# print (stack_get_min.get_min())
# print (stack_get_min.get_top())
# print (stack_get_min.pop())
