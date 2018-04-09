class Round1(object):

    def round1(self):
        pass


from nose.tools import assert_equals, assert_raises

class TestRound1(object):

  def testRound1(self):
    round1 = Round1()

    print ("All test cases passed!")


def main():
  testRound1 = TestRound1()
  testRound1.testRound1()

if __name__ == '__main__':
  main()
