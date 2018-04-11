# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MergeTwoBinaryTrees(object):

    def mergeTrees(self, root1, root2):
        if not(root1 or root2):
            return None

        if (root1 and root2):
            newRoot = TreeNode(root1.val + root2.val)
            newRoot.left = self.mergeTrees(root1.left, root2.left)
            newRoot.right = self.mergeTrees(root1.right, root2.right)
        elif root1:
            newRoot = TreeNode(root1.val)
            newRoot.left = self.mergeTrees(root1.left, None)
            newRoot.right = self.mergeTrees(root1.right, None)
        elif root2:
            newRoot = TreeNode(root2.val)
            newRoot.left = self.mergeTrees(root2.left, None)
            newRoot.right = self.mergeTrees(root2.right, None)
        return newRoot


from nose.tools import assert_equals, assert_raises

class TestMergeTwoBinaryTrees(object):

  def testMergeTwoBinaryTrees(self):
    mergeTwoBinaryTrees = MergeTwoBinaryTrees()

    print ("All test cases passed!")


def main():
  testMergeTwoBinaryTrees = TestMergeTwoBinaryTrees()
  testMergeTwoBinaryTrees.testMergeTwoBinaryTrees()

if __name__ == '__main__':
  main()
