class FlattenBinaryTreeToLinkedList(object):

  def flattenBinaryTreeToLinkedList(self, root):
    # if not root:
    #     return None, None
    # head = tail = None, None
    # if root:
    #     head = root
    #     tail = root
    # if root.left:
    #     left_head, left_tail = self.flattenBinaryTreeToLinkedList(root.left)
    #     root.left = left_head
    #     tail = left_tail
    # if root.right:
    #     right_head, right_tail = self.flattenBinaryTreeToLinkedList(root.right)
    #     tail.left = right_head
    #     tail = right_tail
    # return head, tail

    ans = []
    if root:
        ans.append(root.val)
        ans.extend(self.flattenBinaryTreeToLinkedList(root.left))
        ans.extend(self.flattenBinaryTreeToLinkedList(root.right))
    return ans

    # if not root:
    #     return
    # self.prev = root
    # self.flatten(root.left)
    #
    # temp = root.right
    # root.right, root.left = root.left, None
    # self.prev.right = temp
    #
    # self.flatten(temp)


from nose.tools import assert_equals, assert_raises

class TestFlattenBinaryTreeToLinkedList(object):

  def testFlattenBinaryTreeToLinkedList(self):
    flattenBinaryTreeToLinkedList = FlattenBinaryTreeToLinkedList()

    assert_equals(flattenBinaryTreeToLinkedList.flattenBinaryTreeToLinkedList([]), [])

    print ("All test cases passed!")


def main():
  testFlattenBinaryTreeToLinkedList = TestFlattenBinaryTreeToLinkedList()
  testFlattenBinaryTreeToLinkedList.testFlattenBinaryTreeToLinkedList()

if __name__ == '__main__':
  main()
