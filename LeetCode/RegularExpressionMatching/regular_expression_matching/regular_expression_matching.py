class RegularExpressionMatching(object):

  # Without Kleene star
  # def regularExpressionMatching(self, string, pattern):
  #   if not pattern:
  #     return not string
  #   first_match = bool(string) and pattern[0] in {string[0], '.'}
  #   return first_match and self.regularExpressionMatching(string[1:], pattern[1:])

  # With Kleene star
  # def regularExpressionMatching(self, string, pattern):
  #   if not pattern:
  #     return not string
  #   first_match = bool(string) and pattern[0] in {string[0], '.'}
  #   if len(pattern) >= 2 and pattern[1] == '*':
  #     return (self.regularExpressionMatching(string, pattern[2:]) or 
  #       first_match and self.regularExpressionMatching(string[1:], pattern))
  #   else:
  #     return first_match and self.regularExpressionMatching(string[1:], pattern[1:])

  # With Kleene star and memoization
  def regularExpressionMatching(self, string, pattern):
    self.memo = {}
    return  self._regularExpressionMatching(string, 0, pattern, 0)

  def _regularExpressionMatching(self, string, i, pattern, j):
    if (i, j) not in self.memo:
      if j == len(pattern):
        ans = i == len(string)
      else:
        first_match = i < len(pattern) and pattern[j] in {string[i], '.'}
        if j+1 < len(pattern) and pattern[j+1] == '*':
          ans = self._regularExpressionMatching(string, i, pattern, j+2) or first_match and self._regularExpressionMatching(string, i+1, pattern, j)
        else:
          ans = first_match and self._regularExpressionMatching(string, i+1, pattern, j+1)
      self.memo[i, j] = ans
    return self.memo[i, j]


from nose.tools import assert_equals, assert_raises

class TestRegularExpressionMatching(object):

  def testRegularExpressionMatching(self):
    regularExpressionMatching = RegularExpressionMatching()

    assert_equals(regularExpressionMatching.regularExpressionMatching("aa", "a"), False)

    assert_equals(regularExpressionMatching.regularExpressionMatching("aa", "aa"), True)

    assert_equals(regularExpressionMatching.regularExpressionMatching("aaa", "a"), False)

    assert_equals(regularExpressionMatching.regularExpressionMatching("aa", "a*"), True)

    assert_equals(regularExpressionMatching.regularExpressionMatching("aa", ".*"), True)

    assert_equals(regularExpressionMatching.regularExpressionMatching("ab", ".*"), True)

    assert_equals(regularExpressionMatching.regularExpressionMatching("aab", "c*a*b"), True)

    print ("All test cases passed!")


def main():
  testRegularExpressionMatching = TestRegularExpressionMatching()
  testRegularExpressionMatching.testRegularExpressionMatching()

if __name__ == '__main__':
  main()
    
