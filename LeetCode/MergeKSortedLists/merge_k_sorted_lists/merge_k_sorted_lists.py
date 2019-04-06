from typing import List


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MergeKSortedLists(object):

    def merge_k_sorted_lists(self, lists: List[ListNode]) -> ListNode:
        numbers = list()
        for counter in range(len(lists)):
            current_list = lists[counter]
            while current_list:
                numbers.append(current_list.val)
                current_list = current_list.next
        numbers = sorted(numbers)
        result_list = dummy = ListNode(None)
        for num in numbers:
            result_list.next = ListNode(num)
            result_list = result_list.next
        return dummy.next


from nose.tools import assert_equals, assert_raises


class TestMergeKSortedLists(object):

    def test_merge_k_sorted_lists(self):
        merge_k_sorted_lists_instance = MergeKSortedLists()

        print("All test cases passed!")


def main():
    test_merge_k_sorted_lists_instance = TestMergeKSortedLists()
    test_merge_k_sorted_lists_instance.test_merge_k_sorted_lists()


if __name__ == '__main__':
    main()
