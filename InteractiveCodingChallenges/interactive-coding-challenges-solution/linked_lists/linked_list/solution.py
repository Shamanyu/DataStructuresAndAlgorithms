class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __str__(self):
        return self.data


class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        if self.head is None:
            return 0
        current_node = self.head
        length = 0
        while (current_node is not None):
            length += 1
            current_node = current_node.next
        return length

    def insert_to_front(self, data):
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node

    def append(self, data):
        if data is None:
            return None
        node = Node(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node

    def find(self, data):
        if self.head is None or data is None:
            return None
        current_node = self.head
        while (current_node is not None):
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def delete(self, data):
        if data is None:
            return
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next

    def print_list(self):
        if self.head is None:
            return
        current_node = self.head
        while (current_node is not None):
            print (current_node.data)
            current_node = current_node.next

    def get_all_data(self):
        data = list()
        curr_node = self.head
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        return data

    def reverse_in_place(self):
        pass
        # TODO: Implement me


# %load test_linked_list.py
from nose.tools import assert_equal


class TestLinkedList(object):

    def test_insert_to_front(self):
        print('Test: insert_to_front on an empty list')
        linked_list = LinkedList(None)
        linked_list.insert_to_front(10)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: insert_to_front on a None')
        linked_list.insert_to_front(None)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: insert_to_front general case')
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        assert_equal(linked_list.get_all_data(), ['bc', 'a', 10])

        print('Success: test_insert_to_front\n')

    def test_append(self):
        print('Test: append on an empty list')
        linked_list = LinkedList(None)
        linked_list.append(10)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: append a None')
        linked_list.append(None)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: append general case')
        linked_list.append('a')
        linked_list.append('bc')
        assert_equal(linked_list.get_all_data(), [10, 'a', 'bc'])

        print('Success: test_append\n')

    def test_find(self):
        print('Test: find on an empty list')
        linked_list = LinkedList(None)
        node = linked_list.find('a')
        assert_equal(node, None)

        print('Test: find a None')
        head = Node(10)
        linked_list = LinkedList(head)
        node = linked_list.find(None)
        assert_equal(node, None)

        print('Test: find general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        node = linked_list.find('a')
        assert_equal(str(node), 'a')

        print('Test: find general case with no matches')
        node = linked_list.find('aaa')
        assert_equal(node, None)

        print('Success: test_find\n')

    def test_delete(self):
        print('Test: delete on an empty list')
        linked_list = LinkedList(None)
        linked_list.delete('a')
        assert_equal(linked_list.get_all_data(), [])

        print('Test: delete a None')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.delete(None)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: delete general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        linked_list.delete('a')
        assert_equal(linked_list.get_all_data(), ['bc', 10])

        print('Test: delete general case with no matches')
        linked_list.delete('aa')
        assert_equal(linked_list.get_all_data(), ['bc', 10])

        print('Success: test_delete\n')

    def test_len(self):
        print('Test: len on an empty list')
        linked_list = LinkedList(None)
        assert_equal(len(linked_list), 0)

        print('Test: len general case')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        assert_equal(len(linked_list), 3)

        print('Success: test_len\n')

    def test_reverse_in_place(self):
        pass


def main():
    test = TestLinkedList()
    test.test_insert_to_front()
    test.test_append()
    test.test_find()
    test.test_delete()
    test.test_len()
    test.test_reverse_in_place()


if __name__ == '__main__':
    main()
