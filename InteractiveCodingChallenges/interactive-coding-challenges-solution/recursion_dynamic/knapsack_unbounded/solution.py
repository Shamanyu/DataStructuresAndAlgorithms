class Item(object):

    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)


class Knapsack(object):

    # Time complexity: O(n*w); where 'n' is the number of items and 'w' is the total weight
    # Space complexity: O(w); where 'w' is the total weight
    def fill_knapsack(self, input_items, total_weight):
        if None in (input_items, total_weight):
            raise TypeError('input_items or total_weight cannot be None')
        self.T = [None for counter in range(total_weight+1)]
        return self._fill_knapsack(input_items, total_weight)

    def _fill_knapsack(self, input_items, total_weight):
        if not input_items or total_weight == 0:
            return 0
        overall_maximum_value = 0
        for input_item in input_items:
            if input_item.weight <= total_weight:
                remaining_weight = total_weight - input_item.weight
                if remaining_weight in self.T:
                    maximum_remaining_value = self.T[remaining_weight]
                else:
                    maximum_remaining_value = \
                      self._fill_knapsack(input_items, total_weight-input_item.weight)
                maximum_value = input_item.value + maximum_remaining_value
                if maximum_value > overall_maximum_value:
                    overall_maximum_value = maximum_value
        self.T[total_weight] = overall_maximum_value
        return overall_maximum_value


# %load test_knapsack_unbounded.py
from nose.tools import assert_equal, assert_raises

class TestKnapsack(object):

    def test_knapsack(self):
        knapsack = Knapsack()
        assert_raises(TypeError, knapsack.fill_knapsack, None, None)
        assert_equal(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=1, weight=1))
        items.append(Item(label='b', value=3, weight=2))
        items.append(Item(label='c', value=7, weight=4))
        total_weight = 8
        expected_value = 14
        results = knapsack.fill_knapsack(items, total_weight)
        assert_equal(results, expected_value)
        total_weight = 7
        expected_value = 11
        results = knapsack.fill_knapsack(items, total_weight)
        assert_equal(results, expected_value)
        print('Success: test_knapsack')

def main():
    test = TestKnapsack()
    test.test_knapsack()


if __name__ == '__main__':
    main()