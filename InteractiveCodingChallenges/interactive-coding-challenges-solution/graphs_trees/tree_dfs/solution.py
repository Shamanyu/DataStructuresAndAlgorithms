from BST import Node, Bst
from results import Results

class BstDfs(Bst):

    def in_order_traversal(self, node, visit_func):
        if node is not None:
            self.in_order_traversal(node.left, visit_func)
            visit_func(node)
            self.in_order_traversal(node.right, visit_func)

    def pre_order_traversal(self, node, visit_func):
        if node is not None:
            visit_func(node)
            self.pre_order_traversal(node.left, visit_func)
            self.pre_order_traversal(node.right, visit_func)

    def post_order_traversal(self, node, visit_func):
        if node is not None:
            self.post_order_traversal(node.left, visit_func)
            self.post_order_traversal(node.right, visit_func)
            visit_func(node)


# %load test_dfs.py
from nose.tools import assert_equal

class TestDfs(object):

    def __init__(self):
        self.results = Results()

    def test_dfs(self):
        bst = BstDfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)

        bst.in_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[1, 2, 3, 5, 8]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[5, 2, 1, 3, 8]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[1, 3, 2, 8, 5]")
        self.results.clear_results()

        bst = BstDfs(Node(1))
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)

        bst.in_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[5, 4, 3, 2, 1]")

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()
