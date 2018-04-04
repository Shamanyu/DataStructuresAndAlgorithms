class InvertBinaryTree(object):

    def invertBinaryTree(self, root):
        if root is None:
            return root
        temp = self.invertBinaryTree(root.left)
        root.left = self.invertBinaryTree(root.right)
        root.right = temp
        return root


from nose.tools import assert_equals, assert_raises

class TestInvertBinaryTree(object):

  def testInvertBinaryTree(self):
    invertBinaryTree = InvertBinaryTree()

    print ("All test cases passed!")


def main():
  testInvertBinaryTree = TestInvertBinaryTree()
  testInvertBinaryTree.testInvertBinaryTree()

if __name__ == '__main__':
  main()
