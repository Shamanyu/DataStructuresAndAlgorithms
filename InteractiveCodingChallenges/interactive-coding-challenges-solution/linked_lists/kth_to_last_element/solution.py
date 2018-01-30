from linked_list import Node, LinkedList

class MyLinkedList(LinkedList):

    # Time complexity: O(n)
    # Space complexity: O(1)
    def kth_to_last_elem(self, k):
        if self.head is None:
            return None
        else:
            front_pointer = self.head
        while (k > 0):
            if front_pointer.next is None:
                return None
            front_pointer = front_pointer.next
            k -= 1
        back_pointer = self.head
        while (front_pointer.next != None):
            front_pointer = front_pointer.next
            back_pointer = back_pointer.next
        return back_pointer.data

# %load test_kth_to_last_elem.py
from nose.tools import assert_equal


class Test(object):

    def test_kth_to_last_elem(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        assert_equal(linked_list.kth_to_last_elem(0), None)

        print('Test: k >= len(list)')
        assert_equal(linked_list.kth_to_last_elem(100), None)

        print('Test: One element, k = 0')
        head = Node(2)
        linked_list = MyLinkedList(head)
        assert_equal(linked_list.kth_to_last_elem(0), 2)

        print('Test: General case')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(5)
        linked_list.insert_to_front(7)
        assert_equal(linked_list.kth_to_last_elem(2), 3)

        print('Success: test_kth_to_last_elem')


def main():
    test = Test()
    test.test_kth_to_last_elem()


if __name__ == '__main__':
    main()
