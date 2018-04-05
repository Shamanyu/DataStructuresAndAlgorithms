class TrapRainWater(object):

    def trapRainWater(self, barHeights):
        if barHeights == []:
            return 0

        numberOfBars = len(barHeights)

        leftMaxima = [0 for counter in range(numberOfBars)]
        rightMaxima = [0 for counter in range(numberOfBars)]

        leftMaxima[0] = barHeights[0]
        for counter in range(1, numberOfBars):
            leftMaxima[counter] = max(leftMaxima[counter-1], barHeights[counter])

        rightMaxima[numberOfBars-1] = barHeights[numberOfBars-1]
        for counter in range(numberOfBars-2, -1, -1):
            rightMaxima[counter] = max(rightMaxima[counter+1], barHeights[counter])

        waterTrapped = 0
        for counter in range(0, numberOfBars):
            waterTrapped += (min(leftMaxima[counter], rightMaxima[counter]) - barHeights[counter])

        return waterTrapped


from nose.tools import assert_equals, assert_raises

class TestTrapRainWater(object):

  def testTrapRainWater(self):
    trapRainWater = TrapRainWater()

    assert_equals(trapRainWater.trapRainWater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    print ("All test cases passed!")


def main():
  testTrapRainWater = TestTrapRainWater()
  testTrapRainWater.testTrapRainWater()

if __name__ == '__main__':
  main()
