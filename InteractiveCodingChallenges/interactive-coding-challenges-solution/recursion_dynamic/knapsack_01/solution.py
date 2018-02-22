class Item(object):

    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)


class Knapsack(object):

    # Time complexity: O(n*w)
    # Space complexity: O(n*w)
    def fill_knapsack(self, input_items, total_weight):
        if None in (input_items, total_weight):
            raise TypeError('input_items and total_weight cant be None')
        if not input_items or total_weight == 0:
            return 0
        items = list([Item(label='', value=0, weight=0)] + input_items)
        num_rows = len(items)
        num_cols = total_weight + 1
        T = [[None] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0 or j == 0:
                    T[i][j] = 0
                elif j >= items[i].weight:
                    T[i][j] = max(items[i].value + T[i-1][j - items[i].weight],
                      T[i-1][j])
                else:
                    T[i][j] = T[i-1][j]
        results = list()
        i = num_rows - 1
        j = num_cols - 1
        while T[i][j] != 0:
            if T[i-1][j] == T[i][j]:
                i -= 1
            elif T[i][j-1] == T[i][j]:
                j -= 1
            else:
                results.append(items[i])
                i -= 1
                j -= items[i].weight
        return results



# %load test_knapsack.py
from nose.tools import assert_equal, assert_raises

class TestKnapsack(object):

    def test_knapsack_bottom_up(self):
        knapsack = Knapsack()
        assert_raises(TypeError, knapsack.fill_knapsack, None, None)
        assert_equal(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=2, weight=2))
        items.append(Item(label='b', value=4, weight=2))
        items.append(Item(label='c', value=6, weight=4))
        items.append(Item(label='d', value=9, weight=5))
        total_weight = 8
        expected_value = 13
        results = knapsack.fill_knapsack(items, total_weight)
        assert_equal(results[0].label, 'd')
        assert_equal(results[1].label, 'b')
        total_value = 0
        for item in results:
            total_value += item.value
        assert_equal(total_value, expected_value)
        print('Success: test_knapsack_bottom_up')

    def test_knapsack_top_down(self):
        knapsack = KnapsackTopDown()
        assert_raises(TypeError, knapsack.fill_knapsack, None, None)
        assert_equal(knapsack.fill_knapsack(0, 0), 0)
        items = []
        items.append(Item(label='a', value=2, weight=2))
        items.append(Item(label='b', value=4, weight=2))
        items.append(Item(label='c', value=6, weight=4))
        items.append(Item(label='d', value=9, weight=5))
        total_weight = 8
        expected_value = 13
        assert_equal(knapsack.fill_knapsack(items, total_weight), expected_value)
        print('Success: test_knapsack_top_down')

def main():
    test = TestKnapsack()
    test.test_knapsack_bottom_up()
    # test.test_knapsack_top_down()


if __name__ == '__main__':
    main()
