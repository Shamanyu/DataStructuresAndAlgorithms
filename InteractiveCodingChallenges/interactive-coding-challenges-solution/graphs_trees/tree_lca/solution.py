from Node import Node


class BinaryTree(object):

    # Implementation if nodes have pointers to parents
    # Time complexity: O(h)
    # Space complexity: O(h)
    # def lca(self, root, node1, node2):
    #     if node1 is None or node2 is None:
    #         return None
    #     current = node1
    #     while (current is not None):
    #         if self.find(current, node2):
    #             return current
    #         else:
    #             parent = current.parent
    #             if parent is None:
    #                 return None
    #             else:
    #                 if parent.left == node1:
    #                     if self.find(parent.right, node2):
    #                         return parent.right
    #                     else:
    #                         return None
    #                 else:
    #                     if self.find(parent.left, node2):
    #                         return parent.left
    #                     else:
    #                         return None
    #     return None

    # Implementation if nodes have pointers to parents
    # Time complexity: O(h)
    # Space complexity: O(h)
    # def find(self, root, node):
    #     if root is None:
    #         return False
    #     if root == node:
    #         return True
    #     if (root.left is None and root.right is None and root != node):
    #         return None
    #     else:
    #         return self.find(root.left, node) or self.find(root.right, node)

    # Time complexity: O(h); where h is the height of tree
    # Space complexity: O(h); where h is the recursion depth
    def lca(self, root, node1, node2):
        if None in (root, node1, node2):
            return None
        if  (not self._node_in_tree(root, node1) or
          not self._node_in_tree(root, node2)):
            return None
        return self._lca(root, node1, node2)

    def _node_in_tree(self, root, node):
        if root is None:
            return False
        if root is node:
            return True
        left = self._node_in_tree(root.left, node)
        right = self._node_in_tree(root.right, node)
        return left or right

    def _lca(self, root, node1, node2):
        if root is None:
            return None
        if root is node1 or root is node2:
            return root
        left_node = self._lca(root.left, node1, node2)
        right_node = self._lca(root.right, node1, node2)
        if left_node is not None and right_node is not None:
            return root
        else:
            return left_node if left_node is not None else right_node


  # %load test_lca.py
from nose.tools import assert_equal

class TestLowestCommonAncestor(object):

    def test_lca(self):
        node10 = Node(10)
        node5 = Node(5)
        node12 = Node(12)
        node3 = Node(3)
        node1 = Node(1)
        node8 = Node(8)
        node9 = Node(9)
        node18 = Node(18)
        node20 = Node(20)
        node40 = Node(40)
        node3.left = node1
        node3.right = node8
        node5.left = node12
        node5.right = node3
        node20.left = node40
        node9.left = node18
        node9.right = node20
        node10.left = node5
        node10.right = node9
        root = node10
        node0 = Node(0)
        binary_tree = BinaryTree()
        assert_equal(binary_tree.lca(root, node0, node5), None)
        assert_equal(binary_tree.lca(root, node5, node0), None)
        assert_equal(binary_tree.lca(root, node1, node8), node3)
        assert_equal(binary_tree.lca(root, node12, node8), node5)
        assert_equal(binary_tree.lca(root, node12, node40), node10)
        assert_equal(binary_tree.lca(root, node9, node20), node9)
        assert_equal(binary_tree.lca(root, node3, node5), node5)
        print('Success: test_lca')


def main():
    test = TestLowestCommonAncestor()
    test.test_lca()


if __name__ == '__main__':
    main()