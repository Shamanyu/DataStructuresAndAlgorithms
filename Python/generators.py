class FirstN(object):

    def get_firstN(self, n):
        num, nums = 0, []
        while num < n:
            nums.append(num)
            num += 1
        return nums

    def get_firstN_using_generators(self, n):
        num = 0
        while num < n:
            yield num
            num += 1

from nose.tools import assert_equal
class TestFirstN(object):

    def test_firstN(self, func):
        assert_equal(func(1), [0])

    def test_sum_firstN(self, func):
        print ("Sum is ", sum(func(100000000)))

def main():
    firstN = FirstN()
    testFirstN = TestFirstN()
    testFirstN.test_firstN(firstN.get_firstN)
    # testFirstN.test_firstN(firstN.get_firstN_using_generators)
    # testFirstN.test_sum_firstN(firstN.get_firstN)
    testFirstN.test_sum_firstN(firstN.get_firstN_using_generators)


if __name__ == '__main__':
    main()
