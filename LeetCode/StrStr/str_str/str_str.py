class StrStr(object):

  def strStr(self, haystack, needle):
    # Implement KMP
    return haystack.find(needle)


from nose.tools import assert_equals, assert_raises

class TestStrStr(object):

  def testStrStr(self):
    strStr = StrStr()

    assert_equals(strStr.strStr("hello", "ll"), 2)

    assert_equals(strStr.strStr("aaaaa", "bba"), -1)

    print ("All test cases passed!")


def main():
  testStrStr = TestStrStr()
  testStrStr.testStrStr()

if __name__ == '__main__':
  main()
    
