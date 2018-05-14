class TeemoAttacking(object):

    def findPoisonedDuration(self, timeSeries, duration):
        timePoisoned = 0
        poisonedTill = 0
        for attackTime in timeSeries:
            if attackTime >= poisonedTill:
                timePoisoned += duration
            else:
                timePoisoned += (duration - (poisonedTill-attackTime))
            poisonedTill = attackTime + duration
        return timePoisoned


from nose.tools import assert_equals, assert_raises

class TestTeemoAttacking(object):

  def testTeemoAttacking(self):
    teemoAttacking = TeemoAttacking()

    assert_equals(teemoAttacking.findPoisonedDuration([1, 4], 2), 4)

    assert_equals(teemoAttacking.findPoisonedDuration([1, 2], 2), 3)

    print ("All test cases passed!")


def main():
  testTeemoAttacking = TestTeemoAttacking()
  testTeemoAttacking.testTeemoAttacking()

if __name__ == '__main__':
  main()
