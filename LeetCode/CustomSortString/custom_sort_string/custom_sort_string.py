class CustomSortString(object):

    def customSortString(self, S, T):
        return ''.join(sorted(T, key = lambda x: S.index(x) if x in S else -1))


from nose.tools import assert_equals, assert_raises

class TestCustomSortString(object):

  def testCustomSortString(self):
    customSortString = CustomSortString()

    assert_equals(customSortString.customSortString('cba', 'abcd'), 'dcba')

    print ("All test cases passed!")


def main():
  testCustomSortString = TestCustomSortString()
  testCustomSortString.testCustomSortString()

if __name__ == '__main__':
  main()
