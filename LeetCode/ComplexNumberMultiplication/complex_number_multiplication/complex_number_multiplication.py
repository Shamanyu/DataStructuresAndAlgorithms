import re

class ComplexNumberMultiplication(object):

    def complexNumberMultiplication(self, num1, num2):
        [_, signA, a, signB, b, _] = (re.split('([-]?)([0-9]+)[+]([-]?)([0-9]+)i', num1))
        [_, signC, c, signD, d, _] = (re.split('([-]?)([0-9]+)[+]([-]?)([0-9]+)i', num2))
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        if signA == '-':
            a *= -1
        if signB == '-':
            b *= -1
        if signC == '-':
            c *= -1
        if signD == '-':
            d *= -1
        realPart = (a*c)-(b*d)
        imaginaryPart = (a*d)+(b*c)
        return str(realPart)+'+'+str(imaginaryPart)+'i'

        # Best solution
        # a1, a2 = map(int, a[:-1].split('+'))
        # b1, b2 = map(int, b[:-1].split('+'))
        # return '%d+%di' % (a1 * b1 - a2 * b2, a1 * b2 + a2 * b1)

from nose.tools import assert_equals, assert_raises

class TestComplexNumberMultiplication(object):

  def testComplexNumberMultiplication(self):
    complexNumberMultiplication = ComplexNumberMultiplication()

    assert_equals(complexNumberMultiplication.complexNumberMultiplication('1+1i', '1+1i'), '0+2i')

    assert_equals(complexNumberMultiplication.complexNumberMultiplication('1+-1i', '1+-1i'), '0+-2i')

    assert_equals(complexNumberMultiplication.complexNumberMultiplication('1+-1i', '0+0i'), '0+0i')

    assert_equals(complexNumberMultiplication.complexNumberMultiplication('78+-76i', '-86+72i'), '-1236+12152i')

    print ("All test cases passed!")


def main():
  testComplexNumberMultiplication = TestComplexNumberMultiplication()
  testComplexNumberMultiplication.testComplexNumberMultiplication()

if __name__ == '__main__':
  main()
