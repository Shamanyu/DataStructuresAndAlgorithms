class CoupleHoldingHands(object):

    def minSwapsCouples(self, seatArrangement):
        minSwaps = 0
        positionDict = [-1 for counter in range(len(seatArrangement))]

        for counter in range(len(seatArrangement)):
            positionDict[seatArrangement[counter]] = counter

        for counter in range(len(seatArrangement)):
            innerCounter = self.getPartner(positionDict[self.getPartner(seatArrangement[counter])])
            while (innerCounter != counter):
                seatArrangement[counter], seatArrangement[innerCounter] = seatArrangement[innerCounter], seatArrangement[counter]
                positionDict[seatArrangement[counter]], positionDict[seatArrangement[innerCounter]] = \
                    positionDict[seatArrangement[innerCounter]], positionDict[seatArrangement[counter]]
                minSwaps += 1
                innerCounter = self.getPartner(positionDict[self.getPartner(seatArrangement[counter])])

        return minSwaps


    def getPartner(self, person):
        if person%2 == 0:
            return person+1
        else:
            return person-1

from nose.tools import assert_equals, assert_raises

class TestCoupleHoldingHands(object):

  def testCoupleHoldingHands(self):
    coupleHoldingHands = CoupleHoldingHands()

    assert_equals(coupleHoldingHands.minSwapsCouples([0, 1, 2, 3]), 0)

    assert_equals(coupleHoldingHands.minSwapsCouples([0, 2, 1, 3]), 1)

    assert_equals(coupleHoldingHands.minSwapsCouples([3, 2, 0, 1]), 0)

    assert_equals(coupleHoldingHands.minSwapsCouples([5, 4, 2, 6, 3, 1, 0, 7]), 2)

    print ("All test cases passed!")


def main():
  testCoupleHoldingHands = TestCoupleHoldingHands()
  testCoupleHoldingHands.testCoupleHoldingHands()

if __name__ == '__main__':
  main()
