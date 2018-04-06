class CountSay(object):

  def countSay(self, n):
      if n < 1:
          raise ValueError('Input should be greater than or equal to 1')
      elif n == 1:
          return '1'
      currentCharacter = ''
      currentCharacterCount = 0
      result = list()
      for character in list(self.countSay(n-1)):
          if character != currentCharacter:
              if currentCharacter != '':
                  result.extend([str(currentCharacterCount), currentCharacter])
              currentCharacter = character
              currentCharacterCount = 1
          else:
              currentCharacterCount += 1
      result.extend([str(currentCharacterCount), currentCharacter])
      return ''.join(result)


from nose.tools import assert_equals, assert_raises

class TestCountSay(object):

  def testCountSay(self):
    countSay = CountSay()

    assert_equals(countSay.countSay(1), '1')

    assert_equals(countSay.countSay(2), '11')

    assert_equals(countSay.countSay(3), '21')

    assert_equals(countSay.countSay(4), '1211')

    assert_equals(countSay.countSay(5), '111221')

    print ("All test cases passed!")


def main():
  testCountSay = TestCountSay()
  testCountSay.testCountSay()

if __name__ == '__main__':
  main()
