import math

class BulbSwitcher(object):

  def bulbSwitcher(self, n):
    return math.floor(math.sqrt(n))


from nose.tools import assert_equals, assert_raises

class TestBulbSwitcher(object):

  def testBulbSwitcher(self):
    bulbSwitcher = BulbSwitcher()

    assert_equals(bulbSwitcher.bulbSwitcher(3), 1)

    print ("All test cases passed!")


def main():
  testBulbSwitcher = TestBulbSwitcher()
  testBulbSwitcher.testBulbSwitcher()

if __name__ == '__main__':
  main()
    
