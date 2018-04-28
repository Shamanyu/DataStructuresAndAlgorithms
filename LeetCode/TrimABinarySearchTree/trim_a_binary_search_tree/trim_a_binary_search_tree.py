# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TrimABinarySearchTree(object):

    def trimBST(self, root, L, R):
        if root is None:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root


from nose.tools import assert_equals, assert_raises

class TestTrimABinarySearchTree(object):

  def testTrimABinarySearchTree(self):
    trimABinarySearchTree = TrimABinarySearchTree()

    node0_0 = TreeNode(1)

    node1_0 = TreeNode(0)
    node0_0.left = node1_0
    node1_1 = TreeNode(2)
    node0_0.right = node1_1

    assert_equals(trimABinarySearchTree.trimBST(node0_0, 1, 2), node0_0)

    print ("All test cases passed!")


def main():
  testTrimABinarySearchTree = TestTrimABinarySearchTree()
  testTrimABinarySearchTree.testTrimABinarySearchTree()

if __name__ == '__main__':
  main()
