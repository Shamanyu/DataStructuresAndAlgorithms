class LengthLastWord(object):

    def lengthLastWord(self, sentence):
        words = [word for word in sentence.split(' ') if word is not '']
        if words == []:
            return 0
        return len(words[-1])


from nose.tools import assert_equals, assert_raises

class TestLengthLastWord(object):

  def testLengthLastWord(self):
    lengthLastWord = LengthLastWord()

    assert_equals(lengthLastWord.lengthLastWord("Hello World"), 5)

    assert_equals(lengthLastWord.lengthLastWord("a"), 1)

    assert_equals(lengthLastWord.lengthLastWord("a "), 1)

    assert_equals(lengthLastWord.lengthLastWord("    "), 0)

    print ("All test cases passed!")


def main():
  testLengthLastWord = TestLengthLastWord()
  testLengthLastWord.testLengthLastWord()

if __name__ == '__main__':
  main()
