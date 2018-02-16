from BST import Node, Bst

class BstValidate(Bst):

    # Time complexity: O(n)
    # Space complexity:O(1)
    def validate(self):
        if self.root is None:
            raise Exception
        self.minimum_value = float('-inf')
        return self.traverse(self.root)

    # Time complexity: O(n)
    # Space complexity:O(1)
    def traverse(self, node):
        if node is None:
            pass
        if node.left is not None:
            self.traverse(node.left)
        if not self.compare(node):
            return False
        if node.right is not None:
            self.traverse(node.right)
        return True

    # Time complexity: O(1)
    # Space complexity:O(1)
    def compare(self, node):
        if node.data < self.minimum_value:
            return False
        self.minimum_value = node.data
        return True


# %load test_bst_validate.py
from nose.tools import assert_equal
from nose.tools import raises

class TestBstValidate(object):

    @raises(Exception)
    def test_bst_validate_empty(self):
        validate_bst(None)

    def test_bst_validate(self):
        bst = BstValidate(Node(5))
        bst.insert(8)
        bst.insert(5)
        bst.insert(6)
        bst.insert(4)
        bst.insert(7)
        assert_equal(bst.validate(), True)

        bst = BstValidate(Node(5))
        left = Node(5)
        right = Node(8)
        invalid = Node(20)
        bst.root.left = left
        bst.root.right = right
        bst.root.left.right = invalid
        assert_equal(bst.validate(), False)

        print('Success: test_bst_validate')


def main():
    test = TestBstValidate()
    test.test_bst_validate_empty()
    test.test_bst_validate()


if __name__ == '__main__':
    main()
