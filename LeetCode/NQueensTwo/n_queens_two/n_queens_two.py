class NQueensTwo(object):

    def totalNQueens(self, n):
        self.res = 0
        self.dfs([-1]*n, 0)
        return self.res

    def dfs(self, nums, index):
        if index == len(nums):
            self.res += 1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.valid(nums, index):
                self.dfs(nums, index+1)

    def valid(self, nums, n):
        for i in range(n):
            if nums[i] == nums[n] or abs(nums[n]-nums[i]) == n-i:
                return False
        return True


from nose.tools import assert_equals, assert_raises

class TestNQueensTwo(object):

  def testNQueensTwo(self):
    nQueensTwo = NQueensTwo()

    assert_equals(nQueensTwo.totalNQueens(4), 2)

    print ("All test cases passed!")


def main():
  testNQueensTwo = TestNQueensTwo()
  testNQueensTwo.testNQueensTwo()

if __name__ == '__main__':
  main()
