class BinaryTreePruning(object):

    def pruneTree(self, root):
        self._pruneTree(root)
        return root

    def _pruneTree(self, root):
        if root is None:
            return None
        if not (root.left or root.right):
            return root if root.val == 1 else None
        root.left = self._pruneTree(root.left)
        root.right = self._pruneTree(root.right)
        if (root.left or root.right):
            return root
        else:
            return root if root.val == 1 else None


from nose.tools import assert_equals, assert_raises

class TestBinaryTreePruning(object):

  def testBinaryTreePruning(self):
    binaryTreePruning = BinaryTreePruning()

    print ("All test cases passed!")


def main():
  testBinaryTreePruning = TestBinaryTreePruning()
  testBinaryTreePruning.testBinaryTreePruning()

if __name__ == '__main__':
  main()
