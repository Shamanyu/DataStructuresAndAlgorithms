class BestTimeToBuyAndSellStocks(object):

  def bestTimeToBuyAndSellStocks(self, prices):
    maxProfit = 0
    minPrice = float('inf')
    for price in prices:
        if price - minPrice > maxProfit:
            maxProfit = price - minPrice
        if price < minPrice:
            minPrice = price
    return maxProfit


from nose.tools import assert_equals, assert_raises

class TestBestTimeToBuyAndSellStocks(object):

  def testBestTimeToBuyAndSellStocks(self):
    bestTimeToBuyAndSellStocks = BestTimeToBuyAndSellStocks()

    assert_equals(bestTimeToBuyAndSellStocks.bestTimeToBuyAndSellStocks([7, 1, 5, 3, 6, 4]), 5)

    assert_equals(bestTimeToBuyAndSellStocks.bestTimeToBuyAndSellStocks([7, 6, 4, 3, 1]), 0)

    print ("All test cases passed!")


def main():
  testBestTimeToBuyAndSellStocks = TestBestTimeToBuyAndSellStocks()
  testBestTimeToBuyAndSellStocks.testBestTimeToBuyAndSellStocks()

if __name__ == '__main__':
  main()
