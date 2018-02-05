from stack import Node, Stack

class MyStack(Stack):

    def sort(self):
        buffer_stack = Stack()
        while not self.is_empty():
            temp = self.pop()
            if buffer_stack.is_empty() or temp >= self.peek():
                buffer_stack.push(temp)
            else:
                while not buffer_stack.is_empty() and temp < buffer_stack.peek():
                    self.push(buffer_stack.pop())
        return buffer_stack

class MyStackSimplified(Stack):

    def sort(self):
        buffer_stack = Stack()
        while not self.is_empty():
            temp = self.pop()
            while not buffer_stack.is_empty() and temp < buffer_stack.peek():
                self.push(buffer_stack.pop())
            buffer_stack.push(temp)
        return buffer_stack


# %load test_sort_stack.py
from random import randint
from nose.tools import assert_equal

class TestSortStack(object):

    def get_sorted_stack(self, stack, numbers):
        for x in numbers:
            stack.push(x)
        sorted_stack = stack.sort()
        return sorted_stack

    def test_sort_stack(self, stack):
        print('Test: Empty stack')
        sorted_stack = self.get_sorted_stack(stack, [])
        assert_equal(sorted_stack.pop(), None)

        print('Test: One element stack')
        sorted_stack = self.get_sorted_stack(stack, [1])
        assert_equal(sorted_stack.pop(), 1)

        print('Test: Two or more element stack (general case)')
        num_items = 10
        numbers = [randint(0, 10) for x in range(num_items)]
        sorted_stack = self.get_sorted_stack(stack, numbers)
        sorted_numbers = []
        for _ in range(num_items):
            sorted_numbers.append(sorted_stack.pop())
        assert_equal(sorted_numbers, sorted(numbers, reverse=True))

        print('Success: test_sort_stack')


def main():
    test = TestSortStack()
    test.test_sort_stack(MyStack())
    try:
        test.test_sort_stack(MyStackSimplified())
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()
