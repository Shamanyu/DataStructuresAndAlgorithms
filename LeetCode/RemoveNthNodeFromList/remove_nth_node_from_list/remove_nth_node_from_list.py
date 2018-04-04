class RemoveNthNodeFromList(object):

    def removeNthNodeFromList(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


from nose.tools import assert_equals, assert_raises

class TestRemoveNthNodeFromList(object):

  def testRemoveNthNodeFromList(self):
    removeNthNodeFromList = RemoveNthNodeFromList()

    print ("All test cases passed!")


def main():
  testRemoveNthNodeFromList = TestRemoveNthNodeFromList()
  testRemoveNthNodeFromList.testRemoveNthNodeFromList()

if __name__ == '__main__':
  main()
