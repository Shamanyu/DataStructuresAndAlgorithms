class AddBinary(object):

  def addBinary(self, num1, num2):
    return bin(eval('0b'+num1) + eval('0b'+num2))[2:]


from nose.tools import assert_equals, assert_raises

class TestAddBinary(object):

  def testAddBinary(self):
    addBinary = AddBinary()

    assert_equals(addBinary.addBinary('11', '1'), '100')

    print ("All test cases passed!")


def main():
  testAddBinary = TestAddBinary()
  testAddBinary.testAddBinary()

if __name__ == '__main__':
  main()
