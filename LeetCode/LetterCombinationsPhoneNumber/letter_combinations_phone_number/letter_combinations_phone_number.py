class LetterCombinationsPhoneNumber(object):

    def letterCombinationsPhoneNumber(self, digits):
        phone = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        if(len(digits) == 0):
            return []
        answer = [""]
        for digit in digits:
            outside_answer = answer[:]
            for letter in phone[digit]:
                for ans in outside_answer:
                    answer.append(ans + letter)

        return [x for x in answer if len(x) == len(digits)]



from nose.tools import assert_equals, assert_raises

class TestLetterCombinationsPhoneNumber(object):

  def testLetterCombinationsPhoneNumber(self):
    letterCombinationsPhoneNumber = LetterCombinationsPhoneNumber()

    print ("All test cases passed!")


def main():
  testLetterCombinationsPhoneNumber = TestLetterCombinationsPhoneNumber()
  testLetterCombinationsPhoneNumber.testLetterCombinationsPhoneNumber()

if __name__ == '__main__':
  main()
