class Triangle(object):

    def triangle(self, triangle):
        if not triangle:
            return
        result = triangle[-1]
        for outerCounter in range(len(triangle)-2, -1, -1):
            for innerCounter in range(len(triangle[outerCounter])):
                result[innerCounter] = min(result[innerCounter], \
                    result[innerCounter+1]) + \
                    triangle[outerCounter][innerCounter]
        return result[0]


from nose.tools import assert_equals, assert_raises

class TestTriangle(object):

  def testTriangle(self):
    triangle = Triangle()

    assert_equals(triangle.triangle([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]), 11)

    print ("All test cases passed!")


def main():
  testTriangle = TestTriangle()
  testTriangle.testTriangle()

if __name__ == '__main__':
  main()
