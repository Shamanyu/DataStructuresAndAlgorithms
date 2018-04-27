from collections import defaultdict

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class MostFrequentSubtreeSum(object):

    def __init__(self):
        self.sumDict = defaultdict(int)

    def findFrequentTreeSum(self, root):
        self._calculateSubTreeSum(root)
        return [key for key,value in self.sumDict.items() if value == max(self.sumDict.values())]

    def _calculateSubTreeSum(self, root):
        if root is None:
            return 0
        sum = root.val + self._calculateSubTreeSum(root.left) + self._calculateSubTreeSum(root.right)
        self.sumDict[sum] += 1
        return sum


from nose.tools import assert_equals, assert_raises

class TestMostFrequentSubtreeSum(object):

  def testMostFrequentSubtreeSum(self):
    mostFrequentSubtreeSum = MostFrequentSubtreeSum()

    node0_0 = TreeNode(5)

    node1_0 = TreeNode(2)
    node0_0.left = node1_0
    node1_1 = TreeNode(-3)
    node0_0.right = node1_1

    assert_equals(mostFrequentSubtreeSum.findFrequentTreeSum(node0_0), [2, 4, -3])

    node0_0 = TreeNode(5)

    node1_0 = TreeNode(2)
    node0_0.left = node1_0
    node1_1 = TreeNode(-5)
    node0_0.right = node1_1

    assert_equals(mostFrequentSubtreeSum.findFrequentTreeSum(node0_0), [2])

    print ("All test cases passed!")


def main():
  testMostFrequentSubtreeSum = TestMostFrequentSubtreeSum()
  testMostFrequentSubtreeSum.testMostFrequentSubtreeSum()

if __name__ == '__main__':
  main()
