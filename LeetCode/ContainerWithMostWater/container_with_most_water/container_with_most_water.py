from typing import List


class ContainerWithMostWater(object):

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_water = 0
        while left < right:
            size = min(height[left], height[right])
            max_water = max(max_water, size*(right-left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water


from nose.tools import assert_equals, assert_raises


class TestContainerWithMostWater(object):

    def test_container_with_most_water(self):
        container_with_most_water_instance = ContainerWithMostWater()

        print("All test cases passed!")


def main():
    test_container_with_most_water_instance = TestContainerWithMostWater()
    test_container_with_most_water_instance.test_container_with_most_water()


if __name__ == '__main__':
    main()
