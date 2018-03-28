class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def get_list(self, head):
        current = head
        data = list()
        while (current is not None):
            data.append(current.val)
        return data

    def print_list(self, head):
        print (self.get_list(head))

class SwapNodesInPairs(object):

    def swapNodesInPairs(self, head):
        return self._swapNodesInPairs(head)

    def _swapNodesInPairs(self, head):
        if head is None:
            return None
        nodeToReturn = head if (not head.next) else head.next
        if head and head.next:
            temp = head.next.next
            firstNode = self._swapNodesInPairs(temp)
            head.next.next = head
            head.next = firstNode
        return nodeToReturn


from nose.tools import assert_equals, assert_raises

class TestSwapNodesInPairs(object):

  def testSwapNodesInPairs(self):
    swapNodesInPairs = SwapNodesInPairs()

    print ("All test cases passed!")


def main():
  testSwapNodesInPairs = TestSwapNodesInPairs()
  testSwapNodesInPairs.testSwapNodesInPairs()

if __name__ == '__main__':
  main()
