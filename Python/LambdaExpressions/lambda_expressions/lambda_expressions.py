from functools import reduce

class LambdaExpressions(object):

    def lambdaExpressions(self):

        marks = [96, 94, 91, 92, 48]
        print (reduce(lambda x,y: x+y, marks)/len(marks))

        students = ["Aris", "BhaiMere", "AreyYaar", "N"]
        print (list(map(lambda x: 'Uncool' if len(x) > 3 else 'Cool', students)))

        studentPercents = [93.2, 91.2, 97.8, 34.8, 80, 81.2]
        print (list(filter(lambda x: x>90, studentPercents)))


from nose.tools import assert_equals, assert_raises

class TestLambdaExpressions(object):

  def testLambdaExpressions(self):
    lambdaExpressions = LambdaExpressions()

    lambdaExpressions.lambdaExpressions()

    print ("All test cases passed!")


def main():
  testLambdaExpressions = TestLambdaExpressions()
  testLambdaExpressions.testLambdaExpressions()

if __name__ == '__main__':
  main()
