import sys
from stack import Node, Stack

class StackMin(Stack):

    def __init__(self, top=None):
        super(StackMin, self).__init__(top)
        self.minimum_stack = Stack(Node(sys.maxsize))

    def minimum(self):
        return self.minimum_stack.peek()

    def push(self, data):
        current_minimum_element = self.minimum_stack.peek()
        minimum_element = current_minimum_element if (current_minimum_element is not None and current_minimum_element < data) else data
        super(StackMin, self).push(data)
        self.minimum_stack.push(minimum_element)
        print (self.minimum_stack.peek())

    def pop(self):
        self.minimum_stack.pop()
        return super(StackMin, self).pop()


# %load test_stack_min.py
from nose.tools import assert_equal

class TestStackMin(object):

    def test_stack_min(self):
        print('Test: Push on empty stack, non-empty stack')
        stack = StackMin()
        stack.push(5)
        assert_equal(stack.peek(), 5)
        assert_equal(stack.minimum(), 5)
        stack.push(1)
        assert_equal(stack.peek(), 1)
        assert_equal(stack.minimum(), 1)
        stack.push(3)
        assert_equal(stack.peek(), 3)
        assert_equal(stack.minimum(), 1)
        stack.push(0)
        assert_equal(stack.peek(), 0)
        assert_equal(stack.minimum(), 0)

        print('Test: Pop on non-empty stack')
        assert_equal(stack.pop(), 0)
        assert_equal(stack.minimum(), 1)
        assert_equal(stack.pop(), 3)
        assert_equal(stack.minimum(), 1)
        assert_equal(stack.pop(), 1)
        assert_equal(stack.minimum(), 5)
        assert_equal(stack.pop(), 5)
        assert_equal(stack.minimum(), sys.maxsize)

        print('Test: Pop empty stack')
        assert_equal(stack.pop(), None)

        print('Success: test_stack_min')


def main():
    test = TestStackMin()
    test.test_stack_min()


if __name__ == '__main__':
    main()
