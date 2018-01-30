from linked_list import Node, LinkedList

class MyLinkedList(LinkedList):

    def delete_node(self, node):
        if self.head is None or node is None:
            return self.head
        current_node = self.head
        previous_node = None
        while (current_node != None):
            if current_node == node:
                if previous_node is None:
                    self.head = Node(None)
                else:
                    if current_node.next:
                        previous_node.next = current_node.next
                    else:
                        previous_node.next = Node(None)
                return self.head
            else:
                previous_node = current_node
                current_node = current_node.next
        return self.head


# %load test_delete_mid.py
from nose.tools import assert_equal

class TestDeleteNode(object):

    def test_delete_node(self):
        print('Test: Empty list, null node to delete')
        linked_list = MyLinkedList(None)
        linked_list.delete_node(None)
        assert_equal(linked_list.get_all_data(), [])

        print('Test: One node')
        head = Node(2)
        linked_list = MyLinkedList(head)
        linked_list.delete_node(head)
        assert_equal(linked_list.get_all_data(), [None])

        print('Test: Multiple nodes')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node1)
        assert_equal(linked_list.get_all_data(), [1, 4, 2])

        print('Test: Multiple nodes, delete last element')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node0)
        assert_equal(linked_list.get_all_data(), [1, 4, 3, None])

        print('Success: test_delete_node')


def main():
    test = TestDeleteNode()
    test.test_delete_node()


if __name__ == '__main__':
    main()
