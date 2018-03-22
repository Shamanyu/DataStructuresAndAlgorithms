class MedianSortedArrays(object):

  def median_sorted_arrays(self, nums1, nums2):


from nose.tools import assert_equal, assert_raises

class TestMedianSortedArrays(object):

  def test_median_sorted_arrays(self):
    median_sorted_arrays = MedianSortedArrays()
    median_sorted_arrays.median_sorted_arrays()

    print ("All test cases passed")


def main():
  test_median_sorted_arrays = TestMedianSortedArrays()
  test_median_sorted_arrays.test_median_sorted_arrays()

if __name__ == '__main__':
  main()