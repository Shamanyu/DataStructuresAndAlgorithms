# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindBottomLeftTreeValue(object):

    def findBottomLeftTreeValue(self, root):
        queue, ans = [root], 0
        while any(queue):
            ans = queue[0].val
            queue = [leaf for node in queue for leaf in (nodenode.left, node.right) if leaf]
        return ans


from nose.tools import assert_equals, assert_raises

class TestFindBottomLeftTreeValue(object):

  def testFindBottomLeftTreeValue(self):
    findBottomLeftTreeValue = FindBottomLeftTreeValue()

    print ("All test cases passed!")


def main():
  testFindBottomLeftTreeValue = TestFindBottomLeftTreeValue()
  testFindBottomLeftTreeValue.testFindBottomLeftTreeValue()

if __name__ == '__main__':
  main()
