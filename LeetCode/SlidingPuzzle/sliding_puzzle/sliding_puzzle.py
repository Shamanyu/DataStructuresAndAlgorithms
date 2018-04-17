class SlidingPuzzle(object):

    def slidingPuzzle(self, boardStateList):
        boardState = ''.join([str(data) for data in (boardStateList[0] + boardStateList[1])])
        swapPositions = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
        visited, step = set(), 0
        currentList, nextList = [boardState], []
        while currentList:
            for element in currentList:
                if element == '123450':
                    return step
                index = element.index('0')
                for position in swapPositions[index]:
                    nextStateList = [character for character in element]
                    nextStateList[index], nextStateList[position] = nextStateList[position], nextStateList[index]
                    nextState = ''.join(nextStateList)
                    if nextState not in visited:
                        visited.add(nextState)
                        nextList.append(nextState)
            currentList, nextList = nextList, list()
            step += 1
        return -1


from nose.tools import assert_equals, assert_raises

class TestSlidingPuzzle(object):

  def testSlidingPuzzle(self):
    slidingPuzzle = SlidingPuzzle()

    assert_equals(slidingPuzzle.slidingPuzzle([[1, 2, 3], [4, 0, 5]]), 1)

    assert_equals(slidingPuzzle.slidingPuzzle([[1, 2, 3], [5, 4, 0]]), -1)

    assert_equals(slidingPuzzle.slidingPuzzle([[4, 1, 2], [5, 0, 3]]), 5)

    assert_equals(slidingPuzzle.slidingPuzzle([[3, 2, 4], [1, 5, 0]]), 14)

    print ("All test cases passed!")


def main():
  testSlidingPuzzle = TestSlidingPuzzle()
  testSlidingPuzzle.testSlidingPuzzle()

if __name__ == '__main__':
  main()
