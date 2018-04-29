from collections import defaultdict
import bisect

class MyCalendarThree(object):

    def __init__(self):
        self.bookings = defaultdict(int)
        self.kBookingMax = 0
        self.sortedPositions = list()

    def book(self, start, end):
        self.bookings[start] += 1
        self.bookings[end] -= 1

        positionStart = bisect.bisect_left(self.sortedPositions, start)
        if not self.sortedPositions or positionStart > len(self.sortedPositions) - 1 or \
            self.sortedPositions[positionStart] != start:
            bisect.insort_left(self.sortedPositions, start)

        positionEnd = bisect.bisect_left(self.sortedPositions, end)
        if not self.sortedPositions or positionEnd > len(self.sortedPositions) - 1 or \
            self.sortedPositions[positionEnd] != end:
            bisect.insort_left(self.sortedPositions, end)

        booked = 0
        for booking in self.sortedPositions:
            booked += self.bookings[booking]
            self.kBookingMax = max(self.kBookingMax, booked)

        return self.kBookingMax


from nose.tools import assert_equals, assert_raises

class TestMyCalendarThree(object):

  def testMyCalendarThree(self):
    myCalendarThree = MyCalendarThree()

    assert_equals(myCalendarThree.book(10, 20), 1)

    assert_equals(myCalendarThree.book(50, 60), 1)

    assert_equals(myCalendarThree.book(10, 40), 2)

    assert_equals(myCalendarThree.book(5, 15), 3)

    assert_equals(myCalendarThree.book(5, 10), 3)

    assert_equals(myCalendarThree.book(25, 55), 3)

    print ("All test cases passed!")


def main():
  testMyCalendarThree = TestMyCalendarThree()
  testMyCalendarThree.testMyCalendarThree()

if __name__ == '__main__':
  main()
