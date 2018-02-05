from BST import Node, Bst

class BstHeight(Bst):

    def height(self, node):
        if node is None:
            return 0
        return max(self.height(node.left), self.height(node.right)) + 1



# %load test_height.py
from nose.tools import assert_equal

class TestHeight(object):

    def test_height(self):
        bst = BstHeight(Node(5))
        assert_equal(bst.height(bst.root), 1)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        assert_equal(bst.height(bst.root), 3)

        print('Success: test_height')


def main():
    test = TestHeight()
    test.test_height()


if __name__ == '__main__':
    main()
