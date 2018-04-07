class RoundOne(object):

    def roundOne(self):
        pass


from nose.tools import assert_equals, assert_raises

class TestRoundOne(object):

  def testRoundOne(self):
    roundOne = RoundOne()

    print ("All test cases passed!")


def main():
  testRoundOne = TestRoundOne()
  testRoundOne.testRoundOne()

if __name__ == '__main__':
  main()
