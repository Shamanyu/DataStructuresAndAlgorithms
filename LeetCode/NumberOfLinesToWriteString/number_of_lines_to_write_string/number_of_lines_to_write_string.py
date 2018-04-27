class NumberOfLinesToWriteString(object):

    def __init__(self, lineWidth=100):
        self.lineWidth = lineWidth

    def numberOfLines(self, widths, S):
        linesNeeded = 1
        widthAvailable = self.lineWidth
        for character in S:
            arrayPosition = self.__characterToArrayPosition__(character)
            widthNeeded = widths[arrayPosition]
            if widthNeeded > widthAvailable:
                linesNeeded += 1
                widthAvailable = self.lineWidth
            widthAvailable -= widthNeeded
        return [linesNeeded, self.lineWidth-widthAvailable]

    def __characterToArrayPosition__(self, character):
        return (ord(character) - ord('a'))

from nose.tools import assert_equals, assert_raises

class TestNumberOfLinesToWriteString(object):

  def testNumberOfLinesToWriteString(self):
    numberOfLinesToWriteString = NumberOfLinesToWriteString()

    assert_equals(numberOfLinesToWriteString.numberOfLines(
        [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        'abcdefghijklmnopqrstuvwxyz'),
        [3, 60]
    )

    assert_equals(numberOfLinesToWriteString.numberOfLines(
        [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
        'bbbcccdddaaa'),
        [2, 4]
    )

    print ("All test cases passed!")


def main():
  testNumberOfLinesToWriteString = TestNumberOfLinesToWriteString()
  testNumberOfLinesToWriteString.testNumberOfLinesToWriteString()

if __name__ == '__main__':
  main()
