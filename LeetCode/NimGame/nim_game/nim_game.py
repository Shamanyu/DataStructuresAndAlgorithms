class NimGame(object):

  def nimGame(self, num):
    return num%4 != 0

from nose.tools import assert_equals, assert_raises

class TestNimGame(object):

  def testNimGame(self):
    nimGame = NimGame()

    assert_equals(nimGame.nimGame(1), True)

    assert_equals(nimGame.nimGame(4), False)

    assert_equals(nimGame.nimGame(5), True)

    print ("All test cases passed!")


def main():
  testNimGame = TestNimGame()
  testNimGame.testNimGame()

if __name__ == '__main__':
  main()
    
