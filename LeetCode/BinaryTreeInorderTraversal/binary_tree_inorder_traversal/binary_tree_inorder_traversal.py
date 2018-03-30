class BinaryTreeInorderTraversal(object):

  def binaryTreeInorderTraversal(self, root):
    if not root:
        return []
    ans = list()
    if root.left:
        ans.extend(self.binaryTreeInorderTraversal(root.left))
    ans.append(root.val)
    if root.right:
        ans.extend(self.binaryTreeInorderTraversal(root.right))
    return ans


from nose.tools import assert_equals, assert_raises

class TestBinaryTreeInorderTraversal(object):

  def testBinaryTreeInorderTraversal(self):
    binaryTreeInorderTraversal = BinaryTreeInorderTraversal()

    print ("All test cases passed!")


def main():
  testBinaryTreeInorderTraversal = TestBinaryTreeInorderTraversal()
  testBinaryTreeInorderTraversal.testBinaryTreeInorderTraversal()

if __name__ == '__main__':
  main()
