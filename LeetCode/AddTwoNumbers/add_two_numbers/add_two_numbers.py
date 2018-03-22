class ListNode(object):

  def __init__(self, x):
    self.val = x
    self.next = None

  # Time complexity: O(n)
  # Space complexity: O(n)
  def get_list(self):
    current = self
    data = list()
    while (current is not None):
      data.append(current.val)
      current = current.next
    return data

  # Time complexity: O(n)
  # Space complexity: O(n)
  def print_list(self):
    print (self.get_list)

class AddTwoNumbers(object):

  # Time complexity: O(n)
  # Space complexity: O(n)
  def add_two_numbers(self, l1, l2):
    head = None
    tail = None
    sum = 0
    carry = 0
    while (l1 is not None or l2 is not None):
      l1_val = l1.val if l1 else 0
      l2_val = l2.val if l2 else 0
      sum, carry = self.get_sum_and_carry(l1_val, l2_val, carry)
      if tail is None:
        new_node = ListNode(sum)
        head = new_node
        tail = new_node
      else:
        tail.next = ListNode(sum)
        tail = tail.next
      l1 = l1.next if l1 else l1
      l2 = l2.next if l2 else l2
    if carry:
      new_node = ListNode(carry)
      tail.next = new_node
      tail = tail.next
    return head

  # Time complexity: O(1)
  # Space complexity: O(1)
  def get_sum_and_carry(self, val1, val2, val3):
    sum = val1 + val2 + val3
    return (sum%10, sum//10)


from nose.tools import assert_equal, assert_raises

class TestAddTwoNumbers(object):

  def test_add_two_numbers(self):
    
    # Test case 1

    ## Construct first list
    node0 = ListNode(0)
    node1 = ListNode(1)
    node0.next = node1
    node2 = ListNode(2)
    node1.next = node2
    
    ## Construct second list
    nodeA = ListNode(0)
    nodeB = ListNode(1)
    nodeA.next = nodeB
    nodeC = ListNode(2)
    nodeB.next = nodeC

    ## Construct expected output list
    result_node0 = ListNode(0)
    result_node1 = ListNode(2)
    result_node0.next = result_node1
    result_node2 = ListNode(4)
    result_node1.next = result_node2

    add_two_numbers = AddTwoNumbers()
    sum_of_lists = add_two_numbers.add_two_numbers(node0, nodeA)

    assert_equal(sum_of_lists.get_list(), result_node0.get_list())

    # Test case 2

    ## Construct first list
    node0 = ListNode(7)
    node1 = ListNode(8)
    node0.next = node1
    node2 = ListNode(9)
    node1.next = node2
    
    ## Construct second list
    nodeA = ListNode(5)
    nodeB = ListNode(6)
    nodeA.next = nodeB
    nodeC = ListNode(7)
    nodeB.next = nodeC

    ## Construct expected output list
    result_node0 = ListNode(2)
    result_node1 = ListNode(5)
    result_node0.next = result_node1
    result_node2 = ListNode(7)
    result_node1.next = result_node2
    result_node3 = ListNode(1)
    result_node2.next = result_node3

    add_two_numbers = AddTwoNumbers()
    sum_of_lists = add_two_numbers.add_two_numbers(node0, nodeA)

    assert_equal(sum_of_lists.get_list(), result_node0.get_list())

    # Test case 3

    ## Construct first list
    node0 = ListNode(7)
    node1 = ListNode(8)
    node0.next = node1
    node2 = ListNode(9)
    node1.next = node2
    node3 = ListNode(9)
    node2.next = node3
    
    ## Construct second list
    nodeA = ListNode(5)
    nodeB = ListNode(6)
    nodeA.next = nodeB
    nodeC = ListNode(7)
    nodeB.next = nodeC

    ## Construct expected output list
    result_node0 = ListNode(2)
    result_node1 = ListNode(5)
    result_node0.next = result_node1
    result_node2 = ListNode(7)
    result_node1.next = result_node2
    result_node3 = ListNode(0)
    result_node2.next = result_node3
    result_node4 = ListNode(1)
    result_node3.next = result_node4

    add_two_numbers = AddTwoNumbers()
    sum_of_lists = add_two_numbers.add_two_numbers(node0, nodeA)

    assert_equal(sum_of_lists.get_list(), result_node0.get_list())

    print("All test cases passed")


def main():
  test_add_two_numbers = TestAddTwoNumbers()
  test_add_two_numbers.test_add_two_numbers()

if __name__ == '__main__':
  main()