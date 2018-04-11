class JewelsAndStones(object):

    def jewelsAndStones(self, jewels, stones):
        jewels = set(jewels)
        jewelsPossesed = 0
        for stone in stones:
            if stone in jewels:
                jewelsPossesed += 1
        return jewelsPossesed


from nose.tools import assert_equals, assert_raises

class TestJewelsAndStones(object):

  def testJewelsAndStones(self):
    jewelsAndStones = JewelsAndStones()

    assert_equals(jewelsAndStones.jewelsAndStones("aA", "aAAbbbb"), 3)

    assert_equals(jewelsAndStones.jewelsAndStones("z", "ZZ"), 0)

    print ("All test cases passed!")


def main():
  testJewelsAndStones = TestJewelsAndStones()
  testJewelsAndStones.testJewelsAndStones()

if __name__ == '__main__':
  main()
