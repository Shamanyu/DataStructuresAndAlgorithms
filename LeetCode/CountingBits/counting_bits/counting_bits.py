class CountingBits(object):

    def countingBits(self, num):
        result = [0]
        while len(result) <= num:
            result += [bitCount+1 for bitCount in result]
        return result[:num+1]


from nose.tools import assert_equals, assert_raises

class TestCountingBits(object):

  def testCountingBits(self):
    countingBits = CountingBits()

    assert_equals(countingBits.countingBits(5), [0, 1, 1, 2, 1, 2])

    print ("All test cases passed!")


def main():
  testCountingBits = TestCountingBits()
  testCountingBits.testCountingBits()

if __name__ == '__main__':
  main()
