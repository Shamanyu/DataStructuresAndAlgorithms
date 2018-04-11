class RoundFour(object):

    def roundFour(self):
        pass


from nose.tools import assert_equals, assert_raises

class TestRoundFour(object):

  def testRoundFour(self):
    roundFour = RoundFour()

    print ("All test cases passed!")


def main():
  testRoundFour = TestRoundFour()
  testRoundFour.testRoundFour()

if __name__ == '__main__':
  main()
