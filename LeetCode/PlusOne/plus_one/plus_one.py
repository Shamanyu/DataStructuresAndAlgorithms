class PlusOne(object):

  def plusOne(self, digits):
    return [int(x) for x in str(int(''.join(map(str, digits)))+1)]


from nose.tools import assert_equals, assert_raises

class TestPlusOne(object):

  def testPlusOne(self):
    plusOne = PlusOne()

    print ("All test cases passed!")


def main():
  testPlusOne = TestPlusOne()
  testPlusOne.testPlusOne()

if __name__ == '__main__':
  main()
