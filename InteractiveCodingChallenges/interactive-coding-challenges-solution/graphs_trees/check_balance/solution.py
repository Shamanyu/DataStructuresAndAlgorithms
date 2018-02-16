from BST import Node, Bst

class BstBalance(Bst):

    # Time complexity: O(n)
    # Space complexity: O(1)
    def check_balance(self):
        if self.root is None:
            raise TypeError
        if self.root.left is None and self.root.right is None:
            return True
        self.minimum_height = float('inf')
        self.maximum_height = float('-inf')
        height = 1
        if self.root.left is not None:
            self._calculate_and_update_height(self.root.left, height)
        if self.root.right is not None:
            self._calculate_and_update_height(self.root.right, height)
        return (self.maximum_height - self.minimum_height <= 1)

    # Time complexity: O(n)
    # Space complexity: O(1)
    def _calculate_and_update_height(self, root, height):
        if root is None:
            self.update_height(height)
        if root.left is None and root.right is None:
            self.update_height(height+1)
        if root.left is not None:
            self._calculate_and_update_height(root.left, height+1)
        if root.right is not None:
            self._calculate_and_update_height(root.right, height+1)

    # Time complexity: O(1)
    # Space complexity: O(1)
    def update_height(self, height):
        if height < self.minimum_height:
            self.minimum_height = height
        if height > self.maximum_height:
            self.maximum_height = height



# %load test_check_balance.py
from nose.tools import assert_equal
from nose.tools import raises

class TestCheckBalance(object):

    @raises(TypeError)
    def test_check_balance_empty(self):
        bst = BstBalance(None)
        bst.check_balance()

    def test_check_balance(self):
        bst = BstBalance(Node(5))
        assert_equal(bst.check_balance(), True)

        bst.insert(3)
        bst.insert(8)
        bst.insert(1)
        bst.insert(4)
        assert_equal(bst.check_balance(), True)

        bst = BstBalance(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(9)
        bst.insert(10)
        assert_equal(bst.check_balance(), False)

        bst = BstBalance(Node(3))
        bst.insert(2)
        bst.insert(1)
        bst.insert(5)
        bst.insert(4)
        bst.insert(6)
        bst.insert(7)
        assert_equal(bst.check_balance(), True)

        print('Success: test_check_balance')


def main():
    test = TestCheckBalance()
    test.test_check_balance_empty()
    test.test_check_balance()


if __name__ == '__main__':
    main()
