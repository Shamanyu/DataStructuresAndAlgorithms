from BST import Node, Bst

class MinBst(object):

    def create_min_bst(self, array):
        if array is None:
            return
        return self._create_min_bst(array, 0, len(array) - 1)

    def _create_min_bst(self, array, start, end):
        if end < start:
            return None
        mid = (start + end) // 2
        node = Node(array[mid])
        node.left = self._create_min_bst(array, start, mid - 1)
        node.right = self._create_min_bst(array, mid + 1, end)
        return node

# %load test_bst_min.py
from nose.tools import assert_equal

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left),
                   height(node.right))


class TestBstMin(object):

    def test_bst_min(self):
        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6]
        root = min_bst.create_min_bst(array)
        assert_equal(height(root), 3)

        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        root = min_bst.create_min_bst(array)
        assert_equal(height(root), 4)

        print('Success: test_bst_min')


def main():
    test = TestBstMin()
    test.test_bst_min()


if __name__ == '__main__':
    main()
