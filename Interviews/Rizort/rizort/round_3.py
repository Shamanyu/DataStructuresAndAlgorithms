class Round3(object):

    def round3(self):
        pass


from nose.tools import assert_equals, assert_raises

class TestRound3(object):

  def testRound3(self):
    round3 = Round3()

    print ("All test cases passed!")


def main():
  testRound3 = TestRound3()
  testRound3.testRound3()

if __name__ == '__main__':
  main()
