class ReverseWordsInString(object):

    def reverseWordsInString(self, string):
        return ' '.join(list(reversed(string.split())))


from nose.tools import assert_equals, assert_raises

class TestReverseWordsInString(object):

  def testReverseWordsInString(self):
    reverseWordsInString = ReverseWordsInString()

    assert_equals(reverseWordsInString.reverseWordsInString("the sky is blue"), "blue is sky the")

    assert_equals(reverseWordsInString.reverseWordsInString(""), "")

    print ("All test cases passed!")


def main():
  testReverseWordsInString = TestReverseWordsInString()
  testReverseWordsInString.testReverseWordsInString()

if __name__ == '__main__':
  main()
