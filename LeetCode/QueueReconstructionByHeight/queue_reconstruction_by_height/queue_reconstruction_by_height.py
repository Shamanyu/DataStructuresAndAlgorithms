class QueueReconstructionByHeight(object):

    def queueReconstructionByHeight(self, people):
        people.sort(key=lambda a:[a[0], -a[1]], reverse=True)
        result = list()
        for person in people:
            result.insert(person[1], person)
        return result


from nose.tools import assert_equals, assert_raises

class TestQueueReconstructionByHeight(object):

  def testQueueReconstructionByHeight(self):
    queueReconstructionByHeight = QueueReconstructionByHeight()

    assert_equals(queueReconstructionByHeight.queueReconstructionByHeight(
        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    ),  [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]])

    print ("All test cases passed!")


def main():
  testQueueReconstructionByHeight = TestQueueReconstructionByHeight()
  testQueueReconstructionByHeight.testQueueReconstructionByHeight()

if __name__ == '__main__':
  main()
