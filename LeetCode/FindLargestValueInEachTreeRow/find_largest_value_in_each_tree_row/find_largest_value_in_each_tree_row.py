# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class FindLargestValueInEachTreeRow(object):

    def largestValues(self, root):
        queue = [root]
        result = list()
        while queue:
            queue.sort(key=lambda x:x.val)
            result.append(queue[-1].val)
            newQueue = list()
            for node in queue:
                newQueue.extend([node.left, node.right])
            queue = [node for node in newQueue if node]
        return result


from nose.tools import assert_equals, assert_raises

class TestFindLargestValueInEachTreeRow(object):

  def testFindLargestValueInEachTreeRow(self):
    findLargestValueInEachTreeRow = FindLargestValueInEachTreeRow()

    node0_0 = TreeNode(1)

    node1_0 = TreeNode(3)
    node0_0.left = node1_0
    node1_1 = TreeNode(2)
    node0_0.right = node1_1

    node2_0 = TreeNode(5)
    node1_0.left = node2_0
    node2_1 = TreeNode(3)
    node1_0.right = node2_1
    node2_3 = TreeNode(9)
    node1_1.right = node2_3

    assert_equals(findLargestValueInEachTreeRow.largestValues(node0_0), [1, 3, 9])

    print ("All test cases passed!")


def main():
  testFindLargestValueInEachTreeRow = TestFindLargestValueInEachTreeRow()
  testFindLargestValueInEachTreeRow.testFindLargestValueInEachTreeRow()

if __name__ == '__main__':
  main()
