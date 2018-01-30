from linked_list import Node, LinkedList

class MyLinkedList(LinkedList):

    # Time complexity: O(n)
    # Space complexity: O(n)
    def reverse(self):
        reversed_list = MyLinkedList()
        current = self.head
        while (current is not None):
            reversed_list.insert_to_front(current.data)
            current = current.next
        return reversed_list

    # Time complexity: O(n)
    # Space complexity: O(n)
    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return False
        linked_list_reversed = self.reverse()
        main_list_head = self.head
        reverse_list_head = linked_list_reversed.head
        for counter in range(0, self.__len__()//2+1):
            if main_list_head.data != reverse_list_head.data:
                return False
            main_list_head = main_list_head.next
            reverse_list_head = reverse_list_head.next
        return True


# %load test_palindrome.py
from nose.tools import assert_equal

class TestPalindrome(object):

    def test_palindrome(self):
        print('Test: Empty list')
        linked_list = MyLinkedList()
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: Single element list')
        head = Node(1)
        linked_list = MyLinkedList(head)
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: Two element list, not a palindrome')
        linked_list.append(2)
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: General case: Palindrome with even length')
        head = Node('a')
        linked_list = MyLinkedList(head)
        linked_list.append('b')
        linked_list.append('b')
        linked_list.append('a')
        assert_equal(linked_list.is_palindrome(), True)

        print('Test: General case: Palindrome with odd length')
        head = Node(1)
        linked_list = MyLinkedList(head)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        assert_equal(linked_list.is_palindrome(), True)

        print('Success: test_palindrome')


def main():
    test = TestPalindrome()
    test.test_palindrome()


if __name__ == '__main__':
    main()
