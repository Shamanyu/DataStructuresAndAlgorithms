class UniqueMorseCodeWords(object):

    def __init__(self):
        self.characterToCode = [".-","-...","-.-.","-..",".","..-.","--.",
            "....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
            "...","-","..-","...-",".--","-..-","-.--","--.."]

    def uniqueMorseCodeWords(self, words):
        codeList = list()
        for word in words:
            morseCode = list()
            for character in word:
                morseCode.append(self.characterToCode[ord(character) - ord('a')])
            codeList.append(''.join(morseCode))
        return len(set(codeList))


from nose.tools import assert_equals, assert_raises

class TestUniqueMorseCodeWords(object):

  def testUniqueMorseCodeWords(self):
    uniqueMorseCodeWords = UniqueMorseCodeWords()

    assert_equals(uniqueMorseCodeWords.uniqueMorseCodeWords(["gin", "zen", "gig", "msg"]), 2)

    print ("All test cases passed!")


def main():
  testUniqueMorseCodeWords = TestUniqueMorseCodeWords()
  testUniqueMorseCodeWords.testUniqueMorseCodeWords()

if __name__ == '__main__':
  main()
