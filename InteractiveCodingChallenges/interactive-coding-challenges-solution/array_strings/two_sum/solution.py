class Solution(object):

    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def two_sum(self, nums, val):
        if nums is None:
            raise TypeError('None type not allowed')
        if nums == []:
            raise ValueError('Empty array not allowed')
        sorted_nums = sorted(nums)
        low_pointer = 0
        high_pointer = len(sorted_nums) - 1
        current_sum = sorted_nums[low_pointer] + sorted_nums[high_pointer]
        while (current_sum != val and high_pointer > low_pointer):
            if current_sum > val:
                high_pointer -= 1
            else:
                low_pointer += 1
            current_sum = sorted_nums[low_pointer] + sorted_nums[high_pointer]
        low_element = sorted_nums[low_pointer]
        high_element = sorted_nums[high_pointer]
        return [nums.index(low_element), nums.index(high_element)]

    def two_sum_cache(self, nums, target):
        if nums is None or target is None:
            raise TypeError('nums or target cannot be None')
        if not nums:
            raise ValueError('nums cannot be empty')
        cache = {}
        for index, num in enumerate(nums):
            cache_target = target - num
            if num in cache:
                return [cache[num], index]
            else:
                cache[cache_target] = index
        return None


# %load test_two_sum.py
from nose.tools import assert_equal, assert_raises

class TestTwoSum(object):

    def test_two_sum(self):
        solution = Solution()
        assert_raises(TypeError, solution.two_sum, None, None)
        assert_raises(ValueError, solution.two_sum, [], 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        assert_equal(solution.two_sum(nums, target), expected)
        print('Success: test_two_sum')

    def test_two_sum_cache(self):
        solution = Solution()
        assert_raises(TypeError, solution.two_sum_cache, None, None)
        assert_raises(ValueError, solution.two_sum_cache, [], 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        assert_equal(solution.two_sum_cache(nums, target), expected)
        print('Success: test_two_sum_cache')


def main():
    test = TestTwoSum()
    test.test_two_sum()
    test.test_two_sum_cache()


if __name__ == '__main__':
    main()
