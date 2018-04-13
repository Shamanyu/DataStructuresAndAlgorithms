import heapq

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MaximumBinaryTree(object):

    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        root, maxi = TreeNode(max(nums)), nums.index(max(nums))
        root.left = self.constructMaximumBinaryTree(nums[:maxi])
        root.right = self.constructMaximumBinaryTree(nums[maxi + 1:])
        return root


from nose.tools import assert_equals, assert_raises

class TestMaximumBinaryTree(object):

  def testMaximumBinaryTree(self):
    maximumBinaryTree = MaximumBinaryTree()

    maximumBinaryTree.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])

    print ("All test cases passed!")


def main():
  testMaximumBinaryTree = TestMaximumBinaryTree()
  testMaximumBinaryTree.testMaximumBinaryTree()

if __name__ == '__main__':
  main()
