class DailyTemperatures(object):

    def __init__(self, minTemperature=30, maxTemperature=100):
        self.minTemperature = minTemperature
        self.maxTemperature = maxTemperature
        self.temperatures = [temperature for temperature \
            in range(minTemperature, maxTemperature+1)]

    def dailyTemperatures(self, temperatureRecords):
        daysToWaitList = list()
        temperatureFirstRecordedOn = [-1 for counter \
            in range(self.minTemperature, self.maxTemperature+1)]
        for day in range(len(temperatureRecords)-1, -1, -1):
            temperature = temperatureRecords[day]
            daysToWait = float('inf')
            temperatureFirstRecordedOn[temperature-self.minTemperature] = day
            for innerCounter in range(temperature+1, self.maxTemperature+1, 1):
                possibleDay = temperatureFirstRecordedOn[innerCounter-self.minTemperature]
                if possibleDay != -1:
                    possibleDaysToWait = possibleDay - day
                    if possibleDaysToWait < daysToWait:
                        daysToWait = possibleDaysToWait
            if daysToWait == float('inf'):
                daysToWait = 0
            daysToWaitList.append(daysToWait)
        return list(reversed(daysToWaitList))


from nose.tools import assert_equals, assert_raises

class TestDailyTemperatures(object):

  def testDailyTemperatures(self):
    dailyTemperatures = DailyTemperatures(30, 100)

    assert_equals(dailyTemperatures.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
        [1, 1, 4, 2, 1, 1, 0, 0])

    print ("All test cases passed!")


def main():
  testDailyTemperatures = TestDailyTemperatures()
  testDailyTemperatures.testDailyTemperatures()

if __name__ == '__main__':
  main()
