from linked_list import Node,LinkedList

class MyLinkedList(LinkedList):

    # Time complexity: O(n) - 3 traversals
    # Space complexity: O(n)
    def partition(self, data):
        if self.head is None:
            return None

        new_linked_list = MyLinkedList()

        # Add all elements with value less than 'data' to new list
        current_node = self.head
        while (current_node != None):
            if current_node.data < data:
                new_linked_list.append(current_node.data)
            current_node = current_node.next

        # Add all elements with value data 'data' to new list
        current_node = self.head
        while (current_node != None):
            if current_node.data == data:
                new_linked_list.append(current_node.data)
            current_node = current_node.next

        # Add all elements with value greater than data 'data' to new list
        current_node = self.head
        while (current_node != None):
            if current_node.data > data:
                new_linked_list.append(current_node.data)
            current_node = current_node.next

        return new_linked_list

    # Time complexity: O(n) - 1 traversal
    # Space complexity: O(n)
    def partition_original(self, data):
        if self.head is None:
            return
        left = MyLinkedList(None)
        right = MyLinkedList(None)
        curr = self.head

        # Build the left and right lists
        while curr is not None:
            if curr.data < data:
                left.append(curr.data)
            elif curr.data == data:
                right.insert_to_front(curr.data)
            else:
                right.append(curr.data)
            curr = curr.next
        curr_left = left.head
        if curr_left is None:
            return right
        else:
            # Merge the two lists
            while curr_left.next is not None:
                curr_left = curr_left.next
            curr_left.next = right.head
            return left


# %load test_partition.py
from nose.tools import assert_equal

class TestPartition(object):

    def test_partition(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        linked_list.partition(10)
        assert_equal(linked_list.get_all_data(), [])

        print('Test: One element list, left list empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(0)
        assert_equal(linked_list.get_all_data(), [5])

        print('Test: Right list is empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(10)
        assert_equal(linked_list.get_all_data(), [5])

        print('Test: General case')
        # Partition = 10
        # Input: 4, 3, 13, 8, 10, 1, 14, 10, 12
        # Output: 4, 3, 8, 1, 10, 10, 13, 14, 12
        linked_list = MyLinkedList(Node(12))
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(14)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(8)
        linked_list.insert_to_front(13)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(4)
        partitioned_list = linked_list.partition(10)
        assert_equal(partitioned_list.get_all_data(),
                     [4, 3, 8, 1, 10, 10, 13, 14, 12])

        print('Success: test_partition')


def main():
    test = TestPartition()
    test.test_partition()


if __name__ == '__main__':
    main()
