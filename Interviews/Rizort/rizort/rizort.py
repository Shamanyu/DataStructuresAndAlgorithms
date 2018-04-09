from threading import Thread

class RoundTwo(object):

    def __init__(self, data):
        self.data = data
        self.__iter__()

    def __iter__(self):
        self.counter = -5
        return self

    def __next__(self):
        if self.counter > len(self.data):
            return []
        self.counter += 5
        return [self.counter, self.counter+1, self.counter+2, self.counter+3, self.counter+4]

    def roundTwo(self):

        while (1):
            stringPositionList = self.__next__()
            if stringPositionList == []:
                break
            for position in stringPositionList:
                thread = Thread(target=self.reverseString, args = (position, ))
                thread.start()
                thread.join()

    def reverseString(self, position):
        if position < len(self.data):
            print ("Data ", type(self.data[position]))
            ''.join(list(self.data[position]).reverse())


from nose.tools import assert_equals, assert_raises

class TestRoundTwo(object):

  def testRoundTwo(self):
    roundTwo = RoundTwo(['az', 'by', 'cx', 'dw', 'ev', 'fu', 'gt'])

    roundTwo.roundTwo()

    print ("All test cases passed!")


def main():
  testRoundTwo = TestRoundTwo()
  testRoundTwo.testRoundTwo()

if __name__ == '__main__':
  main()
