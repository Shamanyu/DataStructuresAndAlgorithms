# Definition for a singly linked list node.
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class MergeTwoSortedLists(object):
    def merge_two_sorted_lists(self, list1_head, list2_head):
        list1_pointer = list1_head
        list2_pointer = list2_head
        head = tail = None
        if not list1_head:
            return list2_head
        if not list2_head:
            return list1_head
        while list1_pointer and list2_pointer:
            if not head:
                if list1_pointer.val < list2_pointer.val:
                    head = tail = list1_pointer
                    list1_pointer = list1_pointer.next
                else:
                    head = tail = list2_pointer
                    list2_pointer = list2_pointer.next
            else:
                if list1_pointer.val < list2_pointer.val:
                    tail.next = list1_pointer
                    tail = tail.next
                    list1_pointer = list1_pointer.next
                else:
                    tail.next = list2_pointer
                    tail = tail.next
                    list2_pointer = list2_pointer.next
        while list1_pointer:
            tail.next = list1_pointer
            tail = tail.next
            list1_pointer = list1_pointer.next
        while list2_pointer:
            tail.next = list2_pointer
            tail = tail.next
            list2_pointer = list2_pointer.next

        return head


from nose.tools import assert_equals, assert_raises


class TestMergeTwoSortedLists(object):

    def test_merge_two_sorted_lists(self):
        merge_two_lists_instance = MergeTwoSortedLists()

        # Happy flow
        list1_head = list1_tail = ListNode(1)
        list1_tail.next = ListNode(2)
        list1_tail = list1_tail.next
        list2_head = list2_tail = ListNode(3)
        list2_tail.next = ListNode(4)
        list2_tail = list2_tail.next
        merge_two_lists_instance.merge_two_sorted_lists(list1_head, list2_head)

        print ("All test cases passed!")


def main():
    test_merge_two_sorted_lists_instance = TestMergeTwoSortedLists()
    test_merge_two_sorted_lists_instance.test_merge_two_sorted_lists()


if __name__ == '__main__':
    main()
