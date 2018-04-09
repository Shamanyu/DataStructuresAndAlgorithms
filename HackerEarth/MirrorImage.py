# https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/practice-problems/algorithm/mirror-image-2/

from Tree import Tree
from ParentPointerTree import ParentPointerTree

class TreeMirrorImage(object):

  def __init__(self):
    self.nodes = list()

  def get_user_input(self):
    [self.N, self.Q] = [int(number) for number in input().split()]
    self.nodes.append(ParentPointerTree(1, None, None, None, None))
    self.test_cases = [None for counter in range(0, self.Q)]
    for counter in range(0, self.N-1):
      [parent, child, which_child] = input().split()
      parent = int(parent)
      child = int(child)
      parent_node = self.find_key(parent)
      if parent_node:
        child_node = ParentPointerTree(child, parent_node, which_child, None, None)
        self.nodes.append(child_node)
    for counter in range(0, self.Q):
      self.test_cases[counter] = int(input())

  def find_key(self, key):
    for node in self.nodes:
      if node.get_value() == key:
        return node
    return None

  def get_mirror_images(self):
    output = list()
    for test_case in self.test_cases:
      print (self.get_mirror_image(test_case))
      output.append(self.get_mirror_image(test_case))
    return output

  def get_mirror_image(self, key):
    path_to_route = list()
    node = self.find_key(key)
    while node:
      parent_node = node.get_parent()
      if parent_node:
        path_to_route.append(node.get_which_child())
      node = parent_node
    path_to_mirror_complement = list(reversed(path_to_route))
    path_to_mirror = self.complement(path_to_mirror_complement)
    node = self.find_key(1)
    for direction in path_to_mirror:
      if node:
        if direction == 'L':
          node = node.get_left_child()
        elif direction == 'R':
          node = node.get_right_child()
    return node.get_value() if node else -1

  def complement(self, path):
    for counter in range(0, len(path)):
      if path[counter] == 'L':
        path[counter] = 'R'
      elif path[counter] == 'R':
        path[counter] = 'L'
    return path

tree_mirror_image = TreeMirrorImage()
tree_mirror_image.get_user_input()
print (tree_mirror_image.get_mirror_images())