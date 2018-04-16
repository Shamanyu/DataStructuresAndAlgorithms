class ProductOfArrayExceptSelf(object):

    def productOfArrayExceptSelf(self, nums):
        res = [1]
        prev = 1
        #scan forward
        for i in range(1,len(nums)):
            prev=prev*nums[i-1]
            res.append(prev)
        #scan backward
        prev = 1
        for i in range(len(nums)-2,-1,-1):
            prev = prev*nums[i+1]
            res[i]=res[i]*prev


        return res


from nose.tools import assert_equals, assert_raises

class TestProductOfArrayExceptSelf(object):

  def testProductOfArrayExceptSelf(self):
    productOfArrayExceptSelf = ProductOfArrayExceptSelf()

    assert_equals(productOfArrayExceptSelf.productOfArrayExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    print ("All test cases passed!")


def main():
  testProductOfArrayExceptSelf = TestProductOfArrayExceptSelf()
  testProductOfArrayExceptSelf.testProductOfArrayExceptSelf()

if __name__ == '__main__':
  main()
