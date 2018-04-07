from stack import Node, Stack

class RoundOne(object):



    def roundOne(self, string):
        if string is '':
            return 0

        stack = Stack()
        result = 0

        currentResult = 0
        stringData = list(string)
        for character in stringData:
            if character == '(':
                stack.push('(')
            elif character == ')':
                stackTop = stack.peek()
                if stackTop == ')' or stackTop == None:
                    currentResult = 0
                    stack.push(')')
                elif stackTop == '(':
                    stack.pop()
                    currentResult += 1
                    if currentResult > result:
                        result = currentResult

        print (result*2)
        return result*2


from nose.tools import assert_equals, assert_raises

class TestRoundOne(object):

  def testRoundOne(self):
    roundOne = RoundOne()

    # assert_equals(roundOne.roundOne('((()'), 2)
    #
    # assert_equals(roundOne.roundOne(')()())'), 4)
    #
    # assert_equals(roundOne.roundOne('()(()))))'), 6)

    assert_equals(roundOne.roundOne('())(())()()'), 8)

    assert_equals(roundOne.roundOne(')()())(())'), 4)

    # assert_equals(roundOne.roundOne('()))(())()())()(())()()'), 10)

    print ("All test cases passed!")


def main():
  testRoundOne = TestRoundOne()
  testRoundOne.testRoundOne()

if __name__ == '__main__':
  main()
