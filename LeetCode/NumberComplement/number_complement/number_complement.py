class NumberComplement(object):

    def numberComplement(self, num):
        return num ^ ((1<<num.bit_length())-1) 


from nose.tools import assert_equals, assert_raises

class TestNumberComplement(object):

  def testNumberComplement(self):
    numberComplement = NumberComplement()

    assert_equals(numberComplement.numberComplement(5), 2)

    assert_equals(numberComplement.numberComplement(1), 0)

    print ("All test cases passed!")


def main():
  testNumberComplement = TestNumberComplement()
  testNumberComplement.testNumberComplement()

if __name__ == '__main__':
  main()
