from results import Results
from BST import Node, Bst

class BstBfs(Bst):

    def bfs(self, visit_func):
        queue = list()
        queue.append(self.root)
        while (queue != []):
            node = queue.pop(0)
            visit_func(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)



# %load test_bfs.py
from nose.tools import assert_equal

class TestBfs(object):

    def __init__(self):
        self.results = Results()

    def test_bfs(self):
        bst = BstBfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        bst.bfs(self.results.add_result)
        assert_equal(str(self.results), '[5, 2, 8, 1, 3]')

        print('Success: test_bfs')


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == '__main__':
    main()
