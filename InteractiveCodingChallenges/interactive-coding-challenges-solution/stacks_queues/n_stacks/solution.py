class Stacks(object):

    def __init__(self, num_stacks, stack_size):
        self.stack_capacity = stack_size
        self.stacks_data = [None for counter in range(num_stacks*stack_size)]
        self.stacks_size = [0 for counter in range(0, num_stacks)]

    def abs_index(self, stack_index):
        return stack_index*self.stack_capacity + self.stacks_size[stack_index]

    def push(self, stack_index, data):
        if self.stacks_size[stack_index] == self.stack_capacity:
            raise Exception
        absolute_index = self.abs_index(stack_index)
        self.stacks_data[absolute_index] = data
        self.stacks_size[stack_index] += 1

    def pop(self, stack_index):
        if self.stacks_size[stack_index] is 0:
            raise Exception
        absolute_index = self.abs_index(stack_index) - 1
        popped_value = self.stacks_data[absolute_index]
        self.stacks_size[stack_index] -= 1
        return popped_value


# %load test_n_stacks.py
from nose.tools import assert_equal
from nose.tools import raises

class TestStacks(object):

    @raises(Exception)
    def test_pop_on_empty(self, num_stacks, stack_size):
        print('Test: Pop on empty stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.pop(0)

    @raises(Exception)
    def test_push_on_full(self, num_stacks, stack_size):
        print('Test: Push to full stack')
        stacks = Stacks(num_stacks, stack_size)
        for i in range(0, stack_size):
            stacks.push(2, i)
        stacks.push(2, stack_size)

    def test_stacks(self, num_stacks, stack_size):
        print('Test: Push to non-full stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.push(0, 1)
        stacks.push(0, 2)
        stacks.push(1, 3)
        stacks.push(2, 4)

        print('Test: Pop on non-empty stack')
        assert_equal(stacks.pop(0), 2)
        assert_equal(stacks.pop(0), 1)
        assert_equal(stacks.pop(1), 3)
        assert_equal(stacks.pop(2), 4)

        print('Success: test_stacks\n')


def main():
    num_stacks = 3
    stack_size = 100
    test = TestStacks()
    test.test_pop_on_empty(num_stacks, stack_size)
    test.test_push_on_full(num_stacks, stack_size)
    test.test_stacks(num_stacks, stack_size)


if __name__ == '__main__':
    main()
