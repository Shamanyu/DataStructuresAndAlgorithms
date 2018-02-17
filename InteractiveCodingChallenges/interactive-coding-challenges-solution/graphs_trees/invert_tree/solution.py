from BST import Node, Bst

class InverseBst(Bst):

    def invert_tree(self):
        if self.root is None:
            return None
        self._invert_tree(self.root)
        return self.root

    def _invert_tree(self, root):
        if root is None:
            return 
        temp = root.left
        root.left = root.right
        root.right = temp
        self._invert_tree(root.left)
        self._invert_tree(root.right)

# %load test_invert_tree.py
from nose.tools import assert_equal

class TestInvertTree(object):

    def test_invert_tree(self):
        root = Node(5)
        bst = InverseBst(root)
        node2 = bst.insert(2)
        node3 = bst.insert(3)
        node1 = bst.insert(1)
        node7 = bst.insert(7)
        node6 = bst.insert(6)
        node9 = bst.insert(9)
        result = bst.invert_tree()
        assert_equal(result, root)
        assert_equal(result.left, node7)
        assert_equal(result.right, node2)
        assert_equal(result.left.left, node9)
        assert_equal(result.left.right, node6)
        assert_equal(result.right.left, node3)
        assert_equal(result.right.right, node1)
        print('Success: test_invert_tree')


def main():
    test = TestInvertTree()
    test.test_invert_tree()


if __name__ == '__main__':
    main()