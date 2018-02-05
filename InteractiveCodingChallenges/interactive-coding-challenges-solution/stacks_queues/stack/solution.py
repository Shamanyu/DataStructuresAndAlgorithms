class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class Stack(object):

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next_node
        return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.peek() is None

# %load test_stack.py
from nose.tools import assert_equal

class TestStack(object):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print('Test: Empty stack')
        stack = Stack()
        assert_equal(stack.peek(), None)
        assert_equal(stack.pop(), None)

        print('Test: One element')
        top = Node(5)
        stack = Stack(top)
        assert_equal(stack.pop(), 5)
        assert_equal(stack.peek(), None)

        print('Test: More than one element')
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert_equal(stack.pop(), 3)
        assert_equal(stack.peek(), 2)
        assert_equal(stack.pop(), 2)
        assert_equal(stack.peek(), 1)
        assert_equal(stack.is_empty(), False)
        assert_equal(stack.pop(), 1)
        assert_equal(stack.peek(), None)
        assert_equal(stack.is_empty(), True)

        print('Success: test_end_to_end')


def main():
    test = TestStack()
    test.test_end_to_end()


if __name__ == '__main__':
    main()
