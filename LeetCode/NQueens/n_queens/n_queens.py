class NQueens(object):

    def solveNQueens(self, n):
        def DFS(queens, xy_dif, xy_sum):
            p = len(queens)
            if p==n:
                result.append(queens)
                return None
            for q in range(n):
                if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                    DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
        result = []
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]


from nose.tools import assert_equals, assert_raises

class TestNQueens(object):

  def testNQueens(self):
    nQueens = NQueens()

    assert_equals(nQueens.solveNQueens(4), [
         [".Q..",
          "...Q",
          "Q...",
          "..Q."],
         ["..Q.",
          "Q...",
          "...Q",
          ".Q.."]
        ]
    )

    print ("All test cases passed!")


def main():
  testNQueens = TestNQueens()
  testNQueens.testNQueens()

if __name__ == '__main__':
  main()
