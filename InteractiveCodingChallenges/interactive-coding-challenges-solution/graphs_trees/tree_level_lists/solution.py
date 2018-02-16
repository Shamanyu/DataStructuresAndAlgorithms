from BST import Node, Bst
from results import Results

class BstLevelLists(Bst):

    # Time complexity: O(n)
    # Space complexity: O(n)
    def create_level_lists(self):

        level_lists = list(list())
        level_lists.append([self.root])

        # Traverse the tree and store the nodes in a level wise list
        # Time complexity: O(n)
        # Space complexity: O(n)
        counter = 0
        while (len(level_lists[counter]) > 0):
            level_list = list()
            for node in level_lists[counter]:
                if node.left:
                    level_list.append(node.left)
                if node.right:
                    level_list.append(node.right)
            level_lists.append(level_list)
            counter += 1

        # Traverse the level wise nose list to build level wise node data list
        # Time complexity: O(n)
        # Space complexity: O(n)
        levels_data_list = list(list())
        for level_list in level_lists:
            level_data_list = list()
            for node in level_list:
                level_data_list.append(node.data)
            levels_data_list.append(level_data_list)
        return levels_data_list

# %load test_tree_level_lists.py
from nose.tools import assert_equal

class TestTreeLevelLists(object):

    def test_tree_level_lists(self):
        bst = BstLevelLists(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(2)
        bst.insert(4)
        bst.insert(1)
        bst.insert(7)
        bst.insert(6)
        bst.insert(9)
        bst.insert(10)
        bst.insert(11)

        levels = bst.create_level_lists()
        results_list = []
        for level in levels:
            results = Results()
            for node in level:
                results.add_result(node)
            results_list.append(results)

        assert_equal(str(results_list[0]), '[5]')
        assert_equal(str(results_list[1]), '[3, 8]')
        assert_equal(str(results_list[2]), '[2, 4, 7, 9]')
        assert_equal(str(results_list[3]), '[1, 6, 10]')
        assert_equal(str(results_list[4]), '[11]')

        print('Success: test_tree_level_lists')


def main():
    test = TestTreeLevelLists()
    test.test_tree_level_lists()


if __name__ == '__main__':
    main()
