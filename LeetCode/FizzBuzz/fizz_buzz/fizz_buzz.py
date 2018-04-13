class FizzBuzz(object):

    def fizzBuzz(self, num):
        result = list()
        for counter in range(1, num+1):
            if counter % 15 == 0:
                result.append("FizzBuzz")
            elif counter % 3 == 0:
                result.append("Fizz")
            elif counter % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(counter))
        return result


from nose.tools import assert_equals, assert_raises

class TestFizzBuzz(object):

  def testFizzBuzz(self):
    fizzBuzz = FizzBuzz()

    assert_equals(fizzBuzz.fizzBuzz(15), [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz"
    ])

    print ("All test cases passed!")


def main():
  testFizzBuzz = TestFizzBuzz()
  testFizzBuzz.testFizzBuzz()

if __name__ == '__main__':
  main()
