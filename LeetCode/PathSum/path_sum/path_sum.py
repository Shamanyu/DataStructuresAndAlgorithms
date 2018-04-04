class PathSum(object):

    def pathSum(self, root, sum):
        self.sumList = list()
        self._pathSum(root, 0)
        return sum in self.sumList

    def _pathSum(self, root, sumCurrent):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.sumList.append(sumCurrent+root.val)
            return
        sumCurrent += root.val
        self._pathSum(root.left, sumCurrent)
        self._pathSum(root.right, sumCurrent)

from nose.tools import assert_equals, assert_raises

class TestPathSum(object):

  def testPathSum(self):
    pathSum = PathSum()

    print ("All test cases passed!")


def main():
  testPathSum = TestPathSum()
  testPathSum.testPathSum()

if __name__ == '__main__':
  main()
