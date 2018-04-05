class StringToInteger(object):

    def stringToInteger(self, str):
        str = str.strip()
        str = re.findall('^[+\-]?\d+', str)

        try:
            res = int(''.join(str))
            MAX = 2147483647
            MIN = -2147483648
            if res > MAX:
                return MAX
            if res < MIN:
                return MIN
            return res
        except:
            return 0


from nose.tools import assert_equals, assert_raises

class TestStringToInteger(object):

  def testStringToInteger(self):
    stringToInteger = StringToInteger()

    assert_equals(stringToInteger.stringToInteger('123'), 123)

    print ("All test cases passed!")


def main():
  testStringToInteger = TestStringToInteger()
  testStringToInteger.testStringToInteger()

if __name__ == '__main__':
  main()
