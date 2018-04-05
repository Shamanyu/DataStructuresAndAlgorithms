class GenerateParantheses(object):

    def generateParantheses(self, n):
        # if n == 0:
        #     return []
        # if n == 1:
        #     return ["()"]
        # for counter, element in enumerate(self.generateParantheses(n-1)):
        #     element = list(element)
        #     for outerCounter in range(len(element)):
        #         for innerCounter in range(outerCounter+1, )



from nose.tools import assert_equals, assert_raises

class TestGenerateParantheses(object):

  def testGenerateParantheses(self):
    generateParantheses = GenerateParantheses()

    assert_equals(generateParantheses.generateParantheses(3), set(["((()))", "(()())", "(())()", "()(())", "()()()"]))

    print ("All test cases passed!")


def main():
  testGenerateParantheses = TestGenerateParantheses()
  testGenerateParantheses.testGenerateParantheses()

if __name__ == '__main__':
  main()
