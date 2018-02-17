from BST import Node, Bst

class BstSuccessor(object):

    def get_next(self, node):
        if node is None:
            raise Exception
        elif node.right is not None:
            return self.find_left_most_leaf_data(node.right)
        elif node.parent is not None:
            return self.find_parent_successor_data(node, node.parent)
        return None

    def find_left_most_leaf_data(self, node):
        left_most_leaf = node
        while (node.left is not None):
            left_most_leaf = node.left
            node = node.left
        return left_most_leaf.data

    def find_parent_successor_data(self, child_node, parent_node):
        if parent_node.left == child_node:
            return parent_node.data
        else:
            child_node = parent_node
            parent_node = parent_node.parent
            if parent_node is None:
                return None
            else:
                return self.find_parent_successor_data(child_node, parent_node)



# %load test_bst_successor.py
from nose.tools import assert_equal
from nose.tools import raises

class TestBstSuccessor(object):

    @raises(Exception)
    def test_bst_successor_empty(self):
        bst_successor = BstSuccessor()
        bst_successor.get_next(None)

    def test_bst_successor(self):
        nodes = {}
        node = Node(5)
        nodes[5] = node
        bst = Bst(nodes[5])
        nodes[3] = bst.insert(3)
        nodes[8] = bst.insert(8)
        nodes[2] = bst.insert(2)
        nodes[4] = bst.insert(4)
        nodes[6] = bst.insert(6)
        nodes[12] = bst.insert(12)
        nodes[1] = bst.insert(1)
        nodes[7] = bst.insert(7)
        nodes[10] = bst.insert(10)
        nodes[15] = bst.insert(15)
        nodes[9] = bst.insert(9)

        bst_successor = BstSuccessor()
        assert_equal(bst_successor.get_next(nodes[4]), 5)
        assert_equal(bst_successor.get_next(nodes[5]), 6)
        assert_equal(bst_successor.get_next(nodes[8]), 9)
        assert_equal(bst_successor.get_next(nodes[15]), None)

        print('Success: test_bst_successor')


def main():
    test = TestBstSuccessor()
    test.test_bst_successor()
    test.test_bst_successor_empty()


if __name__ == '__main__':
    main()