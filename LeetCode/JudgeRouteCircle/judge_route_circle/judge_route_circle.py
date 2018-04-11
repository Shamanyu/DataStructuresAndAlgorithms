class JudgeRouteCircle(object):

    def judgeRouteCircle(self, route):
        verticalCount = horizontalCount = 0
        for step in route:
            if step == 'U':
                verticalCount += 1
            elif step == 'D':
                verticalCount -= 1
            elif step == 'R':
                horizontalCount += 1
            elif step == 'L':
                horizontalCount -= 1
        return not(horizontalCount or verticalCount)


from nose.tools import assert_equals, assert_raises

class TestJudgeRouteCircle(object):

  def testJudgeRouteCircle(self):
    judgeRouteCircle = JudgeRouteCircle()

    assert_equals(judgeRouteCircle.judgeRouteCircle("UD"), True)

    assert_equals(judgeRouteCircle.judgeRouteCircle("LL"), False)

    print ("All test cases passed!")


def main():
  testJudgeRouteCircle = TestJudgeRouteCircle()
  testJudgeRouteCircle.testJudgeRouteCircle()

if __name__ == '__main__':
  main()
