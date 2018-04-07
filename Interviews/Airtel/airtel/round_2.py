class RoundTwo(object):

    def __init__(self, dictionaryElements):
        self.dictionaryData = list()
        for element in dictionaryElements:
            self.dictionaryData.append(element)
        self.calculatedData = dict()

    def roundTwo(self, string):
        if string in self.dictionaryData:
            return True

        if len(string) in (0, 1):
            return False

        if string not in self.calculatedData:
            brokenStrings = self._getBrokenStrings(string)
            self.calculatedData[string] = False
            for stringPair in brokenStrings:
                [prefix, suffix] = stringPair
                if (self.roundTwo(prefix) and self.roundTwo(suffix)):
                    self.calculatedData[string] = True
            return self.calculatedData[string]

        return False

    def _getBrokenStrings(self, string):
        if string is None:
            return []
        brokenStrings = list()
        for counter in range(0, len(string)):
            brokenStrings.append([string[0:counter+1], string[counter+1:len(string)]])
        return brokenStrings


from nose.tools import assert_equals, assert_raises

class TestRoundTwo(object):

  def testRoundTwo(self):
    roundTwo = RoundTwo(['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice',
        'cream', 'icecream', 'man', 'go', 'mango'])

    # assert_equals(roundTwo.roundTwo('ilike'), True)

    print (roundTwo.roundTwo('manlikemango'))

    # assert_equals(roundTwo.roundTwo('ilikesamsung'), True)

    # assert_equals(roundTwo.roundTwo('ilikesamsun'), False)

    # assert_equals(roundTwo.roundTwo('likei'), True)

    # assert_equals(roundTwo.roundTwo('liki'), False)

    # print ("All test cases passed!")


def main():
  testRoundTwo = TestRoundTwo()
  testRoundTwo.testRoundTwo()

if __name__ == '__main__':
  main()
