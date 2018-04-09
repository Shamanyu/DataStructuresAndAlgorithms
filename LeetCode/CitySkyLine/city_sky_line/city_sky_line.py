class CitySkyLine(object):

    def citySkyLine(self, buildingHeights):

        rowLimits = [0 for counter in range(len(buildingHeights))]
        columnLimits = [0 for counter in range(len(buildingHeights[0]))]

        for rowCounter, _ in enumerate(buildingHeights):
            for columnCounter, _ in enumerate(buildingHeights[rowCounter]):
                if buildingHeights[rowCounter][columnCounter] > rowLimits[rowCounter]:
                    rowLimits[rowCounter] = buildingHeights[rowCounter][columnCounter]
                if buildingHeights[rowCounter][columnCounter] > columnLimits[columnCounter]:
                    columnLimits[columnCounter] = buildingHeights[rowCounter][columnCounter]

        maxIncreaseInHeightPossible = 0
        for rowCounter, _ in enumerate(buildingHeights):
            for columnCounter, _ in enumerate(buildingHeights[rowCounter]):
                maxIncreaseInHeightPossible += \
                    (min(rowLimits[rowCounter], columnLimits[columnCounter]) -
                    (buildingHeights[rowCounter][columnCounter]))

        return maxIncreaseInHeightPossible


from nose.tools import assert_equals, assert_raises

class TestCitySkyLine(object):

  def testCitySkyLine(self):
    citySkyLine = CitySkyLine()

    assert_equals(citySkyLine.citySkyLine([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]), 35)

    print ("All test cases passed!")


def main():
  testCitySkyLine = TestCitySkyLine()
  testCitySkyLine.testCitySkyLine()

if __name__ == '__main__':
  main()
