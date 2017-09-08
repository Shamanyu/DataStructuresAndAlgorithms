class Node(object):

  def __init__(self):
    self.set_value(None)

  def set_value(self, value):
    self.value = value

  def get_value(self):
    return self.value

  def print_node(self):
    print (self.get_value(), end=' ')