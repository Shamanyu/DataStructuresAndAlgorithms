class SwapAdjacentInLRString(object):

  def swapAdjacentInLRString(self, start, end):
    s = [(c, i) for i, c in enumerate(start) if c == 'L' or c == 'R']
    e = [(c, i) for i, c in enumerate(end) if c == 'L' or c == 'R']
    return len(s) == len(e) and all(c1 == c2 and (i1 >= i2 and c1 == 'L' or i1 <= i2 and c1 == 'R') for (c1, i1), (c2, i2) in zip(s,e))


from nose.tools import assert_equals, assert_raises

class TestSwapAdjacentInLRString(object):

  def testSwapAdjacentInLRString(self):
    swapAdjacentInLRString = SwapAdjacentInLRString()

    assert_equals(swapAdjacentInLRString.swapAdjacentInLRString('RXXLRXRXL', 'XRLXXRRLX'), True)

    print ("All test cases passed!")


def main():
  testSwapAdjacentInLRString = TestSwapAdjacentInLRString()
  testSwapAdjacentInLRString.testSwapAdjacentInLRString()

if __name__ == '__main__':
  main()
    
