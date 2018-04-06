class GrayCode(object):

  def grayCode(self, num):
    pass


from nose.tools import assert_equals, assert_raises

class TestGrayCode(object):

  def testGrayCode(self):
    grayCode = GrayCode()

    assert_equals(grayCode.grayCode(0), [])

    assert_equals(grayCode.grayCode(1), [0, 1])

    assert_equals(grayCode.grayCode(2), [0, 1, 3, 2])

    print ("All test cases passed!")


def main():
  testGrayCode = TestGrayCode()
  testGrayCode.testGrayCode()

if __name__ == '__main__':
  main()
