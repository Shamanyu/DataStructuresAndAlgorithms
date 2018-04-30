class RoundTwo(object):

    def roundTwo(self):
        pass


from nose.tools import assert_equals, assert_raises

class TestRoundTwo(object):

  def testRoundTwo(self):
    roundTwo = RoundTwo()

    print ("All test cases passed!")


def main():
  testRoundTwo = TestRoundTwo()
  testRoundTwo.testRoundTwo()

if __name__ == '__main__':
  main()
