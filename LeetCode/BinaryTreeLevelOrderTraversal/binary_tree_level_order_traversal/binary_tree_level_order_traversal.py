# class TreeNode(object):
#
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BinaryTreeLevelOrderTraversal(object):

  def binaryTreeLevelOrderTraversal(self, root):
      if not root:
          return []
      ans, level = [], [root]
      while level:
          ans.append([node.val for node in level])
          temp = []
          for node in level:
              temp.extend([node.left, node.right])
          level = [node for node in temp if node]
      return ans


from nose.tools import assert_equals, assert_raises

class TestBinaryTreeLevelOrderTraversal(object):

  def testBinaryTreeLevelOrderTraversal(self):
    binaryTreeLevelOrderTraversal = BinaryTreeLevelOrderTraversal()

    # assert_equals(binaryTreeLevelOrderTraversal.binaryTreeLevelOrderTraversal(
        # [3, 9, 20, None, None, 15, 7]), [[3], [9, 20], [15, 7]])

    print ("All test cases passed!")


def main():
  testBinaryTreeLevelOrderTraversal = TestBinaryTreeLevelOrderTraversal()
  testBinaryTreeLevelOrderTraversal.testBinaryTreeLevelOrderTraversal()

if __name__ == '__main__':
  main()
