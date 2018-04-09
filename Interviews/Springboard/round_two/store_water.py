class StoreWater(object):

  def storeWater(self, barHeights):
    
    numberOfBars = len(barHeights)
    waterStored = 0

    leftMaxima = [0]*numberOfBars
    rightMaxima = [0]*numberOfBars
 
    leftMaxima[0] = barHeights[0]
    for counter in range(1, numberOfBars):
        leftMaxima[counter] = max(leftMaxima[counter-1], barHeights[counter])
 
    rightMaxima[numberOfBars-1] = barHeights[numberOfBars-1]
    for counter in range(numberOfBars-2, -1, -1):
        rightMaxima[counter] = max(rightMaxima[counter+1], barHeights[counter]);
 
    for counter in range(0, numberOfBars):
        waterStored += min(leftMaxima[counter],rightMaxima[counter]) - barHeights[counter]
 
    return waterStored


from nose.tools import assert_equals, assert_raises

class TestStoreWater(object):

  def testStoreWater(self):
    storeWater = StoreWater()

    assert_equals(storeWater.storeWater([1, 2, 3]), 0)

    assert_equals(storeWater.storeWater([4, 1, 0, 1, 3, 4]), 11)

    assert_equals(storeWater.storeWater([4, 1, 0, 1, 3, 4, 2, 1, 2]), 12)

    assert_equals(storeWater.storeWater([2, 1, 2, 4, 1, 0, 1, 3, 4, 2, 1, 2]), 13)

    assert_equals(storeWater.storeWater([1, 2, 3, 3, 2, 1]), 0)

    print ("All test cases passed!")


def main():
  testStoreWater = TestStoreWater()
  testStoreWater.testStoreWater()

if __name__ == '__main__':
  main()
    
