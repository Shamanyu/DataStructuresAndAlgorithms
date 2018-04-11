class HammingDistance(object):

    def hammingDistance(self, num1, num2):

        hammingDistance = 0
        while (num1 > 0 and num2 > 0):
            num1Tail = num1 & 1
            num2Tail = num2 & 1
            if num1Tail != num2Tail:
                hammingDistance += 1
            num1 = num1 >> 1
            num2 = num2 >> 1
        while (num1 > 0):
            num1Tail = num1 & 1
            if num1Tail == 1:
                hammingDistance += 1
            num1 = num1 >> 1
        while (num2 > 0):
            num2Tail = num2 & 1
            if num2Tail == 1:
                hammingDistance += 1
            num2 = num2 >> 1

        return hammingDistance

        # One line solution
        #return bin(x^y).count('1')


from nose.tools import assert_equals, assert_raises

class TestHammingDistance(object):

  def testHammingDistance(self):
    hammingDistance = HammingDistance()

    assert_equals(hammingDistance.hammingDistance(1, 4), 2)

    print ("All test cases passed!")


def main():
  testHammingDistance = TestHammingDistance()
  testHammingDistance.testHammingDistance()

if __name__ == '__main__':
  main()
