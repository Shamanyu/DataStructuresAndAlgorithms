from stack import Node, Stack

class QueueFromStacks(object):

    def __init__(self):
        self.primary_stack = Stack()
        self.auxiliary_stack = Stack()

    def shift_stacks(self, source, destination):
        while not source.is_empty():
            data = source.pop()
            destination.push(data)

    def enqueue(self, data):
        self.primary_stack.push(data)

    def dequeue(self):
        self.shift_stacks(self.primary_stack, self.auxiliary_stack)
        return self.auxiliary_stack.pop()
        self.shift_stacks(self.auxiliary_stack, self.primary_stack)


# %load test_queue_from_stacks.py
from nose.tools import assert_equal

class TestQueueFromStacks(object):

    def test_queue_from_stacks(self):
        print('Test: Dequeue on empty stack')
        queue = QueueFromStacks()
        assert_equal(queue.dequeue(), None)

        print('Test: Enqueue on empty stack')
        print('Test: Enqueue on non-empty stack')
        print('Test: Multiple enqueue in a row')
        num_items = 3
        for i in range(0, num_items):
            queue.enqueue(i)

        print('Test: Dequeue on non-empty stack')
        print('Test: Dequeue after an enqueue')
        assert_equal(queue.dequeue(), 0)

        print('Test: Multiple dequeue in a row')
        assert_equal(queue.dequeue(), 1)
        assert_equal(queue.dequeue(), 2)

        print('Test: Enqueue after a dequeue')
        queue.enqueue(5)
        assert_equal(queue.dequeue(), 5)

        print('Success: test_queue_from_stacks')


def main():
    test = TestQueueFromStacks()
    test.test_queue_from_stacks()


if __name__ == '__main__':
    main()
