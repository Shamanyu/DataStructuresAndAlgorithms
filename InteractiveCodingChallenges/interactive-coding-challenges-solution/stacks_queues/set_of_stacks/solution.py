from stack import Node, Stack

class StackWithCapacity(Stack):

    def __init__(self, top=None, capacity=10):
        super(StackWithCapacity, self).__init__(top)
        self.capacity = capacity
        self.current_size = 0

    def push(self, data):
        if self.is_full():
            raise Exception('Stack full')
        super(StackWithCapacity, self).push(data)
        self.current_size += 1

    def pop(self):
        self.current_size -= 1
        return super(StackWithCapacity, self).pop()

    def is_full(self):
        return self.current_size == self.capacity

class SetOfStacks(object):

    def __init__(self, indiv_stack_capacity):
        self.indiv_stack_capacity = indiv_stack_capacity
        self.stacks = list()
        self.last_stack = None

    def push(self, data):
        if self.last_stack is None or self.last_stack.is_full():
            self.last_stack = StackWithCapacity(None, self.indiv_stack_capacity)
            self.stacks.append(self.last_stack)
        self.last_stack.push(data)

    def pop(self):
        if self.last_stack is None:
            return None
        data = self.last_stack.pop()
        if self.last_stack.is_empty():
            self.stacks.pop()
            self.last_stack = self.stacks[-1] if self.stacks else None
        return data


# %load test_set_of_stacks.py
from nose.tools import assert_equal

class TestSetOfStacks(object):

    def test_set_of_stacks(self):
        print('Test: Push on an empty stack')
        stacks = SetOfStacks(indiv_stack_capacity=2)
        stacks.push(3)

        print('Test: Push on a non-empty stack')
        stacks.push(5)

        print('Test: Push on a capacity stack to create a new one')
        stacks.push('a')

        print('Test: Pop on a stack to destroy it')
        assert_equal(stacks.pop(), 'a')

        print('Test: Pop general case')
        assert_equal(stacks.pop(), 5)
        assert_equal(stacks.pop(), 3)

        print('Test: Pop on no elements')
        assert_equal(stacks.pop(), None)

        print('Success: test_set_of_stacks')


def main():
    test = TestSetOfStacks()
    test.test_set_of_stacks()


if __name__ == '__main__':
    main()
