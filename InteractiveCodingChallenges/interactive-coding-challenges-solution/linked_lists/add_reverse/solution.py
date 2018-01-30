from linked_list import Node, LinkedList

class MyLinkedList(LinkedList):

    # Time complexity: O(m+n)
    # Space complexity: O(m>n?m:n)
    def add_reverse(self, first_list, second_list):
        if first_list is None or second_list is None:
            return None
        result = MyLinkedList()
        carry = 0
        first_list_pointer = first_list.head
        second_list_pointer = second_list.head
        while (first_list_pointer != None or second_list_pointer != None):
            if first_list_pointer is None:
                temporary_result = second_list_pointer.data + carry
                second_list_pointer = second_list_pointer.next
            elif second_list_pointer is None:
                temporary_result = first_list_pointer.data + carry
                first_list_pointer = first_list_pointer.next
            else:
                temporary_result = first_list_pointer.data + second_list_pointer.data + carry
                first_list_pointer = first_list_pointer.next
                second_list_pointer = second_list_pointer.next
            if temporary_result > 10:
                carry = temporary_result // 10;
                temporary_result = temporary_result % 10;
            else:
                carry = 0
            result.append(temporary_result)
        if carry:
            result.append(carry)
        return result

    def _add_reverse_original(self, first_node, second_node, carry):
        # Base case
        if first_node is None and second_node is None and not carry:
            return None

        # Recursive case
        value = carry
        value += first_node.data if first_node is not None else 0
        value += second_node.data if second_node is not None else 0
        carry = 1 if value >= 10 else 0
        value %= 10
        node = Node(value)
        node.next = self._add_reverse(
            first_node.next if first_node is not None else None,
            second_node.next if first_node is not None else None,
            carry)
        return node

    def add_reverse_original(self, first_list, second_list):
        # See constraints
        if first_list is None or second_list is None:
            return None
        head = self._add_reverse(first_list.head, second_list.head, 0)
        return MyLinkedList(head)


# %load test_add_reverse.py
from nose.tools import assert_equal

class TestAddReverse(object):

    def test_add_reverse(self):
        print('Test: Empty list(s)')
        assert_equal(MyLinkedList().add_reverse(None, None), None)
        assert_equal(MyLinkedList().add_reverse(Node(5), None), None)
        assert_equal(MyLinkedList().add_reverse(None, Node(10)), None)

        print('Test: Add values of different lengths')
        # Input 1: 6->5->None
        # Input 2: 9->8->7
        # Result: 5->4->8
        first_list = MyLinkedList(Node(6))
        first_list.append(5)
        second_list = MyLinkedList(Node(9))
        second_list.append(8)
        second_list.append(7)
        result = MyLinkedList().add_reverse(first_list, second_list)
        assert_equal(result.get_all_data(), [5, 4, 8])

        print('Test: Add values of same lengths')
        # Input 1: 6->5->4
        # Input 2: 9->8->7
        # Result: 5->4->2->1
        first_head = Node(6)
        first_list = MyLinkedList(first_head)
        first_list.append(5)
        first_list.append(4)
        second_head = Node(9)
        second_list = MyLinkedList(second_head)
        second_list.append(8)
        second_list.append(7)
        result = MyLinkedList().add_reverse(first_list, second_list)
        assert_equal(result.get_all_data(), [5, 4, 2, 1])

        print('Success: test_add_reverse')


def main():
    test = TestAddReverse()
    test.test_add_reverse()


if __name__ == '__main__':
    main()
