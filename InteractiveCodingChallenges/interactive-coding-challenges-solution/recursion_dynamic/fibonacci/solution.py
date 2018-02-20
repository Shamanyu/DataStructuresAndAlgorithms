class Math(object):

    # Time complexity: O(2^n)
    # Space complexity: O(1)
    def fib_iterative(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a, b = 0, 1
        counter = 0
        while (counter < n):
            temp = a
            a = b
            b += temp
            counter += 1
        return a

    # Time complexity: O(2^n)
    # Space complexity: O(n)
    def fib_recursive(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.fib_recursive(n-1) + self.fib_recursive(n-2)

    # Time complexity: O(n)
    # Space complexity: O(n)
    def fib_dynamic(self, n):
        self.fib_table = [None for counter in range(0, n+1)]
        return self._fib_dynamic(n)

    def _fib_dynamic(self, n):
        if self.fib_table[n] is not None:
            return self.fib_table[n]
        else:
            if n in (0, 1):
                self.fib_table[n] = n
            else:
                self.fib_table[n] = self._fib_dynamic(n-1) + self._fib_dynamic(n-2)
            return self.fib_table[n]


# %load test_fibonacci.py
from nose.tools import assert_equal

class TestFib(object):

    def test_fib(self, func):
        result = []
        expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        for i in range(len(expected)):
            result.append(func(i))
        assert_equal(result, expected)
        print('Success: test_fib')


def main():
    test = TestFib()
    math = Math()
    test.test_fib(math.fib_recursive)
    test.test_fib(math.fib_dynamic)
    test.test_fib(math.fib_iterative)


if __name__ == '__main__':
    main()