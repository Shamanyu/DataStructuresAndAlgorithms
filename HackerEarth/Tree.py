# https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/tutorial/

class Tree(object):

  def __init__(self, value=None, left_child=None, right_child=None):
    self.set_value(value)
    self.set_left_child(left_child)
    self.set_right_child(right_child)

  def get_value_from_user(self):
    value = int(input())
    self.set_value(value)

  def set_value(self, value):
    self.value = value

  def set_left_child(self, tree):
    self.left_child = tree

  def set_right_child(self, tree):
    self.right_child = tree

  def get_value(self):
    return self.value

  def get_left_child(self):
    return self.left_child

  def get_right_child(self):
    return self.right_child

  def get_depth(self):
    left_depth = self.get_left_child().get_depth() \
      if self.get_left_child() else 0
    right_depth = self.get_right_child().get_depth() \
      if self.get_right_child() else 0
    return max(left_depth, right_depth) + 1

  def get_diameter(self):
    left_child = self.get_left_child()
    right_child = self.get_right_child()
    left_depth = left_child.get_depth() if left_child else 0
    right_depth = right_child.get_depth() if right_child else 0
    return max(left_depth+right_depth+1, left_child.get_diameter() if left_child else 0,
      right_child.get_diameter() if right_child else 0)

# Node1 = Tree(1, None, None)
# Node2 = Tree(2, None, None)
# Node3 = Tree(3, Node1, Node2)
# Node4 = Tree(4, None, None)
# Node5 = Tree(5, None, None)
# Node6 = Tree(6, Node4, Node5)
# Node7 = Tree(7, Node3, Node6)
# Node8 = Tree(8, None, Node7)

# print (Node1.get_depth())
# print (Node1.get_diameter())

# print (Node2.get_depth())
# print (Node2.get_diameter())

# print (Node3.get_depth())
# print (Node3.get_diameter())

# print (Node4.get_depth())
# print (Node4.get_diameter())

# print (Node5.get_depth())
# print (Node5.get_diameter())

# print (Node6.get_depth())
# print (Node6.get_diameter())

# print (Node7.get_depth())
# print (Node7.get_diameter())

# print (Node8.get_depth())
# print (Node8.get_diameter())