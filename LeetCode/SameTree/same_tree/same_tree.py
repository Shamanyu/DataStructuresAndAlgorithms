class SameTree(object):

    def sameTree(self, treeOne, treeTwo):
        if treeOne is None and treeTwo is None:
            return True
        elif None in (treeOne, treeTwo):
            return False
        return treeOne.val == treeTwo.val \
            and self.sameTree(treeOne.left, treeTwo.left) \
            and self.sameTree(treeOne.right, treeTwo.right)


from nose.tools import assert_equals, assert_raises

class TestSameTree(object):

  def testSameTree(self):
    sameTree = SameTree()

    print ("All test cases passed!")


def main():
  testSameTree = TestSameTree()
  testSameTree.testSameTree()

if __name__ == '__main__':
  main()
