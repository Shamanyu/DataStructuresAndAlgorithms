class ShortestDistanceToCharacter(object):

    def shortestDistanceToCharacter(self, S, C):
        result = [None for counter in range(len(S))]
        characterList = list(S)
        lastCPosition = None
        for counter, character in enumerate(characterList):
            if character != C:
                if lastCPosition != None:
                    result[counter] = counter - lastCPosition
                else:
                    result[counter] = None
            else:
                if lastCPosition != None:
                    reEvaluationStartPosition = (counter+lastCPosition)//2 + 1
                else:
                    reEvaluationStartPosition = 0
                lastCPosition = counter
                for innerCounter in range(reEvaluationStartPosition, counter+1):
                    result[innerCounter] = lastCPosition - innerCounter
        return result


from nose.tools import assert_equals, assert_raises

class TestShortestDistanceToCharacter(object):

  def testShortestDistanceToCharacter(self):
    shortestDistanceToCharacter = ShortestDistanceToCharacter()

    assert_equals(shortestDistanceToCharacter.shortestDistanceToCharacter('loveleetcode', 'e'), [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0])

    print ("All test cases passed!")


def main():
  testShortestDistanceToCharacter = TestShortestDistanceToCharacter()
  testShortestDistanceToCharacter.testShortestDistanceToCharacter()

if __name__ == '__main__':
  main()
