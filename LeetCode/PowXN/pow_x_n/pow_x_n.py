class PowXN(object):

  def powXN(self, X, N):
    self.memo = dict()
    if N < 0:
      X = 1/X
      N = abs(N)
    return self._powXN(X, N)

  def _powXN(self, X, N):
    if N not in self.memo:
      if N == 0:
        return 1
      elif N == 1:
        return X
      else:
        if N % 2 == 0:
          self.memo[N] = self._powXN(X, N//2)*self._powXN(X, N//2)
        else:
          self.memo[N] = self._powXN(X, N//2)*self._powXN(X, N//2)*self._powXN(X, 1)
    return round(self.memo[N], 5)


from nose.tools import assert_equals, assert_raises

class TestPowXN(object):

  def testPowXN(self):
    powXN = PowXN()

    assert_equals(powXN.powXN(2.00000, 10), 1024.00000)

    assert_equals(powXN.powXN(2.10000, 3), 9.26100)

    print ("All test cases passed!")


def main():
  testPowXN = TestPowXN()
  testPowXN.testPowXN()

if __name__ == '__main__':
  main()
    
