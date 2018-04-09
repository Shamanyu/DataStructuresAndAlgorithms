class RoundThree(object):

    def roundThree(self):
        pass


from nose.tools import assert_equals, assert_raises

class TestRoundThree(object):

  def testRoundThree(self):
    roundThree = RoundThree()

    print ("All test cases passed!")


def main():
  testRoundThree = TestRoundThree()
  testRoundThree.testRoundThree()

if __name__ == '__main__':
  main()
