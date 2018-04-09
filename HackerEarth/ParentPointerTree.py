# https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/tutorial/

from Tree import Tree

class ParentPointerTree(Tree):

  def __init__(self, value=None, parent=None, which_child = None, left_child=None, right_child=None):
    Tree.__init__(self, value, left_child, right_child)
    self.set_parent(parent, which_child)

  def set_parent(self, tree, which_child):
    self.parent = tree
    self.which_child = which_child
    if self.which_child == 'L':
      tree.set_left_child(self)
    elif self.which_child == 'R':
      tree.set_right_child(self)

  def get_parent(self):
    return self.parent

  def get_which_child(self):
    return self.which_child

# parent_pointer_tree1 = ParentPointerTree(1, None, None, None)
# parent_pointer_tree2 = ParentPointerTree(2, parent_pointer_tree1, 'L', None, None)
# parent_pointer_tree3 = ParentPointerTree(3, parent_pointer_tree1, 'R', None, None)
# parent_pointer_tree4 = ParentPointerTree(4, parent_pointer_tree2, 'L', None, None)

# print (parent_pointer_tree1.get_value())
# print (parent_pointer_tree1.get_left_child().get_value() if parent_pointer_tree1.get_left_child() else None)
# print (parent_pointer_tree1.get_right_child().get_value() if parent_pointer_tree1.get_right_child() else None)
# print (parent_pointer_tree1.get_parent().get_value() if parent_pointer_tree1.get_parent() else None)

# print (parent_pointer_tree2.get_value())
# print (parent_pointer_tree2.get_left_child().get_value() if parent_pointer_tree2.get_left_child() else None)
# print (parent_pointer_tree2.get_right_child().get_value() if parent_pointer_tree2.get_right_child() else None)
# print (parent_pointer_tree2.get_parent().get_value() if parent_pointer_tree2.get_parent() else None)

# print (parent_pointer_tree3.get_value())
# print (parent_pointer_tree3.get_left_child().get_value() if parent_pointer_tree3.get_left_child() else None)
# print (parent_pointer_tree3.get_right_child().get_value() if parent_pointer_tree3.get_right_child() else None)
# print (parent_pointer_tree3.get_parent().get_value() if parent_pointer_tree3.get_parent() else None)

# print (parent_pointer_tree4.get_value())
# print (parent_pointer_tree4.get_left_child().get_value() if parent_pointer_tree4.get_left_child() else None)
# print (parent_pointer_tree4.get_right_child().get_value() if parent_pointer_tree4.get_right_child() else None)
# print (parent_pointer_tree4.get_parent().get_value() if parent_pointer_tree4.get_parent() else None)