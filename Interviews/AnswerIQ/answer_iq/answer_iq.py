class AnswerIq(object):

  def answerIq(self):
    pass


from nose.tools import assert_equals, assert_raises

class TestAnswerIq(object):

  def testAnswerIq(self):
    answerIq = AnswerIq()

    print ("All test cases passed!")


def main():
  testAnswerIq = TestAnswerIq()
  testAnswerIq.testAnswerIq()

if __name__ == '__main__':
  main()
    
