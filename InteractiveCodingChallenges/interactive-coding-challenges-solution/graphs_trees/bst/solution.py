from results import Results
from dfs import *

class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Bst(object):

    def insert(self, data):
        if not hasattr(self, 'root'):
            self.root = Node(data)
        else:
            self._insert(self.root, data)

    def _insert(self, root, data):
        if root.data > data:
            if root.left is None:
                root.left = Node(data)
            else:
                self._insert(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                self._insert(root.right, data)

# %load test_bst.py
from nose.tools import assert_equal

class TestTree(object):

    def __init__(self):
        self.results = Results()

    def test_tree_one(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        in_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), '[1, 2, 3, 5, 8]')
        self.results.clear_results()

    def test_tree_two(self):
        bst = Bst()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)
        in_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), '[1, 2, 3, 4, 5]')

        print('Success: test_tree')


def main():
    test = TestTree()
    test.test_tree_one()
    test.test_tree_two()


if __name__ == '__main__':
    main()