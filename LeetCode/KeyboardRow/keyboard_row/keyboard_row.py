class KeyboardRow(object):

    def __init__(self):
        self.rows = [
            set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']),
            set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']),
            set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        ]

    def findWords(self, words):
        result = list()
        for word in words:
            rowsUsed = set()
            for character in word:
                for counter, row in enumerate(self.rows):
                    if character.lower() in row:
                        rowsUsed.add(counter)
            if len(rowsUsed) <= 1:
                result.append(word)
        return result


from nose.tools import assert_equals, assert_raises

class TestKeyboardRow(object):

  def testKeyboardRow(self):
    keyboardRow = KeyboardRow()

    assert_equals(keyboardRow.findWords(["Hello", "Alaska", "Dad", "Peace"]),
        ["Alaska", "Dad"]
    )

    print ("All test cases passed!")


def main():
  testKeyboardRow = TestKeyboardRow()
  testKeyboardRow.testKeyboardRow()

if __name__ == '__main__':
  main()
