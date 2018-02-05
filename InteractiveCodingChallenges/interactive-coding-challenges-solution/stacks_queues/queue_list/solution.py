class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None


class Queue(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        if self.tail is None:
            self.tail = Node(data)
            self.head = self.tail
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def dequeue(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data


# %load test_queue_list.py
from nose.tools import assert_equal

class TestQueue(object):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print('Test: Dequeue an empty queue')
        queue = Queue()
        assert_equal(queue.dequeue(), None)

        print('Test: Enqueue to an empty queue')
        queue.enqueue(1)

        print('Test: Dequeue a queue with one element')
        assert_equal(queue.dequeue(), 1)

        print('Test: Enqueue to a non-empty queue')
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        print('Test: Dequeue a queue with more than one element')
        assert_equal(queue.dequeue(), 2)
        assert_equal(queue.dequeue(), 3)
        assert_equal(queue.dequeue(), 4)

        print('Success: test_end_to_end')


def main():
    test = TestQueue()
    test.test_end_to_end()


if __name__ == '__main__':
    main()
